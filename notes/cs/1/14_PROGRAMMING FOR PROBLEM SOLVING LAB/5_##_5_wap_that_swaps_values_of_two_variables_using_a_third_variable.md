## 5. WAP that swaps values of two variables using a third variable.

```
#include <iostream>

int main() {
  int a, b, temp;
  std::cout << "Enter two integers: ";
  std::cin >> a >> b;
  temp = a;
  a = b;
  b = temp;
  std::cout << "After swapping: " << a << " " << b;
  return 0;
}
```
