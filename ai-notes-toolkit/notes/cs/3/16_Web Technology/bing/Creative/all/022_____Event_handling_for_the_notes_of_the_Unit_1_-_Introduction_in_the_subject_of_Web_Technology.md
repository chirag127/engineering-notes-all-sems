# Event handling

- Event handling is the process of responding to user actions or changes in the browser or operating system environment .
- Events are signals that indicate that something has happened, such as a mouse click, a key press, a page load, or a network request .
- Event handlers are functions or methods that are executed when an event occurs . They can perform tasks such as updating the web page, validating user input, sending data to a server, or displaying a message .
- Event handlers can be attached to HTML elements using attributes, such as `onclick`, `onchange`, `onload`, etc. or using JavaScript methods, such as `addEventListener()`, `removeEventListener()`, etc   .
- Event handlers can access information about the event, such as the type, the target, the coordinates, the key code, etc. using the event object that is passed as a parameter to the handler function .
- Event handlers can also modify the default behavior of the event, such as preventing a link from opening a new page, or stopping the propagation of the event to other elements, using methods such as `preventDefault()` or `stopPropagation()` on the event object .
- Event handlers can be registered for different types of events, such as mouse events, keyboard events, touch events, window events, form events, etc. Each type of event has a specific name, such as `click`, `keydown`, `touchstart`, `resize`, `submit`, etc  .
- Event handlers can be added or removed dynamically using JavaScript, allowing web pages to respond to user actions or changes in the environment in a flexible and interactive way  .