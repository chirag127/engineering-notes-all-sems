# Data Carving

- Data carving is a term used in the field of cyber forensics, which is the process of acquisition, authentication, analysis, and documentation of evidence extracted from and/or contained in a computer system, computer network, and digital media   .
- Data carving is the technique of extracting data (file) out of undifferentiated blocks (raw data) without relying on the file system or metadata   .
- Data carving is useful for finding hidden or deleted files from digital media, which may contain valuable information for forensic investigation.
- Data carving can be performed on areas like lost clusters, unallocated clusters, and slack space of the disk or digital media, where files may be partially or fully stored.
- Data carving requires a file to have a standard file signature called a file header (start of the file) and optionally a file footer (end of the file), which can be used to identify the file type and boundaries .
- Data carving can be classified into two types: header/footer carving and semantic carving.
  - Header/footer carving is the simplest and most common type of data carving, which uses the file header and footer to locate and extract the file.
  - Semantic carving is a more advanced type of data carving, which uses the internal structure and content of the file to locate and extract the file, without relying on the file header and footer.
- Data carving can be performed using various tools, such as Foremost, Scalpel, PhotoRec, and Autopsy.
- Data carving has some limitations and challenges, such as:
  - Data carving may produce false positives, which are files that are incorrectly identified or extracted.
  - Data carving may produce incomplete or corrupted files, which are files that are missing some data or have incorrect data due to fragmentation, overwriting, encryption, or compression .
  - Data carving may be time-consuming and resource-intensive, especially for large or complex digital media .
  - Data carving may not be able to recover all types of files, especially those that do not have distinctive file signatures or internal structures .