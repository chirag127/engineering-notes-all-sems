 Here is the formal content on I/O in Core Java in markdown format without any emojis or external links:

#### I/O in Core Java

1. Java I/O (Input and Output) is used to process the input and produce the output.
2. There are two types of I/O:
    - Byte Stream I/O: Used to perform input and output of bytes. eg. FileInputStream and FileOutputStream.
    - Character Stream I/O: Used to perform input and output of characters. eg. FileReader and FileWriter.
3. Java uses streams to handle I/O. A stream is a sequence of data and the Java I/O streams are byte streams or character streams.
4. Some important classes for file I/O:
    - File - Used to create, delete, rename files/folders and get file attributes.
    - FileInputStream - Used to read bytes from a file.
    - FileOutputStream - Used to write bytes to a file.
    - FileReader - Used to read characters from a file.
    - FileWriter - Used to write characters to a file.
5. The File class is used to get file attributes such as name, path, size etc. but it cannot be used to read/write file contents. The FileInputStream/FileOutputStream and FileReader/FileWriter classes are used to read/write file contents.
6. While reading/writing files, it is important to close the stream after use using the close() method to release resources. Also, files should be flushed if only some buffered data is to be written using the flush() method.