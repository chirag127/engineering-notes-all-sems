## 31. WAP to compare the contents of two files and determine whether they are same or not.

- To compare the contents of two files and determine whether they are same or not, we can use the following algorithm:

  - Step 1: Open the first file in read mode and store its file pointer in a variable, say fp1.
  - Step 2: Open the second file in read mode and store its file pointer in a variable, say fp2.
  - Step 3: Initialize a flag variable to 1, which indicates that the files are same by default.
  - Step 4: Repeat the following steps until the end of either file is reached:
    - Step 4.1: Read a character from the first file and store it in a variable, say ch1.
    - Step 4.2: Read a character from the second file and store it in a variable, say ch2.
    - Step 4.3: If ch1 is not equal to ch2, then set the flag to 0, which indicates that the files are different, and break out of the loop.
  - Step 5: Close both the files using the file pointers fp1 and fp2.
  - Step 6: If the flag is 1, then print "The files are same." Otherwise, print "The files are different."

- A possible implementation of this algorithm in C language is given below:

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Declare file pointers for the two files
    FILE *fp1, *fp2;

    // Declare variables to store the characters read from the files
    char ch1, ch2;

    // Declare a flag variable to indicate whether the files are same or not
    int flag = 1;

    // Open the first file in read mode and check for errors
    fp1 = fopen("file1.txt", "r");
    if (fp1 == NULL)
    {
        printf("Error in opening file1.txt\n");
        exit(1);
    }

    // Open the second file in read mode and check for errors
    fp2 = fopen("file2.txt", "r");
    if (fp2 == NULL)
    {
        printf("Error in opening file2.txt\n");
        exit(1);
    }

    // Compare the contents of the files character by character
    while (1)
    {
        // Read a character from the first file
        ch1 = fgetc(fp1);

        // Read a character from the second file
        ch2 = fgetc(fp2);

        // If the end of either file is reached, break out of the loop
        if (ch1 == EOF || ch2 == EOF)
        {
            break;
        }

        // If the characters are not equal, set the flag to 0 and break out of the loop
        if (ch1 != ch2)
        {
            flag = 0;
            break;
        }
    }

    // Close both the files
    fclose(fp1);
    fclose(fp2);

    // Print the result based on the flag value
    if (flag == 1)
    {
        printf("The files are same.\n");
    }
    else
    {
        printf("The files are different.\n");
    }

    return 0;
}
```