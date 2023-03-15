### Iterated messages

- An iterated message is a message that is repeated a certain number of times or until a condition is met in a sequence diagram.
- An iterated message is represented by a frame with a label * and a guard condition in square brackets.
- The guard condition specifies the iteration clause, which can be a numeric range, a boolean expression, or a natural language description.
- The frame encloses the messages that are part of the iteration, which can be synchronous, asynchronous, or reply messages.
- An example of an iterated message is shown below:

![Iterated message example](https://i.stack.imgur.com/2wZ4a.png)

- In this example, the DataControl object sends an iterated message to the DataSource object to get the data from an array.
- The guard condition is array_size, which means the iteration will repeat as many times as the size of the array.
- The messages inside the frame are synchronous messages, indicated by the solid arrowheads and the filled rectangles on the lifelines.