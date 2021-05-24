import glob
import os

import pyheif
from PIL import Image

PATH = r"images"

if __name__ == "__main__":
    files = glob.glob(os.path.join(PATH, "*.HEIC"))

    for file in files:
        heif_file = pyheif.read(file)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )

        image.save(file + ".jpg", "JPEG")

