A grammar-based language model (LM) is a type of LM that uses a formal grammar to generate sentences and assign probabilities to them. A grammar is a set of rules that define the syntax and structure of a language. A grammar-based LM can capture the long-range dependencies and hierarchical structure of natural language better than a n-gram LM, which only considers a fixed number of previous words. However, a grammar-based LM is also more complex and computationally expensive than a n-gram LM.

The following diagram illustrates the basic architecture of a grammar-based LM:

```
+-----------------+    +-----------------+    +-----------------+
| Sentence        |    | Grammar         |    | Probability     |
| Generator       |    | Parser          |    | Estimator       |
+-----------------+    +-----------------+    +-----------------+
| Input:          |    | Input:          |    | Input:          |
| A grammar G     |    | A sentence S    |    | A parse tree T  |
| Output:         |    | Output:         |    | Output:         |
| A sentence S    |    | A parse tree T  |    | A probability P |
| that conforms   |    | that represents |    | that represents |
| to G            |    | the syntactic   |    | the likelihood  |
|                 |    | structure of S  |    | of T given G    |
+-----------------+    +-----------------+    +-----------------+
        |                     ^                      ^
        |                     |                      |
        +---------------------+----------------------+
```

The sentence generator takes a grammar G as input and outputs a sentence S that conforms to G. The grammar parser takes a sentence S as input and outputs a parse tree T that represents the syntactic structure of S. The probability estimator takes a parse tree T as input and outputs a probability P that represents the likelihood of T given G. The probability of a sentence S given a grammar G is then the product of the probabilities of all the parse trees that can be derived from S using G.