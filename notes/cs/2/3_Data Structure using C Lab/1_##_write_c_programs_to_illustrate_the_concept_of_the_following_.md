## Write C Programs to illustrate the concept of the following:

1. Hello World Program:
```
#include <stdio.h>

int main() 
{
    printf("Hello, World!\n");
    return 0;
}
```

2. Input/Output Program:
```
#include <stdio.h>

int main() 
{
    int number;
    printf("Enter an integer: ");
    scanf("%d", &number);
    printf("You entered: %d\n", number);
    return 0;
}
```

3. For Loop Program:
```
#include <stdio.h>

int main() 
{
    int i;
    for (i = 1; i <= 10; i++) {
        printf("%d\n", i);
    }
    return 0;
}
```

4. While Loop Program:
```
#include <stdio.h>

int main() 
{
    int i = 1;
    while (i <= 10) {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
```

5. Array Program:
```
#include <stdio.h>

int main() 
{
    int numbers[5], i;
    for (i = 0; i < 5; i++) {
        printf("Enter a number: ");
        scanf("%d", &numbers[i]);
    }
    printf("The numbers are: ");
    for (i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    return 0;
}
```

6. Function Program:
```
#include <stdio.h>

int square(int x) 
{
    return x * x;
}

int main() 
{
    int number;
    printf("Enter an integer: ");
    scanf("%d", &number);
    printf("The square of %d is %d\n", number, square(number));
    return 0;
}
```

Note: These programs are just simple examples to illustrate the concepts. They may not be the most efficient or optimal solutions for the respective problems.
