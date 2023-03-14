Tokenization is the process of breaking down a text into smaller units called tokens. In the context of natural language processing, tokens are usually words or punctuation marks. Tokenization is a crucial step in many NLP tasks, such as part-of-speech tagging and text classification .

The following diagram illustrates the basic architecture of a tokenization process:

```
+-----------------+     +-----------------+     +-----------------+
| Input text      |     | Tokenizer       |     | Output tokens   |
|                 |     |                 |     |                 |
| "Hello, world!" | --> | White space     | --> | ["Hello", ",",  |
|                 |     | based           |     | "world", "!"]   |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows an example of white space based tokenization, which is the simplest tokenization technique. It splits the input text whenever a white space is encountered. However, this technique may not work for languages that do not use white spaces to separate words, such as Chinese or Japanese. Other tokenization techniques include dictionary based, rule based, and subword based tokenization . Each technique has its own advantages and disadvantages depending on the language and the task.