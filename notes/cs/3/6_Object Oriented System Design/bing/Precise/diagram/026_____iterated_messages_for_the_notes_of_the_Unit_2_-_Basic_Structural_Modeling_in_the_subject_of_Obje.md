### Iterated Messages

Iterated messages are used in sequence diagrams to represent a repetitive action. They are depicted using a frame with a guard condition in square brackets, which specifies the number of iterations or the condition under which the iteration occurs.

Here are some key points to remember about iterated messages:

1. Iterated messages are used to represent a repetitive action in a sequence diagram.
2. They are depicted using a frame with a guard condition in square brackets.
3. The guard condition specifies the number of iterations or the condition under which the iteration occurs.
4. The iteration can be over a fixed number of times or until a certain condition is met.
5. The frame is labeled with an asterisk (*) to indicate that it is an iteration.

Example:

```
+----------------+
| [i < 5] *      |
|  :             |
|  doSomething() |
+----------------+
```

In this example, the `doSomething()` method is called 5 times, as specified by the guard condition `[i < 5]`. The frame is labeled with an asterisk (*) to indicate that it is an iteration.
