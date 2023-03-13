### CSS in Web Page Designing

- CSS stands for Cascading Style Sheets. It is a language that defines how HTML elements are displayed on a web page.
- CSS can be used to control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the web page design.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.
  - Inline CSS is written inside the style attribute of an HTML element. It affects only that element and has the highest priority.
  - Internal CSS is written inside the style element in the head section of an HTML document. It affects all the elements in that document and has the second highest priority.
  - External CSS is written in a separate file with the .css extension and linked to the HTML document using the link element in the head section. It affects all the elements in the linked documents and has the lowest priority.
- CSS uses selectors to target HTML elements and apply styles to them. There are different types of selectors, such as element, class, id, attribute, pseudo-class, and pseudo-element selectors.
  - Element selectors match HTML elements by their tag name, such as p, h1, div, etc.
  - Class selectors match HTML elements by their class attribute value, such as .red, .big, .center, etc. They are preceded by a dot (.).
  - Id selectors match HTML elements by their id attribute value, such as #header, #footer, #main, etc. They are preceded by a hash (#).
  - Attribute selectors match HTML elements by their attribute name or value, such as [href], [src="logo.png"], [type="checkbox"], etc. They are enclosed in square brackets ([]).
  - Pseudo-class selectors match HTML elements based on their state or position, such as :hover, :active, :first-child, :nth-child, etc. They are preceded by a colon (:).
  - Pseudo-element selectors match parts of HTML elements, such as ::before, ::after, ::first-line, ::first-letter, etc. They are preceded by two colons (::).
- CSS uses properties and values to define the styles for the selected elements. There are hundreds of properties, such as color, font-family, font-size, width, height, display, position, etc. Each property has a set of possible values, such as red, Arial, 16px, 100%, block, relative, etc.
- CSS uses rules to combine selectors, properties, and values. A rule consists of a selector and a declaration block. A declaration block contains one or more declarations, each consisting of a property and a value, separated by a colon and ending with a semicolon. A rule is written as follows:

  selector {
    property: value;
    property: value;
    ...
  }

- CSS uses the cascade to resolve conflicts between multiple rules that apply to the same element. The cascade follows a set of rules to determine which rule has more specificity and precedence. The rules are as follows:
  - If a property is inherited from the parent element, the inherited value has the lowest specificity and precedence.
  - If a property is defined by the browser's default style sheet, the default value has the second lowest specificity and precedence.
  - If a property is defined by an external style sheet, the external value has the third lowest specificity and precedence.
  - If a property is defined by an internal style sheet, the internal value has the fourth lowest specificity and precedence.
  - If a property is defined by an inline style, the inline value has the highest specificity and precedence.
  - If a property is defined by multiple rules with the same specificity and precedence, the rule that comes later in the source order has more precedence.
- CSS uses the box model to describe how the size and spacing of an element are calculated. The box model consists of four parts: content, padding, border, and margin.
  - Content is the actual text or image inside the element.
  - Padding is the space between the content and the border of the element. It can be set using the padding property or the padding-top, padding-right, padding-bottom, and padding-left properties.
  - Border is the line that surrounds the element. It can be set using the border property or the border-width, border-style, and border-color properties.
  - Margin is the space between the border of the element and the adjacent elements. It can be set using the margin property or the margin-top, margin-right, margin-bottom, and margin-left properties.
- CSS uses the display property to determine how an element is rendered on the web page. The display property can have different values, such as block, inline, inline-block, none, flex, grid,