### Create a style sheet in CSS/ XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

In this unit, we will learn how to create a style sheet in CSS/XSL and display the document in Internet Explorer. A style sheet is a collection of rules that define how our web pages should look. We can use CSS or XSL to create a style sheet.

#### Creating a style sheet in CSS

To create a style sheet in CSS, we need to follow these steps:

1. Create a new text file and save it with the ".css" extension.
2. Open the file in a text editor.
3. Write CSS rules to define the style for elements in our web page.
4. Save the file.

Here is an example of a simple CSS rule:

```
h1 {
  color: red;
}
```

This rule sets the color of all `h1` elements to red.

#### Displaying the document in Internet Explorer

To display our document in Internet Explorer, we need to follow these steps:

1. Open Internet Explorer.
2. Click on the "File" menu and select "Open".
3. Navigate to the location of our HTML file.
4. Select the file and click "Open".

Our HTML document will now be displayed in Internet Explorer with the styles defined in our CSS file.

#### Creating a style sheet in XSL

To create a style sheet in XSL, we need to follow these steps:

1. Create a new text file and save it with the ".xsl" extension.
2. Open the file in a text editor.
3. Write XSL rules to define the style for elements in our web page.
4. Save the file.

Here is an example of a simple XSL rule:

```
<xsl:template match="h1">
  <h1 style="color: red;">
    <xsl:apply-templates/>
  </h1>
</xsl:template>
```

This rule sets the color of all `h1` elements to red.

#### Advantages of using CSS/XSL

- Separation of content and presentation: CSS/XSL allows us to separate the content of our web page from its presentation. This makes it easier to maintain and update our web pages.
- Consistency: By using CSS/XSL, we can ensure that all of our web pages have a consistent look and feel.
- Easy to learn: CSS/XSL is easy to learn and use, even for beginners.

#### Disadvantages of using CSS/XSL

- Browser compatibility: Some older browsers may not support all of the features of CSS/XSL, which can lead to inconsistencies in how our web pages are displayed.
- Steep learning curve: While CSS/XSL is easy to learn for beginners, mastering it can take some time.

#### Examples and applications

CSS/XSL is used extensively in web design and development. Some examples of its applications include:

- Creating responsive web designs that adapt to different screen sizes.
- Creating custom themes for content management systems like WordPress and Drupal.
- Creating custom styles for charts and graphs in data visualization.

In conclusion, creating a style sheet in CSS/XSL and displaying the document in Internet Explorer is an essential skill for web designers and developers. By mastering this skill, we can create web pages that look great and are easy to maintain.