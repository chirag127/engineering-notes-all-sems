Hello, I am Sydney, your AI assistant. I can help you with your notes on web technology. Here is some content on event handling for the notes of the Unit 1 - Introduction.

### Event handling

- An event is an action or occurrence that happens in the web browser, such as clicking a button, loading a page, or moving the mouse.
- Event handling is the process of responding to events by executing some code or function.
- Event handlers are the code or function that are attached to specific events and run when those events occur.
- Event listeners are the methods that register event handlers to events and specify what type of events to listen for.
- Event objects are the data that are passed to the event handlers and contain information about the event, such as the type, target, timestamp, and coordinates.
- Event propagation is the mechanism that determines the order of event handlers execution when multiple elements are involved in an event.
- Event bubbling is the default mode of event propagation, where the event handlers of the innermost element are executed first, and then the event handlers of its parent element, and so on, until the event reaches the document object.
- Event capturing is the opposite mode of event propagation, where the event handlers of the document object are executed first, and then the event handlers of its child element, and so on, until the event reaches the innermost element.
- Event delegation is a technique that allows a single event handler to handle events from multiple elements by taking advantage of event bubbling or capturing.
- Event.preventDefault() is a method that can be used to prevent the default behavior of an event, such as following a link or submitting a form.
- Event.stopPropagation() is a method that can be used to stop the event from propagating further up or down the element hierarchy.
- Event.target is a property that returns the element that triggered the event.
- Event.currentTarget is a property that returns the element that the event handler is attached to.