### File Compression-UNIX compress

- File compression is a technique to reduce the size of files by removing redundant or unnecessary information.
- UNIX compress is one of the compression utilities available on UNIX systems. It uses the Lempel-Ziv algorithm to compress files and appends a ".Z" extension to the compressed file name.
- The syntax of the compress command is:

  ```
  compress [options] [files]
  ```

- Some of the options are:

  - `-v`: verbose mode, displays the name and percentage reduction for each file compressed
  - `-f`: force compression, overwrites existing compressed files if any
  - `-b n`: specifies the maximum number of bits to use for compression, where n is a number between 9 and 16. The default is 16.

- To decompress a file compressed by compress, use the uncompress command:

  ```
  uncompress [options] [files]
  ```

- Some of the options are:

  - `-v`: verbose mode, displays the name of each file uncompressed
  - `-f`: force decompression, overwrites existing files if any
  - `-c`: writes the uncompressed data to standard output, does not modify the original file

- Example:

  - To compress a file named data.txt and display the percentage reduction, use:

    ```
    compress -v data.txt
    ```

  - To decompress the file data.txt.Z and overwrite the existing data.txt, use:

    ```
    uncompress -f data.txt.Z
    ```

- Advantages of UNIX compress:

  - It is fast and simple to use
  - It is widely available on UNIX systems
  - It can compress any type of file

- Disadvantages of UNIX compress:

  - It does not support multiple files or directories in one command
  - It does not preserve file permissions or ownership
  - It has a limited compression ratio compared to other utilities