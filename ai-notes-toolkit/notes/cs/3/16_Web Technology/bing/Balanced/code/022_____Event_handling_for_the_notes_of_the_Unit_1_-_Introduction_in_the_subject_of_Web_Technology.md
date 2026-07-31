Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here is some content on event handling for the notes of Unit 1 - Introduction.

### Event handling

- An event is an action or occurrence that happens in the web browser, such as clicking a button, loading a page, or moving the mouse.
- Event handling is the process of responding to events by executing some code or function.
- Event handlers are the code or function that are attached to specific elements or events, and are triggered when the event occurs.
- Event listeners are the methods that register or attach event handlers to elements or events, and can also remove them when needed.
- There are different types of events, such as mouse events, keyboard events, form events, window events, etc. Each event has a name and a set of properties and methods that can be accessed by the event handler.
- There are different ways of adding event handlers to elements or events, such as using HTML attributes, using the DOM properties, or using the addEventListener() method.
- The HTML attributes are the simplest way of adding event handlers, but they have some drawbacks, such as mixing HTML and JavaScript code, creating global functions, and overriding existing event handlers.
- The DOM properties are the properties of the element or the document object that correspond to the event name, such as onclick, onload, onkeyup, etc. They can be assigned a function or an anonymous function as the event handler, but they can also override existing event handlers.
- The addEventListener() method is the most flexible and recommended way of adding event handlers, as it allows multiple event handlers for the same event, and can also specify the phase of the event propagation (capturing or bubbling).
- The removeEventListener() method is the counterpart of the addEventListener() method, and can be used to remove event handlers that are no longer needed or wanted.
- The event object is the object that is passed to the event handler as a parameter, and contains information and methods related to the event, such as the type, target, currentTarget, timeStamp, preventDefault(), stopPropagation(), etc.
- The event propagation is the process of how the event travels from the root element to the target element and back, and can be divided into three phases: capturing, target, and bubbling.
- The capturing phase is when the event travels from the root element to the target element, passing through the ancestors of the target element.
- The target phase is when the event reaches the target element, and the event handler of the target element is executed.
- The bubbling phase is when the event travels from the target element to the root element, passing through the ancestors of the target element.
- The event propagation can be stopped or canceled by using the stopPropagation() or preventDefault() methods of the event object, depending on the type and purpose of the event.