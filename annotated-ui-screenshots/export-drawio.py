import re
import subprocess

path_to_drawio_cli = "/Applications/draw.io.app/Contents/MacOS/draw.io"
input_file = "Outline parts of JupyterLab UI.drawio"


def main():
    drawio_file = open(input_file, "r")
    # the draw.io file has multiple pages
    page_name_pattern = re.compile("name=\"(.*?)\"")
    page_index = 0
    for line in drawio_file:
        for match in re.finditer(page_name_pattern, line):
            page_name = match.group(1)
            page_name_spaces_to_dashes = page_name.replace(' ', '-')
            subprocess.run([path_to_drawio_cli,
                            "--export",
                            "--page-index", str(page_index),
                            "--transparent",
                            "--width", "1200",
                            "--output", page_name_spaces_to_dashes + ".png",
                            input_file])
            page_index = page_index + 1


if __name__ == "__main__":
    main()
