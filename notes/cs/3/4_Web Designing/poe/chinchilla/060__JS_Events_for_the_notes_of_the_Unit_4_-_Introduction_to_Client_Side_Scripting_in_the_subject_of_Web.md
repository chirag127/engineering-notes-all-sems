### JS Events

JavaScript events are actions or occurrences that take place on a web page, which can be detected and handled by JavaScript code. These events can be triggered by user actions like clicking a button or hovering over an element, or they can be triggered by the browser itself, such as when a page is finished loading.

Here are some important concepts related to JS events:

1. **Event Listeners**: Event listeners are functions that are executed when an event is fired. They are used to handle events and respond to them in some way. In JavaScript, you can add event listeners to HTML elements using the `addEventListener()` method.

2. **Event Handlers**: Event handlers are functions that are associated with a specific event. They are typically included inline in HTML using the `on[event]` attribute, where `[event]` is the name of the event. For example, the `onclick` attribute is used to define an event handler for the `click` event.

3. **Event Objects**: When an event is fired, an event object is created that contains information about the event, such as the target element, the type of event, and any additional data associated with the event. You can access this object using the `event` parameter that is passed to the event listener or handler function.

4. **Event Propagation**: Event propagation refers to the way that events are handled by nested HTML elements. When an event is triggered on an element, it can propagate up or down the hierarchy of elements. By default, events bubble up from the target element to its parent elements, but they can also be stopped or captured at any point along the way.

5. **Event Types**: There are many different types of events that can be handled by JavaScript code, including mouse events, keyboard events, form events, and window events. Some common event types include `click`, `mouseover`, `keydown`, `submit`, and `load`.

6. **Event Delegation**: Event delegation is a technique that allows you to handle events for multiple elements using a single event listener attached to a common ancestor element. This can be useful for handling events for dynamically created elements or for reducing the number of event listeners needed on a page.

In conclusion, understanding JavaScript events is crucial for creating dynamic and interactive web pages. By using event listeners, handlers, objects, propagation, types, and delegation, you can make your web pages more engaging and responsive to user actions.