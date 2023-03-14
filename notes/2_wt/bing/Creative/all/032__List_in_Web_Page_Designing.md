### List in Web Page Designing

- A list is a collection of items that are related in some way and displayed in a specific order.
- Lists are useful for organizing and presenting information in a web page, such as menus, steps, categories, etc.
- There are three types of lists in web page designing: ordered lists, unordered lists, and definition lists.

#### Ordered Lists
- An ordered list is a list that displays the items in a numerical or alphabetical order.
- An ordered list is created using the `<ol>` tag, and each item is enclosed in a `<li>` tag.
- The `<ol>` tag has an attribute called `type` that can specify the style of the numbering or lettering, such as `1`, `a`, `A`, `i`, or `I`.
- The `<ol>` tag also has an attribute called `start` that can specify the starting value of the numbering or lettering, such as `start="5"` or `start="c"`.
- The `<ol>` tag can be nested inside another `<ol>` tag to create sublists.
- Example of an ordered list:

```html
<ol type="A" start="c">
  <li>First item</li>
  <li>Second item</li>
  <li>Third item
    <ol type="i">
      <li>First subitem</li>
      <li>Second subitem</li>
    </ol>
  </li>
  <li>Fourth item</li>
</ol>
```

- Output of the example:

C. First item
D. Second item
E. Third item
  i. First subitem
  ii. Second subitem
F. Fourth item

#### Unordered Lists
- An unordered list is a list that displays the items in no particular order.
- An unordered list is created using the `<ul>` tag, and each item is enclosed in a `<li>` tag.
- The `<ul>` tag has an attribute called `type` that can specify the style of the bullet, such as `disc`, `circle`, or `square`.
- The `<ul>` tag can be nested inside another `<ul>` tag to create sublists.
- Example of an unordered list:

```html
<ul type="square">
  <li>First item</li>
  <li>Second item</li>
  <li>Third item
    <ul type="circle">
      <li>First subitem</li>
      <li>Second subitem</li>
    </ul>
  </li>
  <li>Fourth item</li>
</ul>
```

- Output of the example:

▪ First item
▪ Second item
▪ Third item
  ○ First subitem
  ○ Second subitem
▪ Fourth item

#### Definition Lists
- A definition list is a list that displays the items as terms and definitions, or names and values.
- A definition list is created using the `<dl>` tag, and each term is enclosed in a `<dt>` tag, and each definition is enclosed in a `<dd>` tag.
- The `<dl>` tag can be nested inside another `<dl>` tag to create sublists.
- Example of a definition list:

```html
<dl>
  <dt>HTML</dt>
  <dd>Hypertext Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
  <dt>JavaScript</dt>
  <dd>A scripting language for web pages</dd>
</dl>
```

- Output of the example:

HTML
Hypertext Markup Language
CSS
Cascading Style Sheets
JavaScript
A scripting language for web pages

#### Mnemonics and Learning Tricks
- A possible mnemonic to remember the three types of lists is: **OUD** (sounds like "owed"), which stands for **O**rdered, **U**nordered, and **D**efinition lists.
- A possible learning trick to remember the tags for each type of list is: **OLULDL** (sounds like "oh lulul"), which stands for **O**rdered **L**ist, **U**nordered **L**ist, and **D**efinition **L**ist. The first letter of each word matches the first letter of the tag. The second letter of each word is always L, which stands for List. The third letter of each word is the closing tag.
- A possible learning trick to remember the tags for each item in a list is: **LITD** (sounds like "lit"), which stands for **L**ist **I**tem