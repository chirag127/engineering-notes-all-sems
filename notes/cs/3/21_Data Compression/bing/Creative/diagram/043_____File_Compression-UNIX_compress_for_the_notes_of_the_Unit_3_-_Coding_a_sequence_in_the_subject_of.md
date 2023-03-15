### File Compression-UNIX compress

- File compression is a technique to reduce the size of files by removing redundant or unnecessary information, such as repeating patterns, spaces, or symbols.
- File compression can save disk space, bandwidth, and transmission time, and can also protect data from unauthorized access or modification.
- UNIX compress is a file compression utility that uses the Lempel-Ziv-Welch (LZW) algorithm to compress files.
- UNIX compress can reduce the size of text files by 40% to 60%, and binary files by 20% to 40%, depending on the file content and format.
- UNIX compress adds a .Z extension to the compressed file name, and preserves the original file name, permissions, and timestamp.
- UNIX compress can be used with the tar command to create compressed archive files, which can store multiple files and directories in a single file.
- UNIX compress can be invoked by the command `compress [options] [files]`, where options can be:

  - `-b n`: Set the maximum number of bits per code to n (default is 16, minimum is 9, maximum is 24).
  - `-c`: Write the output to the standard output, and do not change the input files.
  - `-d`: Decompress the input files.
  - `-f`: Force compression or decompression, even if the file has multiple links, the output file already exists, or the file has a special or non-regular type.
  - `-v`: Write the name and percentage reduction for each file to the standard error.

- UNIX compress can be used with the following commands to perform various operations on compressed files:

  - `uncompress [options] [files]`: Decompress the files compressed by compress.
  - `zcat [files]`: Write the contents of the compressed files to the standard output, without changing the input files.
  - `zmore [files]`: Display the contents of the compressed files one screen at a time, without changing the input files.
  - `zgrep [options] [pattern] [files]`: Search for a pattern in the compressed files, without changing the input files.
  - `zdiff [options] [file1] [file2]`: Compare two compressed files, without changing the input files.
  - `znew [files]`: Recompress the files from .Z (compress) format to .gz (gzip) format.

- UNIX compress is compatible with most UNIX and Linux systems, but it is not widely used anymore, as newer compression utilities, such as gzip and bzip2, offer better compression ratios and more features.