### Validation of Forms for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing

- Validation of forms is the process of checking the user input data against a set of rules or constraints before submitting it to the server.
- Validation of forms can be done on the client side or the server side, or both.
- Client side validation is performed by the web browser using HTML, CSS, or JavaScript, before sending the data to the server.
- Client side validation has the following advantages:
  - It provides faster feedback to the user, without reloading the page or waiting for the server response.
  - It reduces the network traffic and the server load, by preventing invalid or incomplete data from being sent.
  - It enhances the user experience and the usability of the web form, by providing clear and immediate error messages and hints.
- Client side validation has the following disadvantages:
  - It can be bypassed or disabled by the user, by modifying the browser settings or the source code of the web page.
  - It may not be compatible with all browsers or devices, especially older or non-standard ones.
  - It may not be sufficient or secure enough for some types of data, such as passwords, credit card numbers, or personal information, which require server side validation as well.
- There are two main approaches to client side validation:
  - Display the errors one by one, focusing on the offending field. This approach is more user-friendly and less cluttered, but it may require more JavaScript code and event handlers.
  - Display all errors simultaneously, server side validation style. This approach is more consistent and simple, but it may overwhelm the user with too many error messages at once.
- There are two main methods to implement client side validation:
  - Use the built-in form validation features of HTML5, such as the `required`, `pattern`, `min`, `max`, `minlength`, `maxlength`, `type`, and `step` attributes, and the `:valid` and `:invalid` pseudo-classes of CSS. This method is easy and convenient, but it may not be supported by all browsers or customized to fit the design of the web page.
  - Use JavaScript to validate the form values, using the `onsubmit`, `onchange`, `onblur`, `onfocus`, or `oninput` events, and the `checkValidity()`, `setCustomValidity()`, `reportValidity()`, and `validity` properties and methods of the `HTMLFormElement` and `HTMLInputElement` objects. This method is more flexible and powerful, but it may require more coding and testing.