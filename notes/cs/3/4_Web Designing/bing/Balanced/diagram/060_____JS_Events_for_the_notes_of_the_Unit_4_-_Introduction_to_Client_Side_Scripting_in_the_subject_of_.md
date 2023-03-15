### JS Events

- JS events are changes in the state of an object that occur in the browser, such as user actions, browser actions, or DOM modifications    .
- JS events can be used to provide a dynamic and interactive interface to a webpage, by executing some code when an event occurs  .
- JS events can be handled by event handlers, which are functions that are attached to an element or a document, and are triggered when a specific event occurs on that element or document.
- JS events can be categorized into different types, such as mouse events, keyboard events, form events, window events, etc. Each type of event has a name and a set of properties that describe the event  .
- JS events can be registered using different methods, such as HTML attributes, DOM properties, or event listeners. Event listeners are the preferred method, as they allow more flexibility and control over the event handling .
- JS events use a propagation model, which determines how the event travels through the DOM hierarchy. There are two types of propagation: bubbling and capturing. Bubbling means the event goes from the target element to its ancestors, while capturing means the event goes from the root element to the target element  .
- JS events can be modified or canceled using methods such as preventDefault(), stopPropagation(), or stopImmediatePropagation(). These methods can be used to prevent the default behavior of the event, stop the event from reaching other elements, or stop other event handlers from running .