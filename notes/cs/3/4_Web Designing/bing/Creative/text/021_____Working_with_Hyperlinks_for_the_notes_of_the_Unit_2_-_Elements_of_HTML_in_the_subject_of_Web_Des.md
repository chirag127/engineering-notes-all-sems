### Working with Hyperlinks

- Hyperlinks are elements of HTML that allow users to navigate from one web page to another or to a different section of the same web page.
- Hyperlinks are created using the `<a>` tag, which stands for anchor. The `<a>` tag has an attribute called `href`, which specifies the destination of the link. The text or image between the opening and closing `<a>` tags is the visible part of the link that the user can click on.
- Example of a hyperlink with text:

```html
<a href="https://www.example.com">Click here to visit Example.com</a>
```

- Example of a hyperlink with an image:

```html
<a href="https://www.example.com"><img src="logo.png" alt="Example logo"></a>
```

- Hyperlinks can have different types depending on the value of the `href` attribute. Some common types are:

  - Absolute links: These links specify the full URL of the destination, including the protocol, domain name, and path. For example, `https://www.example.com/about.html` is an absolute link.
  - Relative links: These links specify the destination relative to the current location of the web page. For example, if the current web page is `https://www.example.com/index.html`, then `about.html` is a relative link that points to `https://www.example.com/about.html`.
  - Fragment links: These links specify a section of the same web page using an identifier preceded by a hash sign (#). For example, if the current web page has a section with an id of "contact", then `#contact` is a fragment link that scrolls to that section.
  - Mailto links: These links specify an email address that opens the user's default email client when clicked. For example, `mailto:info@example.com` is a mailto link that opens a new email message addressed to info@example.com.
  - Tel links: These links specify a phone number that opens the user's default phone app when clicked. For example, `tel:+1234567890` is a tel link that initiates a call to +1234567890.

- Hyperlinks can also have some optional attributes that modify their behavior or appearance. Some common attributes are:

  - `target`: This attribute specifies where to open the destination of the link. The possible values are:
    - `_self`: This is the default value that opens the destination in the same tab or window as the current web page.
    - `_blank`: This value opens the destination in a new tab or window.
    - `_parent`: This value opens the destination in the parent frame of the current web page, if it is inside a frame.
    - `_top`: This value opens the destination in the top-level window of the current web page, if it is inside a frame.
    - A name of a frame: This value opens the destination in the specified frame of the current web page, if it has frames.
  - `title`: This attribute specifies a text that appears when the user hovers over the link. For example, `title="Visit our homepage"` adds a tooltip to the link that says "Visit our homepage".
  - `style`: This attribute specifies a CSS style that applies to the link. For example, `style="color: red; font-weight: bold;"` makes the link red and bold.
  - `class`: This attribute specifies a CSS class that applies to the link. For example, `class="button"` applies the CSS rules defined for the class "button" to the link.
  - `id`: This attribute specifies a unique identifier for the link that can be used for styling or scripting purposes. For example, `id="special-link"` assigns the id "special-link" to the link.