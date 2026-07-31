### Data Carving

- Data carving is a technique used in cyber forensics to extract data from a disk drive or other storage device without the assistance of the file system that originality created the file.
- Data carving is useful for finding hidden or deleted files from digital media, especially in areas like lost clusters, unallocated clusters and slack space of the disk.
- Data carving relies on the standard file signatures or headers that mark the start and end of a file. For example, JPEG files start with `FF D8 FF` and end with `FF D9`.
- Data carving can be performed using various tools, such as Scalpel, Foremost, PhotoRec, etc. These tools scan the raw data of the disk and look for the file signatures to identify and recover the files.
- Data carving can also be performed manually using a hex editor, such as HxD, WinHex, etc. These tools allow the user to view and edit the hexadecimal values of the disk data and copy the file segments based on the file signatures.
- Data carving has some limitations, such as:
  - It can be time-consuming and resource-intensive to scan the entire disk for file signatures.
  - It can produce false positives or incomplete files if the file signatures are corrupted, overwritten or fragmented.
  - It can miss some files that do not have standard file signatures or use encryption or compression.