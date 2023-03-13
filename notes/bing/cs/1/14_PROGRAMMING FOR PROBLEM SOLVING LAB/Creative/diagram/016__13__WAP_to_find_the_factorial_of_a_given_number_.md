## 13. WAP to find the factorial of a given number.

The following is a possible pseudocode for finding the factorial of a given number n:

```
function factorial(n)
  if n == 0 or n == 1 then
    return 1
  else
    return n * factorial(n-1)
  end if
end function
```

The following is a possible ASCII diagram for illustrating the recursive calls of the factorial function:

```
factorial(5) = 5 * factorial(4)
             / \
            /   \
           /     \
          /       \
         /         \
        /           \
       /             \
      /               \
     /                 \
    /                   \
   /                     \
  /                       \
 /                         \
factorial(4) = 4 * factorial(3)
             / \
            /   \
           /     \
          /       \
         /         \
        /           \
       /             \
      /               \
     /                 \
    /                   \
   /                     \
  /                       \
 /                         \
factorial(3) = 3 * factorial(2)
             / \
            /   \
           /     \
          /       \
         /         \
        /           \
       /             \
      /               \
     /                 \
    /                   \
   /                     \
  /                       \
 /                         \
factorial(2) = 2 * factorial(1)
             / \
            /   \
           /     \
          /       \
         /         \
        /           \
       /             \
      /               \
     /                 \
    /                   \
   /                     \
  /                       \
 /                         \
factorial(1) = 1
```