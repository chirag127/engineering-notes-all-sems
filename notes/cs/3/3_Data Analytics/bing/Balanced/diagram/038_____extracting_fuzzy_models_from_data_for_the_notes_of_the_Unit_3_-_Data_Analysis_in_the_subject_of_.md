### Extracting fuzzy models from data

- Fuzzy models are mathematical means of representing vagueness and imprecise information (hence the term fuzzy) .
- Fuzzy models have the capability of recognising, representing, manipulating, interpreting, and using data and information that are vague and lack certainty .
- Fuzzy models are useful for dealing with data and information that are typical of Big Data, such as vague, uncertain and imprecise data .
- Fuzzy models can also provide interpretable results, which is important for understanding and explaining the data analysis process .
- There are different types of fuzzy models, such as fuzzy sets, fuzzy logic, fuzzy rules, fuzzy systems, fuzzy clustering, fuzzy classification, fuzzy regression, etc.  .
- Each type of fuzzy model has its own methods and algorithms for extracting fuzzy models from data, such as fuzzy c-means, fuzzy subtractive clustering, fuzzy inference systems, etc.  .
- The general steps for extracting fuzzy models from data are:

  - Preprocessing the data, such as normalising, scaling, filtering, etc.
  - Selecting the appropriate type of fuzzy model and the parameters, such as the number of fuzzy sets, the membership functions, the fuzzy operators, etc.
  - Applying the learning algorithm to the data, such as clustering, rule extraction, parameter estimation, etc.
  - Evaluating the performance and quality of the fuzzy model, such as accuracy, validity, interpretability, etc.
  - Refining or modifying the fuzzy model if needed, such as adding or deleting fuzzy sets, rules, etc.
  - Applying the fuzzy model to new data or scenarios, such as prediction, classification, decision making, etc.

- The following diagram illustrates the general steps for extracting fuzzy models from data:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Data          |       |  Fuzzy Model   |       |  Application   |
|  Preprocessing |  ---> |  Extraction    |  ---> |  of Fuzzy      |
|                |       |                |       |  Model         |
+----------------+       +----------------+       +----------------+
      ^                         ^   |                     |
      |                         |   v                     |
      |                         | +----------------+      |
      |                         +-|  Evaluation     |<----+
      |                           |  and Refinement |
      |                           +----------------+
      |
      +-----------------------------+
                                    |
                                    v
                              +----------------+
                              |                |
                              |  Data          |
                              |                |
                              +----------------+
```