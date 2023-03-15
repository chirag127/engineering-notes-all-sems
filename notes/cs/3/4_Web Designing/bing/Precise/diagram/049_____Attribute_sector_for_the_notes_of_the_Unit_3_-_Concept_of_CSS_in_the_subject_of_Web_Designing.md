### Attribute Selector

Attribute selectors are used to select elements based on their attribute values. They are written inside square brackets `[]`. Here are some examples:

1. `[attribute]`: This selector matches all elements with the specified attribute. For example, `input[type]` selects all `input` elements that have a `type` attribute.

2. `[attribute=value]`: This selector matches all elements with the specified attribute and value. For example, `input[type=text]` selects all `input` elements that have a `type` attribute with the value `text`.

3. `[attribute~=value]`: This selector matches all elements with the specified attribute whose value contains the specified value as one of a space-separated list of words. For example, `p[class~=example]` selects all `p` elements that have a `class` attribute containing the word `example`.

4. `[attribute|=value]`: This selector matches all elements with the specified attribute whose value is either exactly the specified value or begins with the specified value immediately followed by a hyphen `-`. For example, `p[lang|=en]` selects all `p` elements that have a `lang` attribute with the value `en` or beginning with `en-`.

5. `[attribute^=value]`: This selector matches all elements with the specified attribute whose value begins with the specified value. For example, `a[href^=https]` selects all `a` elements that have an `href` attribute value beginning with `https`.

6. `[attribute$=value]`: This selector matches all elements with the specified attribute whose value ends with the specified value. For example, `a[href$=.pdf]` selects all `a` elements that have an `href` attribute value ending with `.pdf`.

7. `[attribute*=value]`: This selector matches all elements with the specified attribute whose value contains the specified value as a substring. For example, `a[href*=example]` selects all `a` elements that have an `href` attribute value containing the substring `example`.

These are some of the attribute selectors that can be used in CSS to select elements based on their attribute values. They provide a powerful way to select elements and apply styles to them.