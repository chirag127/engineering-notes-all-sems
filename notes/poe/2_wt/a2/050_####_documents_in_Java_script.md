 Here is the content in markdown format on the topic '#### documents in Java script':

### Documents in JavaScript

JavaScript allows us to dynamically generate and manipulate documents and their content. This can be done in a few ways:

#### DOM manipulation
The Document Object Model (DOM) represents the page so that programs can change the document structure, style and content. The DOM can be manipulated directly using JavaScript to change what displays on the page.
For example, to change the page title:
document.title = 'New Title'

To add an element:
const newElement = document.createElement('p')
newElement.textContent = 'This is a new paragraph!'
document.body.appendChild(newElement)

**Mnemonic:** Remember DOM as the 'Document Object Model' - a representation of the page as objects that can be manipulated.

#### Templating
Pages can be pre-built as templates with placeholders, and JavaScript can then fill in the placeholders dynamically. This keeps the JavaScript separate from the HTML structure and can make maintenance easier.
For example, using a library like Mustache:
const template = `
<h2>{{title}}</h2>
<p>{{message}}</p>
`
Mustache.render(template, { title: 'Hello!', message: 'Welcome to my page' })

**Mnemonic:** Think of templates as pre-built 'templates' that you 'fill in' with data.

#### Generation
JavaScript can generate entire HTML documents from scratch. This may be useful for single-page apps that display multiple views/pages in the one HTML document, with only the relevant section being shown at a time.
For example:
const html = `
<h1>My App</h1>
<p>This is my app's homepage</p>
`

**Mnemonics/Learning tricks:**
- Practice manipulating DOM elements to get a feel for how it changes the page
- Try building simple templates then passing in data to render them
- Generate full HTML pages with JS to see how flexible this approach is

[Other examples, diagrams, etc. could be included here if helpful for learning]