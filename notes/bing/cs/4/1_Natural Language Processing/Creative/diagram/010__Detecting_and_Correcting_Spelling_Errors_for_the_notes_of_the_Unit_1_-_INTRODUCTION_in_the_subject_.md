The following diagram illustrates the basic architecture of a spell checker system for detecting and correcting spelling errors in natural language processing. The diagram is drawn using ASCII characters.

```
+-----------------+     +-----------------+     +-----------------+
| Input text      |     | Tokenizer       |     | Spelling errors |
|                 |---->|                 |---->|                 |
| e.g. I liek NLP |     | e.g. I, liek, NLP|     | e.g. liek       |
+-----------------+     +-----------------+     +-----------------+
                                        |       |
                                        |       |
                                        v       v
                                  +-----------------+
                                  | Dictionary      |
                                  |                 |
                                  | e.g. like, lake |
                                  +-----------------+
                                        |       |
                                        |       |
                                        v       v
+-----------------+     +-----------------+     +-----------------+
| Suggestions     |     | Scorer          |     | Output text     |
|                 |<----|                 |<----|                 |
| e.g. like, lake |     | e.g. edit dist. |     | e.g. I like NLP |
+-----------------+     +-----------------+     +-----------------+
```