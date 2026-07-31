## 31. WAP to compare the contents of two files and determine whether they are same or not.

In order to compare the contents of two files and determine whether they are the same or different, we can use the following steps:

1. Open both files using the `fopen()` function in read mode.
2. Read the contents of both files using the `fgets()` function and store them in separate variables.
3. Compare the contents of both variables using the `strcmp()` function.
4. If the contents of both files are the same, then the `strcmp()` function will return a value of 0. If the contents are different, then the function will return a non-zero value.
5. Close both files using the `fclose()` function.

Here is an example code that implements the above steps:

```
#include <stdio.h>
#include <string.h>

int main()
{
    FILE *file1, *file2;
    char buffer1[100], buffer2[100];

    file1 = fopen("file1.txt", "r");
    file2 = fopen("file2.txt", "r");

    if (file1 == NULL || file2 == NULL)
    {
        printf("Error opening files.\n");
        return 1;
    }

    while (fgets(buffer1, 100, file1) != NULL && fgets(buffer2, 100, file2) != NULL)
    {
        if (strcmp(buffer1, buffer2) != 0)
        {
            printf("Files are different.\n");
            return 0;
        }
    }

    if (fgets(buffer1, 100, file1) != NULL || fgets(buffer2, 100, file2) != NULL)
    {
        printf("Files are different.\n");
        return 0;
    }

    fclose(file1);
    fclose(file2);

    printf("Files are the same.\n");
    return 0;
}
```

Note that this code assumes that both files have the same number of lines and that each line is no longer than 100 characters. If this is not the case, then the code will need to be modified accordingly. Additionally, this code only compares the contents of the files line by line. If you need to compare the files byte by byte, then you will need to use a different approach.