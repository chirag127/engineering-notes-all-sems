# Event handling

- Event handling is the process of defining how a web page responds to user actions, such as clicking a button, moving the mouse, typing a text, etc.
- Events are occurrences that happen in the browser, such as loading a page, submitting a form, hovering over an element, etc.
- Event handlers are functions or methods that are executed when an event occurs, such as displaying a message, validating an input, changing the style of an element, etc.
- Event listeners are objects that register event handlers for specific events, such as `window.addEventListener("load", function() {...})`, which registers a function to be executed when the window loads.
- Event objects are parameters that are passed to event handlers, which contain information about the event, such as the type, the target, the coordinates, the key pressed, etc.
- Event propagation is the process of how events are transmitted from one element to another in the document tree, such as from a child element to its parent element, or vice versa.
- Event bubbling is the default mode of event propagation, where an event on a child element triggers the event handlers of its parent elements, up to the document root.
- Event capturing is the opposite mode of event propagation, where an event on a parent element triggers the event handlers of its child elements, down to the target element.
- Event delegation is a technique of using a single event handler on a parent element to handle events on its child elements, which reduces the number of event listeners and improves performance.
- Event.preventDefault() is a method that can be called on an event object to prevent the default action of the event, such as submitting a form, following a link, etc.
- Event.stopPropagation() is a method that can be called on an event object to stop the event from propagating further, either in the bubbling or capturing phase.