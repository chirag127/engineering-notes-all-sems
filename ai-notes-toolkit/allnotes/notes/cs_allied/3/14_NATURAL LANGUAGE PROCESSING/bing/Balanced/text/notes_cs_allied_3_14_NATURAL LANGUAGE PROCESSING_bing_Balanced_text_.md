

# Natural Language Processing

Natural language processing (NLP) is an interdisciplinary subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data.

Some of the main goals and applications of NLP are:

- To enable computers to understand, interpret and manipulate human language, such as text and speech, in much the same way human beings can.
- To develop systems that can perform tasks such as machine translation, speech recognition, sentiment analysis, information extraction, text summarization, question answering, natural language generation, and more.
- To advance the state of the art in natural language understanding and generation, by using techniques such as deep learning, rule-based modeling, statistical methods, and knowledge representation .
- To leverage the power of natural language processing to enhance various domains and industries, such as education, health care, business, social media, entertainment, and more.

Some of the main challenges and limitations of NLP are:

- To deal with the ambiguity, variability, and complexity of natural language, which can have different meanings, structures, and contexts depending on the situation, speaker, and listener.
- To cope with the diversity and evolution of natural language, which can have different dialects, accents, slang, idioms, and neologisms depending on the culture, region, and time.
- To bridge the gap between natural language and formal logic, which can have different levels of abstraction, expressiveness, and inference depending on the domain, task, and goal.
- To balance the trade-off between generality and specificity, which can have different degrees of accuracy, efficiency, and robustness depending on the data, model, and algorithm.



## Unit 1 - INTRODUCTION

- This unit introduces the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI can be divided into two main branches: symbolic AI and sub-symbolic AI.
  - Symbolic AI uses logic, rules, and symbols to represent and manipulate knowledge. Examples of symbolic AI include expert systems, knowledge bases, and logic programming.
  - Sub-symbolic AI uses numerical and statistical methods to model and learn from data. Examples of sub-symbolic AI include neural networks, evolutionary algorithms, and reinforcement learning.
- AI can also be classified according to the type and complexity of the problems it addresses. Some common types of AI problems are:
  - Search: finding a solution or an optimal path in a large space of possibilities. Examples of search problems include pathfinding, planning, and game playing.
  - Optimization: finding the best or most efficient solution among a set of alternatives. Examples of optimization problems include scheduling, resource allocation, and design.
  - Classification: assigning a label or a category to an input based on some criteria. Examples of classification problems include spam filtering, face recognition, and sentiment analysis.
  - Regression: predicting a numerical value or a function based on some input. Examples of regression problems include curve fitting, stock market prediction, and weather forecasting.
  - Clustering: grouping similar or related inputs together based on some measure of similarity or distance. Examples of clustering problems include image segmentation, customer segmentation, and anomaly detection.
  - Natural language processing: understanding and generating natural language texts or speech. Examples of natural language processing problems include machine translation, speech recognition, and text summarization.
  - Computer vision: processing and interpreting visual information from images or videos. Examples of computer vision problems include object detection, face recognition, and scene understanding.
  - Machine learning: creating systems that can learn from data and improve their performance over time. Examples of machine learning problems include supervised learning, unsupervised learning, and reinforcement learning.



### Origins and challenges of NLP

- Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.
- The origins of NLP can be traced back to the early attempts to use computers for translation, information retrieval, and text analysis in the 1950s and 1960s.
- Some of the influential figures in the history of NLP include Alfred Korzybski, who proposed the theory of general semantics in 1933, Noam Chomsky, who developed the theory of generative grammar in 1957, and Alan Turing, who proposed the Turing test for machine intelligence in 1950.
- NLP has evolved over the years, from using complex, handwritten rules to using statistical and machine learning methods, from focusing on syntax and semantics to incorporating pragmatics and discourse, and from processing monolingual texts to handling multilingual and multimodal data.
- NLP faces many challenges due to the complexity, diversity, ambiguity, and dynamism of natural language. Some of the major challenges are :
  - Dealing with the sparsity, high dimensionality, and noise of natural language data.
  - Handling the variability, inconsistency, and incompleteness of natural language expressions.
  - Resolving the ambiguity and vagueness of natural language meanings.
  - Capturing the context, background knowledge, and common sense of natural language users.
  - Adapting to the changes, variations, and innovations of natural language use.
- NLP has many applications and benefits for various domains and tasks, such as information retrieval, information extraction, text summarization, sentiment analysis, machine translation, speech recognition, natural language generation, question answering, chatbots, and more.
- NLP is still an emerging and evolving field, with many open problems and opportunities for research and development. NLP has the potential to enhance human-computer communication, enable natural language understanding, and empower natural language users.



### Language Modeling

- Language modeling is the task of estimating the probability of a sequence of words or a word given its context .
- Language models are useful for various natural language processing applications, such as speech recognition, machine translation, text summarization, text generation, etc .
- Language models can be classified into two types: **generative** and **discriminative**.
  - Generative models learn the joint probability of the input and the output, and can generate new samples from the learned distribution. Examples of generative models are n-gram models, hidden Markov models, etc.
  - Discriminative models learn the conditional probability of the output given the input, and can predict the most likely output for a given input. Examples of discriminative models are logistic regression, support vector machines, neural networks, etc.
- Language models can also be categorized based on the level of granularity they operate on: **word-level**, **character-level**, or **subword-level**.
  - Word-level models treat each word as an atomic unit and assign a probability to each word in the vocabulary. Word-level models suffer from data sparsity and out-of-vocabulary issues.
  - Character-level models treat each character as an atomic unit and assign a probability to each character in the alphabet. Character-level models can handle any word, but they require longer sequences and more computation.
  - Subword-level models split words into smaller units, such as syllables, morphemes, or byte-pair encodings. Subword-level models can balance between word-level and character-level models, and can capture both lexical and morphological information.
- Language models can also be distinguished based on the architecture they use: **statistical** or **neural** .
  - Statistical models rely on counting and smoothing techniques to estimate the probabilities of word sequences. Statistical models are simple, fast, and interpretable, but they have limited expressive power and cannot capture long-term dependencies .
  - Neural models use artificial neural networks to learn the probabilities of word sequences. Neural models are complex, slow, and opaque, but they have high expressive power and can capture long-term dependencies .
- Language models can be evaluated using two main metrics: **perplexity** and **likelihood** .
  - Perplexity measures how well a language model predicts a test set. It is the inverse of the geometric mean of the probabilities assigned to each word in the test set. Lower perplexity means better performance .
  - Likelihood measures how probable a test set is according to a language model. It is the product of the probabilities assigned to each word in the test set. Higher likelihood means better performance .



### Grammar-based LM for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A language model (LM) is a system that assigns probabilities to sequences of words or symbols in a language. It can be used to generate or evaluate natural language texts.
- A grammar-based language model (GLM) is a type of LM that uses a formal grammar to define the structure and rules of a language. A grammar is a set of symbols and rules that specify how to form valid sentences in a language.
- A GLM can be seen as a generative model that produces sentences by applying grammar rules in a probabilistic way. For example, a GLM can generate a sentence by starting with a symbol S (representing a sentence) and then expanding it into a noun phrase (NP) and a verb phrase (VP) according to a rule S -> NP VP, and then expanding each phrase further until reaching terminal symbols (words).
- A GLM can also be seen as a discriminative model that assigns probabilities to sentences by computing the product of the probabilities of the grammar rules used to derive the sentence. For example, a GLM can assign a probability to a sentence by multiplying the probabilities of the rules S -> NP VP, NP -> Det N, VP -> V NP, etc.
- A GLM can be based on different types of grammars, such as context-free grammars (CFGs), context-sensitive grammars (CSGs), or even more complex grammars. The choice of the grammar affects the expressiveness and complexity of the GLM.
- A GLM can capture some syntactic and semantic aspects of a language, such as word order, agreement, and subcategorization. However, a GLM may not be able to capture some pragmatic and contextual aspects of a language, such as discourse coherence, common sense, and world knowledge.
- A GLM can be used for various natural language processing (NLP) tasks, such as parsing, generation, summarization, and translation. However, a GLM may not be able to handle some linguistic phenomena, such as ambiguity, idioms, and neologisms.
- A GLM can be trained on a corpus of sentences annotated with grammar rules, or on a grammar manually constructed by experts. However, a GLM may suffer from data sparsity, overfitting, and lack of generalization.



### Statistical Language Model for Natural Language Processing

- A statistical language model (SLM) is a mathematical tool that assigns probabilities to sequences of words or symbols in a natural language, such as English or Hindi.
- SLMs are used to generate or analyze natural language texts for various applications, such as speech recognition, machine translation, text summarization, information retrieval, and natural language generation.
- SLMs are based on the assumption that the probability of a word or symbol depends on its previous words or symbols, or its context. This is known as the Markov property.
- SLMs can be classified into two types: n-gram models and neural network models.
- N-gram models are the simplest and most widely used SLMs. They estimate the probability of a word or symbol based on the previous n-1 words or symbols, where n is a fixed number. For example, a bigram model (n=2) estimates the probability of a word based on the previous word, and a trigram model (n=3) estimates the probability of a word based on the previous two words.
- Neural network models are more complex and powerful SLMs. They use artificial neural networks to learn the probability distribution of words or symbols in a natural language. They can capture long-range dependencies and semantic similarities between words or symbols. For example, a recurrent neural network (RNN) model can process variable-length sequences of words or symbols, and a transformer model can encode the context and attention of words or symbols.
- SLMs are trained on large corpora of natural language texts, such as books, news articles, or social media posts. The training process involves estimating the parameters of the model, such as the probabilities or weights, that maximize the likelihood of the observed data.
- SLMs are evaluated on unseen test data, such as sentences or paragraphs, using metrics such as perplexity, accuracy, or BLEU score. Perplexity measures how well the model predicts the next word or symbol, accuracy measures how often the model predicts the correct word or symbol, and BLEU score measures how similar the model-generated text is to the human-generated text.



### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.
- RE consists of a set of symbols and operators that define the rules for constructing valid expressions.
- Some of the common symbols and operators in RE are:

| Symbol | Meaning |
| --- | --- |
| . | Matches any single character |
| [ ] | Matches any character(s) inside the brackets |
| [^ ] | Matches any character(s) not inside the brackets |
| * | Matches zero or more occurrences |
| + | Matches one or more occurrences |
| ? | Matches zero or one occurrence |
| | | Matches a choice between the expressions on either side |
| ( ) | Groups the expression inside the parentheses |
| { } | Matches a specific number of occurrences |
| \ | Escapes a special character |

- Examples of RE and their corresponding regular sets are:

| RE | Regular Set |
| --- | --- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s such as {ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb, …} |

- RE can be used for various NLP tasks, such as:

  - Tokenization: splitting a text into smaller units, such as words or sentences, using RE as delimiters.
  - Stemming: reducing a word to its base or root form, such as removing suffixes or prefixes, using RE as rules.
  - Normalization: transforming a text into a standard or canonical form, such as converting numbers, dates, abbreviations, etc., using RE as patterns.
  - Extraction: retrieving specific information from a text, such as names, entities, keywords, etc., using RE as filters.
  - Validation: checking if a text conforms to a certain format or structure, such as email addresses, phone numbers, URLs, etc., using RE as criteria.



### Finite-State Automata for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Finite-state automata (FSA) are abstract machines that can recognize and generate patterns of symbols, such as words, sentences, or phonetic sequences .
- FSA consist of a finite set of states, a finite set of input symbols, a transition function that maps states and symbols to new states, and a set of final or accepting states .
- FSA can be deterministic (DFA) or non-deterministic (NFA). A DFA has exactly one transition for each state and symbol pair, while an NFA can have zero, one, or more transitions for each state and symbol pair .
- FSA can be represented by state diagrams, where states are circles, transitions are arrows labeled with symbols, and final states are double circles .
- FSA can be used to model various aspects of natural language processing (NLP), such as morphology, syntax, phonology, and text processing   .
- FSA can be combined with output symbols to form finite-state transducers (FST), which can map input strings to output strings . FST can be used to perform tasks such as morphological analysis, spelling correction, text normalization, and speech recognition   .
- FSA and FST have several advantages in NLP, such as efficiency, modularity, transparency, and reversibility   . However, they also have some limitations, such as the inability to handle long-distance dependencies, recursion, and ambiguity   .
- FSA and FST can be extended with features such as weights, probabilities, stacks, and registers to overcome some of these limitations and to model more complex linguistic phenomena   .



### English Morphology

- Morphology is the **study of the internal structure of words** and forms a core part of linguistic study today.
- Morphology also deals with the **functional changes in the forms of words**, such as inflection and compounding.
- Morphology analyzes the **structure of words and parts of words** such as stems, root words, prefixes, and suffixes.
- Morphology can be divided into two main branches: **derivational morphology** and **inflectional morphology**.
  - Derivational morphology creates new words from existing ones by adding affixes or changing the root (e.g., happy -> unhappy, sing -> singer).
  - Inflectional morphology modifies the form of words to indicate grammatical information such as tense, number, person, gender, case, etc. (e.g., walk -> walks, walk -> walked, walk -> walking).
- Morphology is related to other aspects of linguistics such as **phonology**, **syntax**, and **semantics**.
  - Phonology studies the **sound patterns** of language and how they affect the formation and pronunciation of words.
  - Syntax studies the **rules and principles** that govern the structure and combination of sentences.
  - Semantics studies the **meaning** of words and sentences and how they are interpreted in different contexts.



### Transducers for lexicon

- A transducer is a device or a model that converts one form of data into another, such as sound to electrical signals, or text to speech.
- A lexical transducer is a specialised finite-state automaton that maps inflected surface forms to lexical forms, and vice versa  .
- A lexical form is a representation of a word that contains its lemma (base form) and its morphological features, such as part of speech, number, gender, tense, etc.
- A surface form is a representation of a word that appears in a text, such as a spelling or a pronunciation.
- A lexical transducer can be used for various natural language processing tasks, such as morphological analysis, generation, normalization, correction, and parsing   .
- A lexical transducer can be constructed using finite-state methods, such as regular expressions, rewrite rules, or weighted finite-state machines  .
- A lexical transducer can be composed with other transducers, such as context dependency transducers, language models, or speech recognizers, to form complex language processing pipelines .
- A lexical transducer can be compressed using various techniques, such as minimization, pruning, factorization, or Huffman coding, to reduce its size and improve its efficiency .



### Tokenization

- Tokenization is the process of breaking down a piece of text into small units called tokens.
- A token may be a word, part of a word or just characters like punctuation.
- Tokenization is the first step in any natural language processing (NLP) pipeline.
- Tokenization is used in NLP to split paragraphs and sentences into smaller units that can be more easily assigned meaning.
- Tokenization is useful for a number of tasks in NLP, including sentiment analysis, topic modeling, and machine translation.
- One of the main advantages of tokenization is that it can help to improve the accuracy of these tasks by providing more context for each word.
- The token occurrences in a document can be used directly as a vector representing that document.

### Types of Tokenization

- There are different types of tokenization depending on the level of granularity and the language of the text.
- Some of the common types of tokenization are:

  - **Word Tokenization**: This is the most basic type of tokenization, where the text is split into words based on whitespace and punctuation. For example, the sentence "Hello, world!" would be tokenized into two tokens: "Hello" and "world".
  - **Sentence Tokenization**: This is the type of tokenization where the text is split into sentences based on punctuation and capitalization. For example, the paragraph "Hi. How are you? I'm fine." would be tokenized into three sentences: "Hi.", "How are you?" and "I'm fine.".
  - **Subword Tokenization**: This is the type of tokenization where the text is split into smaller units than words, such as syllables, morphemes, or n-grams. For example, the word "tokenization" could be tokenized into four subwords: "tok", "en", "iz", and "ation".
  - **Character Tokenization**: This is the type of tokenization where the text is split into individual characters. For example, the word "hello" would be tokenized into five characters: "h", "e", "l", "l", and "o".

### Challenges of Tokenization

- Tokenization is a crucial step in many NLP tasks, but it is also a difficult one, because every language has its own grammatical constructs, which are often difficult to write down as rules.
- Some of the challenges of tokenization are:

  - **Ambiguity**: Sometimes, the same text can be tokenized in different ways depending on the context or the intended meaning. For example, the sentence "She saw a man on a hill with a telescope." can be tokenized into different phrases depending on who has the telescope and where they are located.
  - **Contractions**: Some languages, such as English, have contractions, where two words are combined into one with an apostrophe. For example, "don't" is a contraction of "do not". Tokenizing contractions can be tricky, because sometimes they should be split into two tokens, and sometimes they should be kept as one token depending on the task.
  - **Multiword Expressions**: Some languages, such as Chinese, have multiword expressions, where a group of words form a single unit of meaning. For example, "红烧肉" (red braised pork) is a multiword expression in Chinese. Tokenizing multiword expressions can be challenging, because sometimes they should be treated as one token, and sometimes they should be split into multiple tokens depending on the task.
  - **Non-standard Text**: Some texts, such as social media posts, emails, or chats, may contain non-standard spelling, grammar, or punctuation. For example, "lol" is a non-standard abbreviation for "laugh out loud". Tokenizing non-standard text can be difficult, because sometimes they should be normalized, and sometimes they should be preserved depending on the task.

### Examples of Tokenization

- Here are some examples of tokenization using different types and languages:

  - Word Tokenization (English): "I love NLP." -> ["I", "love", "NLP", "."]
  - Sentence Tokenization (English): "Hello. How are you?" -> ["Hello.", "How are you?"]
  - Subword Tokenization (English): "



### Detecting and Correcting Spelling Errors

- Spelling errors are deviations from the standard or correct form of a word in a written text.
- Spelling errors can be caused by various factors, such as typing mistakes, lack of knowledge, dialectal variations, or foreign accents.
- Spelling errors can affect the readability, comprehension, and credibility of a text, as well as the performance of natural language processing (NLP) systems that rely on accurate spelling.
- Detecting and correcting spelling errors is a challenging task that involves identifying the errors, finding the intended words, and replacing the errors with the correct words.
- Some of the methods and techniques for detecting and correcting spelling errors are:

  - Dictionary-based methods: These methods compare each word in the text with a list of valid words (a dictionary) and flag the words that are not in the list as errors. Then, they generate a list of candidate corrections for each error by applying some rules or heuristics, such as deleting, inserting, substituting, or transposing letters. Finally, they select the best correction from the candidates based on some criteria, such as frequency, similarity, or context.
  - Statistical methods: These methods use probabilistic models to estimate the likelihood of a word being an error and the likelihood of a correction being the intended word. They use large corpora of text to learn the probabilities of words and word sequences, and use them to rank the candidate corrections. They can also use machine learning techniques to learn the features and weights that are relevant for spelling correction.
  - Neural methods: These methods use neural networks to learn the mapping between errors and corrections from data. They can use different architectures, such as feed-forward, recurrent, or attention-based networks, to encode the errors and decode the corrections. They can also use character-level, word-level, or subword-level representations to capture the spelling variations. They can leverage the context and semantics of the text to generate more accurate corrections.



### Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are, based on the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, each with a certain cost.
- For example, the minimum edit distance between "kitten" and "sitting" is 3, because we can transform "kitten" into "sitting" by substituting "k" with "s", inserting "i" after "t", and substituting "e" with "g".
- The minimum edit distance can be computed using a dynamic programming algorithm that fills a matrix with the optimal costs for each substring pair.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of inserting or deleting the characters of the strings.
  - For each cell in the matrix, compute the minimum cost of transforming the substring up to that cell, by taking the minimum of three possible costs:
    - The cost of the cell above plus the cost of deleting a character from the first string.
    - The cost of the cell to the left plus the cost of inserting a character to the second string.
    - The cost of the cell diagonally above and to the left plus the cost of substituting a character if the characters are different, or zero if they are the same.
  - The minimum edit distance is the value of the bottom-right cell of the matrix.

- Here is an example of computing the minimum edit distance between "intention" and "execution" with unit costs for each operation:

|       |   | e | x | e | c | u | t | i | o | n |
| ----- | - | - | - | - | - | - | - | - | - | - |
|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| i     | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| n     | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 6 | 7 |
| t     | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 7 | 7 |
| e     | 4 | 3 | 4 | 3 | 4 | 5 | 6 | 7 | 8 | 8 |
| n     | 5 | 4 | 5 | 4 | 5 | 6 | 7 | 8 | 8 | 8 |
| t     | 6 | 5 | 6 | 5 | 6 | 7 | 6 | 7 | 8 | 9 |
| i     | 7 | 6 | 7 | 6 | 7 | 8 | 7 | 6 | 7 | 8 |
| o     | 8 | 7 | 8 | 7 | 8 | 9 | 8 | 7 | 6 | 7 |
| n     | 9 | 8 | 9 | 8 | 9 | 10| 9 | 8 | 7 | 6 |

- The minimum edit distance is 6, and one possible sequence of operations is:

  - Substitute "i" with "e"
  - Substitute "n" with "x"
  - Substitute "t" with "e"
  - Insert "c"
  - Insert "u"
  - Substitute "i" with "o"



### WORD LEVEL ANALYSIS

Word level analysis is the process of identifying and analyzing the individual words or tokens in a natural language text. It is an important step in natural language processing (NLP) as it helps to extract meaningful information from the text and prepare it for further processing. Some of the tasks involved in word level analysis are:

- **Tokenization**: This is the process of splitting a text into smaller units called tokens, which can be words, punctuation marks, numbers, symbols, etc. Tokenization can be done using various methods, such as whitespace, regular expressions, or predefined rules. For example, the sentence "I love NLP." can be tokenized into ["I", "love", "NLP", "."].
- **Normalization**: This is the process of transforming the tokens into a standard or canonical form, which can reduce the variability and complexity of the text. Normalization can include tasks such as case folding, spelling correction, lemmatization, or stemming. For example, the tokens ["loved", "loving", "loves"] can be normalized to ["love", "love", "love"] using lemmatization, which reduces the words to their base form.
- **Morphological analysis**: This is the process of identifying and analyzing the internal structure and meaning of the tokens, such as their root, prefix, suffix, part of speech, tense, number, gender, etc. Morphological analysis can help to understand the grammatical and semantic role of the tokens in the text. For example, the token "books" can be morphologically analyzed as ["book", "+s"], where "book" is the root and "+s" is the suffix indicating plural noun.
- **Word sense disambiguation**: This is the process of determining the correct meaning or sense of a token in a given context, especially when the token has multiple possible meanings. Word sense disambiguation can help to resolve the ambiguity and improve the understanding of the text. For example, the token "bank" can have different meanings depending on the context, such as a financial institution, a river shore, or a verb meaning to rely on.



### Unsmoothed N-grams

- An n-gram is a sequence of n words or tokens in a text. For example, "natural language processing" is a trigram (n = 3).
- N-grams are used to model the probability of a word given its previous words or context. For example, P(processing | natural language) is the probability of the word "processing" given the previous words "natural language".
- N-gram models are based on the assumption of the Markov property, which states that the probability of a word only depends on a fixed number of previous words. For example, a bigram model (n = 2) assumes that P(w | w1, w2, ..., wn-1) = P(w | wn-1), where w is the current word and wn-1 is the previous word.
- Unsmoothed n-gram models estimate the probabilities of n-grams by counting their frequencies in a corpus or a large collection of texts. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C(x) is the count of x in the corpus.
- Unsmoothed n-gram models have some limitations, such as data sparsity and zero probabilities. Data sparsity refers to the problem of having insufficient data to estimate the probabilities of rare or unseen n-grams. Zero probabilities refer to the problem of assigning zero probability to n-grams that do not occur in the corpus, which can lead to inaccurate predictions or underflow errors.
- To overcome these limitations, smoothed n-gram models are used, which apply various techniques to adjust the probabilities of n-grams based on their frequencies and contexts. Some examples of smoothing techniques are Laplace smoothing, Good-Turing smoothing, Kneser-Ney smoothing, etc.



### Evaluating N-grams for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- N-grams are sequences of N words that are used to model natural language .
- N-grams can be used to capture the local context and dependencies of words in a text .
- N-grams can be extracted from a text by sliding a window of size N over the words and counting the frequency of each sequence .
- N-grams can be used to estimate the probability of a word given its previous N-1 words, using the formula:

P(w<sub>N</sub>|w<sub>1</sub>,...,w<sub>N-1</sub>) = C(w<sub>1</sub>,...,w<sub>N</sub>)/C(w<sub>1</sub>,...,w<sub>N-1</sub>)

where C is the count function and P is the probability function .

- N-grams can be used to generate text by sampling words from the probability distribution given by the N-gram model .
- N-grams have some limitations, such as data sparsity, curse of dimensionality, and lack of long-term dependencies .
- N-grams can be evaluated using various metrics, such as perplexity, log-likelihood, cross-entropy, and accuracy .
- Perplexity measures how well the N-gram model predicts the test data, and is defined as the inverse of the geometric mean of the probabilities of each word in the test data .
- Log-likelihood measures how likely the N-gram model is to generate the test data, and is defined as the sum of the logarithms of the probabilities of each word in the test data .
- Cross-entropy measures the average number of bits needed to encode the test data using the N-gram model, and is defined as the negative of the log-likelihood divided by the number of words in the test data .
- Accuracy measures how often the N-gram model predicts the correct word, and is defined as the ratio of the number of correct predictions to the total number of predictions .



### Smoothing

- Smoothing is the process of flattening a probability distribution implied by a language model so that all reasonable word sequences can occur with some probability .
- Smoothing often involves broadening the distribution by redistributing weight from high probability regions to zero probability regions .
- Smoothing is very important in natural language processing, as some words may have zero or close to zero probabilities such as the out-of-vocabulary words (words that do not exist in the vocabulary), but the same rare words may not have the same values in test data.
- Smoothing techniques in NLP are used to address scenarios related to determining probability / likelihood estimate of a sequence of words (say, a sentence) occurring together when one or more words individually (unigram) or N-grams such as bigram or trigram in the given set have never occurred in the past.
- Smoothing can help performance whenever data sparsity is an issue, and data sparsity is almost always an issue in statistical modeling.
- Some examples of smoothing techniques are add-one smoothing, add-k smoothing, Good-Turing smoothing, Kneser-Ney smoothing, etc .



### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models, which are used to estimate the probability of a word given its previous n-1 words in a sequence.
- Smoothing is necessary to deal with the problem of data sparsity, which occurs when some n-grams are not observed in the training data, resulting in zero probabilities that can affect the performance of language models.
- Interpolation is a method that combines the probabilities of n-grams of different orders, such as unigrams, bigrams, and trigrams, using some weights that sum to one. For example, the interpolated trigram probability can be written as:

    P(w_i|w_{i-2},w_{i-1}) = \lambda_1 P(w_i|w_{i-2},w_{i-1}) + \lambda_2 P(w_i|w_{i-1}) + \lambda_3 P(w_i)

- The weights \lambda_1, \lambda_2, and \lambda_3 can be estimated using various methods, such as maximum likelihood estimation, expectation-maximization, or cross-validation. Interpolation can capture both long-range and short-range dependencies between words, and can assign non-zero probabilities to unseen n-grams by using lower-order n-grams.
- Backoff is a method that uses a lower-order n-gram probability only when the higher-order n-gram probability is zero or unreliable. For example, the backoff trigram probability can be written as:

    P(w_i|w_{i-2},w_{i-1}) = \begin{cases} P(w_i|w_{i-2},w_{i-1}), & \text{if } C(w_{i-2},w_{i-1},w_i) > 0 \\ \alpha(w_{i-2},w_{i-1}) P(w_i|w_{i-1}), & \text{otherwise} \end{cases}

- The function \alpha(w_{i-2},w_{i-1}) is a discounting factor that adjusts the lower-order probability to preserve the total probability mass. Backoff can avoid relying on unreliable estimates based on sparse data, and can also assign non-zero probabilities to unseen n-grams by using lower-order n-grams.
- In general, interpolation works better than backoff, as it can use more information from different n-gram orders. However, backoff is simpler and faster to implement, and can also achieve good results in combination with smoothing techniques.



### Word Classes for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Word classes, also known as **parts of speech**, are categories of words that share similar syntactic and semantic properties in a language.
- Word classes are useful for natural language processing (NLP) because they help to define the structure and meaning of sentences, and to identify the possible words that can fill a given position in a sentence.
- There are different ways to classify words into word classes, depending on the criteria and the level of granularity. Some common word classes are:
  - **Nouns**: words that denote entities, such as people, places, things, concepts, etc. Examples: _book, dog, John, love_.
  - **Verbs**: words that denote actions, states, or events, and that can have tense, aspect, mood, and voice. Examples: _read, run, be, have_.
  - **Adjectives**: words that modify nouns, and that can have degree, comparison, and agreement. Examples: _big, red, happy, beautiful_.
  - **Adverbs**: words that modify verbs, adjectives, or other adverbs, and that can have degree, comparison, and manner. Examples: _quickly, very, well, too_.
  - **Pronouns**: words that substitute for nouns or noun phrases, and that can have person, number, gender, case, and reference. Examples: _I, you, he, she, it, they, this, that_.
  - **Prepositions**: words that introduce phrases that function as modifiers or complements of other words, and that can have direction, location, time, or relation. Examples: _in, on, at, with, from, to_.
  - **Conjunctions**: words that connect words, phrases, or clauses, and that can have coordination, subordination, or correlation. Examples: _and, but, or, because, although, both, either_.
  - **Determiners**: words that specify or limit the reference of nouns or noun phrases, and that can have quantity, definiteness, possession, or demonstrativeness. Examples: _a, the, some, many, my, your, this, that_.
  - **Interjections**: words that express emotions, attitudes, or reactions, and that are usually followed by an exclamation mark. Examples: _ouch, wow, hey, ouch_.
- Some words can belong to more than one word class, depending on their function and meaning in a sentence. For example, _book_ can be a noun or a verb, _well_ can be an adverb or an interjection, _that_ can be a pronoun, a determiner, or a conjunction.
- Word classes can be further divided into subcategories or subclasses, such as proper nouns, countable nouns, transitive verbs, modal verbs, comparative adjectives, etc.
- Word classes can also be grouped into larger categories, such as **open classes** and **closed classes**. Open classes are word classes that can accept new members, such as nouns, verbs, adjectives, and adverbs. Closed classes are word classes that have a fixed and limited set of members, such as pronouns, prepositions, conjunctions, and determiners.



### Part-of-Speech Tagging

- Part-of-speech (POS) tagging is the process of assigning a grammatical category to each word in a sentence, such as noun, verb, adjective, adverb, etc. based on its definition and context  .
- POS tagging is an important task in natural language processing (NLP), as it can help to analyze the structure and meaning of sentences, and to perform other NLP tasks such as parsing, named entity recognition, sentiment analysis, machine translation, etc .
- POS tagging can be done manually by human annotators, or automatically by computer programs. Manual POS tagging is more accurate but time-consuming and costly, while automatic POS tagging is faster and cheaper but prone to errors.
- There are different methods and techniques for automatic POS tagging, such as rule-based, statistical, and neural network-based approaches. Rule-based methods use predefined rules and dictionaries to assign tags, while statistical methods use probabilistic models and machine learning algorithms to learn from annotated data and predict tags, and neural network-based methods use deep learning architectures and embeddings to capture the features and context of words and assign tags .
- One of the most widely used statistical methods for POS tagging is the Hidden Markov Model (HMM), which is a probabilistic model that assumes that the tag of a word depends on the tag of the previous word, and that the word itself depends on its tag. HMMs can be trained on a large corpus of tagged data, and then used to tag new sentences by finding the most likely sequence of tags given the words.
- POS tagging is not a trivial task, as there are many challenges and difficulties involved, such as ambiguity, variation, and sparsity. Ambiguity means that a word can have more than one possible tag depending on the context, such as "book" being a noun or a verb. Variation means that the same word can have different forms or spellings, such as "color" and "colour". Sparsity means that there are many rare or unknown words that are not seen in the training data, such as names, acronyms, or neologisms .
- Therefore, POS tagging requires a lot of linguistic knowledge, computational resources, and data to achieve high accuracy and robustness. POS tagging is also language-dependent, as different languages have different grammatical systems and conventions. Therefore, POS taggers need to be adapted and customized for different languages and domains .



### Rule-based

- Rule-based natural language processing is an approach that relies on predefined rules and patterns to analyze and manipulate natural language data.
- Rules can be based on syntax, semantics, morphology, pragmatics, or domain knowledge of the natural language.
- Rule-based methods can be used for various natural language processing tasks, such as tokenization, stemming, lemmatization, part-of-speech tagging, parsing, named entity recognition, sentiment analysis, machine translation, and information extraction.
- Rule-based methods have some advantages, such as:
  - They are transparent and interpretable, as the rules are explicitly defined and can be inspected and modified by human experts.
  - They are robust and consistent, as they do not depend on the quality and quantity of the training data, and they can handle unseen or rare cases that match the rules.
  - They are efficient and scalable, as they do not require expensive computational resources or complex optimization algorithms to process natural language data.
- Rule-based methods also have some limitations, such as:
  - They are labor-intensive and domain-specific, as they require a lot of manual effort and expertise to create and maintain the rules for each natural language and domain.
  - They are rigid and brittle, as they cannot handle ambiguity, variability, and creativity of natural language, and they may fail or produce incorrect results when the rules do not match the input data.
  - They are incomplete and outdated, as they cannot cover all the possible cases and scenarios of natural language, and they may not adapt to the changes and evolution of natural language over time.



### Stochastic for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Stochastic means involving randomness or probability.
- Stochastic methods are widely used in natural language processing (NLP) to deal with uncertainty and ambiguity in natural languages.
- Stochastic methods can be applied at different levels of NLP, such as syntax, semantics, and pragmatics.
- Some examples of stochastic methods in NLP are:

  - Stochastic grammar: A grammar that assigns probabilities to grammar rules, and uses them to parse sentences and generate language .
  - Stochastic semantic analysis: A semantic analysis that uses segments of words as basic semantic units, and models their probabilities and relations.
  - Statistical parsing: A parsing method that uses probabilistic models to select the most likely syntactic structure for a given sentence.
  - Language modeling: A method that estimates the probability of a word or a sequence of words in a language, and uses it to generate or evaluate text.

- Stochastic methods in NLP can be based on different types of models, such as:

  - N-gram models: Models that use the frequencies of n consecutive words in a corpus to estimate the probabilities of words or sentences.
  - Hidden Markov models: Models that use a sequence of hidden states and their transitions to generate or analyze observable symbols.
  - Neural network models: Models that use artificial neural networks to learn complex patterns and representations from data.
  - Bayesian models: Models that use prior knowledge and evidence to update the probabilities of hypotheses or parameters.



### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text.  
- It is also called Brill tagging, after its inventor Eric Brill.  
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns a series of transformation rules from data.   
- The basic idea of transformation-based tagging is to start with a simple baseline tagger, such as a unigram tagger, and then iteratively apply transformation rules that correct the errors made by the baseline tagger.  
- The transformation rules are learned from a tagged corpus using an error-driven learning algorithm, which selects the rule that reduces the most errors at each iteration.   
- The transformation rules have the form: change the tag of a word from X to Y if condition Z is met, where Z can be based on the surrounding words, tags, or other features.   
- For example, a possible transformation rule is: change the tag of a word from NN (singular noun) to NNS (plural noun) if the word ends with "s".  
- The advantage of transformation-based tagging is that it allows us to have linguistic knowledge in a readable form, and it can capture complex patterns that depend on multiple features.   
- The disadvantage of transformation-based tagging is that it can be slow to train and apply, and it can overfit the training data if the number of rules is too large.



### Issues in PoS tagging

- PoS tagging is the task of assigning a part-of-speech (PoS) label to each word in a sentence, such as noun, verb, adjective, etc.
- PoS tagging is useful for many natural language processing (NLP) applications, such as syntactic parsing, semantic analysis, information extraction, machine translation, etc.
- PoS tagging is not a trivial task, as there are many issues and challenges involved, such as:

  - **Ambiguity**: Many words can have more than one possible PoS tag, depending on the context. For example, the word "book" can be a noun or a verb, and the word "can" can be a modal verb or a noun. PoS taggers need to disambiguate the words based on the surrounding words and their tags.
  - **Sparsity**: Many words are rare or unseen in the training data, and PoS taggers need to generalize to new words based on their morphology, semantics, or other cues. For example, the word "quark" may not appear in the training data, but it can be inferred to be a noun based on its suffix "-k".
  - **Variation**: Different languages, domains, genres, and styles may have different PoS tag sets, conventions, and distributions. For example, the PoS tag set for English may not be suitable for Chinese, and the PoS tag distribution for news articles may not be the same as for tweets. PoS taggers need to adapt to different scenarios and data sources.
  - **Error propagation**: PoS tagging is often a preprocessing step for other NLP tasks, and any errors in PoS tagging may affect the downstream tasks. For example, a wrong PoS tag may lead to a wrong syntactic parse, which may affect the semantic analysis or information extraction. PoS taggers need to minimize the error rate and provide confidence scores or alternative tags for uncertain cases.



### Hidden Markov and Maximum Entropy models for natural language processing

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions).
- HMMs are widely used in natural language processing, especially in speech recognition, part-of-speech tagging, named entity recognition, and machine translation.
- HMMs are based on the assumption that the hidden state at a given time depends only on the previous hidden state, and the emission at a given time depends only on the current hidden state. This is known as the Markov property.
- HMMs can be represented by a set of parameters: the initial state distribution, the state transition matrix, and the emission probability matrix. These parameters can be estimated from training data using algorithms such as the Baum-Welch algorithm or the Viterbi training algorithm.
- HMMs can be used to perform two main tasks: decoding and learning. Decoding is the process of finding the most likely sequence of hidden states given a sequence of emissions. This can be done using algorithms such as the Viterbi algorithm or the forward-backward algorithm. Learning is the process of finding the optimal parameters of the HMM given a set of training data. This can be done using algorithms such as the Baum-Welch algorithm or the Viterbi training algorithm.
- Maximum Entropy Markov Model (MEMM) is a discriminative model that extends a standard maximum entropy classifier by assuming that the unknown values to be learnt are connected in a Markov chain rather than being conditionally independent of each other.
- MEMMs find applications in natural language processing, specifically in part-of-speech tagging and information extraction.
- MEMMs are based on the principle of maximum entropy, which states that the best model is the one that makes the fewest assumptions about the data, or equivalently, the one that has the highest entropy (or uncertainty) subject to the constraints imposed by the data.
- MEMMs can be represented by a set of features and weights, where each feature is a function of the current observation and the previous state, and each weight is a parameter that determines the importance of the feature. The probability of a state given an observation and a previous state is computed by applying the softmax function to the weighted sum of the features.
- MEMMs can be trained using algorithms such as the generalized iterative scaling algorithm or the improved iterative scaling algorithm, which iteratively adjust the weights to maximize the likelihood of the training data.
- MEMMs can be used to perform decoding by finding the most likely sequence of states given a sequence of observations. This can be done using algorithms such as the Viterbi algorithm or the beam search algorithm.
- MEMMs have some advantages over HMMs, such as the ability to incorporate arbitrary features, the avoidance of the label bias problem, and the ease of parameter estimation. However, they also have some disadvantages, such as the loss of the Markov property, the requirement of labeled data, and the complexity of decoding.



## Unit 2 - SYNTACTIC ANALYSIS

- Syntactic analysis is the process of analyzing the structure and grammar of a natural language sentence or program code.
- Syntactic analysis can be performed by using formal methods such as grammars, parsers, and automata, or by using statistical methods based on data and probabilities.
- Syntactic analysis can be used for various applications, such as natural language processing, compiler design, code analysis, and artificial intelligence.
- Syntactic analysis can be divided into two main phases: lexical analysis and parsing.
- Lexical analysis is the process of breaking down a sentence or code into its smallest meaningful units, called tokens. Tokens can be words, symbols, numbers, or identifiers.
- Parsing is the process of arranging the tokens into a hierarchical structure, called a parse tree, that represents the syntactic rules and relationships of the language.
- A parse tree can be represented by using brackets, diagrams, or tables.
- A parse tree can be used to check the validity, meaning, and ambiguity of a sentence or code.
- A parse tree can also be used to generate intermediate or final outputs, such as abstract syntax trees, semantic representations, or executable code.



### Context Free Grammars

- A context-free grammar (CFG) is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a left-hand side, which identifies a syntactic category, and a right-hand side, which defines its alternative component parts, reading from left to right.
- A syntactic category is a label for a group of words or phrases that share some common properties, such as noun, verb, adjective, etc.
- A context-free grammar is called so because the rules can be applied regardless of the surrounding context of the words or phrases.
- A context-free grammar can be formally defined as a 4-tuple (V, Σ, R, S), where:
  - V is a finite set of variables or non-terminals, which represent syntactic categories.
  - Σ is a finite set of terminals, which represent words or symbols in the language.
  - R is a finite set of rules or productions, which have the form A → α, where A ∈ V and α ∈ (V ∪ Σ)*.
  - S ∈ V is a designated start symbol, which represents the whole sentence or program.
- A context-free grammar can be used to generate or parse sentences or programs in a language by applying the rules recursively, starting from the start symbol.
- A context-free grammar can be represented graphically by a parse tree, which shows the hierarchical structure of a sentence or program and the application of the rules.
- A context-free grammar can be used to model the constituent structure of natural language, which is the way words and phrases are grouped together to form larger units of meaning.
- A context-free grammar can also be used to define the high level structure of a programming language, which is the way statements and expressions are composed to form programs.
- A context-free grammar can capture some aspects of natural language syntax, such as word order, agreement, and recursion, but it cannot capture other aspects, such as pronoun reference, ellipsis, and coordination.
- Natural languages are not strictly context-free, but rather mildly context-sensitive, which means they require some additional mechanisms or constraints to account for their syntactic complexity.



### Grammar rules for English for the notes of the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Syntactic analysis is the process of analyzing natural language with the rules of formal grammar.
- Syntactic analysis assigns a semantic structure to text, which helps to understand how words fit together to form meaningful sentences .
- Syntactic analysis involves the following steps:
  - Segmentation I: Identifying clause boundaries and word boundaries
  - Classification I: Determining the parts of speech
  - Segmentation II: Identifying constituents
  - Classification II: Determining the syntactic categories for the constituents
  - Determining the grammatical functions of the constituents
  - Drawing the syntactic structure
- Syntactic analysis uses grammar rules, which define the structure of a sentence. For example, in English, grammar rules would determine whether a sentence should have a subject, verb, and object, or if it should be in the active or passive voice.
- Syntactic analysis also follows ordering patterns in sentences and clauses, such as compound sentences are joined by conjunctions (and, but, or) or that multiple adjectives modifying the same noun follow a particular order according to their class (such as number-size-color, as in "six small green chairs").
- Syntactic analysis can be used to create various rhetorical or literary effects by manipulating the syntax of a sentence. For example, using parallelism, inversion, ellipsis, or anaphora can enhance the style, clarity, or emphasis of a sentence.



### Treebanks

- A treebank is a corpus of natural language sentences annotated with syntactic structure, such as phrase structure trees or dependency graphs .
- Treebanks are useful for linguistic research, as they provide empirical evidence for syntactic phenomena and allow for quantitative analysis.
- Treebanks are also essential for natural language processing, as they provide training and evaluation data for data-driven models such as part-of-speech taggers, parsers, semantic analyzers and machine translation systems .
- Treebanks can vary in their annotation scheme, granularity, domain, genre, language and size .
- Some examples of widely used treebanks are the Penn Treebank for English, the Universal Dependencies project for cross-lingual syntactic annotation, and the Sta nz a toolkit for neural natural language processing  .



### Normal Forms for Grammar

- A normal form for grammar is a standard way of representing the rules and structure of a formal language, such as a natural language or a programming language.
- Normal forms for grammar can simplify the process of parsing and analyzing sentences, as well as proving properties of languages and grammars.
- There are different types of normal forms for grammar, depending on the class of languages and grammars they apply to. Some common normal forms for grammar are:

  - **Chomsky Normal Form (CNF)**: A normal form for context-free grammars, where every rule has the form A -> BC or A -> a, where A, B, and C are non-terminal symbols and a is a terminal symbol. CNF is widely used in natural language processing for parsing and analyzing natural language sentences.
  - **Greibach Normal Form (GNF)**: A normal form for context-free grammars, where every rule has the form A -> aB1B2...Bn, where A and Bi are non-terminal symbols and a is a terminal symbol. GNF is useful for constructing pushdown automata and bottom-up parsers for context-free languages.
  - **Backus-Naur Form (BNF)**: A normal form for context-free grammars, where every rule has the form <symbol> ::= <expression>, where <symbol> is a non-terminal symbol and <expression> is a sequence of terminal and non-terminal symbols. BNF is commonly used for specifying the syntax of programming languages and data formats.
  - **Extended Backus-Naur Form (EBNF)**: A normal form for context-free grammars, where every rule has the form <symbol> ::= <expression>, where <symbol> is a non-terminal symbol and <expression> is a sequence of terminal and non-terminal symbols, with optional extensions such as repetition, alternation, grouping, and comments. EBNF is a more expressive and readable version of BNF, and is also widely used for specifying the syntax of programming languages and data formats.



### Dependency Grammar

- Dependency grammar is a descriptive and theoretical tradition in linguistics that can be traced back to antiquity.
- It has long been influential in the European linguistics tradition and has more recently become a mainstream approach to representing syntactic and semantic structure in natural language processing.
- Dependency grammar is based on the idea that syntactic structure is determined by the relations between words, rather than by the categories or positions of words.
- A dependency relation is a binary asymmetric relation between a head word and a dependent word. The head word is the one that determines the syntactic and semantic properties of the phrase, while the dependent word is the one that modifies or complements the head word.
- A dependency structure is a set of dependency relations that form a tree or a graph. The root of the tree or graph is usually the main predicate of the sentence, and the other words are attached to it or to its dependents.
- A dependency grammar is a set of rules or principles that specify how dependency structures are formed and interpreted.
- Dependency parsing is a technique used to identify semantic relations between words in a sentence. Dependency parsers are used to map the words in a sentence to semantic roles, thereby identifying the syntactic relations between words.
- Dependency parsing can be done using rule-based, statistical, or neural methods. Rule-based methods rely on hand-crafted rules and dictionaries to assign dependency labels to words. Statistical methods use probabilistic models and machine learning algorithms to learn dependency patterns from annotated corpora. Neural methods use deep neural networks and word embeddings to encode and decode dependency structures.
- Dependency parsing has many applications in natural language processing, such as information extraction, question answering, machine translation, sentiment analysis, and text summarization.



### Syntactic Parsing

- Syntactic parsing is the process of analyzing natural language with the rules of a formal grammar .
- Formal grammar is a system of symbols and rules that defines the syntax of a language.
- Syntax is the study of how words are combined to form sentences and phrases.
- Syntactic parsing aims to uncover the syntactic structure of an input sentence, such as a constituent or dependency tree.
- A constituent tree shows how words are grouped into phrases and clauses, and how they function as parts of speech.
- A dependency tree shows how words are related to each other by dependency relations, such as subject, object, modifier, etc.
- Syntactic parsing is also known as syntax analysis or parsing .
- Syntactic parsing is different from lexical analysis, which is the process of identifying and categorizing individual words in a sentence.
- Syntactic parsing is an important task in natural language processing, and has been a subject of research since the mid-20th century with the advent of computers.
- Syntactic parsing can be useful for downstream tasks such as semantic parsing, relation extraction, and machine translation.
- Syntactic parsing can be performed by different methods, such as rule-based, probabilistic, or neural network-based approaches .
- Syntactic parsing can be supervised, semi-supervised, or unsupervised, depending on the availability and quality of annotated data.



### Ambiguity for the notes of the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Ambiguity is the property of natural language that allows multiple interpretations of a sentence or a word.
- Ambiguity can occur at various levels of natural language processing, such as lexical, syntactic, semantic, and pragmatic  .
- Ambiguity is a challenging task in natural language understanding (NLU), as it requires resolving the intended meaning of the speaker or the writer.
- The process of handling the ambiguity is called disambiguation, which can be done using various techniques, such as word sense disambiguation, part of speech tagging, hidden Markov models, machine learning, etc.  .
- Ambiguity can affect the quality and efficiency of natural language processing applications, such as machine translation, information extraction, question answering, text summarization, etc. .
- Ambiguity can also be a source of creativity and humor in natural language, as it allows for multiple meanings and interpretations of the same expression.

: Ambiguities in Natural Language Processing - rroij.com
: Ambiguity in Natural Language Processing - The NorthCap University
: Ambiguity in Natural Language Processing - Tutorials and Notes
: A comprehensive review on resolving ambiguities in natural language processing - ScienceDirect
: Types of language ambiguity in natural language processing - Omar Meriwani



### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- It is based on the idea of storing and reusing partial results of the parsing process in a table or chart, rather than recomputing them.
- It is also known as chart parsing or tabular parsing.
- It can handle ambiguous grammars and produce all possible parse trees for a given sentence.
- It has a time complexity of O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar.

#### CKY Parsing Algorithm

- CKY stands for Cocke-Kasami-Younger, the names of the researchers who developed the algorithm independently.
- It is a bottom-up dynamic programming parsing algorithm that starts from the words (terminal symbols) and builds larger constituents (non-terminal symbols) using the grammar rules.
- It requires the grammar to be in CNF, which means that every rule has the form A -> BC or A -> a, where A, B, and C are non-terminals and a is a terminal.
- It uses a triangular matrix or chart to store the partial results, where each cell (i, j) represents the span of words from i to j in the sentence.
- It fills the chart in a diagonal fashion, starting from the cells along the main diagonal (i, i) and moving to the cells above and to the right (i, j) where i < j.
- For each cell (i, j), it checks if there is a rule A -> a that matches the word at position i, and if so, it adds A to the cell.
- Then, it checks if there is a rule A -> BC that matches the combination of two cells below and to the left of the current cell, and if so, it adds A to the cell and records the backpointers to the two cells.
- The algorithm terminates when the cell (0, n) is filled, where n is the length of the sentence.
- If the cell (0, n) contains the start symbol of the grammar, then the sentence is accepted and the parse trees can be extracted by following the backpointers from the cell.
- If the cell (0, n) does not contain the start symbol, then the sentence is rejected and no parse trees are possible.



### Shallow parsing

- Shallow parsing (also called chunking or light parsing) is an analysis of a sentence which first identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and then links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.).
- Shallow parsing is different from deep parsing, which aims to produce a complete and detailed syntactic structure of a sentence, such as a parse tree. Shallow parsing is faster and less complex than deep parsing, but it also provides less information about the sentence structure and meaning.
- Shallow parsing can be used for various natural language processing tasks, such as:
  - Semantic role labeling, which is the process of assigning labels to words or phrases in a sentence that indicate their semantic role in the sentence, such as that of an agent, goal, or result. It serves to find the meaning of the sentence.
  - Information extraction, which is the process of extracting structured information from unstructured or semi-structured text, such as names, dates, locations, events, etc. It serves to organize and summarize the text.
  - Text summarization, which is the process of creating a concise and coherent summary of a longer text, such as a news article, a book, or a speech. It serves to provide the main points and gist of the text.
- Shallow parsing can be performed by using various methods, such as:
  - Rule-based methods, which use predefined rules and patterns to identify and label the chunks in a sentence. For example, a rule might state that a noun phrase consists of a determiner followed by zero or more adjectives followed by a noun. Rule-based methods are easy to implement and understand, but they also require a lot of manual effort and domain knowledge to create and maintain the rules.
  - Machine learning methods, which use data-driven approaches to learn and apply the chunking models. For example, a machine learning method might use a classifier to predict the chunk boundaries and labels based on the features of the words and their context. Machine learning methods are more flexible and adaptable, but they also require a lot of annotated data and computational resources to train and test the models.



### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probabilities of the rules are estimated from a corpus of annotated sentences, called a treebank.
- The sum of the probabilities of all the rules with the same left-hand side must be equal to one.
- A PCFG can be used to model the syntactic structure of natural language sentences, and to assign probabilities to different possible parses of a sentence.
- A PCFG can also be used to generate random sentences from a given grammar, by randomly choosing rules according to their probabilities.
- A PCFG can be parsed by a modified version of the CKY algorithm, which is a bottom-up dynamic programming algorithm that finds the most probable parse tree for a given sentence and grammar.
- The CKY algorithm works by filling a triangular chart with the probabilities of all possible constituents that span a substring of the sentence, and then backtracking to find the best parse tree.
- The CKY algorithm requires the PCFG to be in Chomsky Normal Form (CNF), which means that every rule has either two nonterminal symbols or one terminal symbol on the right-hand side.
- A PCFG can be converted to CNF by introducing new nonterminal symbols and adding new rules that preserve the original probabilities.
- A PCFG can capture some aspects of natural language syntax, such as word order, agreement, and subcategorization, but it cannot capture long-distance dependencies, such as wh-movement, or semantic constraints, such as selectional restrictions.



### Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees for each substring of the input sentence in a triangular matrix.
- The algorithm works as follows:
  - Initialize the matrix with the probabilities of the terminal symbols for each word in the sentence.
  - For each substring of length 2 or more, consider all possible ways of splitting it into two smaller substrings, and all possible rules of the form A -> BC, where A, B, and C are nonterminal symbols.
  - For each split and rule, compute the probability of the subtree rooted at A by multiplying the probabilities of the subtrees rooted at B and C, and the probability of the rule A -> BC.
  - Store the maximum probability and the corresponding rule and split for each nonterminal symbol A in the matrix cell for the substring.
  - Repeat until the matrix cell for the whole sentence is filled.
  - Trace back the matrix from the top cell to find the most likely parse tree and its probability.
- The probabilistic CYK algorithm can be used for parsing natural language sentences, as well as other applications that involve probabilistic grammars, such as speech recognition, machine translation, and bioinformatics.



### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule in a CFG.
- The probability of a rule A -> α is the conditional probability of expanding A to α given A, written as P(A -> α | A) or P(A -> α).
- The probability of a derivation or a parse tree is the product of the probabilities of all the rules used in the derivation.
- PCFGs can be used to model the syntactic structure of natural language sentences, and to perform parsing tasks such as finding the most probable parse tree for a given sentence.
- Lexicalized PCFGs (L-PCFGs) are a type of PCFGs that incorporate lexical information into the nonterminal symbols of the grammar.
- L-PCFGs use a head-driven annotation scheme, where each nonterminal symbol is annotated with the head word of its subtree.
- The head word is the most important word in a phrase that determines its syntactic and semantic properties.
- For example, in the phrase "the big red car", the head word is "car", and the nonterminal symbol for the phrase is NP(car).
- L-PCFGs can capture more fine-grained syntactic distinctions and dependencies than PCFGs, and can improve the accuracy of parsing natural language sentences.
- Neural bi-lexicalized PCFGs (NBL-PCFGs) are a type of L-PCFGs that use neural networks to model the probabilities of the rules and the head words.
- NBL-PCFGs use two types of head words: the left head word and the right head word, which are the head words of the left and right children of a nonterminal symbol respectively.
- NBL-PCFGs use a neural network to compute the probability of a rule A -> BC given the left head word of A and the right head word of A, written as P(A -> BC | A.l, A.r).
- NBL-PCFGs also use a neural network to compute the probability of a head word given the rule and the head words of the children, written as P(A.l | A -> BC, B.l, C.l) and P(A.r | A -> BC, B.r, C.r).
- NBL-PCFGs can learn more complex and expressive syntactic representations than L-PCFGs, and can achieve state-of-the-art results on unsupervised grammar induction.



### Feature structures for the notes of the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Feature structures are a way of representing linguistic information in a structured and hierarchical way.
- Feature structures consist of a set of attribute-value pairs, where the attributes are names of linguistic features and the values are either atomic symbols or other feature structures.
- Feature structures can be used to encode various aspects of linguistic analysis, such as morphology, syntax, semantics and pragmatics.
- Feature structures can be represented graphically as boxes with labeled slots, or textually as brackets with colons.
- For example, the following feature structure represents some information about the word "dog":

```
[POS: N
 NUMBER: SG
 GENDER: M
 SEM: [CLASS: ANIMAL
       SPECIES: DOG]]
```

- Feature structures can be nested, as shown by the SEM attribute, which has another feature structure as its value.
- Feature structures can also be shared, as shown by the coindexation of the two NP feature structures in the following example:

```
[S [NP NUM: PL
      PERS: 3
      GENDER: F]_i
   [VP [V FORM: PRES
          AGR: [NUM: PL
                PERS: 3]] 
      [NP NUM: PL
          PERS: 3
          GENDER: F]_i]]
```

- Feature structures can be manipulated by the operation of unification, which allows us to combine the information contained in two different feature structures.
- Unification is a process of finding the most general feature structure that is compatible with both input feature structures, or failing if there is no such feature structure.
- Unification is useful for implementing grammatical constraints, such as agreement, subcategorization and selectional restrictions.
- For example, the following unification of a verb and its subject results in a feature structure that represents the agreement information:

```
[V FORM: PRES
 AGR: [NUM: ?x
       PERS: ?y]] 
 unify
[NP NUM: SG
    PERS: 3
    GENDER: M]
 =
[V FORM: PRES
 AGR: [NUM: SG
       PERS: 3]] 
```

- Feature structures can be implemented and manipulated in NLTK using the `nltk.FeatStruct` class and its methods.
- NLTK also provides a parser for reading feature structures from strings, and a graphical interface for displaying feature structures.
- For example, the following code creates and displays a feature structure in NLTK:

```
>>> import nltk
>>> fs = nltk.FeatStruct('[POS: N, NUMBER: SG, GENDER: M, SEM: [CLASS: ANIMAL, SPECIES: DOG]]')
>>> print(fs)
[ GENDER = 'M'   POS = 'N'   NUMBER = 'SG'   SEM = [ CLASS = 'ANIMAL'   SPECIES = 'DOG' ] ]
>>> fs.draw()
```



### Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- A feature structure is a set of attribute-value pairs, where the values can be atomic symbols or other feature structures.
- For example, the feature structure for a noun phrase "the dog" can be written as:

```
[CAT: NP
 DET: [CAT: DET
       FORM: the]
 N: [CAT: N
     FORM: dog]]
```

- Unification is a (partial) operation on feature structures. Intuitively, it is the operation of combining two feature structures such that the new feature structure contains all the information of the original two, and nothing more.
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- For example, the unification of the feature structures `[A: a B: b]` and `[A: a C: c]` is `[A: a B: b C: c]`.
- Unification can fail if the feature structures are incompatible, i.e., they have different values for the same attribute. For example, the unification of `[A: a B: b]` and `[A: a B: c]` fails.
- Unification is widely used in natural language processing (NLP) for various tasks, such as parsing, generation, and semantic interpretation.
- Unification can be extended to E-unification, which allows the use of equations or constraints on the values of the feature structures .
- E-unification can capture more complex linguistic phenomena, such as agreement, anaphora, and ellipsis.
- E-unification is more expressive and powerful than structural unification, but also more computationally expensive and difficult .



## Unit 3 - SEMANTICS AND PRAGMATICS

- Semantics and pragmatics are two important branches of linguistics (the study of language) that deal with meaning  .
- Semantics studies the meaning of words and sentences in a language, regardless of the context or the speaker's intention  .
- Pragmatics studies the meaning of words and sentences in a language, taking into account the context, the speaker's intention, and the listener's interpretation  .
- Semantics is limited to the relationship between words, whereas pragmatics covers the relationships between words, people, and contexts  .
- Semantics is context-independent, while pragmatics is context-dependent.
- Semantics has a narrower scope than pragmatics, as it only deals with meaning in a general sense, using the general rules used in a language.
- Pragmatics has a broader scope than semantics, as it deals with meaning in a specific situation, using the speaker's knowledge, beliefs, and goals.
- Semantics and pragmatics are complementary to one another in the study of meaning, but semantics is less comprehensive than pragmatics.
- Pragmatics can be defined as meaning minus truth-conditions, as pragmatics goes beyond the truth-conditional aspect of language that semantics focuses on.
- Semantics and pragmatics can be illustrated by the following example:

  - Sentence: "It's cold in here."
  - Semantic meaning: The temperature in this room is low.
  - Pragmatic meaning: The speaker wants someone to turn up the heat or close the window.



### Requirements for representation for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Semantics is the study of meaning at the level of words, phrases, sentences, and texts. It deals with how natural language expressions convey information, truth conditions, entailment, and ambiguity.
- Pragmatics is the study of meaning in context, taking into account the speaker's intention, the listener's inference, the common ground, and the situational factors. It deals with how natural language expressions are used to perform speech acts, convey implicatures, and achieve coherence.
- A representation for semantics and pragmatics should be able to capture the following aspects of natural language meaning:
  - The lexical meaning of words and how they are composed to form complex expressions.
  - The syntactic structure and the semantic roles of the constituents of a sentence.
  - The logical form and the truth conditions of a sentence in a given model or world.
  - The discourse structure and the relations between sentences in a text or dialogue.
  - The pragmatic functions and the illocutionary force of utterances in a communicative situation.
  - The contextual factors and the background knowledge that influence the interpretation and generation of natural language expressions.
- Some of the common methods and frameworks for representing semantics and pragmatics are:
  - First-order logic and lambda calculus, which provide a formal language for expressing propositions, predicates, quantifiers, and functions.
  - Semantic networks and frames, which provide a graphical and hierarchical way of organizing concepts, properties, and relations.
  - Ontologies and knowledge bases, which provide a structured and standardized way of storing and retrieving information about entities, categories, and facts.
  - Semantic parsing and generation, which provide a way of mapping natural language expressions to and from logical forms or other formal representations.
  - Discourse representation theory and dynamic semantics, which provide a way of accounting for the anaphoric and temporal aspects of discourse and dialogue.
  - Speech act theory and Gricean pragmatics, which provide a way of analyzing the communicative intentions and implications of utterances and their relation to the cooperative principle and the maxims of conversation.



### First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL consists of symbols for constants, variables, predicates, functions, logical connectives, and quantifiers.
- A constant symbol represents a specific object or entity, such as `John` or `2`.
- A variable symbol represents an unspecified object or entity, such as `x` or `y`.
- A predicate symbol represents a property or relation of one or more objects or entities, such as `Human(x)` or `Loves(x,y)`.
- A function symbol represents a mapping from one or more objects or entities to another object or entity, such as `Father(x)` or `Plus(x,y)`.
- A logical connective represents a logical operation on one or more propositions, such as `and`, `or`, `not`, `implies`, or `equals`.
- A quantifier represents a scope of a variable over a domain of objects or entities, such as `forall` or `exists`.
- A term is either a constant, a variable, or a function applied to one or more terms, such as `John`, `x`, or `Father(John)`.
- A formula is either a predicate applied to one or more terms, a logical connective applied to one or more formulas, or a quantifier applied to a variable and a formula, such as `Human(John)`, `Loves(x,y) and Human(x)`, or `forall x (Human(x) implies Loves(x,x))`.
- A sentence is a formula that contains no free variables, that is, variables that are not bound by a quantifier, such as `forall x (Human(x) implies Loves(x,x))`.
- The semantics of FOL defines the truth value of a sentence with respect to a model, which consists of a domain of objects or entities and an interpretation of the symbols in the language.
- A model assigns a specific object or entity to each constant symbol, a subset of the domain to each predicate symbol, a function from the domain to the domain to each function symbol, and a truth value to each logical connective.
- A model satisfies a sentence if the sentence is true under the model, according to the rules of FOL.
- A sentence is valid if it is satisfied by every model, such as `forall x (x equals x)`.
- A sentence is satisfiable if it is satisfied by some model, such as `exists x (Human(x) and Loves(x,John))`.
- A sentence is unsatisfiable if it is satisfied by no model, such as `forall x (Human(x) and not Human(x))`.
- A sentence is a logical consequence of a set of sentences if it is satisfied by every model that satisfies the set of sentences, such as `forall x (Human(x) implies Loves(x,x))` is a logical consequence of `forall x (Human(x) implies Loves(x,John))`.
- FOL is a powerful and expressive language for natural language processing, as it can capture many aspects of natural language semantics, such as quantification, negation, implication, and equality.
- FOL can also be used to perform automated inference, that is, to derive new sentences from existing sentences using logical rules and algorithms, such as resolution or natural deduction.
- FOL parsing is the task of mapping natural language sentences to FOL sentences, which can be modeled as a sequence to sequence problem using neural networks or other methods.
- FOL reasoning is the task of evaluating the truth value or the logical consequence of FOL sentences, which can be modeled as a natural language inference problem using neural networks or other methods.



### Description Logics for Natural Language Processing

- Description logics (DLs) are a family of logic-based knowledge representation formalisms that allow for the representation of concepts, roles, and individuals, and the reasoning about their properties and relations .
- DLs are used for various applications, such as the representation of ontologies, natural language processing, and the semantics of UML class diagrams .
- In natural language processing, DLs can be used to model the meaning of natural language expressions, such as sentences, phrases, and words, and to perform various tasks, such as semantic analysis, inference, and generation .
- Some of the advantages of using DLs for natural language processing are :
  - They provide a clear and precise semantics for natural language expressions, based on the notions of interpretation, satisfaction, and entailment.
  - They allow for the modularization and reuse of knowledge, by supporting the definition of complex concepts and roles from simpler ones, and the import and export of ontologies.
  - They enable the use of efficient and sound reasoning services, such as subsumption, consistency, and classification, which can be used to check the validity, coherence, and informativeness of natural language expressions.
  - They facilitate the integration of natural language processing with other domains and applications, by providing a common and interoperable representation language and a standard interface for communication and query answering.
- Some of the challenges of using DLs for natural language processing are :
  - They require a careful design and implementation of the mapping between natural language expressions and DL constructs, which may involve syntactic, semantic, and pragmatic aspects.
  - They may not be able to capture all the nuances and variations of natural language, such as ambiguity, vagueness, context-dependence, and figurative language, which may require the use of additional mechanisms or extensions of DLs.
  - They may not be able to handle the dynamic and interactive nature of natural language communication, such as dialogue, discourse, and pragmatics, which may require the use of additional models or frameworks.
  - They may not be able to scale up to the large and complex knowledge bases that are needed for natural language processing, which may require the use of optimization techniques or trade-offs between expressivity and tractability.



### Syntax-Driven Semantic Analysis

- Syntax-driven semantic analysis is a method of deriving the meaning of natural language sentences from their syntactic structure and lexical information.
- Syntax-driven semantic analysis involves applying rules of formal grammar to assign semantic structures to sentences or phrases, such as logical forms, semantic roles, or predicate-argument structures.
- Syntax-driven semantic analysis assumes that there is a correspondence between the syntactic and semantic components of natural language, and that the meaning of a sentence can be computed from its syntactic constituents and their relations.
- Syntax-driven semantic analysis can be performed using different types of grammars, such as context-free grammars, dependency grammars, or lexical-functional grammars, depending on the level of detail and complexity required for the semantic representation.
- Syntax-driven semantic analysis can be used for various natural language processing tasks, such as information extraction, question answering, machine translation, or text summarization, by providing a formal and explicit representation of the meaning of natural language texts.



### Semantic attachments for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Semantic attachments are a way of connecting the syntactic structure of a sentence with its semantic representation, which is often a logical formula or a semantic network.
- Semantic attachments are usually defined as functions or rules that map syntactic categories or constituents to semantic entities or relations.
- Semantic attachments can be used to perform various tasks in natural language processing, such as:
  - Semantic parsing: the process of converting a natural language sentence into a formal representation of its meaning, such as a logical form or a semantic frame.
  - Semantic interpretation: the process of assigning a meaning to a natural language sentence or a discourse, taking into account the context, the world knowledge, and the pragmatics.
  - Semantic generation: the process of producing a natural language sentence that expresses a given meaning, such as a logical form or a semantic frame.
  - Semantic inference: the process of deriving new information from a given meaning representation, such as a logical form or a semantic frame, using logical rules or semantic relations.
- Semantic attachments can be implemented in different ways, depending on the type of syntactic and semantic representations used, and the level of granularity and complexity of the semantic analysis. Some examples are:
  - Feature structures: a way of representing syntactic and semantic information as sets of attribute-value pairs, where the values can be atomic symbols, variables, or other feature structures. Semantic attachments can be defined as constraints or equations that relate the features of different structures.
  - Lambda calculus: a way of representing syntactic and semantic information as expressions that consist of variables, constants, and functions, where functions can be applied to arguments using the lambda operator. Semantic attachments can be defined as functions that map syntactic categories or constituents to lambda expressions.
  - Semantic networks: a way of representing syntactic and semantic information as graphs, where the nodes are concepts or entities, and the edges are relations or roles. Semantic attachments can be defined as rules that map syntactic categories or constituents to nodes or edges in the network.



### Word Senses

- A word sense is a representation of one aspect of a word's meaning.
- A word can have multiple senses, depending on the context in which it is used. For example, the word "bank" can mean a financial institution, a sloping mound, a biological repository, or a building where a bank does its business.
- Word sense disambiguation (WSD) is the task of assigning the appropriate sense to a given word in a text or discourse  .
- WSD is a challenging problem in natural language processing (NLP) because natural language is ambiguous, and many words can be interpreted in multiple ways depending on the context .
- WSD is important for many NLP applications, such as machine translation, information retrieval, text summarization, question answering, and sentiment analysis, because the correct interpretation of a word can affect the overall meaning and quality of the output .
- WSD can be performed using various methods, such as rule-based, knowledge-based, supervised, semi-supervised, or unsupervised approaches .
- Neural word representations, such as word embeddings, have proven useful in WSD because they can efficiently model complex semantic and syntactic word relationships.
- However, most word embedding techniques model only one representation per word, despite the fact that a single word can have multiple senses.
- Sense2vec is a method for word sense disambiguation that leverages word embeddings and part-of-speech tags to create multiple representations for each word sense.
- Sense2vec can achieve fast and accurate WSD by using a simple nearest neighbor approach to find the most similar sense vector for a given word in a context.



### Relations between Senses

- Senses are the meanings of words or expressions in a given context or situation.
- Semantics is the study of the relations between senses and the objects or concepts they refer to.
- Pragmatics is the study of the relations between senses and the users or contexts of language.
- There are different types of relations between senses, such as:
  - Synonymy: when two or more senses have the same or very similar meaning, e.g. big and large, sofa and couch, happy and glad.
  - Antonymy: when two senses have opposite or contrasting meanings, e.g. hot and cold, up and down, true and false.
  - Hyponymy: when one sense is more specific or included in another sense, e.g. rose and flower, dog and animal, red and color.
  - Meronymy: when one sense is a part or component of another sense, e.g. finger and hand, wheel and car, chapter and book.
  - Homonymy: when two or more senses have the same form but different meanings, e.g. bank (financial institution) and bank (river side), bat (animal) and bat (sport equipment), date (fruit) and date (calendar day).
  - Polysemy: when one sense has multiple related meanings, e.g. head (body part) and head (leader), foot (body part) and foot (unit of measurement), eye (organ) and eye (hole in a needle).
- Relations between senses can be studied at different levels of language, such as:
  - Lexical: the relations between the senses of individual words, e.g. synonyms, antonyms, hyponyms, etc.
  - Phrasal: the relations between the senses of phrases or combinations of words, e.g. idioms, metaphors, collocations, etc.
  - Sentential: the relations between the senses of sentences or clauses, e.g. entailment, implication, contradiction, etc.
  - Discourse: the relations between the senses of larger units of language, such as paragraphs, texts, conversations, etc., e.g. coherence, cohesion, relevance, etc.
- Relations between senses are influenced by various factors, such as:
  - Context: the situation or environment in which language is used, e.g. time, place, speaker, listener, purpose, etc.
  - Culture: the shared beliefs, values, norms, and practices of a group of people, e.g. religion, ethnicity, nationality, etc.
  - World knowledge: the general or specific information that a speaker or listener has about the world, e.g. facts, opinions, experiences, etc.
  - Inference: the process of deriving or drawing conclusions from the available information, e.g. logic, reasoning, evidence, etc.



### Thematic Roles

- Thematic roles are the semantic relationships between a verb and its arguments (the noun phrases that appear with the verb).
- Thematic roles describe the role or function of each argument in relation to the verb.
- Thematic roles are also known as theta roles or semantic roles.
- Thematic roles are important for natural language processing because they help to identify the meaning and structure of sentences.
- Different verbs assign different thematic roles to their arguments, depending on their meaning and usage.
- Some of the major thematic roles are:

  - Agent: The entity that intentionally performs the action of the verb. Example: *John* opened the door. (*John* is the agent of the verb opened.)
  - Patient: The entity that undergoes the action or is affected by the action of the verb. Example: John opened *the door*. (*The door* is the patient of the verb opened.)
  - Theme: The entity that is moved or changes location or state as a result of the action of the verb. Example: John gave *a book* to Mary. (*A book* is the theme of the verb gave.)
  - Experiencer: The entity that perceives or feels something expressed by the verb. Example: John *likes* chocolate. (John is the experiencer of the verb likes.)
  - Instrument: The entity that is used to perform the action of the verb. Example: John opened the door *with a key*. (*A key* is the instrument of the verb opened.)
  - Beneficiary: The entity that benefits from or is intended to benefit from the action of the verb. Example: John baked *a cake* for Mary. (Mary is the beneficiary of the verb baked.)
  - Source: The entity from which something originates or moves away. Example: John took the book *from the shelf*. (*The shelf* is the source of the verb took.)
  - Goal: The entity to which something moves or is directed. Example: John gave the book *to Mary*. (*Mary* is the goal of the verb gave.)
  - Location: The entity that specifies the place or position of something. Example: John put the book *on the table*. (*The table* is the location of the verb put.)

- Thematic roles are assigned by the verb to its arguments based on the theta criterion, which states that each argument must receive exactly one thematic role, and each thematic role must be assigned to exactly one argument.



### Selectional restrictions

- Selectional restrictions are semantic constraints that limit the possible arguments of a word or a phrase .
- They account for the implausibility or ungrammaticality of sentences such as *Colorless green ideas slept furiously* or *The chair ate the sandwich* .
- They are often represented as semantic features or types that specify the legal combinations of senses that can co-occur  .
- They can be used in natural language processing for tasks such as disambiguation, pronoun resolution, and sentence generation  .
- They can be violated for rhetorical or poetic effects, such as metaphor, irony, or humor. For example, *The sun smiled at me* violates the selectional restriction of *smile* that requires a human or animate subject.



### Word Sense Disambiguation

- Word sense disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings (polysemy).
- WSD is important for natural language processing applications such as machine translation, information retrieval, text summarization, question answering, etc.
- WSD can be classified into two types: lexical and structural.
  - Lexical WSD is based on the similarity or relatedness of the words in the context, such as synonyms, antonyms, hypernyms, hyponyms, etc.
  - Structural WSD is based on the syntactic and semantic roles of the words in the context, such as subject, object, modifier, etc.
- WSD can be approached by different methods, such as supervised, unsupervised, semi-supervised, and knowledge-based.
  - Supervised WSD uses annotated corpora to train machine learning models that can predict the word sense based on features extracted from the context.
  - Unsupervised WSD uses clustering algorithms to group similar word senses based on their co-occurrence patterns in large corpora.
  - Semi-supervised WSD combines supervised and unsupervised methods to leverage both labeled and unlabeled data.
  - Knowledge-based WSD uses external resources such as dictionaries, thesauri, ontologies, etc. to infer the word sense based on the definitions, examples, relations, etc. of the word and its context.
- WSD is a challenging and open problem in natural language processing, as it requires a deep understanding of the language, the domain, and the world knowledge. Some of the difficulties and limitations of WSD are:
  - The lack of standard and comprehensive sense inventories that can cover all the possible meanings of a word in different domains and languages.
  - The sparsity and noise of the annotated data that can affect the performance and generalization of the supervised methods.
  - The ambiguity and variability of the natural language that can make the word sense dependent on the speaker, the listener, the situation, the culture, etc.
  - The granularity and specificity of the word sense that can vary depending on the task and the application. For example, a coarse-grained sense may be sufficient for information retrieval, but a fine-grained sense may be needed for machine translation.



### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the common supervised WSD algorithms are:
  - Naive Bayes: This is a probabilistic classifier that assigns the most likely sense to a word based on the frequencies of its features in the training data.
  - Decision Trees: This is a rule-based classifier that splits the feature space into regions based on a series of binary decisions, and assigns the most frequent sense in each region.
  - Support Vector Machines: This is a linear classifier that finds the optimal hyperplane that separates the feature vectors of different senses with the maximum margin.
  - Neural Networks: This is a non-linear classifier that learns a complex function that maps the input features to the output senses, using hidden layers of neurons and activation functions.
- Supervised WSD methods have the advantage of being able to learn from large amounts of data and achieve high accuracy, but they also have some limitations, such as:
  - Data sparsity: The sense-annotated corpora are often incomplete, noisy, and inconsistent, and may not cover all the possible senses and contexts of a word .
  - Domain adaptation: The trained models may not generalize well to new domains or genres that have different distributions of words and senses .
  - Sense granularity: The sense inventory used for annotation may not match the level of detail required for a specific application or task .



### Dictionary & Thesaurus for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- A dictionary is a resource that provides information about the meaning, spelling, pronunciation, and usage of words in a language.
- A thesaurus is a resource that provides synonyms and antonyms of selected words in a language, thus grouping words according to similarity.
- Both dictionary and thesaurus are useful for natural language processing (NLP), which is the application of machine learning algorithms to the analysis, understanding, and manipulation of written or spoken examples of human language.
- Some of the benefits of using dictionary and thesaurus for NLP are:
  - They can help to resolve lexical ambiguity, which is the problem of determining the correct sense of a word in a given context.
  - They can help to enrich the vocabulary and improve the style of natural language generation, which is the task of producing natural language text from non-linguistic data.
  - They can help to enhance the performance of various NLP tasks, such as information retrieval, text summarization, sentiment analysis, and machine translation.
- Some of the challenges of using dictionary and thesaurus for NLP are:
  - They may introduce a large measure of hard-to-resolve ambiguity to the NLP task, if the thesaurus is viewed as a classification of word senses, since different words may have multiple and overlapping senses.
  - They may not cover all the possible words and senses in a language, especially for new and domain-specific terms, thus limiting the coverage and accuracy of the NLP task.
  - They may not reflect the dynamic and evolving nature of natural language, as words may change their meaning and usage over time and across contexts, thus requiring constant updating and maintenance.



### Bootstrapping methods for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a mapping from input to output.
- Bootstrapping methods can be applied to various natural language processing tasks, such as part-of-speech tagging, named entity recognition, relation extraction, semantic parsing, etc .
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., tags, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., rules, patterns, examples, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using pattern matching, classification, clustering, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more new things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can benefit from a broad-coverage, rule-based parser that can compute probabilities while parsing an untagged corpus of natural language text, and then incorporate those probabilities into the processing of the same parser as it analyzes new text.
- Bootstrapping methods can face some challenges, such as data sparsity, noise propagation, semantic drift, etc . Various techniques have been proposed to address these challenges, such as using multiple seed sets, filtering unreliable patterns, incorporating external knowledge, etc .



### Word Similarity using Thesaurus and Distributional methods

- Word similarity is a measure of how closely related two words are in terms of their meaning, usage, or association.
- Word similarity can be computed using different methods, such as thesaurus-based methods and distributional methods.
- Thesaurus-based methods rely on manually curated lexical resources, such as WordNet, that group words into synsets (sets of synonyms) and link them with semantic relations, such as hypernymy (is-a), meronymy (part-of), antonymy (opposite-of), etc.
- Thesaurus-based methods can compute word similarity by counting the number of steps or links between two words in the thesaurus hierarchy, or by comparing the features or attributes of the words, such as their definitions, examples, or glosses.
- Distributional methods rely on large corpora of text, such as Wikipedia, that provide statistical information about how words co-occur with other words in different contexts.
- Distributional methods can compute word similarity by representing words as vectors of numerical values, where each value corresponds to the frequency or weight of a word in a given dimension or feature, such as a document, a topic, or a word cluster.
- Distributional methods can compare word vectors using different similarity measures, such as cosine similarity, Jaccard similarity, or Euclidean distance, to obtain a score between 0 and 1, where 0 means no similarity and 1 means perfect similarity.
- Both thesaurus-based methods and distributional methods have advantages and disadvantages, such as:
  - Thesaurus-based methods can capture fine-grained semantic distinctions and relations, but they are limited by the coverage and quality of the thesaurus, and they may not reflect the current or dynamic usage of words in natural language.
  - Distributional methods can capture general and contextual similarity, but they may not capture the nuances or subtleties of meaning, and they may be affected by noise or sparsity of data in the corpus.



## Unit 4 - BASIC CONCEPTS of Speech Processing

Speech processing is the study of how humans produce, perceive, and understand speech, as well as how speech can be processed by machines. Speech processing involves three major levels of processing: production, perception, and analysis.

- Speech production is the process by which thoughts are translated into speech. This includes the selection of words, the organization of relevant grammatical forms, and then the articulation of the resulting sounds by the motor system using the vocal apparatus.
- Speech perception is the process by which the acoustic signals of speech are decoded and interpreted by the auditory system and the brain. This involves the recognition of speech sounds, words, phrases, and sentences, as well as the extraction of meaning and intention from speech.
- Speech analysis is the process by which speech signals are transformed into numerical or symbolic representations that can be manipulated by machines. This involves the extraction of features, such as pitch, intensity, duration, and spectral properties, from speech signals, as well as the application of algorithms and techniques, such as segmentation, classification, recognition, synthesis, and enhancement, to achieve various objectives, such as speech recognition, speech synthesis, speech compression, speech enhancement, and speech translation.

Some of the basic concepts of speech processing are:

- Speech is a complex and dynamic signal that varies in time and frequency. Speech signals can be represented in different domains, such as time domain, frequency domain, and cepstral domain, depending on the purpose of analysis and processing.
- Speech is composed of basic units, such as phonemes, syllables, words, and phrases, that have different levels of linguistic and acoustic information. Speech signals can be segmented and labeled according to these units, using methods such as acoustic-phonetic, statistical, or hybrid approaches.
- Speech is influenced by various factors, such as speaker identity, gender, age, accent, emotion, and noise. Speech signals can be characterized and modeled by these factors, using methods such as speaker recognition, speaker adaptation, speech emotion recognition, and speech enhancement.
- Speech is a natural and intuitive mode of communication for humans. Speech signals can be used to interact with machines, using methods such as speech recognition, speech synthesis, speech dialogue systems, and speech translation.



### Speech Fundamentals

- Speech is a natural mode of communication for humans, and it has many applications in natural language processing (NLP), such as speech recognition, speech synthesis, speech translation, speech emotion recognition, etc.
- Speech is a complex signal that consists of acoustic, linguistic, and paralinguistic information. Acoustic information refers to the physical properties of sound waves, such as frequency, amplitude, and duration. Linguistic information refers to the meaning and structure of words, phrases, and sentences. Paralinguistic information refers to the speaker's identity, emotion, attitude, and intention.
- Speech processing is the field of study that deals with the analysis, synthesis, and manipulation of speech signals. Speech processing can be divided into two main subfields: speech analysis and speech synthesis. Speech analysis is the process of extracting useful information from speech signals, such as the speaker's identity, emotion, language, accent, etc. Speech synthesis is the process of generating speech signals from text or other sources, such as images, videos, etc.
- Speech processing involves various techniques and methods from different disciplines, such as signal processing, machine learning, linguistics, phonetics, etc. Some of the common techniques and methods used in speech processing are:

  - **Feature extraction**: The process of transforming speech signals into a set of numerical values that represent the salient characteristics of the speech, such as pitch, energy, spectral envelope, etc. Feature extraction is usually done by applying various filters, transformations, and statistical methods to the speech signals.
  - **Classification**: The process of assigning a label or a category to a speech signal or a segment of a speech signal, such as the speaker's identity, emotion, language, etc. Classification is usually done by applying various machine learning algorithms, such as decision trees, support vector machines, neural networks, etc., to the extracted features.
  - **Recognition**: The process of converting speech signals into text or other symbolic representations, such as phonetic symbols, words, phrases, etc. Recognition is usually done by applying various models and algorithms, such as hidden Markov models, n-gram models, deep neural networks, etc., to the extracted features and the linguistic knowledge.
  - **Synthesis**: The process of generating speech signals from text or other sources, such as images, videos, etc. Synthesis is usually done by applying various models and algorithms, such as concatenative synthesis, parametric synthesis, neural network synthesis, etc., to the input source and the acoustic knowledge.
  - **Transformation**: The process of modifying speech signals to achieve a desired effect, such as changing the speaker's identity, emotion, accent, etc. Transformation is usually done by applying various methods, such as pitch shifting, time scaling, spectral manipulation, etc., to the speech signals.



### Articulatory Phonetics

- Articulatory phonetics is the branch of phonetics that studies how speech sounds are produced by the human vocal tract .
- Speech sounds are produced by the movements and/or positions of the vocal organs, such as the tongue, lips, teeth, palate, velum, glottis, etc. These are called articulators .
- Articulatory phonetics is concerned with the transformation of aerodynamic energy (airflow through the vocal tract) into acoustic energy (sound waves) .
- Articulatory phonetics can be used to describe and classify the speech sounds of the world's languages in terms of their articulatory features, such as place of articulation, manner of articulation, voicing, etc.  .
- Articulatory phonetics can also be used to analyze the patterns and rules of sound change and variation in different languages and dialects  .
- Articulatory phonetics is an integrated part of a communication system that also includes speech perception, speech acoustics, and speech physiology .



### Production And Classification Of Speech Sounds

- Speech sounds are the basic units of human communication that are produced by the vocal organs and perceived by the auditory system.
- Speech sounds can be classified into two broad categories: vowels and consonants.
- Vowels are speech sounds that are produced with no obstruction or narrowing of the air stream in the vocal tract, allowing the air to flow freely. Vowels are usually voiced, meaning that the vocal folds vibrate during their production. Vowels are characterized by their height, backness, roundness, and length.
- Consonants are speech sounds that are produced with some degree of constriction or closure of the air stream in the vocal tract, creating friction or turbulence. Consonants can be voiced or voiceless, depending on whether the vocal folds vibrate or not. Consonants are characterized by their place, manner, and voicing.
- The production of a speech sound involves four main processes: initiation, phonation, oro-nasal process, and articulation.
  - Initiation is the generation of the air stream that powers the speech sound, usually by the lungs.
  - Phonation is the modulation of the air stream by the vocal folds in the larynx, creating periodic or aperiodic vibrations that affect the pitch and quality of the sound.
  - Oro-nasal process is the direction of the air stream into either the oral cavity or the nasal cavity by the velum, a soft tissue that can open or close the passage to the nose.
  - Articulation is the shaping of the air stream by the tongue, lips, teeth, and other parts of the oral cavity, creating different resonances and noises that distinguish the speech sounds.
- Speech sounds can be represented by symbols that indicate their phonetic features, such as the International Phonetic Alphabet (IPA). The IPA is a standardized system of symbols that can transcribe any speech sound in any language. The IPA symbols are enclosed in square brackets [ ] to indicate that they are phonetic transcriptions, not orthographic spellings. For example, the word 'cat' can be transcribed as [kæt] in IPA, where [k] is a voiceless velar stop, [æ] is a low front unrounded vowel, and [t] is a voiceless alveolar stop.



### Acoustic Phonetics

- Acoustic phonetics is the branch of phonetics that studies the acoustic properties of speech sounds, such as their frequency, intensity, and duration .
- Acoustic phonetics relies on instruments and methods to record, store, visualize, and analyze the speech signal.
- Acoustic phonetics can be divided into three main areas: source, filter, and transmission.
  - Source: The source of speech sounds is the vibration of the vocal folds in the larynx, which produces a complex periodic wave called the glottal source or the voice source.
  - Filter: The filter is the vocal tract, which shapes the glottal source by resonating at certain frequencies, called formants, and attenuating others. The vocal tract can be modeled as a series of tubes with different lengths and diameters, which affect the acoustic output.
  - Transmission: The transmission is the propagation of the speech signal from the speaker's mouth to the listener's ear, which involves factors such as distance, direction, environment, and noise.
- Acoustic phonetics uses various tools and techniques to measure and represent the speech signal, such as:
  - Waveform: A waveform is a graphical representation of the variation of amplitude (or pressure) over time. A waveform can show the overall loudness and duration of a speech sound, as well as the presence or absence of voicing.
  - Spectrum: A spectrum is a graphical representation of the variation of amplitude (or energy) over frequency. A spectrum can show the frequency components of a speech sound, such as the fundamental frequency (or pitch) and the formants (or resonances).
  - Spectrogram: A spectrogram is a graphical representation of the variation of amplitude (or energy) over both time and frequency. A spectrogram can show the temporal and spectral changes of a speech sound, such as the onset and offset of voicing, the transitions between formants, and the presence of noise.
- Acoustic phonetics can be applied to various fields and purposes, such as:
  - Speech synthesis: Speech synthesis is the process of generating artificial speech from text or other input. Acoustic phonetics can provide the rules and parameters for creating natural-sounding speech sounds.
  - Speech recognition: Speech recognition is the process of converting speech into text or other output. Acoustic phonetics can provide the features and models for identifying and classifying speech sounds.
  - Speech analysis: Speech analysis is the process of examining speech for various purposes, such as linguistic research, forensic investigation, clinical diagnosis, and education. Acoustic phonetics can provide the methods and tools for describing and comparing speech sounds.



### Acoustics of Speech Production

- Acoustics of speech production is the study of how speech sounds are generated and modified by the human vocal tract.
- Speech production involves a source of sound energy (e.g. the larynx) and a filter function (e.g. the vocal tract) that shapes the sound spectrum.
- The source of sound energy can be either periodic (e.g. voiced sounds) or aperiodic (e.g. voiceless sounds).
- The filter function is determined by the shape and size of the vocal tract, which can vary depending on the position of the articulators (e.g. tongue, lips, jaw, etc.) .
- The vocal tract can be modeled as a series of connected tubes with different cross-sectional areas and lengths .
- The acoustic characteristics of speech sounds depend on the resonance frequencies of the vocal tract, which are called formants .
- Formants are peaks of energy in the sound spectrum that correspond to the natural frequencies of vibration of the vocal tract .
- Different speech sounds have different patterns of formants, which can be used to identify and classify them .
- Speech production is also influenced by feedback mechanisms, such as hearing, perception, and information processing in the nervous system and the brain .
- Speech production is a complex and dynamic process that involves multiple levels of analysis and representation .



### Review Of Digital Signal Processing Concepts

- Digital signal processing (DSP) is the use of digital processing, such as by computers or more specialized digital signal processors, to perform a wide variety of signal processing operations.
- The digital signals processed in this manner are a sequence of numbers that represent samples of a continuous variable in a domain such as time, space, frequency, etc.
- Digital signal processing is used for storing, transmitting, analyzing, modifying, and extracting the information contained in the signals.
- Digital signal processing is essential for applications such as speech recognition, natural language processing, audio and video processing, biomedical signal processing, etc.
- The most common core steps of digital signal processing are:
  - Data digitizing – Convert continuous signals to finite discrete digital signals using analog-to-digital converters (ADCs).
  - Eliminate unwanted noise using filters, such as low-pass, high-pass, band-pass, etc.
  - Improve quality by increasing/decreasing certain signal amplitudes using amplifiers, attenuators, equalizers, etc.
  - Ensure security during transmission by encoding the data using techniques such as encryption, compression, modulation, etc.
  - Minimize errors by detecting and correcting them using techniques such as error detection and correction codes, checksums, parity bits, etc.
  - Store data using digital storage devices, such as hard disks, flash drives, etc.
  - Easy and secure access to the stored data using techniques such as authentication, authorization, encryption, etc.
- A typical block diagram of a digital signal processing system is shown below:

Block diagram of a digital signal processing system

- Some of the advantages of digital signal processing are:
  - Higher accuracy and precision
  - Higher speed and efficiency
  - Higher flexibility and scalability
  - Higher reliability and robustness
  - Lower cost and power consumption
- Some of the disadvantages of digital signal processing are:
  - Loss of information due to quantization and sampling
  - Delay and latency due to processing time
  - Complexity and difficulty of design and implementation
  - Hardware and software limitations and constraints



### Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique for analyzing the frequency content of a signal over time.
- It involves dividing the signal into overlapping segments, applying a window function to each segment, and computing the discrete Fourier transform (DFT) of the windowed segments.
- The result is a two-dimensional representation of the signal, where the horizontal axis is time and the vertical axis is frequency.
- The STFT can reveal how the spectral properties of the signal change over time, such as the onset and decay of harmonics, the modulation of frequency and amplitude, and the presence of noise and interference.
- The STFT is widely used for speech and audio processing, such as speech enhancement, speech recognition, speaker identification, audio compression, audio synthesis, and audio effects.
- The STFT has some limitations, such as the trade-off between time and frequency resolution, the leakage of spectral components due to windowing, and the redundancy of the overlapping segments.
- The STFT can be modified or extended to overcome some of these limitations, such as using different window functions, different segment lengths, different overlap ratios, or different types of transforms, such as the discrete cosine transform (DCT) or the wavelet transform.



### Filter Bank and LPC Methods

- Filter bank and LPC methods are two techniques for extracting features from speech signals for speech processing applications such as speech recognition, speech synthesis, and speech coding.
- Filter bank methods divide the speech signal into frequency bands and compute the energy or power spectrum of each band. The most common filter bank method is the mel-frequency cepstral coefficients (MFCC) method, which uses a set of triangular filters spaced according to the mel scale, which approximates the human perception of frequency. The MFCC method consists of the following steps:
  - Pre-emphasize the speech signal to boost the high-frequency components and reduce the effect of noise.
  - Apply a Hamming window to the speech signal to reduce the spectral leakage and smooth the edges of the signal.
  - Perform a fast Fourier transform (FFT) on the windowed signal to obtain the magnitude spectrum.
  - Apply the mel filter bank to the magnitude spectrum and sum the energy in each filter.
  - Take the logarithm of the filter bank energies to mimic the human perception of loudness.
  - Perform a discrete cosine transform (DCT) on the log filter bank energies to obtain the cepstral coefficients, which are the features used for speech processing.
- LPC methods model the speech signal as the output of a linear filter driven by an excitation signal. The linear filter represents the vocal tract, which shapes the speech signal by resonating at certain frequencies called formants. The excitation signal represents the source of the speech, which can be either a periodic pulse train for voiced sounds or a random noise for unvoiced sounds. The LPC method consists of the following steps:
  - Estimate the coefficients of the linear filter by minimizing the prediction error, which is the difference between the actual speech signal and the predicted speech signal based on the past samples. This can be done by solving the Yule-Walker equations or using the Levinson-Durbin algorithm.
  - Apply the inverse of the linear filter to the speech signal to obtain the residual signal, which is the excitation signal.
  - Quantize the filter coefficients and the residual signal to reduce the bit rate for speech coding or transmission.
  - Synthesize the speech signal by reversing the process: use the residual signal as the source signal, use the filter coefficients to create a filter that represents the vocal tract, and run the source signal through the filter to obtain the speech signal.



## Unit 5 - SPEECH-ANALYSIS

- Speech-analysis is the process of examining the features and characteristics of spoken language, such as sounds, words, sentences, intonation, rhythm, and meaning.
- Speech-analysis can be done for various purposes, such as:
  - Speech recognition: the task of converting speech signals into text or commands that can be understood by a computer system.
  - Speech synthesis: the task of generating speech signals from text or commands that can be spoken by a computer system.
  - Speech enhancement: the task of improving the quality and intelligibility of speech signals by reducing noise, distortion, or interference.
  - Speech segmentation: the task of dividing speech signals into smaller units, such as phonemes, syllables, words, or phrases.
  - Speech transcription: the task of writing down the words and symbols that represent the speech signals.
  - Speech translation: the task of converting speech signals from one language to another.
  - Speech diarization: the task of identifying and separating the speakers and their turns in a multi-speaker speech signal.
  - Speech emotion recognition: the task of detecting and classifying the emotional states and attitudes of the speakers from their speech signals.
  - Speech summarization: the task of extracting the main points and information from a speech signal and presenting them in a concise and coherent way.
  - Speech evaluation: the task of assessing the quality, accuracy, fluency, and appropriateness of speech signals, such as in language learning or speech therapy.
- Speech-analysis can be done using different methods and techniques, such as:
  - Acoustic analysis: the method of measuring and analyzing the physical properties of speech signals, such as frequency, amplitude, duration, and spectrum.
  - Phonetic analysis: the method of describing and classifying the sounds of speech signals, such as vowels, consonants, and tones, using symbols and rules.
  - Prosodic analysis: the method of studying and modeling the patterns of stress, pitch, and intonation in speech signals, which convey information about the structure, meaning, and emotion of speech.
  - Lexical analysis: the method of identifying and extracting the words and their parts, such as roots, prefixes, and suffixes, from speech signals, using dictionaries and rules.
  - Syntactic analysis: the method of analyzing and parsing the structure and grammar of sentences in speech signals, using rules and algorithms.
  - Semantic analysis: the method of understanding and representing the meaning and logic of sentences and discourse in speech signals, using concepts and relations.
  - Pragmatic analysis: the method of interpreting and inferring the context, intention, and implication of speech signals, using knowledge and reasoning.
- Speech-analysis can be done using different tools and software, such as:
  - Speech-analysis software: the software that provides various functions and features for speech-analysis, such as recording, editing, annotating, visualizing, and processing speech signals.
  - Speech-analysis libraries: the libraries that provide various modules and functions for speech-analysis, such as speech recognition, speech synthesis, speech segmentation, and speech emotion recognition.
  - Speech-analysis frameworks: the frameworks that provide various components and interfaces for speech-analysis, such as speech databases, speech models, speech algorithms, and speech applications.



### Features for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotions, intent, and the content of the speech.
- Speech analysis is a subfield of natural language processing (NLP), which is the branch of computer science and artificial intelligence that deals with understanding and generating natural language  .
- Speech analysis involves various techniques and applications, such as speech recognition, speech synthesis, speech segmentation, speech enhancement, speech coding, speech translation, speech summarization, speech emotion recognition, speaker identification, and speech diarization.
- Speech analysis can be performed at different levels of linguistic representation, such as acoustic, phonetic, phonological, lexical, syntactic, semantic, pragmatic, and discourse.
- Speech analysis can be based on different approaches, such as rule-based, statistical, neural, or hybrid.
- Speech analysis can be used for various purposes, such as human-computer interaction, voice-based authentication, voice search, voice assistants, voice cloning, voice analytics, voice biometrics, voice forensics, voice therapy, and voice education.



### Feature Extraction And Pattern Comparison Techniques for Speech Analysis

- Feature extraction is the process of transforming the speech signal into a set of features that represent the characteristics of the speech and the speaker.
- Feature extraction is important for speech analysis because it reduces the dimensionality and complexity of the speech signal, and enhances the discriminative and robust aspects of the speech.
- Feature extraction techniques can be divided into two categories: time-domain and frequency-domain techniques.
- Time-domain techniques operate on the speech waveform directly, and extract features such as zero-crossing rate, energy, pitch, and formants.
- Frequency-domain techniques transform the speech waveform into a spectral representation, and extract features such as cepstral coefficients, filter-bank coefficients, and spectral features.
- Some of the most popular feature extraction techniques for speech analysis are:
  - Linear Predictive Coding (LPC): LPC is a time-domain technique that models the speech signal as a linear combination of past samples, and estimates the coefficients of the linear predictor. LPC features are the predictor coefficients, the residual error, and the gain. LPC features are widely used for speech coding and synthesis, and can also be used for speech recognition and speaker identification  .
  - Mel-Frequency Cepstral Coefficients (MFCC): MFCC is a frequency-domain technique that applies a mel-scale filter bank to the speech spectrum, and computes the discrete cosine transform (DCT) of the log-filtered spectrum. MFCC features are the DCT coefficients, which capture the envelope of the speech spectrum. MFCC features are the most widely used features for speech recognition and speaker recognition, as they are robust to noise and channel variations   .
  - Linear Predictive Cepstral Coefficients (LPCC): LPCC is a frequency-domain technique that converts the LPC features into cepstral coefficients by applying a recursive relation. LPCC features are similar to MFCC features, but they are more sensitive to the spectral peaks and valleys. LPCC features are also used for speech recognition and speaker recognition, but they are less robust to noise and channel variations than MFCC features  .
  - Perceptual Linear Prediction (PLP): PLP is a frequency-domain technique that applies a perceptual weighting to the speech spectrum, and computes the LPC features of the weighted spectrum. PLP features are similar to LPC features, but they are more consistent with the human auditory perception. PLP features are also used for speech recognition and speaker recognition, and they are more robust to noise and channel variations than LPC features  .
  - Wavelet Transform (WT): WT is a frequency-domain technique that decomposes the speech signal into a set of wavelet coefficients, which represent the speech signal at different scales and resolutions. WT features are the wavelet coefficients, which capture the transient and non-stationary aspects of the speech signal. WT features are used for speech enhancement, speech segmentation, and speech recognition .
  - Other feature extraction techniques include Unique Mapped Real Transform (UMRT), Real Cepstral Coefficients (RCC), and Spectral Features  .

- Pattern comparison is the process of matching the extracted features of an unknown speech signal with the features of a known speech signal, and computing a similarity or distance measure between them.
- Pattern comparison is important for speech analysis because it enables the identification and recognition of the speech and the speaker, based on the features extracted from the speech signal.
- Pattern comparison techniques can be divided into two categories: template-based and model-based techniques.
- Template-based techniques compare the extracted features of an unknown speech signal with the features of a stored template, which represents a reference speech signal. Template-based techniques include Dynamic Time Warping (DTW), Vector Quantization (VQ), and Nearest Neighbor (NN)  .
  - Dynamic Time Warping (DTW): DTW is a template-based technique that aligns the extracted features of an unknown speech signal with the features of a stored template, by applying a non-linear warping function that minimizes the distance between them. DTW is used for speech recognition and speaker verification, as it can handle the variations in the speech duration and speed  .
  - Vector Quantization (VQ): VQ is a template-based technique that quantizes the extracted features of an unknown speech signal into a set of code vectors, which are selected from a codebook that represents



### Speech Distortion Measures

- Speech distortion measures are methods to quantify the amount and type of distortion that occurs in speech signals due to various factors, such as hearing loss, hearing aids, noise, or speech processing algorithms.
- Speech distortion measures can be classified into two categories: subjective and objective.
  - Subjective measures are based on human perception and evaluation of speech quality, intelligibility, or naturalness. They require human listeners to rate speech samples on a scale or to transcribe speech utterances. Examples of subjective measures are mean opinion score (MOS), speech intelligibility index (SII), or word recognition score (WRS).
  - Objective measures are based on mathematical or statistical calculations that compare speech signals or their features. They do not require human listeners, but they may or may not correlate well with subjective measures. Examples of objective measures are signal-to-noise ratio (SNR), spectral distortion (SD), or log-likelihood ratio (LLR).
- Speech distortion measures can be used for various purposes, such as evaluating the performance of hearing aids, speech enhancement algorithms, speech recognition systems, or speech synthesis systems. They can also be used for diagnosing and treating speech sound disorders, such as articulation or phonological impairments.



### Mathematical And Perceptual Speech Analysis

- Mathematical speech analysis is the study of how human language and mathematics relate to each other and to the real world. It involves the use of mathematical models, methods, and tools to describe, analyze, and understand various aspects of speech and language, such as phonology, morphology, syntax, semantics, and pragmatics.  
- Perceptual speech analysis is the study of how human speech is perceived and processed by the auditory system. It involves the use of psychophysical and physiological principles to derive and evaluate features of speech that are relevant for speech recognition, understanding, and communication. 
- Some of the topics covered in mathematical and perceptual speech analysis are:

  - Speech signal processing: the techniques for acquiring, transforming, enhancing, and synthesizing speech signals, such as sampling, filtering, Fourier analysis, linear prediction, cepstral analysis, etc.
  - Speech recognition: the techniques for identifying and transcribing the words and phrases spoken by a speaker, such as acoustic modeling, language modeling, decoding, adaptation, etc.
  - Speech synthesis: the techniques for generating natural-sounding speech from text or other symbolic representations, such as text analysis, prosody modeling, waveform generation, etc.
  - Speech coding: the techniques for compressing and transmitting speech signals over limited bandwidth channels, such as quantization, entropy coding, source coding, channel coding, etc.
  - Speech enhancement: the techniques for improving the quality and intelligibility of speech signals in noisy or reverberant environments, such as noise reduction, echo cancellation, dereverberation, etc.
  - Speech modification: the techniques for altering the characteristics of speech signals for various purposes, such as pitch shifting, time scaling, voice conversion, etc.
  - Speech segmentation: the techniques for dividing speech signals into smaller units, such as syllables, phonemes, words, etc., for further analysis or processing.
  - Speech feature extraction: the techniques for extracting relevant information from speech signals, such as spectral, temporal, prosodic, or articulatory features, for various applications, such as speaker identification, emotion recognition, speech pathology detection, etc.
  - Speech modeling: the techniques for representing and simulating the properties and behaviors of speech signals, such as statistical, physical, or neural models, for various tasks, such as speech generation, speech analysis, speech understanding, etc.
  - Speech perception: the study of how speech signals are interpreted and understood by the human auditory system, such as auditory scene analysis, auditory masking, auditory attention, etc.
  - Speech production: the study of how speech signals are generated and controlled by the human vocal tract, such as articulatory phonetics, speech motor control, speech aerodynamics, etc.
  - Speech communication: the study of how speech signals are used and exchanged in human interaction, such as speech acts, discourse analysis, pragmatics, etc.



### Log–Spectral Distance

- The log-spectral distance (LSD) is a distance measure between two spectra, expressed in decibels (dB).
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as:

$$
D_{LS} = \frac{1}{2\pi} \int_{-\pi}^{\pi} \left[ 10 \log_{10} \frac{P(\omega)}{P^(\omega)} \right]^2 d\omega
$$

- The log-spectral distance is symmetric, unlike the Itakura–Saito distance, which is another distance measure between spectra.
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum.
- The log-spectral distance can be used to evaluate the quality of speech synthesis or speech enhancement methods, by comparing the spectra of the original and the processed speech signals.
- The log-spectral distance can also be used to measure the similarity of speech signals from different speakers or languages, by comparing the average spectra of the speech signals.



### Cepstral Distances for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Cepstral distance is a measure of the similarity or dissimilarity between two speech frames based on their cepstral coefficients.
- Cepstral coefficients are obtained by applying the inverse Fourier transform to the logarithm of the spectrum of a speech signal .
- Cepstral distance can be used for various applications in speech analysis, such as endpoint detection, emotion recognition, speaker identification, and voice quality assessment  .
- One of the most common cepstral distance measures is the Euclidean distance between mel frequency cepstral coefficients (MFCC), which are cepstral coefficients derived from a filter bank algorithm that mimics the human auditory system.
- Cepstral distance can be combined with other features, such as speech energy, to improve the performance of speech analysis tasks.
- Cepstral distance can also be normalized or weighted to account for the perceptual significance of different cepstral coefficients.



### Weighted Cepstral Distances And Filtering

- Cepstrum is the inverse Fourier transform of the logarithm of the spectrum of a signal.
- Cepstral distance is a measure of similarity between two signals based on their cepstral coefficients, which are obtained by applying cepstral analysis to the signals.
- Cepstral analysis is a technique for extracting features from a signal, such as the vocal tract shape and the pitch of speech, by separating the source and the filter components of the signal.
- Weighted cepstral distance is a variant of cepstral distance that assigns different weights to different cepstral coefficients, according to their importance or relevance for a specific task or application.
- Weighted cepstral distance can be used for speech recognition, speaker identification, speech enhancement, and speech coding   .
- Weighted cepstral distance can be computed using different weighting schemes, such as inverse variance, perceptual, or deterministic  .
- Weighted cepstral distance can be combined with dynamic time warping (DTW) to align and compare two signals of different lengths or rates.
- Weighted cepstral distance can be interpreted as a weighted cepstral model norm, which reflects the underlying dynamics of the input/output signal pairs.
- Weighted cepstral distance can be extended to include higher-order cepstral coefficients, which capture more details of the signal characteristics.
- Weighted cepstral filtering is a technique for modifying the cepstral coefficients of a signal, such as to compensate for the spectral tilt or to enhance the perceptual quality of the signal.



### Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the similarity or dissimilarity between two short-time spectra of speech signals, which are often used in speech recognition systems to compare the input speech with the stored templates or models.
- Likelihood distortions can be derived from the likelihood function of a statistical model of speech, such as the Gaussian model or the autoregressive model, which assumes that the speech spectrum follows a certain probability distribution.
- Likelihood distortions can be classified into two types: log likelihood ratio (LLR) and likelihood ratio (LR). The LLR distortion is defined as the negative logarithm of the likelihood ratio, while the LR distortion is simply the likelihood ratio itself.
- The LLR distortion has some desirable properties, such as being symmetric, additive, and bounded, while the LR distortion is asymmetric, multiplicative, and unbounded.
- The LLR distortion can be further divided into two subtypes: the Itakura-Saito (IS) distortion and the cepstral (CEP) distortion. The IS distortion is derived from the Gaussian model with a diagonal covariance matrix, while the CEP distortion is derived from the Gaussian model with a full covariance matrix.
- The IS distortion is computationally efficient and invariant to the gain of the speech signal, but it is sensitive to the spectral shape and does not account for the perceptual relevance of different frequency bands. The CEP distortion is more accurate and robust, but it is computationally expensive and requires the inversion of the covariance matrix.
- To overcome the limitations of the IS and CEP distortions, some perceptually based distortions have been proposed, such as the weighted likelihood ratio (WLR) and the weighted slope metric (WSM) distortions. The WLR distortion is a modified version of the LR distortion that applies a frequency-dependent weighting function to the likelihood ratio, while the WSM distortion is a modified version of the LLR distortion that applies a frequency-dependent weighting function to the slope of the log spectrum.
- The WLR and WSM distortions aim to incorporate the perceptual importance of different frequency bands, such as the Bark scale or the mel scale, which are more consistent with the human auditory system. The WLR and WSM distortions also account for the suprasegmental information of speech, such as the energy and loudness, which can improve the recognition performance.
- According to a comparative study of several distortion measures for speech recognition, the LLR and WSM distortions gave the highest recognition accuracy, while the IS distortion gave the lowest score . The addition of suprasegmental information helped the recognition performance, while the use of gain and absolute loudness degraded the performance. The Bark-scale frequency warping did not perform as well as the unwarped counterpart for the highly bandlimited telephone data base. The WLR distortion did not perform as well as the unweighted counterpart.



### Spectral Distortion Using A Warped Frequency Scale

- Spectral distortion is the difference between the original and the reconstructed spectra of a speech signal, usually measured in decibels (dB).
- A warped frequency scale is a nonlinear transformation of the frequency axis that changes the resolution and spacing of the frequency bins.
- Warping the frequency scale can improve the perceptual accuracy and robustness of spectral analysis and modeling techniques, such as linear prediction (LP) and cepstral analysis.
- A common example of a warped frequency scale is the Bark scale, which is based on the critical band-rate of the human auditory system. The Bark scale compresses the high frequencies and expands the low frequencies, reflecting the higher sensitivity and resolution of the human ear at lower frequencies.
- Another example of a warped frequency scale is the Mel scale, which is based on the just noticeable differences in frequency of the human ear. The Mel scale is similar to the Bark scale, but it has a linear segment at low frequencies and a logarithmic segment at high frequencies.
- To apply a warped frequency scale to spectral analysis, the speech signal is first filtered by a bank of band-pass filters that have center frequencies and bandwidths corresponding to the warped scale. Then, the spectral coefficients are computed from the filtered signal using a suitable technique, such as LP or cepstral analysis.
- To measure the spectral distortion between the original and the reconstructed spectra on a warped frequency scale, the inverse warping function is applied to the spectral coefficients, and then the distortion is computed in dB using a suitable metric, such as log-spectral distortion or cepstral distortion.
- The advantage of using a warped frequency scale for spectral distortion measurement is that it can reduce the influence of the harmonic peaks and the spectral tilt of the speech signal, and focus more on the spectral envelope, which is more relevant for speech perception and recognition.



### LPC for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- LPC stands for Linear Predictive Coding, which is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model .
- LPC analyzes the speech signal by estimating the formants, which are the resonant frequencies of the vocal tract, and removing their effects from the speech signal, resulting in a residual signal that contains the pitch and the glottal excitation.
- The process of removing the formants is called inverse filtering, and the residual signal after the subtraction of the filtered modeled signal is called the residue.
- LPC can be used for speech coding, speech synthesis, speech recognition, and speaker identification .
- LPC is based on the assumption that a speech sample can be approximated by a linear combination of past samples, and that the coefficients of this linear combination can be obtained by minimizing the mean squared error between the original and the predicted samples .
- LPC can be performed in two steps: analysis and synthesis.
  - In the analysis step, the reflection coefficients are extracted from the speech signal using an algorithm such as autocorrelation, covariance, or Burg's method, and then converted to the LPC coefficients, which represent the filter that models the spectral envelope of the speech signal .
  - In the synthesis step, the LPC coefficients are used to reconstruct the speech signal by applying the inverse filter to the residual signal, which can be either the original residue or a synthetic one generated by a source model such as an impulse train or a white noise .
- LPC can be evaluated by measuring the quality and intelligibility of the synthesized speech, as well as the compression ratio and the bit rate of the encoded speech .



### PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction, which is the computation of a set of parameters that represent the characteristics of the speech signal.
- Feature extraction methods aim to reduce the dimensionality of the speech signal, remove the irrelevant or redundant information, and enhance the discriminative power of the features.
- Some of the most widely used feature extraction methods for speech analysis are Perceptual Linear Prediction (PLP) and Mel Frequency Cepstral Coefficients (MFCC).

#### Perceptual Linear Prediction (PLP)

- PLP is a feature extraction method that mimics the human auditory system, by applying a series of transformations to the speech signal that simulate the perceptual effects of the ear.
- PLP consists of the following steps :
  - Pre-emphasis: a high-pass filtering that enhances the high-frequency components of the speech signal and reduces the effect of noise.
  - Framing and windowing: dividing the speech signal into short segments (frames) of 20-30 ms, and applying a window function (such as Hamming) to each frame to smooth the edges and reduce spectral leakage.
  - Critical-band analysis: applying a filter bank that divides the frequency spectrum into a number of bands that correspond to the critical bands of the human ear. The critical bands are non-uniformly spaced, with higher resolution at lower frequencies and lower resolution at higher frequencies.
  - Intensity-loudness conversion: applying a non-linear transformation that converts the intensity (power) of each critical band into loudness (perceived sound level). The loudness is proportional to the logarithm of the intensity, and is scaled by a factor that depends on the frequency.
  - Equal-loudness pre-emphasis: applying a weighting function that compensates for the variation of the loudness sensitivity of the human ear across different frequencies. The weighting function boosts the low-frequency components and attenuates the high-frequency components of the loudness spectrum.
  - Autoregressive modeling: fitting an autoregressive (AR) model to the loudness spectrum, which estimates the spectral envelope of the speech signal. The AR model is a linear predictor that expresses the current value of the signal as a linear combination of its past values. The coefficients of the AR model are the PLP features, which capture the spectral shape of the speech signal.
  - Cepstral analysis: applying a discrete cosine transform (DCT) to the PLP features, which decorrelates them and reduces their dimensionality. The DCT coefficients are called the PLP cepstrum, which are the final features used for speech analysis.

#### Mel Frequency Cepstral Coefficients (MFCC)

- MFCC is another feature extraction method that mimics the human auditory system, by applying a similar series of transformations to the speech signal as PLP, but with some differences.
- MFCC consists of the following steps  :
  - Pre-emphasis: same as PLP.
  - Framing and windowing: same as PLP.
  - Mel-filter bank analysis: applying a filter bank that divides the frequency spectrum into a number of bands that correspond to the mel scale. The mel scale is a perceptual scale that relates the frequency to the pitch of the sound, and is linear at low frequencies and logarithmic at high frequencies. The filter bank has triangular filters that are uniformly spaced on the mel scale, and overlap with each other.
  - Logarithmic compression: applying a logarithmic function to the output of the filter bank, which converts the power of each band into a measure of loudness. The logarithmic function also enhances the dynamic range of the features and reduces the effect of noise.
  - Cepstral analysis: applying a discrete cosine transform (DCT) to the log filter bank output, which decorrelates the features and reduces their dimensionality. The DCT coefficients are called the MFCC, which are the final features used for speech analysis.

#### Comparison of PLP and MFCC

- Both PLP and MFCC are based on the principle of cepstral analysis, which is the extraction of the spectral envelope of the speech signal by applying a logarithmic function and a DCT.
- Both PLP and MFCC aim to model the human auditory system, by applying a filter bank that mimics the frequency resolution of the ear, and a non-linear transformation that mimics the loudness



### Time Alignment And Normalization for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Time alignment is the process of finding the optimal alignment between two speech signals that are related by some transformation, such as speaker variation, speaking rate variation, or noise distortion .
- Time alignment is useful for many applications of speech analysis, such as speaker recognition, voice conversion, speech synthesis, and speech recognition .
- Time alignment can be achieved by using a measure of similarity or dissimilarity between speech events, such as spectral features, and applying a dynamic programming algorithm that minimizes the total cost of aligning the events  .
- One of the common methods for time alignment is dynamic time warping (DTW), which allows for non-linear warping of the time axis to match the speech events .
- DTW can be improved by using some modifications, such as refinement, normalization, and comparisons between the preceding and the following frames, to reduce the alignment error and increase the sound correspondence between the speech signals.
- Normalization is the process of reducing the variability of speech signals that is caused by factors other than the linguistic content, such as speaker characteristics, channel characteristics, or environmental noise.
- Normalization is important for speech analysis, as it can enhance the performance of speech processing systems by making the speech signals more comparable and consistent.
- Normalization can be achieved by using various techniques, such as vocal tract length normalization, cepstral mean subtraction, z-score normalization, or feature warping, that aim to remove or reduce the effects of the unwanted factors on the speech features.



### Dynamic Time Warping

- Dynamic Time Warping (DTW) is an algorithm for measuring the similarity between two temporal sequences, such as speech signals, that may vary in speed or length.
- DTW can align the sequences by stretching or compressing them along the time axis, and find the optimal matching between them.
- DTW can be used for various applications, such as speech recognition, data mining, gesture recognition, financial markets, etc .
- DTW works by constructing a matrix that contains the distances between all possible pairs of points from the two sequences, and then finding the shortest path through the matrix that minimizes the total distance.
- DTW can be implemented using dynamic programming, which breaks down the problem into smaller subproblems and stores the solutions in a table.
- DTW can be improved by using various techniques, such as pruning, constraints, normalization, weighting, etc .



### Multiple Time – Alignment Paths for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications of speech analysis, such as speech recognition, speech synthesis, voice conversion, speech enhancement, and speech-to-lips synchronization  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or temporal variations  .
- One common method for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the total distance between the corresponding frames.
- DTW can be implemented using various algorithms, such as the classical dynamic programming, the ordered graph search, or the multiview temporal alignment by dependence maximization in the latent space .
- DTW can also be modified or extended to handle different types of time series, such as non-parallel, multivariate, or multimodal data .
- Multiple time-alignment paths are possible when there are multiple ways to align two time series with similar distances or costs.
- Multiple time-alignment paths can be useful for finding alternative or robust alignments, or for exploring the variability or diversity of the time series.
- Multiple time-alignment paths can be obtained by using different algorithms, such as the N-best paths, the multiple beam search, or the multiple alignment by dependence maximization .
- Multiple time-alignment paths can also be evaluated or compared using different criteria, such as the alignment accuracy, the alignment diversity, or the alignment stability .



### SPEECH MODELING

- Speech modeling is the process of representing speech signals in a mathematical or statistical way that captures the relevant information and patterns in the speech data.
- Speech modeling is an important task in natural language processing (NLP), which is a branch of artificial intelligence that deals with the interaction between computers and human languages.
- Speech modeling can be used for various applications, such as speech recognition, speech synthesis, speech enhancement, speech compression, speech analysis, speech translation, and speech emotion recognition.
- Speech modeling can be divided into two main types: acoustic modeling and linguistic modeling.

#### Acoustic Modeling

- Acoustic modeling is the process of mapping speech signals to acoustic units, such as phonemes, syllables, or words, that represent the basic sounds of a language.
- Acoustic modeling involves extracting features from the speech signals, such as pitch, energy, spectral shape, and duration, and using them to train statistical models, such as hidden Markov models (HMMs), Gaussian mixture models (GMMs), or deep neural networks (DNNs), that can recognize the acoustic units from new speech signals.
- Acoustic modeling can be influenced by various factors, such as speaker characteristics, background noise, channel distortion, and accent variation, that affect the quality and variability of the speech signals.
- Acoustic modeling can be improved by using techniques, such as speaker adaptation, noise reduction, feature normalization, and data augmentation, that can reduce the mismatch between the training and testing conditions and increase the robustness and accuracy of the models.

#### Linguistic Modeling

- Linguistic modeling is the process of mapping acoustic units to linguistic units, such as words, phrases, sentences, or meanings, that represent the structure and content of a language.
- Linguistic modeling involves applying rules or probabilities to the acoustic units, such as grammar, syntax, semantics, and pragmatics, that can generate or parse the linguistic units from the speech signals.
- Linguistic modeling can be influenced by various factors, such as vocabulary size, language complexity, domain specificity, and context dependency, that affect the diversity and ambiguity of the speech signals.
- Linguistic modeling can be improved by using techniques, such as language modeling, parsing, disambiguation, and semantic analysis, that can increase the fluency and coherence of the models.



### Hidden Markov Models for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- A hidden Markov model (HMM) is a statistical model that explains the probability of the observable state or variable by learning the hidden or unobservable states.
- HMMs are widely used in fields where the hidden variables control the observable variables, such as speech recognition, image recognition, gesture recognition, handwriting recognition, parts of speech tagging, and time series analysis.
- In speech recognition, HMMs are used to model the acoustic features of speech signals and to recognize the words or phonemes that are spoken .
- An HMM consists of the following components :
  - A set of hidden states, denoted by Q = {q1, q2, ..., qN}, where N is the number of states.
  - A set of observable symbols, denoted by V = {v1, v2, ..., vM}, where M is the size of the vocabulary.
  - A transition probability matrix, denoted by A = {aij}, where aij is the probability of transitioning from state qi to state qj.
  - An emission probability matrix, denoted by B = {bj(k)}, where bj(k) is the probability of emitting symbol vk from state qj.
  - An initial state distribution, denoted by π = {πi}, where πi is the probability of starting in state qi.
- The goal of HMMs is to find the most likely sequence of hidden states that generated the observed sequence of symbols, given the model parameters .
- There are three main problems that HMMs can solve :
  - The evaluation problem: Given an HMM and an observation sequence, compute the probability of the observation sequence given the model.
  - The decoding problem: Given an HMM and an observation sequence, find the most likely sequence of hidden states that generated the observation sequence.
  - The learning problem: Given an observation sequence and the number of hidden states, estimate the model parameters that maximize the probability of the observation sequence.
- There are various algorithms that can solve these problems, such as the forward-backward algorithm, the Viterbi algorithm, and the Baum-Welch algorithm .
- HMMs have some advantages and disadvantages for speech recognition:
  - Advantages:
    - They can model the temporal dynamics of speech signals and capture the sequential dependencies among acoustic features.
    - They can handle variability and uncertainty in speech signals by using probabilistic models and learning from data.
    - They can be easily extended and modified to incorporate different features, constraints, and structures.
  - Disadvantages:
    - They assume that the hidden states are discrete and independent, which may not reflect the true nature of speech signals and phonetic units.
    - They assume that the observable symbols are independent given the hidden states, which may not capture the correlations among acoustic features.
    - They require a large amount of training data and computational resources to estimate the model parameters and to perform inference.



### Markov Processes

- A Markov process is a random process indexed by time, and with the property that the future is independent of the past, given the present.
- Markov processes are the natural stochastic analogs of the deterministic processes described by differential and difference equations.
- Markov processes can be classified into discrete-time and continuous-time Markov processes, depending on whether the time index is discrete or continuous.
- Discrete-time Markov processes are also known as Markov chains, and they are characterized by a transition matrix that specifies the probabilities of moving from one state to another in each time step.
- Continuous-time Markov processes are characterized by a transition rate matrix that specifies the rates of moving from one state to another in infinitesimal time intervals.
- Examples of discrete-time Markov processes are the partial sum process associated with a sequence of independent, identically distributed random variables, and the bus ridership process that models the probability of a person regularly riding the bus in a given year .
- Examples of continuous-time Markov processes are the diffusion processes that model the random motion of particles, and the Poisson and Wiener processes that model the occurrence of events in time.
- Markov processes are useful for modeling various phenomena in natural language processing, such as speech recognition, text generation, and part-of-speech tagging.



### HMMs for Speech Analysis

- Hidden Markov Models (HMMs) are a statistical framework for modeling time-varying spectral vector sequences, such as speech signals .
- HMMs assume that the speech signal is generated by a Markov process with unobservable (hidden) states, and that each state produces an observable output according to some probability distribution.
- HMMs can be used for speech recognition, speech synthesis, speech segmentation, and speech enhancement   .
- HMMs have some advantages, such as:
  - They can capture the temporal dynamics and variability of speech signals .
  - They can be trained from data using efficient algorithms, such as the Baum-Welch algorithm.
  - They can be adapted, interpolated, and modified to model different voice characteristics, speaking styles, or emotions.
- HMMs also have some limitations, such as:
  - They rely on the independence assumption, which means that the current state depends only on the previous state, and that the current observation depends only on the current state .
  - They require a large amount of training data to estimate the model parameters accurately .
  - They may not capture the fine details and naturalness of speech signals, especially in speech synthesis .
- HMMs can be improved by using more complex models, such as Gaussian mixture models, deep neural networks, or recurrent neural networks, to model the state-output distributions or the state transitions   .



### Evaluation for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- The notes of the Unit 5 - SPEECH-ANALYSIS cover the following topics:
  - Speech recognition: the process of converting speech signals into text or commands.
  - Speech synthesis: the process of generating speech signals from text or commands.
  - Speech segmentation: the process of dividing speech signals into smaller units, such as words, syllables, or phonemes.
  - Speech features: the characteristics of speech signals that can be used for analysis, such as pitch, intensity, duration, or spectral properties.
  - Speech models: the mathematical representations of speech signals or speech units, such as hidden Markov models, neural networks, or n-grams.
  - Speech applications: the practical uses of speech analysis, such as speech-to-text, text-to-speech, speech translation, speech enhancement, or speech verification.

- The notes of the Unit 5 - SPEECH-ANALYSIS are well-organized, clear, and comprehensive. They provide the following benefits for the students:
  - They explain the basic concepts and principles of speech analysis in a simple and intuitive way.
  - They illustrate the methods and techniques of speech analysis with examples and diagrams.
  - They compare and contrast the advantages and disadvantages of different approaches and algorithms for speech analysis.
  - They highlight the challenges and limitations of speech analysis in real-world scenarios.
  - They suggest the possible directions and trends for future research and development in speech analysis.

- The notes of the Unit 5 - SPEECH-ANALYSIS can be improved by adding the following elements:
  - More exercises and quizzes to test the students' understanding and application of speech analysis.
  - More references and links to external resources and literature for further reading and exploration of speech analysis.
  - More interactive and multimedia content to enhance the students' engagement and interest in speech analysis.



### Optimal State Sequence for Speech Analysis

- Speech analysis is the process of extracting meaningful information from speech signals, such as words, phonemes, emotions, speakers, etc.
- Speech analysis often involves modeling speech signals as observations generated by a hidden Markov model (HMM), which is a probabilistic model that assumes a sequence of hidden states and a set of emission probabilities for each state.
- The optimal state sequence for speech analysis is the sequence of hidden states that best explains the observed speech signals, given the HMM parameters and the prior probabilities of the states.
- The optimal state sequence can be found by using the Viterbi algorithm, which is a dynamic programming algorithm that computes the most likely path through the HMM states, given the observations and the transition and emission probabilities.
- The Viterbi algorithm works by initializing a matrix of scores for each state and time step, and then updating the scores by maximizing the product of the previous score, the transition probability, and the emission probability for each state and observation. The algorithm also keeps track of the back pointers that indicate the previous state for each score. The optimal state sequence is then obtained by tracing back the pointers from the final state with the highest score.
- The optimal state sequence can be used for various speech-related tasks, such as speech recognition, speaker identification, speech segmentation, speech synthesis, etc. The optimal state sequence can also be used to update the HMM parameters by using the Baum-Welch algorithm, which is an expectation-maximization algorithm that iteratively improves the HMM parameters by using the expected counts of the state transitions and emissions, computed from the optimal state sequence and the forward-backward algorithm.



### Viterbi Search for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Viterbi search is a dynamic programming algorithm that finds the most likely sequence of hidden states in a hidden Markov model (HMM) given a sequence of observations .
- Viterbi search is widely used in speech analysis applications, such as speech recognition, speech synthesis, and speech enhancement  .
- Viterbi search consists of two main steps: forward computation and backtracking .
- Forward computation calculates the probability of the most likely path ending at each state for each observation, using the transition and emission probabilities of the HMM .
- Backtracking traces back the most likely path from the final state to the initial state, using pointers that store the previous state for each state and observation .
- Viterbi search can be implemented using a trellis diagram, where each node represents a state and each edge represents a transition .
- Viterbi search can be optimized by using logarithms of probabilities, pruning low-probability paths, and using beam search .
- Viterbi search can be extended to handle multiple observations, such as microphone array signals, by using a 3-D Viterbi search that considers the spatial information of the sources.



### Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a Hidden Markov Model (HMM) given a set of observed feature vectors.
- The algorithm consists of two steps: the E-step and the M-step.
- In the E-step, the algorithm computes the posterior probabilities of the hidden states given the observations and the current parameters, using the forward-backward algorithm.
- In the M-step, the algorithm updates the parameters by maximizing the expected log-likelihood of the observations given the hidden states, using the posterior probabilities computed in the E-step.
- The algorithm iterates between the E-step and the M-step until convergence or a maximum number of iterations is reached.
- The algorithm requires an initial guess of the parameters, which can be obtained by random initialization, clustering, or other methods.
- The algorithm can be applied to discrete or continuous HMMs, with different formulas for updating the parameters depending on the type of HMM.
- The algorithm is also known as the forward-backward algorithm or the EM algorithm for HMMs.



### Implementation Issues

Speech recognition is the process of converting spoken words into text or commands. It is a challenging task that involves many technical and social issues. Some of the common implementation issues are:

- **Accuracy**: The accuracy of a speech recognition system depends on many factors, such as the quality of the speech signal, the background noise, the speaker's accent, the vocabulary size, the grammar complexity, and the domain knowledge. A low accuracy rate can lead to frustration, misunderstanding, and errors. To improve accuracy, speech recognition systems need to use robust algorithms, large and diverse training data, and domain-specific models .
- **Language diversity**: Speech recognition systems need to support different languages and dialects, which may have different phonetic, syntactic, and semantic features. However, most speech recognition systems are developed and trained on English, which is not the universal language. This can result in bias, discrimination, and exclusion of non-English speakers. To overcome this challenge, speech recognition systems need to use multilingual and cross-lingual models, and incorporate linguistic and cultural knowledge .
- **Privacy and security**: Speech recognition systems often require access to the user's voice, which is a biometric data that can reveal personal and sensitive information, such as identity, emotion, health, and location. However, many users are not aware of how their voice data is collected, stored, processed, and shared by speech recognition systems. This can pose risks of data breach, identity theft, fraud, and surveillance. To protect the user's privacy and security, speech recognition systems need to use encryption, anonymization, consent, and transparency .
- **Ethical and social implications**: Speech recognition systems can have positive and negative impacts on the user and the society. On one hand, speech recognition systems can enhance accessibility, convenience, and productivity for the user, especially for those who have disabilities, literacy issues, or mobility limitations. On the other hand, speech recognition systems can also create ethical and social dilemmas, such as bias, discrimination, manipulation, and dehumanization. To address these issues, speech recognition systems need to follow ethical principles, such as fairness, accountability, and transparency .

