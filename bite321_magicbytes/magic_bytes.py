from typing import Union
from io import StringIO
import pathlib
import csv
from rich import print
from itertools import islice

# Extracted from https://en.wikipedia.org/wiki/List_of_file_signatures
MAGIC_IMAGE_TABLE = """
"magic_bytes","text_representation","offset","extension","description"
"47 49 46 38 37 61
47 49 46 38 39 61","GIF87a
GIF89a",0,"gif","Image file encoded in the Graphics Interchange Format (GIF)"
"FF D8 FF DB
FF D8 FF E0 00 10 4A 46 49 46 00 01
FF D8 FF EE
FF D8 FF E1 ?? ?? 45 78 69 66 00 00","ÿØÿÛ
ÿØÿà..JFIF..
ÿØÿîÿØÿá..Exif..",0,"jpg
jpeg","JPEG raw or in the JFIF or Exif file format"
"89 50 4E 47 0D 0A 1A 0A",".PNG....",0,"png","Image encoded in the Portable Network Graphics format"
"49 49 2A 00 (little-endian format)
4D 4D 00 2A (big-endian format)","II*.MM.*",0,"tif
tiff","Tagged Image File Format (TIFF)"
"50 31 0A","P1.",0,"pbm","Portable bitmap"
"""  # noqa: E501


class FileNotRecognizedException(Exception):
    """
    File cannot be identified using a magic table
    """

# Taken from https://github.com/python/cpython/issues/98363 for compatibility with Python 3.10
def batched(iterable, n):
      """Batch data into lists of length n. The last batch may be shorter."""
      # batched('ABCDEFG', 3) --> ABC DEF G
      if n < 1:
          raise ValueError('n must be >= 1')
      it = iter(iterable)
      # changed list for tuple return type to make it hashable
      while (batch := tuple(islice(it, n))):
          yield batch


def determine_filetype_by_magic_bytes(
    file_name: Union[str, pathlib.Path],
    lookup_table_string: str = MAGIC_IMAGE_TABLE,
) -> str:
    """
    file_name: file name with path
    lookup_table_string: a comma separated text containing a magic table

    Returns: file format based on the magic bytes
    """
    csv_file = StringIO(lookup_table_string)
    reader = csv.DictReader(
        csv_file,
        fieldnames=["magic_bytes","text_representation","offset","extension","description"],
        )
    next(reader,None)
    magic_list = [row for row in reader]
    matched = None
    # print(magic_list)
    with open(file_name, "rb") as f:
        for file_type in magic_list:
            f.seek(int(file_type['offset'].strip().replace("\"", "")))
            byte_count = len(file_type["magic_bytes"].split(" "))
            # gets a hex string representation of the bytes
            bytes_to_test = f.read(byte_count).hex().upper()
            # gets a hex string representation of the bytes with no spaces
            magic_bytes = file_type["magic_bytes"].split("(")[0].replace(" ", "")
            # print(f"Comparing {bytes_to_test} with {magic_bytes}")
            mask = zip(batched(magic_bytes, 2), batched(bytes_to_test, 2))
            matched = file_type
            for magic_byte, file_byte in mask:
                print(f"{magic_byte=}")
                if magic_byte in {('?', '?') , file_byte}:
                    continue
                matched = None
                break
            if matched:
                return matched['description'].strip().replace("\"", "")
    raise FileNotRecognizedException(f"{file_name} type not found")







# Set up for your convenience when coding:
#  - creates a test_image.gif GIF file
#  - calls determine_filetype_by_magic_bytes
#  - prints out file type
if __name__ == "__main__":
    test_filename = "test_image.gif"
    print(f"Script invoked directly. Writing out test file {test_filename}")
    with open(test_filename, "wb") as f:
        f.write(
            b"\x47\x49\x46\x38\x37\x61\x01\x00x01\x00\x80\x00\x00\xff\xff\xff"
            b"\xff\xff\xff\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02"
            b"\x44\x01\x00\x3b"
        )
    print("Testing file format")
    print(determine_filetype_by_magic_bytes(test_filename))
