# Validation of Forms for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing

- Validation of forms is the process of checking the user input data against a set of rules or constraints before submitting it to the server.
- Validation of forms can be done on the client side or the server side, or both.
- Client side validation is performed by the web browser using HTML, CSS, and JavaScript, before sending the data to the server.
- Client side validation has the following advantages:
  - It provides faster feedback to the user, without reloading the page or waiting for the server response.
  - It reduces the network traffic and the server load, by preventing invalid or incomplete data from being sent to the server.
  - It enhances the user experience and the usability of the web form, by providing interactive and dynamic features, such as highlighting errors, disabling submit buttons, or showing hints.
- Client side validation has the following disadvantages:
  - It can be bypassed or disabled by the user, by modifying the HTML code, disabling JavaScript, or using a different browser or device.
  - It does not guarantee the security or the integrity of the data, as the user can still send malicious or forged data to the server.
  - It may not be consistent or compatible across different browsers or devices, as they may have different implementations or interpretations of the validation rules or features.
- Therefore, client side validation should not be used as the only method of validation, but as a complement to the server side validation, which is more reliable and secure.
- There are two different types of client side validation that you'll encounter on the web:
  - Built-in form validation uses HTML form validation features, such as the `required`, `pattern`, `min`, `max`, `type`, or `step` attributes, which define the validation rules for each input element. The browser will automatically check the validity of the input data and display a default error message if it is invalid. This validation generally doesn't require much JavaScript, but it may not be supported by older browsers or customized by the developer.
  - Custom form validation uses JavaScript code to define and implement the validation logic and the error handling for each input element. The developer can use the `ValidityState` object or the `checkValidity()` and `setCustomValidity()` methods to access and manipulate the validity state of the input elements. The developer can also use CSS selectors or classes to style the input elements and the error messages according to their validity state. This validation gives more flexibility and control to the developer, but it requires more coding and testing.