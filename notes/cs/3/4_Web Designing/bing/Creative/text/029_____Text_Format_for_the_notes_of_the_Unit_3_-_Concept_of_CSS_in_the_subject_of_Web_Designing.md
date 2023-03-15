### Text Format for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page.
- CSS can be used to control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the presentation of HTML elements.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.
  - Inline CSS is written inside the `style` attribute of an HTML element. It affects only that element and has the highest priority.
  - Internal CSS is written inside the `<style>` tag in the `<head>` section of an HTML document. It affects all the elements in that document and has the second highest priority.
  - External CSS is written in a separate file with the `.css` extension and linked to an HTML document using the `<link>` tag in the `<head>` section. It affects all the elements in the linked document and has the lowest priority.
- CSS uses selectors to target HTML elements and apply styles to them. Selectors can be based on element names, classes, ids, attributes, pseudo-classes, pseudo-elements, or combinations of them.
- CSS uses properties and values to define the styles for the selected elements. Properties are the aspects of the presentation that can be controlled, such as `color`, `font-size`, `width`, etc. Values are the specific settings for the properties, such as `red`, `16px`, `50%`, etc.
- CSS uses rules to group selectors and declarations. A rule consists of a selector followed by a declaration block. A declaration block contains one or more declarations separated by semicolons. A declaration consists of a property and a value separated by a colon.
- CSS follows a cascading order to resolve conflicts between multiple rules that apply to the same element. The order is based on the following factors: specificity, importance, and source order.
  - Specificity is a measure of how precise a selector is. A more specific selector has a higher priority than a less specific one. The specificity of a selector is calculated based on the number of ids, classes, attributes, and elements it contains.
  - Importance is a way of overriding the specificity of a selector by using the `!important` keyword after a value. A declaration with `!important` has a higher priority than a declaration without it, regardless of the specificity of the selector.
  - Source order is the order in which the rules appear in the source code. A rule that comes later has a higher priority than a rule that comes earlier, if they have the same specificity and importance.