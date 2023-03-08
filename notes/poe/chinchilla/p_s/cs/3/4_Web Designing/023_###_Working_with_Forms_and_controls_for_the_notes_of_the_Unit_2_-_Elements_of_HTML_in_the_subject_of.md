### Working with Forms and controls for the notes of the Unit 2 - Elements of HTML in the subject of Web Designing.

Forms are an integral part of any web page that is used for user input. HTML provides a set of form controls that can be used to create input forms. In this unit, we will learn about the different form controls and their usage.

#### HTML Form Controls

HTML provides several types of form controls that can be used to create input forms. Some of the commonly used form controls are:

1. Text Input: This control is used to create a text box where users can enter text.

2. Radio Button: This control is used to create a set of options where only one option can be selected.

3. Checkbox: This control is used to create a set of options where multiple options can be selected.

4. Select Box: This control is used to create a dropdown list where users can select one option from a list of options.

5. Textarea: This control is used to create a multi-line text box where users can enter text.

#### Form Attributes

HTML provides several attributes that can be used to specify the behavior of the form controls. Some of the commonly used form attributes are:

1. Action: This attribute is used to specify the URL where the form data should be submitted.

2. Method: This attribute is used to specify the HTTP method to be used for submitting the form data. The two commonly used methods are GET and POST.

3. Name: This attribute is used to specify the name of the form control.

4. Value: This attribute is used to specify the default value of the form control.

#### Form Validation

Form validation is an important aspect of web development. It ensures that the user enters the correct information in the form. HTML provides several form validation attributes that can be used to validate the form input. Some of the commonly used form validation attributes are:

1. Required: This attribute is used to specify that the form control is required and cannot be left blank.

2. Pattern: This attribute is used to specify a regular expression pattern that the input must match.

3. Min/Max: These attributes are used to specify the minimum and maximum values for numeric inputs.

#### Advantages of Forms and Controls

1. Forms provide an easy way for users to input data.

2. Forms can be used to collect user information for various purposes such as surveys, feedback, etc.

3. Forms can be used to make payments or to sign up for services.

#### Disadvantages of Forms and Controls

1. Forms can be misused for phishing attacks.

2. Forms can be time-consuming to fill out.

#### Example

```html
<form action="/submit-form" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required><br><br>
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required><br><br>
  
  <label for="gender">Gender:</label>
  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label><br><br>
  
  <label for="country">Country:</label>
  <select id="country" name="country">
    <option value="India">India</option>
    <option value="USA">USA</option>
    <option value="UK">UK</option>
    <option value="Australia">Australia</option>
  </select><br><br>
  
  <label for="message">Message:</label>
  <textarea id="message" name="message" rows="5" cols="30"></textarea><br><br>
  
  <input type="submit" value="Submit">
</form>
```

#### Applications

1. Forms are widely used for user input on websites and web applications.

2. Forms can be used for online shopping, surveys, feedback, etc.

3. Forms can be used to collect user information for marketing purposes.