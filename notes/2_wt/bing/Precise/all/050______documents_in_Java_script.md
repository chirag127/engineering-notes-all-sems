#### Documents in JavaScript

- In JavaScript, the `document` object represents the web page loaded in the browser and serves as an entry point to the page's content, which is the DOM (Document Object Model).
- The `document` object has various properties and methods that can be used to manipulate the content and structure of the web page.
- For example, the `getElementById()` method can be used to access an element on the page by its `id` attribute: `document.getElementById('myElement')`.
- The `innerHTML` property can be used to get or set the HTML content of an element: `document.getElementById('myElement').innerHTML = '<p>New content</p>'`.
- The `createElement()` method can be used to create a new element and add it to the page: `var newElement = document.createElement('p'); newElement.innerHTML = 'New content'; document.body.appendChild(newElement);`.
- The `addEventListener()` method can be used to attach an event listener to an element, allowing it to respond to user interactions: `document.getElementById('myButton').addEventListener('click', function() { alert('Button clicked!'); });`.
- The `document` object also provides access to other objects, such as the `window` object, which represents the browser window, and the `location` object, which represents the URL of the page.
- Mnemonic: **D**o **E**verything **C**orrectly, **A**dd **L**isteners, **W**ith **D**ocuments. (DECALWD)