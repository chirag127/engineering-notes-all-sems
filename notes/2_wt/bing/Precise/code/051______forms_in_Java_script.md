#### Forms in JavaScript

Here is an example of a simple form in JavaScript:

```javascript
// Get the form element
var form = document.getElementById('myForm');

// Add an event listener to the form
form.addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get the form data
    var formData = new FormData(form);

    // Log the form data to the console
    for (var pair of formData.entries()) {
        console.log(pair[0] + ': ' + pair[1]);
    }
});
```
