# Iterated Messages

- An iterated message is a message that is repeated a certain number of times or until a condition is met in a sequence diagram.
- An iterated message is represented by a frame with a label * and a guard condition in square brackets.
- The guard condition specifies the iteration clause, which can be a numeric range, a boolean expression, or a natural language description.
- The frame encloses the messages that are iterated, and the lifelines involved in the iteration are shown with dashed lines.
- An example of an iterated message is shown below:

![Iterated message example](https://www.ibm.com/support/pages/sites/default/files/inline-images/iteration.jpg)

- In this example, the message `getData()` is iterated until the `array_size` condition is met.
- The iteration clause is `array_size`, which can be interpreted as the size of the array that holds the data.
- The messages inside the frame are repeated `array_size` times, and the lifelines of `DataControl` and `DataSource` are dashed.