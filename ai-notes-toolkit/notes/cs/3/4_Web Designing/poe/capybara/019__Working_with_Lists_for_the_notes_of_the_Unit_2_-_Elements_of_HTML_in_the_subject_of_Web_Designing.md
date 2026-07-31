### Working with Lists

Lists are an essential feature of HTML and are used to organize content into a structured format. There are two main types of lists in HTML: ordered and unordered.

#### Unordered Lists

Unordered lists are used to present a list of items that are not in any particular order. To create an unordered list, use the `<ul>` tag followed by a series of `<li>` tags, which represent each list item. Here's an example:

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

This will produce an unordered list that looks like this:

- Item 1
- Item 2
- Item 3

#### Ordered Lists

Ordered lists are used to present a list of items in a specific order. To create an ordered list, use the `<ol>` tag followed by a series of `<li>` tags, which represent each list item. Here's an example:

```html
<ol>
  <li>First Item</li>
  <li>Second Item</li>
  <li>Third Item</li>
</ol>
```

This will produce an ordered list that looks like this:

1. First Item
2. Second Item
3. Third Item

#### Nested Lists

HTML also allows for nested lists, which are lists within lists. To create a nested list, simply include another `<ul>` or `<ol>` list within an `<li>` tag. Here's an example:

```html
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

This will produce an unordered list with a nested list that looks like this:

- Item 1
- Item 2
  - Nested Item 1
  - Nested Item 2
- Item 3

#### Summary

- Lists are used to organize content into a structured format.
- There are two main types of lists in HTML: ordered and unordered.
- Ordered lists present items in a specific order, and unordered lists do not.
- HTML also allows for nested lists, which are lists within lists.