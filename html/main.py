import os
import webbrowser
from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape

this = Path(__file__)
pkg_path = this.parent.joinpath("gallery")
out_dir = pkg_path.joinpath("out")
testdata_dir = pkg_path.joinpath("testdata")
jpg_dir = testdata_dir.joinpath("jpg")
testdata_dir2 = Path("C:/Users/Yoann/Pictures")

env = Environment(
    loader=PackageLoader('gallery', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


def main():

    template = env.get_template('index.html')

    img_list = get_img_list(testdata_dir2)
    kw = {'title': 'Image Gallery', 'img_list': img_list}

    result = template.render(kw)

    file_out = out_dir.joinpath("index.html")
    file_out.touch(exist_ok=True)
    with open(file_out, 'w') as fo:
        fo.writelines(result)
    print("Done")

    webbrowser.open_new_tab(file_out.as_posix())


def get_img_list(folder):
    return [file for file in folder.iterdir() if file.suffix.lower() in [".jpg", ".png"]]




if __name__ == '__main__':
    main()