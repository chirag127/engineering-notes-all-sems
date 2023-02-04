# making  A Contact Form using HTML, CSS, and JavaScript

Of course! Here's an example of how you could create a beautiful, professional, and well-featured contact form using HTML, CSS, and JavaScript:

HTML:
```
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Contact Form</title>
  <style>
    /* Add your CSS styles here */
  </style>
</head>
<body>
  <div class="container">
    <h1>Contact Us</h1>
    <form id="contact-form">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
      </div>
      <div class="form-group">
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
  <script>
    /* Add your JavaScript code here */
  </script>
</body>
</html>
```

CSS:
```
/* Add your CSS styles here */
.container {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 10px;
}

.form-group {
  margin: 20px 0;
  text-align: left;
}

label {
  font-weight: bold;
}

input, textarea {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-top: 10px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px;
}

button:hover {
  background-color: #3e8e41;
}
```

JavaScript:
```
/* Add your JavaScript code here */
const form = document.querySelector("#contact-form");

form.addEventListener("submit", function(event) {
  event.preventDefault();
  const name = document.querySelector("#name").value;
  const email = document.querySelector("#email").value;
  const message = document.querySelector("#message").value;
  
  // Add your form submission logic here
});
```

Note that this is just a basic example and you can customize it further to fit your needs.
