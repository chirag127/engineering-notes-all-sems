 Here is the content in markdown format with formal tone without any emojis or external links:

### Data Carving for the notes of the Unit 2 - Cyber Forensics in the subject of CYBER FORENSIC ANALYTICS

1. Data Carving is a process of recovering files from a disk or device where the normal methods of file system access are not working. This means the files on the media have somehow become corrupted or deleted.
2. Data Carving is done by searching for known headers and footers of files and trying to rebuild full files out of fragmented parts. Things like JPG, PNG and MP3 files all have known headers that Data Carving tools look for.
3. Data Carving is often done when a disk has been formatted or when files have been deleted. Even though the file system says the space is available, the actual file data may still be present on the media until it is overwritten. Data Carving can grab these orphaned file parts and reassemble the files.
4. Some of the tools used for Data Carving are PhotoRec, Scalpel, Foremost, bulk_extractor, etc. These tools scan through the bytes of the disk or image looking for headers and footers of known file types and then recover the full files.
5. Limitations of Data Carving:
    - It can't recover files if the headers or footers are not found.
    - It can lead to false positives where bad data is misidentified as files.
    - File names and paths are lost as Data Carving just recovers the raw files.
    - It requires a lot of processing power and time to scan large disks or images.

6. Data Carving is an important technique for Cyber Forensics analysts to retrieve and recover lost or deleted data from disks and images. It can help recover documents, images, videos, and other files that may contain relevant evidence. Although, the limitations should be kept in mind and other forensic techniques should also be used to analyze the recovered data.