Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some steps to create a style sheet in CSS and display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab.

- A style sheet is a set of rules that define how to style and format the elements of a web page. There are three ways to add CSS to an HTML document: inline, internal, and external .
- Inline CSS means adding the style attribute to each HTML element and specifying the CSS properties and values. This method is not recommended as it makes the HTML code messy and hard to maintain.
- Internal CSS means adding a <style> element inside the <head> section of the HTML document and writing the CSS rules inside it. This method is useful for applying styles to a single web page, but not for multiple pages that share the same style.
- External CSS means creating a separate file with the .css extension and writing the CSS rules inside it. This method is the most common and preferred way to add CSS, as it allows you to change the look of an entire website by changing just one file. To link an external CSS file to an HTML document, you need to use the <link> element inside the <head> section and specify the href attribute with the URL of the CSS file, the rel attribute with the value "stylesheet", and the type attribute with the value "text/css" .
- To create a style sheet in CSS, you need to follow the syntax of CSS, which consists of selectors and declarations. A selector is the name of an HTML element or a class or an id that you want to style. A declaration is a pair of a property and a value that defines how to style the selector. A declaration is enclosed in curly braces and consists of a property name followed by a colon and a value. Multiple declarations are separated by semicolons. Multiple selectors can be grouped together by separating them with commas. For example, the following CSS code styles the <h1> and <p> elements with different colors and fonts:

```css
h1, p {
  color: blue;
  font-family: Arial;
}

h1 {
  font-size: 36px;
}

p {
  font-size: 18px;
}
```

- To display the document in internet explorer, you need to save the HTML file and the CSS file in the same folder on your computer. Then, you can open the HTML file with internet explorer and see the effect of the CSS style sheet. Alternatively, you can upload the files to a web server and access them through a URL. You can also use the developer tools in internet explorer to inspect and modify the CSS rules and see the changes in real time. To open the developer tools, press F12 or click on the Tools menu and select Developer Tools.