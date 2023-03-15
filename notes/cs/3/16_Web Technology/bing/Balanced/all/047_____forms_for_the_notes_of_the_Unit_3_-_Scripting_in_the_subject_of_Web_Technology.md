Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of forms for the Unit 3 - Scripting.

# Forms

- Forms are HTML elements that allow users to enter data or make choices on a web page.
- Forms consist of one or more form controls, such as text fields, checkboxes, radio buttons, drop-down lists, buttons, etc.
- Forms can be used for various purposes, such as collecting user information, conducting surveys, submitting orders, performing calculations, etc.
- Forms are enclosed by the `<form>` tag, which has two attributes: `action` and `method`.
  - The `action` attribute specifies the URL of the server-side script that will process the form data.
  - The `method` attribute specifies the HTTP method to use when sending the form data. The two common methods are `GET` and `POST`.
    - The `GET` method appends the form data to the URL as a query string, and is suitable for short and non-sensitive data.
    - The `POST` method sends the form data as part of the request body, and is suitable for long and sensitive data.
- Each form control has a `name` attribute, which identifies the data entered by the user.
- Some form controls also have a `value` attribute, which specifies the default or initial value of the control.
- Some form controls also have a `type` attribute, which specifies the kind of input expected by the control. For example, `type="text"` for a text field, `type="password"` for a password field, `type="checkbox"` for a checkbox, etc.
- Some form controls also have a `checked` attribute, which specifies whether the control is selected by default. For example, `checked` for a checkbox or a radio button.
- Some form controls also have a `disabled` attribute, which specifies whether the control is disabled or not. A disabled control cannot be edited or clicked by the user.
- Some form controls also have a `required` attribute, which specifies whether the control is mandatory or not. A required control must be filled or selected by the user before submitting the form.
- Some form controls also have a `placeholder` attribute, which specifies a hint or a sample value for the control. The placeholder text is displayed inside the control when it is empty, and disappears when the user starts typing.
- Some form controls also have a `pattern` attribute, which specifies a regular expression that the input value must match. The pattern is used to validate the input value before submitting the form.
- Some form controls also have a `min` and `max` attribute, which specify the minimum and maximum value or length of the input value. The min and max are used to limit the range of the input value before submitting the form.
- Some form controls also have a `step` attribute, which specifies the increment or decrement value of the input value. The step is used to adjust the input value before submitting the form.
- Some form controls also have a `size` attribute, which specifies the width of the control in characters. The size is used to adjust the appearance of the control on the web page.
- Some form controls also have a `maxlength` attribute, which specifies the maximum number of characters that the user can enter in the control. The maxlength is used to limit the input value before submitting the form.
- Some form controls also have a `multiple` attribute, which specifies whether the user can select more than one option from the control. For example, `multiple` for a drop-down list or a file input.
- Some form controls also have a `accept` attribute, which specifies the file types that the user can select from the control. For example, `accept="image/*"` for a file input that accepts only images.
- Some form controls also have a `autocomplete` attribute, which specifies whether the browser can suggest or fill the input value based on the user's previous entries. For example, `autocomplete="on"` or `autocomplete="off"` for a text field.
- Some form controls also have a `autofocus` attribute, which specifies whether the control should get the focus when the web page loads. For example, `autofocus` for a text field that the user should fill first.
- Some form controls also have a `list` attribute, which specifies the id of a `<datalist>` element that contains a list of predefined options for the control. For example, `list="countries"` for a text field that can choose from a list of countries.
- The `<datalist>` element is used to create a list of options for a form control. The `<datalist>` element contains one or