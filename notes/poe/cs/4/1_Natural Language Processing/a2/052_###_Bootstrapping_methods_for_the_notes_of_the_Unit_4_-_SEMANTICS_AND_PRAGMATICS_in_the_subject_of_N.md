 Here is the content in markdown format:

### Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

Some key points to remember:

1. Bootstrapping is a technique to learn semantic lexicons from a corpus with little or no human annotation. It works by iteratively expanding a seed lexicon using patterns and context.
2. The basic idea is to start with a small seed lexicon of terms with known semantics and use patterns over the lexicon to extract new terms and their possible semantics. The newly extracted terms can then be added to the lexicon and the process repeats.
3. Two common bootstrapping approaches are:
- Pattern bootstrapping: Uses patterns containing lexicon terms to extract new terms and their possible senses. E.g. "X such as Y" where Y is a lexicon term can be used to extract possible senses of X.
- Context bootstrapping: Uses the context around lexicon terms to extract new terms and their possible senses. E.g. terms that co-occur with lexicon terms may have a related sense.

Advantages:
- Requires little human annotation thereby scaling to large corpora.
- Can discover semantic relations and concepts not foreseen by humans.

Disadvantages:
- May introduce errors or biases that propagate through iterations.
- May get stuck in local optima or extract spurious patterns/terms.
- Difficult to determine when to stop the bootstrapping process.

Examples of bootstrapping methods:
- Thesaurus extraction using patterns (Lin, 1998)
- Automatic acquisition of hyponymy relationships (Hearst, 1992)
- Unsupervised semantic lexicon acquisition (Riloff & Jones, 1999)

Applications:
- Automated lexicon acquisition
- Relationship extraction (hyponymy, synonymy, etc.)
- Ontology learning
- Text categorization and clustering

Mnemonics:
- Start small (seed lexicon) and grow (iterate)
- Patterns or context around known terms to find new related terms
- Risk of error propagation and getting stuck in local optima

Let me know if you would like me to elaborate on any of the points or include additional details.