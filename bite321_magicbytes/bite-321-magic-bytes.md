# Bite 321. Magic bytes

Magic numbers are bytes that can be used to uniquely identify certain file formats. Portable Network Graphics (PNG) files, for example, usually start with the byte sequence 89 50 4E 47 0D 0A 1A 0A. This can be useful to determine file types when file extensions are missing or wrong.

In this Bite you will write a function that identifies file types using a supplied magic numbers table. Arbitrary single bytes in the magic byte sequence are indicated by two question marks (??) as in the case of the JPG format. If the file type cannot be determined the function should raise an FileNotRecognizedException.

```repl
>>> determine_filetype_by_magic_bytes("/tmp/image.png")
'Image encoded in the Portable Network Graphics format'
>>> determine_filetype_by_magic_bytes("/tmp/image.txt")
Traceback (most recent call last):
...
magic_bytes.FileNotRecognizedException: /tmp/image.txt: File format not recognized
```

Note: Make sure to strip out the comments in parenthesis from byte sequences in the magic table (e.g. JPG format).