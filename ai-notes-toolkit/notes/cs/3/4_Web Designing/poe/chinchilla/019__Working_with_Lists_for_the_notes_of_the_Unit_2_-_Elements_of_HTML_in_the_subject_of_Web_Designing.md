### Working with Lists

Lists are an important element of HTML and are used to organize and display information in a structured manner on a webpage. There are two types of lists in HTML: ordered lists and unordered lists.

#### Unordered Lists

An unordered list is a list of items that are not in any particular order. The list items are marked with bullet points or other symbols to indicate separate items. To create an unordered list, you can use the `<ul>` tag.

Here's an example:

```
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

In this example, we have created an unordered list with three items. Each item is marked with the `<li>` tag.

#### Ordered Lists

An ordered list is a list of items that are in a specific order. The list items are numbered to indicate their order. To create an ordered list, you can use the `<ol>` tag.

Here's an example:

```
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>
```

In this example, we have created an ordered list with three items. Each item is marked with the `<li>` tag and numbered in order.

#### Nested Lists

Nested lists are lists within lists. You can create nested lists by placing one list inside another. To create a nested list, you simply need to add another `<ul>` or `<ol>` tag within an existing list.

Here's an example:

```
<ul>
  <li>Item 1</li>
  <li>Item 2
    <ul>
      <li>Nested Item 1</li>
      <li>Nested Item 2</li>
    </ul>
  </li>
  <li>Item 3</li>
</ul>
```

In this example, we have created a nested list within the second item of an unordered list. The nested list is another unordered list with two items.

#### Conclusion

Lists are a useful way to organize and present information on a webpage. Whether you are creating an unordered list or an ordered list, HTML provides you with the tools to create structured and visually appealing lists. By using nested lists, you can take your list organization to the next level and create even more complex and informative displays of information.