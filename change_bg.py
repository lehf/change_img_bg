from rembg import remove
from PIL import Image
import sys
from pathlib import Path
import glob
import argparse


def dir_change_bg(dir_path, to_path, bg="#fff"):
    files = (p.resolve() for p in Path(dir_path).glob("**/*") if p.suffix in {".png", ".jpg", ".jpeg" ".webp"})
    file_num = len(glob.glob(dir_path+"/*.png")+glob.glob(dir_path+"/*.jpg")+glob.glob(dir_path+"/*.jpeg")+glob.glob(dir_path+"/*.webp"))
    num = 0

    Path(to_path).mkdir(parents=True, exist_ok=True)

    for file in files:
        num += 1
        progress_rate = str(num) + "/" + str(file_num)+"  "
        input_path = Path("/".join([dir_path, file.name]))
        output_path = Path("/".join([to_path, file.name.split(".")[0]+".png"]))

        print(progress_rate + file.name + " background color is removing...")
        input_image = Image.open(input_path)
        output = remove(input_image)
        output.save(output_path)

        foreground = Image.open(output_path).convert("RGBA")
        if Path(bg).is_file():
            background = Image.open(bg).resize(foreground.size).convert("RGBA")
        else:
            background = Image.new(mode='RGB', size=foreground.size, color=bg).convert("RGBA")

        print(progress_rate + file.name+" is changing...")
        background.paste(foreground, (0, 0), foreground)
        background.convert("RGB").save(output_path)
        print(progress_rate + file.name + " is saved...")


def img_change_bg(img_path, to_path, bg="#fff"):

    print("background color is removing...")
    input_image = Image.open(img_path)
    output = remove(input_image)
    output.save(to_path)

    foreground = Image.open(to_path).convert("RGBA")

    if Path(bg).is_file():
        background = Image.open(bg).resize(foreground.size).convert("RGBA")
    else:
        background = Image.new(mode='RGB', size=foreground.size, color=bg).convert("RGBA")

    print("Image is changing...")
    background.paste(foreground, (0, 0), foreground)
    background.convert("RGB").save(to_path)
    print("Image is saved...")


if __name__ == "__main__":
    # change_bg(sys.argv[1], sys.argv[2], sys.argv[3])
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", help="New bg-color; default: #fff;  OR new bg-img path")
    parser.add_argument("-i", help="Folder or image path to input")
    parser.add_argument("-o", help="Folder or image path to output")
    # parser.add_argument("-img", help="New bg-img path;")
    args = parser.parse_args()
    if args.i:
        if args.o:
            if args.b:
                if Path(args.i).is_dir():
                    dir_change_bg(args.i, args.o, args.b)
                else:
                    img_change_bg(args.i, args.o, args.b)

        else:
            print("Please input -o argument for to output")
    else:
        print("Please input -i argument for need change")

