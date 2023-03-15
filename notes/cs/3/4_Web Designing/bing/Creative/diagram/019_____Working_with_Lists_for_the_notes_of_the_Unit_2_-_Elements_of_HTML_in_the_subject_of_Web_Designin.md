### Working with Lists

Lists are a common way to organize and present information on web pages. Lists can be ordered or unordered, and can contain different types of items. In this section, we will learn how to create and style lists using HTML and CSS.

#### Ordered Lists

An ordered list is a list that has a specific order or sequence. For example, a list of steps in a recipe, or a list of events in a timeline. To create an ordered list, we use the `<ol>` element, which stands for ordered list. Inside the `<ol>` element, we use the `<li>` element, which stands for list item, to add each item to the list. For example:

```html
<ol>
  <li>Preheat oven to 375°F.</li>
  <li>Mix flour, baking soda, and salt in a bowl.</li>
  <li>Cream butter, sugar, and vanilla in another bowl.</li>
  <li>Add eggs and beat well.</li>
  <li>Stir in chocolate chips.</li>
  <li>Drop by rounded tablespoon onto baking sheets.</li>
  <li>Bake for 9 to 11 minutes or until golden brown.</li>
</ol>
```

This will produce a list that looks like this:

1. Preheat oven to 375°F.
2. Mix flour, baking soda, and salt in a bowl.
3. Cream butter, sugar, and vanilla in another bowl.
4. Add eggs and beat well.
5. Stir in chocolate chips.
6. Drop by rounded tablespoon onto baking sheets.
7. Bake for 9 to 11 minutes or until golden brown.

By default, an ordered list uses numbers to indicate the order of the items. However, we can change the style of the list markers using the `type` attribute on the `<ol>` element. The `type` attribute can take one of the following values:

- `1`: numbers (default)
- `A`: uppercase letters
- `a`: lowercase letters
- `I`: uppercase Roman numerals
- `i`: lowercase Roman numerals

For example, to use uppercase letters for the list markers, we can write:

```html
<ol type="A">
  <li>Preheat oven to 375°F.</li>
  <li>Mix flour, baking soda, and salt in a bowl.</li>
  <li>Cream butter, sugar, and vanilla in another bowl.</li>
  <li>Add eggs and beat well.</li>
  <li>Stir in chocolate chips.</li>
  <li>Drop by rounded tablespoon onto baking sheets.</li>
  <li>Bake for 9 to 11 minutes or until golden brown.</li>
</ol>
```

This will produce a list that looks like this:

A. Preheat oven to 375°F.
B. Mix flour, baking soda, and salt in a bowl.
C. Cream butter, sugar, and vanilla in another bowl.
D. Add eggs and beat well.
E. Stir in chocolate chips.
F. Drop by rounded tablespoon onto baking sheets.
G. Bake for 9 to 11 minutes or until golden brown.

We can also use the `start` attribute on the `<ol>` element to specify the starting number or letter of the list. For example, to start the list from 5, we can write:

```html
<ol start="5">
  <li>Stir in chocolate chips.</li>
  <li>Drop by rounded tablespoon onto baking sheets.</li>
  <li>Bake for 9 to 11 minutes or until golden brown.</li>
</ol>
```

This will produce a list that looks like this:

5. Stir in chocolate chips.
6. Drop by rounded tablespoon onto baking sheets.
7. Bake for 9 to 11 minutes or until golden brown.

#### Unordered Lists

An unordered list is a list that does not have a specific order or sequence. For example, a list of ingredients, or a list of hobbies. To create an unordered list, we use the `<ul>` element, which stands for unordered list. Inside the `<ul>` element, we use the `<li>` element, which stands for list item, to add each item to the list. For example:

```html
<ul>
  <li>Flour</li>
  <li>Baking soda</li>
  <li>Salt</li>
  <li>Butter</li>
  <li>Sugar</li>
  <li>Vanilla</li>
  <li>Eggs</li>
  <li>Chocolate chips</li>
</ul>
```

This will produce a list that looks like