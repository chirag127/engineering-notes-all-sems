 Here is the content in markdown format with formal tone and without any emojis or external links:

#### Forms in JavaScript

1. Introduction to Forms
- Forms are a collection of form elements/controls that allow users to enter data.
- Form elements include input fields, radio buttons, checkboxes, submit buttons, etc.
- The data from forms is sent to a server for processing using HTTP methods GET or POST.

2. Accessing Form Elements
- Form elements can be accessed using their id, name, class, tag name, etc.
- For example: document.getElementById('id'), document.getElementsByName('name'), document.getElementsByClassName('class'), etc.
- The elements can then be read or modified using properties and methods.

3. Submitting a Form
- The form is submitted using the submit() method on the form.
- For example: formObject.submit()
- The submitted data can be accessed on the server side to be processed.
- Preventing default submission action: The default submission behavior can be prevented using e.preventDefault() on the submit event. This is useful when you want to perform client side validation or processing before sending the data to the server.

4. Form Validation
- Form validation is essential to ensure correct user input.
- It can be done on both client side (using JavaScript) and server side (using a server side programming language like PHP, Java, etc.).
- Client side validation is faster but can be bypassed, server side validation is more secure but results in latency.
- Common validations include checking for required fields, data type, length, format, etc.

5. Conclusion
- Forms are an important way to collect user input data.
- JavaScript can be used to access form elements, modify them and validate user input.
- The data can then be sent to the server for subsequent processing using HTTP methods.