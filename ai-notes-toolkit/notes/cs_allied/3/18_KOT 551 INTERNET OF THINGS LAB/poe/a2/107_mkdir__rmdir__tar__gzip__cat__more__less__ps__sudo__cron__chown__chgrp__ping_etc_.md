 Here is the formal content on the given Linux commands in points:

mkdir:
- Used to create directories or folders.
- Syntax: mkdir [options] directory_name
- Options: -m (to set permission), -p (to create parent directories if they don't exist)

rmdir:
- Used to remove empty directories.
- Syntax: rmdir directory_name
- Cannot remove non-empty directories.

tar:
- Used to archive files and directories.
- Syntax: tar [options] [archive_name] [file/directory_names]
- Options: -c (create), -x (extract), -f (use archive file), -v (verbose), -z (gzip compressed), -j (bzip2 compressed)

gzip:
- Used to compress files.
- Syntax: gzip [options] [file_name]
- Options: -d (decompress), -c (write output to stdout)

cat:
- Used to display and concatenate files.
- Syntax: cat [options] [file_name]
- Options: -n (number all output lines), -s (suppress repeated empty output lines)

more:
- Used to display the contents of a file one page at a time.
- Syntax: more [options] [file_name]
- Options: -num (set the number of lines displayed, default is one page)

less:
- Similar to more but has more features like backwards scrolling and searching.
- Syntax: less [options] [file_name]
- Options: -N (prefix line numbers), /string (search for string), n (next match), N (previous match), q (quit)

[The content continues with points on ps, sudo, cron, chown, chgrp, ping commands...]