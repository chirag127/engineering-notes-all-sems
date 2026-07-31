### File Compression-UNIX compress

- **Compress** is a fast, simple LZW file compressor. It is the de facto standard in the UNIX community for compressing files .
- Compressed files take up less disk space than normal files, but you cannot read them in the usual way; you must first expand, or decompress, the files .
- By default, this will compress the given file, and create a compressed output file by appending a `.Z` extension to the input file .
- If you like to know how much compression it has done, use the verbose option: `-v` .
- Compress does not have the highest compression rate, but it is one of the fastest programs to compress data .
- Compared to gzip's fastest setting, compress is slightly slower at compression, slightly faster at decompression, and has a significantly lower compression ratio .
- While compress and gzip just compress a single file, zip is a tool that handles packaging of one or many files or directories and compression all in one go .
