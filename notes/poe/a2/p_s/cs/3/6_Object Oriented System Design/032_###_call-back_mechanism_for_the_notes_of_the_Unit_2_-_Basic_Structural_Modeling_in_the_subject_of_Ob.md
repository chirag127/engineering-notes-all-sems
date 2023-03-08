 Here is the content in markdown format for the topic - ### Call-back mechanism for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design:

A call-back is a function that is passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

Call-backs are often used to continue code execution after an asynchronous operation has completed — for example, performing some action after a file has finished loading from disk.

Advantages:
- It avoids blocking and allows a function to continue its execution without waiting for the callback function to finish.
- It leads to shorter and more modular code.
- It facilitates reusability of code.

Disadvantages:
- May lead to what is known as "callback hell" due to excessive nesting.
- Error handling can become complex because any errors in the callback are harder to recover from.
- Can make code harder to understand due to non-sequential flow.

Examples:
LOAD_FILE(file_name, load_callback); // asynchronous

function load_callback(file_contents) {
  // use file contents
}

Applications:
- Asynchronous notifications
- Timers
- Continuation passing style
- Event driven programming

[Include diagrams or codes if required to understand the concept better]

This is how you can write the content for the given topic in markdown format with relevant points, examples, advantages, disadvantages, applications, etc to learn and read from for exams. Let me know if you would like me to elaborate on any of the points or modify the content.