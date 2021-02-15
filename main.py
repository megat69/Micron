"""
Micron is a small open source web browser made in Python.
Currently, it only supports local plain HTML files, and with very few functionalities.
TODO : get_attribute()
"""
import tkinter as tk
import sys
import os
from functions import *
import re
from functools import partial

# Constants
FILE = "index.html"
DEBUG = False
BACKGROUND_COLOR = "white"
FONT_COLOR = "black"
FONT = ("Times New Roman", 12)
SIZES = {
    "H1": 43,
    "H2": 35,
    "H3": 29,
    "H4": 27,
    "H5": 17,
    "H6": 15
}


# See if there are CLI arguments
# So we can open a different file or show help.
for i in range(1, len(sys.argv), 2):
    if sys.argv[i].lower() == "--file" or sys.argv[i].lower() == "-f":
        try:
            FILE = sys.argv[i + 1]
        except IndexError:
            print("Parameter 'file' is empty ! You must specify a file to look for.")
            sys.exit(1)
    elif sys.argv[i].lower() == "--help" or sys.argv[i].lower() == "-h":
        print("Syntax : python main.py [*args]\n"
              "Args :\n"
              "- '--help' or '-h' : Show this help message and exit.\n"
              "- '--file' or '-f' : Display the file specified at this path. Default : index.html\n")
        sys.exit(0)

# See if the file exists
if not os.path.isfile(FILE):
    raise Exception(f"File '{FILE}' does not exist !")

# Open the HTML file and print its contents
opened_file = open(FILE, "r", encoding="utf-8")
file_contents = recreate_string(opened_file.readlines())
opened_file.close()

# Splitting the file
try:
    HEAD = re.findall("<head>.*</head>", file_contents, re.DOTALL)[0]
    # We replace the 'head'
    HEAD = HEAD.replace("<head>", "", 1)[:-7]
    # Replace useless line breaks, tabs, and multiple spaces
    HEAD = HEAD.replace("\n", "").replace("\t", "").replace("  ", "")
except IndexError:
    HEAD = ""
try:
    BODY = re.findall("<body>.*</body>", file_contents, re.DOTALL)[0]
    # We replace the 'body'
    BODY = BODY.replace("<body>", "", 1)[:-7]
    # Replace useless line breaks, tabs, and multiple spaces
    BODY = BODY.replace("\n", "").replace("\t", "").replace("  ", "")
except IndexError:
    BODY = ""

if DEBUG: print(HEAD, BODY)

# Creation of the window
window = tk.Tk()
window.state('zoomed')
window.configure(bg=BACKGROUND_COLOR)

# Analysis of the file

# Getting the title
try:
    title = re.findall("<title>.*</title>", HEAD)[0]
    # We replace the 'title'
    title = title.replace("<title>", "", 1)[:-len("</title>")]
except IndexError:  # If the title is not defined,
    # We put the filename as title
    title = FILE
# We define the window title as wanted
window.title(title)

# Getting the links
links = re.findall("<link>.*</link>", HEAD)
for link in links:
    type = re.findall("type=\".*\"", link)[0].replace("type=\"", "", 1)[:-1]
    if type.lower() == "icon":
        icon = re.findall("href=\".*\"", link)[0].replace("icon=\"", "", 1)[:-1]


# We define the window title and icon as wanted
window.title(title)
try:
    window.iconbitmap(icon)
except NameError:
    window.iconbitmap("Micron_Icon.ico")

labels = []

# We add every element of the body to the window
# H1s
if DEBUG: print(BODY)
text_elements = re.findall("<([hH][1-6]( align=\"(center|left|right)\")?)>(.+?)<\/[hH][1-6]>", BODY)
if DEBUG: print(text_elements)
for element in text_elements:
    BODY = BODY.replace(f"<{element[0]}>{element[3]}</{element[0].split(' ')[0]}>", "", 1)
    labels.append(tk.Label(window, text=element[3], font=(FONT[0], SIZES[element[0].split(" ")[0].upper()]), fg=FONT_COLOR, bg=BACKGROUND_COLOR))
    if element[2] == "center":
        labels[len(labels) - 1].pack(anchor=tk.N)
    elif element[2] == "right":
        labels[len(labels) - 1].pack(anchor=tk.NE)
    else:
        labels[len(labels)-1].pack(anchor=tk.NW)


# links
text_elements = re.findall("<a href=\"(.+?)\" ?(align=\"(center|left|right)\")?>(.+?)<\/a>", BODY)
if DEBUG: print(text_elements)

# Creation of a function that will go to the clicked link
def link_clicked(destination:str):
    """
    Destroys the current window and launches a new one, with the specified destination.
    """
    global window
    window.destroy()
    os.system(f"python main.py -f {destination}")
    sys.exit(0)

for element in text_elements:
    labels.append(
        tk.Button(window,
            text=element[3],
            command=partial(link_clicked, element[0]),
            font=FONT,
            fg="blue",
            bg=BACKGROUND_COLOR
        )
    )
    if element[2] == "center":
        labels[len(labels) - 1].pack(anchor=tk.N)
    elif element[2] == "right":
        labels[len(labels) - 1].pack(anchor=tk.NE)
    else:
        labels[len(labels)-1].pack(anchor=tk.NW)

    if element[1] == "":
        BODY = BODY.replace(f"<a href=\"{element[0]}\">{element[3]}</a>", "", 1)
    else:
        BODY = BODY.replace(f"<a href=\"{element[0]}\" {element[1]}>{element[3]}</a>", "", 1)

# br
text_elements = re.split("<br ?/?>", BODY)
for element in text_elements:
    labels.append(tk.Label(window, text=element, font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR).pack(anchor=tk.NW))

# Displaying the window
window.mainloop()

#print(file_contents)
