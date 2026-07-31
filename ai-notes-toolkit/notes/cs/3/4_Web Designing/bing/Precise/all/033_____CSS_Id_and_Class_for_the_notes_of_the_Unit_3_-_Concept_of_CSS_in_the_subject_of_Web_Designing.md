### CSS Id and Class

#### Unit 3 - Concept of CSS in the subject of Web Designing

- CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in a markup language like HTML.
- CSS allows you to apply styles to web pages.
- CSS has a simple syntax and uses a number of English keywords to specify the names of various style properties.
- A style sheet consists of a list of rules.
- Each rule or rule-set consists of one or more selectors, and a declaration block.
- In CSS, selectors declare which part of the markup a style applies to by matching tags and attributes in the markup itself.
- There are several different types of selectors in CSS.
- One of the most commonly used selectors is the element selector.
- An element selector is used to select elements based on their element name.
- Another commonly used selector is the class selector.
- A class selector is used to select elements with a specific class attribute.
- To select elements with a specific class, write a period (.) character, followed by the name of the class.
- An ID selector is similar to a class selector, but with a difference: an ID selector is used to select an element with a specific ID attribute.
- To select an element with a specific ID, write a hash (#) character, followed by the ID of the element.
- The ID of an element should be unique within a page, so the ID selector is used to select one unique element.
- To style a specific element with a unique ID, use the ID selector.
- To style a group of elements with the same class, use the class selector.
- The class and ID selectors are case-sensitive, so make sure to match the case of the class and ID names in the HTML and CSS.
- It is possible to combine multiple selectors to create more specific selections.
- For example, to select all the paragraphs inside a div element with the class "container", you can use the following selector: div.container p.
- The order of the selectors matters. The above selector will select all paragraphs that are descendants of a div element with the class "container", but not paragraphs that are outside of the div element or inside another div element with a different class.
- It is also possible to group multiple selectors by separating them with a comma. This will apply the same styles to all the elements selected by the different selectors.
- For example, to select all the h1 and h2 elements, you can use the following selector: h1, h2.
- This will apply the same styles to all h1 and h2 elements on the page.
- It is important to note that the order of the selectors in the group does not matter. The above selector will select all h1 and h2 elements, regardless of their order in the HTML.
- In conclusion, the class and ID selectors are powerful tools that allow you to select and style specific elements on a web page. By combining different types of selectors, you can create complex and specific selections to apply styles to your web pages. Remember to use the class selector to style groups of elements with the same class, and the ID selector to style a unique element with a specific ID. Also, keep in mind that the order of the selectors matters when combining them, and that you can group multiple selectors to apply the same styles to different elements.