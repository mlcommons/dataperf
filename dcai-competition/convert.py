import cv2
import os

from pathlib import Path
from glob import glob


def convert_images(input_folder, output_folder):
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    input_files = glob(os.path.join(input_folder, "*.png"))
    for f in input_files:
        image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        # quantize
        image = (image // 43) * 43
        image[image > 43] = 255
        cv2.imwrite(os.path.join(output_folder, os.path.basename(f)), image)


if __name__ == "__main__":
    folder_name = "YOUR_FOLDER_NAME"
    folders = glob(f"{folder_name}/*")
    for f in folders:
        convert_images(f, f.replace(f"{folder_name}", f"{folder_name}_processed"))
