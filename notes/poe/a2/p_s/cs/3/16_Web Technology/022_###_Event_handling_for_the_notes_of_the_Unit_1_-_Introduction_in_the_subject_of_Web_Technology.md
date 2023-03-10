 Here is the content written in markdown format for the given topic:

### Event handling for the notes of the Unit 1 - Introduction in the subject of Web Technology

- Events are actions or occurrences that happen in the system you are programming, which the system tells you about so you can respond to them in some way if desired.
- For example, when a web page has finished loading, a load event is triggered, or when a button on a web page is clicked, a click event is triggered.
- Event handling is the process of reacting to and dealing with such events.
- To handle an event, you specify an event handler - a piece of code to run when the event occurs. When the event occurs, its event handler runs.
- HTML exposes a set of common events that you can handle. Some of them are:
  - load - page has loaded
  - click - a pointer button is pressed and released
  - dblclick - a pointer button is double-clicked
  - keypress - a key is pressed down
  - keydown - a key is pressed down
  - keyup - a key is released
  - mousedown - a pointer button is pressed down
  - mouseup - a pointer button is released
  - mouseover - a pointer is moved onto an element
  - mouseout - a pointer is moved off an element
  - submit - a form is submitted
  - change - form control loses focus with changed value
- You can attach event handlers to HTML elements using HTML attributes, but more commonly event handlers are specified using JavaScript.
- The basic syntax for adding an event handler to an element using JavaScript is:
element.addEventListener("eventtype", functionName);
- For example:
myButton.addEventListener("click", handleClick);

[Detailed diagrams, examples, advantages, disadvantages and applications can be added here for better understanding and learning.]