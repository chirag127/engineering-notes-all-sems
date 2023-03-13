Rule-based word level analysis in natural language processing is a method of processing natural language by applying a set of predefined rules that specify how to segment, label, and parse text data. Rule-based word level analysis can perform tasks such as tokenization, part-of-speech tagging, stemming, lemmatization, and morphological analysis. The following diagram illustrates the basic architecture of a rule-based word level analysis system:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input text   +---->+  Tokenization  +---->+  Part-of-speech|
|                |     |                |     |     tagging    |
+----------------+     +----------------+     +----------------+
                                             / \
                                            /   \
                                           /     \
                                          /       \
                                         /         \
                                        /           \
                                       /             \
                                      /               \
                                     /                 \
                                    /                   \
                                   /                     \
                                  /                       \
                                 /                         \
                                /                           \
                               /                             \
                              /                               \
                             /                                 \
                            /                                   \
                           /                                     \
                          /                                       \
                         /                                         \
                        /                                           \
                       /                                             \
                      /                                               \
                     /                                                 \
                    /                                                   \
                   /                                                     \
                  /                                                       \
                 /                                                         \
                /                                                           \
               /                                                             \
              /                                                               \
             /                                                                 \
            /                                                                   \
           /                                                                     \
          /                                                                       \
         /                                                                         \
        /                                                                           \
       /                                                                             \
      /                                                                               \
     /                                                                                 \
    /                                                                                   \
   /                                                                                     \
  /                                                                                       \
 /                                                                                         \
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Stemming and  +---->+ Morphological  +---->+  Parsing and   +---->+  Output text   |
| lemmatization  |     |   analysis     |     |  syntactic     |     |                |
|                |     |                |     |  analysis      |     +----------------+
+----------------+     +----------------+     +----------------+
```