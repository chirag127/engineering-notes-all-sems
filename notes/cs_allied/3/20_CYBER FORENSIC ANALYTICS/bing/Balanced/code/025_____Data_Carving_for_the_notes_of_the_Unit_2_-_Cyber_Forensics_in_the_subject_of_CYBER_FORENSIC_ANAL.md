### Data Carving

- Data carving is a technique used in cyber forensics to extract data from a disk drive or other storage device without the assistance of the file system that originality created the file .
- Data carving is useful for finding hidden or deleted files from digital media, especially in areas like lost clusters, unallocated clusters and slack space of the disk.
- Data carving relies on the standard file signatures or headers that mark the start and end of a file. For example, a JPEG file starts with `FF D8 FF` and ends with `FF D9` in hexadecimal notation.
- Data carving can be performed using various tools, such as Foremost, Scalpel, PhotoRec, etc. These tools scan the raw data of the disk and look for the file signatures to identify and recover the files.
- Data carving can also be performed manually using a hex editor, such as HxD, WinHex, etc. These tools allow the user to view and edit the raw data of the disk in hexadecimal or ASCII format.
- Data carving has some limitations, such as:
  - It can be time-consuming and resource-intensive, as it requires scanning the entire disk or a large portion of it.
  - It can produce false positives, as some file signatures may appear in the middle of other files or data.
  - It can produce incomplete or corrupted files, as some files may be fragmented, overwritten, or encrypted.
  - It can miss some files that do not have standard file signatures or headers, such as plain text files.