 Here is the formal content on the given topic in Markdown format:

# mkdir, rmdir, tar, gzip

## mkdir

- Used to create directories (folders)
- Syntax: `mkdir [options] directory_name`
- Options:
    - `-p`: Creates parent directories as needed
    - `-m`: Sets permission mode (who can access the directory)
- Example: `mkdir my_directory` creates a directory called "my_directory"

## rmdir

- Used to remove empty directories
- Syntax: `rmdir [options] directory_name`
- Options:
    - `-p`: Removes parent directories if empty
- Cannot remove non-empty directories. Must use `rm -r` to remove non-empty directories.
- Example: `rmdir my_directory` removes the directory "my_directory" if empty

## tar

- Used to create/extract archive files (packages multiple files into one)
- Syntax: `tar [options] [file]`
- Common options:
    - `-c`: Creates archive
    - `-x`: Extracts archive
    - `-v`: Verbose output
    - `-f`: Uses archive file name
    - `-z`: Filters archive through gzip for compression
- Examples:
    - `tar -cvf archive.tar file1 file2`: Creates archive.tar containing file1 and file2
    - `tar -xvf archive.tar`: Extracts files from archive.tar

## gzip

- Used to compress/decompress files
- Syntax: `gzip [options] [file]`
- Common options:
    - `-d`: Decompresses
    - `-c`: Outputs to standard output
- Examples:
    - `gzip file`: Compresses file, creates file.gz
    - `gzip -d file.gz`: Decompresses file.gz, creates file