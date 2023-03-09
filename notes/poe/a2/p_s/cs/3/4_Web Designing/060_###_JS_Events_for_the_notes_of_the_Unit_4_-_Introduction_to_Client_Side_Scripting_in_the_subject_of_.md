 Here is the content in markdown format for the topic ### JS Events for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing:

### JS Events

- Events are actions or occurrences that happen in the system you are programming, which the system tells you about so you can respond to them in some way if desired.
- In JavaScript, events are detected and handled with functions known as event handlers.
- Some common examples of JavaScript events are:
    - Page loading - `load` event
    - Button click - `click` event
    - Mouse movement - `mousemove` event
    - Keyboard press - `keydown` event
    - Form submission - `submit` event
    - And many more
- The HTML elements in a web page can trigger events. For example, clicking a button fires a `click` event and entering text into an input field fires a `keypress` event. These events can be detected using event handlers.
- The syntax to add an event handler to an HTML element is:

`<element event='event-name' handler='function-name'></element>`

For example:

`<button onclick='displayMessage()'>Click Me</button>`

- The event handler function can also be defined separately in the `<head>` section or in an external JavaScript file and then referred in the event attribute.
- Advantages:
    - Make web pages interactive and dynamic.
    - Respond to user actions.
    - Validate forms.
    - Display customized messages.
- Disadvantages:
    - Too many events and handlers can affect performance.
    - Difficult to debug if multiple events and handlers are used.

[Detailed diagrams and examples can be added here if required]