### Rule-based for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Word level analysis is the task of identifying and processing the basic units of meaning in a natural language, such as words, morphemes, and lexemes.
- Rule-based word level analysis is an approach that relies on predefined rules and grammars to analyze and manipulate natural language data.
- Rule-based word level analysis can be divided into two subtasks: morphological analysis and lexical analysis.

#### Morphological analysis
- Morphological analysis is the process of identifying and describing the structure and formation of words in a natural language.
- Morphological analysis involves breaking down words into their smallest meaningful units, called morphemes, and determining their part of speech, number, tense, aspect, mood, etc.
- Morphemes can be classified into two types: free morphemes and bound morphemes.
  - Free morphemes are morphemes that can stand alone as words, such as cat, dog, run, etc.
  - Bound morphemes are morphemes that cannot stand alone as words, but modify the meaning or function of other morphemes, such as -s, -ed, -ing, etc.
- Morphological analysis can be performed by using two methods: segmentation and generation.
  - Segmentation is the process of splitting a word into its constituent morphemes, such as cats -> cat + -s, running -> run + -ing, etc.
  - Generation is the process of combining morphemes to form a word, such as cat + -s -> cats, run + -ing -> running, etc.
- Rule-based morphological analysis uses a set of rules and a lexicon to perform segmentation and generation.
  - A rule is a statement that specifies how a morpheme or a word can be formed or modified, such as -s -> plural, -ed -> past tense, etc.
  - A lexicon is a list of words and their properties, such as part of speech, number, gender, etc.
  - For example, to segment the word cats, a rule-based morphological analyzer would look up the word in the lexicon and find that it is a noun, then apply the rule -s -> plural to split it into cat and -s.
  - To generate the word cats, a rule-based morphological analyzer would take the morphemes cat and -s, look up their properties in the lexicon, and apply the rule plural -> -s to combine them into cats.

#### Lexical analysis
- Lexical analysis is the process of identifying and categorizing the words and tokens in a natural language text.
- Lexical analysis involves splitting a text into its individual words or tokens, and assigning them a lexical category or part of speech, such as noun, verb, adjective, etc.
- Lexical analysis can be performed by using two methods: tokenization and part-of-speech tagging.
  - Tokenization is the process of splitting a text into its individual words or tokens, such as "The cat is black." -> "The", "cat", "is", "black", "." etc.
  - Part-of-speech tagging is the process of assigning a lexical category or part of speech to each word or token, such as "The" -> determiner, "cat" -> noun, "is" -> verb, "black" -> adjective, "." -> punctuation, etc.
- Rule-based lexical analysis uses a set of rules and a lexicon to perform tokenization and part-of-speech tagging.
  - A rule is a statement that specifies how a word or a token can be identified or categorized, such as a word that ends with -s is a plural noun, a word that follows a determiner is a noun, etc.
  - A lexicon is a list of words and their properties, such as part of speech, number, gender, etc.
  - For example, to tokenize and tag the sentence "The cat is black.", a rule-based lexical analyzer would split the sentence into tokens by using whitespace and punctuation as delimiters, then look up each token in the lexicon and assign it a part of speech, and finally apply the rules to check and correct the tags if needed.

#### Advantages and disadvantages of rule-based word level analysis
- Rule-based word level analysis has some advantages, such as:
  - It is transparent and explainable, as the rules and the lexicon are explicitly defined and can be inspected and modified.
  - It is consistent and reliable, as it always produces the same output for the same input, and does not depend on external factors such as data quality or availability