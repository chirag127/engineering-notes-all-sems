 Here are the notes for the topic -

### Create a style sheet in CSS/ XSL & display the document in internet explorer

1. Cascading Style Sheets (CSS) - CSS is a style sheet language used to style an XML document. It separates the presentation of a document from the document's content.
Advantages -
- Faster loading web pages as the styling is in a separate CSS file rather than in the HTML document.
- Easy maintenance as the style is defined in a single CSS file which can be used by multiple HTML documents.
- Web accessibility is improved as the users can select their own style sheet.

2. Creating a CSS style sheet -
- Write CSS rules within braces { }.
- Use selectors to select the element(s) you want to style. Eg. h1 { }, p { }
- Declare properties and assign values to them. Eg. color: red; font-size: 16px;
- You can specify styles for different media types like screen, print, handheld, etc. Use @media rule for this.
- Comments can be added using /* This is a comment */

3. Applying CSS to HTML -
- Inline - Using the style attribute in HTML elements. <h1 style="color:red;">
- Internal stylesheet - Using a <style> element in the head section of the HTML document.
- External stylesheet - Using a link to an external .css file within the <link> element in the HTML head section.
<link rel="stylesheet" href="styles.css">

4. Extensible Stylesheet Language Transformations (XSLT) -
- XSLT is a language used to transform an XML document into another format (like converting XML to HTML to display in a browser).
- It uses templates with patterns to match nodes in the source document and outputs elements in the result tree.
- An XSLT processor is required to perform the transformation.

5. Displaying the styled document in Internet Explorer -
- Internet Explorer (IE) supports CSS and can apply styles to HTML elements.
- To display an XML document styled using XSLT, set the content-type to "text/xml" and include a <?xml-stylesheet> processing instruction pointing to the XSLT stylesheet in the XML document. IE will then automatically apply the XSLT and display the output.