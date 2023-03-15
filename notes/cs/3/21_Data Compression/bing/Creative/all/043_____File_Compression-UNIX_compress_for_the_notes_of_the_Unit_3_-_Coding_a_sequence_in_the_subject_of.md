# File Compression-UNIX compress

- File compression is the process of reducing the size of a file by encoding its data more efficiently.
- File compression can save disk space, bandwidth, and transmission time.
- UNIX compress is one of the file compression utilities available on UNIX systems.
- UNIX compress uses the Lempel-Ziv algorithm to compress files, which is a lossless data compression technique.
- UNIX compress adds a .Z extension to the compressed file name and preserves the original file name and time stamp.
- UNIX compress can compress only one file at a time. To compress multiple files or directories, one can use the tar command to create an archive and then compress it with UNIX compress.
- UNIX compress can achieve a compression ratio of about 2:1 on average, depending on the type and content of the file.
- UNIX compress is compatible with the gzip utility, which is another file compression utility on UNIX systems. gzip can decompress files compressed by UNIX compress, and vice versa.
- To compress a file with UNIX compress, one can use the following syntax:

  `compress [options] filename`

  where options can be:

  - `-v`: verbose mode, displays the name and percentage reduction for each file compressed
  - `-f`: force compression, overwrites existing compressed files without prompting
  - `-b n`: specifies the maximum number of bits to use for compression, where n can be between 9 and 16, with the default being 16
  - `-c`: writes the output to the standard output, does not modify the original file

- To decompress a file with UNIX compress, one can use the following syntax:

  `uncompress [options] filename`

  where options can be:

  - `-v`: verbose mode, displays the name and percentage reduction for each file decompressed
  - `-f`: force decompression, overwrites existing uncompressed files without prompting
  - `-c`: writes the output to the standard output, does not modify the original file

- Alternatively, one can use the gzip command with the `-d` option to decompress files compressed by UNIX compress, and the compress command with the `-d` option to decompress files compressed by gzip.

- Examples of using UNIX compress:

  - To compress a file named data.txt and save it as data.txt.Z:

    `compress data.txt`

  - To compress a file named data.txt and write the output to the standard output:

    `compress -c data.txt`

  - To compress a file named data.txt with 12 bits and overwrite the existing compressed file if any:

    `compress -f -b 12 data.txt`

  - To decompress a file named data.txt.Z and save it as data.txt:

    `uncompress data.txt.Z`

  - To decompress a file named data.txt.Z and write the output to the standard output:

    `uncompress -c data.txt.Z`

  - To decompress a file named data.txt.Z with gzip and save it as data.txt:

    `gzip -d data.txt.Z`

  - To decompress a file named data.txt.gz with compress and save it as data.txt:

    `compress -d data.txt.gz`