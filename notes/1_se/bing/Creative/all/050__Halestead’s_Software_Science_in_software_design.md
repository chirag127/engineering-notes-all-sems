##### Halestead’s Software Science in software design

- Halestead’s Software Science is a set of software metrics introduced by Maurice Howard Halestead in 1977 to measure the complexity and quality of a program based on its source code.
- The basic idea of Halestead’s Software Science is to count the number of operators and operands in a program and use them to derive various measures of the program, such as its length, vocabulary, volume, difficulty, effort, and error proneness.
- Operators are the basic symbols that perform some action, such as arithmetic operators, logical operators, assignment operators, etc. Operands are the entities on which the operators act, such as variables, constants, literals, etc.
- Halestead’s Software Science defines the following base measures for a program :
  - n1 = Number of distinct operators
  - n2 = Number of distinct operands
  - N1 = Total number of occurrences of operators
  - N2 = Total number of occurrences of operands
- From these base measures, the following derived measures can be calculated :
  - Program vocabulary: n = n1 + n2
  - Program length: N = N1 + N2
  - Estimated program length: N^ = n1 * log2(n1) + n2 * log2(n2)
  - Program volume: V = N * log2(n)
  - Potential minimum volume: V* = (2 + n2*) * log2(2 + n2*)
  - Program level: L = V* / V
  - Program difficulty: D = (n1 / 2) * (N2 / n2)
  - Program effort: E = D * V
  - Time required to program: T = E / 18
  - Number of delivered bugs: B = E^(2/3) / 3000
- Halestead’s Software Science can be used to compare the complexity and quality of different programs or different versions of the same program. It can also be used to estimate the development time and the number of errors in a program.
- Some advantages of Halestead’s Software Science are:
  - It is easy to compute and automate
  - It is language-independent and platform-independent
  - It is based on objective and measurable properties of the source code
- Some disadvantages of Halestead’s Software Science are:
  - It does not consider the logical structure or the functionality of the program
  - It does not account for the programmer’s skill or experience
  - It may not reflect the actual effort or difficulty of the program
- An example of applying Halestead’s Software Science to a C program that calculates the factorial of a number is:

```c
#include <stdio.h>

int factorial(int n) {
  int f = 1;
  for (int i = 1; i <= n; i++) {
    f = f * i;
  }
  return f;
}

int main() {
  int n;
  printf("Enter a positive integer: ");
  scanf("%d", &n);
  printf("Factorial of %d = %d\n", n, factorial(n));
  return 0;
}
```

- The base measures for this program are:
  - n1 = 11 (distinct operators are #, <, >, int, (), =, ;, for, <=, *, and return)
  - n2 = 9 (distinct operands are stdio.h, n, f, i, 1, printf, scanf, %d, and 0)
  - N1 = 21 (total occurrences of operators)
  - N2 = 16 (total occurrences of operands)
- The derived measures for this program are:
  - Program vocabulary: n = n1 + n2 = 11 + 9 = 20
  - Program length: N = N1 + N2 = 21 + 16 = 37
  - Estimated program length: N^ = n1 * log2(n1) + n2 * log2(n2) = 11 * log2(11) + 9 * log2(9) = 39.86
  - Program volume: V = N * log2(n) = 37 * log2(20) = 185.64
  - Potential minimum volume: V* = (2 + n2*) * log2(2 + n2*) = (2 +