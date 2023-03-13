 Here is the content in markdown format on the topic ### List in Web Page Designing:

### List in Web Page Designing

Lists are a useful way to present related items in a structured way on a web page. There are three main types of lists used in HTML:

1. Ordered lists - Used for lists where the order of the items is important, e.g. steps in a process. Each item is numbered.
2. Unordered lists - Used for lists where the order of the items is unimportant, e.g. a shopping list. Each item is marked with a bullet point.
3. Definition lists - Used to define terminology, e.g. a glossary. Each term is followed by its definition.

#### Ordered Lists

To create an ordered list, use the `<ol>` element. Each list item is placed between an opening `<li>` tag and a closing `</li>` tag.

For example:
<ol>
  <li>Step 1</li>
  <li>Step 2</li>
  <li>Step 3</li>
</ol>

Would display as:
1. Step 1
2. Step 2
3. Step 3

The type attribute can be used to specify the type of numbering used (e.g. uppercase Roman numerals, lowercase Latin letters).

#### Unordered Lists

To create an unordered list, use the `<ul>` element. As with ordered lists, each list item goes between an opening `<li>` tag and a closing `</li>` tag.

For example:
<ul>
  <li>Milk</li>
  <li>Bread</li>
  <li>Apples</li>
</ul>

Would display as:
• Milk
• Bread
• Apples

#### Definition Lists

To create a definition list, use the `<dl>` element. Each term goes between an opening `<dt>` tag and a closing `</dt>` tag. Each definition goes between an opening `<dd>` tag and a closing `</dd>` tag.

For example:
<dl>
  <dt>HTML</dt>
  <dd>Hypertext Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>

Would display as:
HTML
Hypertext Markup Language
CSS
Cascading Style Sheets

Mnemonics:

- OLO for Ordered Li<O>st
- ULU for Unordered <U>L<U>ist
- DLD for <D>efinition <L>ist

Advantages:

- Help to structure content and make it more readable
- Aid navigation and scanning
- Provide extra semantic meaning to content

Disadvantages:

- Can be overused and make a page look 'listy' if not used properly
- Need to be consistently and logically structured

[More details, examples, ascii diagrams, codes, etc. can be added here if required.]