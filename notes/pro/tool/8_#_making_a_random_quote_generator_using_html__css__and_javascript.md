# making A Random Quote Generator using HTML, CSS, and JavaScript

Sure, here's an example of how you can make a random quote generator using HTML, CSS, and JavaScript:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Random Quote Generator</title>
  <style>
    /* Add your CSS styles here */
    body {
      font-family: Arial, sans-serif;
      background-color: #f2f2f2;
      text-align: center;
      padding: 2rem;
    }

    .quote-box {
      background-color: white;
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }

    .quote-text {
      font-size: 1.5rem;
      margin: 1rem 0;
    }

    .quote-author {
      font-size: 1.2rem;
      font-style: italic;
    }

    button {
      background-color: #333;
      color: #fff;
      padding: 0.5rem 1rem;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="quote-box">
    <p class="quote-text">Loading...</p>
    <p class="quote-author">- Unknown</p>
  </div>
  <button>New Quote</button>
  <script>
    /* Add your JavaScript code here */
    const quoteBox = document.querySelector(".quote-box");
    const quoteText = document.querySelector(".quote-text");
    const quoteAuthor = document.querySelector(".quote-author");
    const button = document.querySelector("button");

    const quotes = [
      {
        text: "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",
        author: "Helen Keller"
      },
      {
        text: "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        author: "Winston Churchill"
      },
      {
        text: "Believe you can and you're halfway there.",
        author: "Theodore Roosevelt"
      }
    ];

    function getRandomQuote() {
      return quotes[Math.floor(Math.random() * quotes.length)];
    }

    function displayQuote() {
      const quote = getRandomQuote();
      quoteText.innerText = quote.text;
      quoteAuthor.innerText = `- ${quote.author}`;
    }

    displayQuote();

    button.addEventListener("click", displayQuote);
  </script>
</body>
</html>
```

This code creates a random quote generator that displays a quote and its author in a box. The CSS styles are used to style the page and make it look professional, while the JavaScript code is used to generate a random quote and display it on the page. The button is used to generate a new quote when clicked.
