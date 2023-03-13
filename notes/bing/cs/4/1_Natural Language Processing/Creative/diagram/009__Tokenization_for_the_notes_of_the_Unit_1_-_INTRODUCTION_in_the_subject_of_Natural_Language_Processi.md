Tokenization is a common task in natural language processing (NLP). It is the process of breaking down a text into smaller units called tokens, which are usually words or punctuation marks. Tokenization is a crucial step in many NLP tasks, such as part-of-speech tagging and text classification.

The following diagram illustrates the basic process of tokenization in NLP:

```
+---------------------+    +---------------------+    +---------------------+
| Input text          |    | Tokenizer           |    | Output tokens       |
+---------------------+    +---------------------+    +---------------------+
| "Hello, world!"     | -> | Split by whitespace | -> | ["Hello,", "world!"] |
+---------------------+    +---------------------+    +---------------------+
| "I'm learning NLP." | -> | Split by whitespace | -> | ["I'm", "learning", |
+---------------------+    +---------------------+    | "NLP."]              |
                                                     +---------------------+
```

There are different types of tokenizers, such as word tokenizer, sentence tokenizer, character tokenizer, etc. The choice of tokenizer depends on the language and the task. For example, some languages do not have clear word boundaries, such as Chinese or Japanese, so character tokenization may be more suitable. Some tasks may require sentence-level tokens, such as sentiment analysis or summarization, so sentence tokenization may be more appropriate.