# Micron
Micron is a small open source web browser made in Python.

Currently, it only supports local plain HTML files, and with very few functionalities.

## Install
<details>
<summary>Open</summary>
To install Micron, go in the [releases tab and select the latest one](https://github.com/megat69/Micron/releases/latest).

You will find a ZIP file, which contains a python file (`main.py`), and an HTML file (`index.html`).

Modify the HTML file as you wish.
</details>

## Running my HTML file
<details open>
<summary>Open</summary>

- If you modified `index.html`, then you should just type `python main.py` in the any console of your computer.
- If you created another file, then type `python main.py -f path`.
- For more help, type `python main.py -h`

</details>

## Changelog
<details>

<summary><b>Alpha 0.3</b></summary>

First official commit.
Supports at the moment :
- Titles (h1 to h6)
- Links to local files
- `br`

Current bug going on :<br/>
The titles will be at the top of the page, the links after them, and the regular text at the end.
</details>
