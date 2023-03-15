Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Designing. Here are some notes on JS Events for Unit 4 - Introduction to Client Side Scripting.

### JS Events

- JS events are actions or occurrences that happen in the browser that can be detected and responded to by JS code.
- Some examples of JS events are: clicking a button, loading a web page, pressing a key, resizing a window, submitting a form, etc.
- JS events can be used to create dynamic and interactive web pages that respond to user input and actions.
- To use JS events, we need to:
  - Define an event handler function that contains the code to execute when the event occurs.
  - Register the event handler function with the event target, which is the HTML element that triggers the event.
  - Use the `addEventListener()` method to register the event handler function with the event target and specify the type of event to listen for.
  - Use the `removeEventListener()` method to unregister the event handler function from the event target and stop listening for the event.
- The event handler function can access an event object that contains information about the event, such as the type, target, time, coordinates, etc.
- The event object can be passed as a parameter to the event handler function or accessed through the `this` keyword inside the function.
- Some common properties and methods of the event object are:
  - `type`: the name of the event, such as "click", "load", "keydown", etc.
  - `target`: the HTML element that triggered the event, such as a button, a link, a form, etc.
  - `currentTarget`: the HTML element that the event handler is registered with, which may be different from the target if the event bubbles up the DOM tree.
  - `preventDefault()`: a method that prevents the default action of the event, such as following a link, submitting a form, etc.
  - `stopPropagation()`: a method that stops the event from bubbling up the DOM tree and reaching other event handlers.
  - `stopImmediatePropagation()`: a method that stops the event from bubbling up the DOM tree and also prevents other event handlers on the same element from executing.
- Some common types of JS events are:
  - Mouse events: events that occur when the user interacts with the mouse, such as "click", "dblclick", "mouseover", "mouseout", "mousemove", etc.
  - Keyboard events: events that occur when the user presses or releases a key on the keyboard, such as "keydown", "keyup", "keypress", etc.
  - Form events: events that occur when the user interacts with a form element, such as "submit", "reset", "change", "input", "focus", "blur", etc.
  - Window events: events that occur when the browser window changes, such as "load", "unload", "resize", "scroll", etc.
  - Document events: events that occur when the document or its elements change, such as "DOMContentLoaded", "readystatechange", "error", etc.