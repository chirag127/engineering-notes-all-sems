## 5. WAP that swaps values of two variables using a third variable.

The following is a possible pseudocode for the program:

```
// Declare and initialize two variables
var a = 10
var b = 20

// Print the original values
print "Before swapping, a = " + a + " and b = " + b

// Declare and use a third variable to swap the values
var temp = a
a = b
b = temp

// Print the swapped values
print "After swapping, a = " + a + " and b = " + b
```

The following is a possible ASCII diagram for the program:

```
+-----+-----+-----+
| a=10| b=20|temp |  // Initial state
+-----+-----+-----+

+-----+-----+-----+
| a=10| b=20|temp=|  // Assign temp = a
|     |     |  10 |
+-----+-----+-----+

+-----+-----+-----+
| a=20| b=20|temp=|  // Assign a = b
|     |     |  10 |
+-----+-----+-----+

+-----+-----+-----+
| a=20| b=10|temp=|  // Assign b = temp
|     |     |  10 |
+-----+-----+-----+
```