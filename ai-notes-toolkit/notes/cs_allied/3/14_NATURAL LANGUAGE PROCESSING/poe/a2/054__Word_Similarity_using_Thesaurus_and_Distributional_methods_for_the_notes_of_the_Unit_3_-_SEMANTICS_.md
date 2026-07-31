 Here is the formal content in markdown format without any feeling or friendliness for the given topic:

### Word Similarity using Thesaurus and Distributional methods

**Thesaurus-based methods:**

-   Words are represented as sets of synonyms from a thesaurus
-   Similarity is calculated as the overlap between synsets
-   Pros: Captures semantic similarity;Easy to implement
-   Cons: Limited coverage (only includes words in thesaurus);Synonymy is coarse; ignores word order/context

**Distributional methods:**

-   Words are represented as vectors of co-occurrences with context words
-   Similarity is calculated using vector similarity measures (cosine, Jaccard, etc.)
-   Pros: Captures more contextual similarity;applicable to new words/phrases (not just single words)
-   Cons: Vectors can be high-dimensional; hard to interpret; ignores syntactic relationships

**Combined methods:**

-   Combine thesaurus-based and distributional methods
-   Weigh pros/cons of each; tune combination for task
-   Example: Use distributional methods, but "back off" to thesaurus for low-frequency words
-   Can further incorporate other knowledge (e.g. WordNet relations, semantic hierarchies)

The content is written in points and in a formal manner as you asked without any emojis or external links. The content covers the major thesaurus and distributional methods of calculating word similarity which is the topic given. Please let me know if you would like me to modify or add any other points to the content.