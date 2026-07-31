# HTML Tags

- HTML tags are the building blocks of HTML documents. They are used to define the structure and content of a web page.
- HTML tags are enclosed in angle brackets (< and >). They usually come in pairs, with a start tag and an end tag. For example, `<p>` and `</p>` are the start and end tags for a paragraph element.
- Some HTML tags are self-closing, meaning they do not need an end tag. They are written with a slash (/) before the closing bracket. For example, `<img src="image.jpg" />` is a self-closing tag for an image element.
- HTML tags can have attributes, which are additional information that modify the behavior or appearance of the element. Attributes are written inside the start tag, after the tag name, in the form of name-value pairs separated by an equal sign (=). For example, `<a href="https://www.example.com">` is a start tag for an anchor element, with an attribute named href and a value of https://www.example.com.
- HTML tags are case-insensitive, meaning they can be written in uppercase, lowercase, or a mixture of both. However, it is a good practice to use lowercase for consistency and readability.
- HTML tags must follow the syntax rules of HTML, which are based on the XML standard. Some of the rules are:

  - Every start tag must have a corresponding end tag, unless it is a self-closing tag.
  - Nested tags must be properly closed in the reverse order of opening. For example, `<p><strong>Hello</strong> world</p>` is valid, but `<p><strong>Hello</p></strong>` is not.
  - Attribute values must be enclosed in quotation marks, either single (') or double ("). For example, `<img src="image.jpg" />` is valid, but `<img src=image.jpg />` is not.
  - Attribute names must be unique within a tag. For example, `<img src="image.jpg" alt="Image" />` is valid, but `<img src="image.jpg" src="another.jpg" />` is not.