

## Unit 1 - INTRODUCTION

- This unit introduces the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and software that can perform tasks that normally require human intelligence, such as reasoning, learning, planning, decision making, natural language processing, computer vision, etc.
- AI can be classified into two main categories: weak AI and strong AI.
  - Weak AI, also known as narrow AI, is the type of AI that can perform specific tasks or solve specific problems, but does not have general intelligence or understanding of the world. Examples of weak AI include speech recognition, face detection, chess playing, etc.
  - Strong AI, also known as artificial general intelligence (AGI), is the type of AI that can perform any intellectual task that a human can, and has human-like consciousness, self-awareness, and common sense. Examples of strong AI include HAL 9000 from 2001: A Space Odyssey, Data from Star Trek, etc. Strong AI is still a hypothetical and elusive goal of AI research.
- AI can also be classified into two main approaches: symbolic AI and sub-symbolic AI.
  - Symbolic AI, also known as classical AI or rule-based AI, is the type of AI that uses symbols and rules to represent and manipulate knowledge. Symbolic AI relies on logic, search, and knowledge representation and reasoning techniques to solve problems. Examples of symbolic AI include expert systems, theorem provers, natural language understanding, etc.
  - Sub-symbolic AI, also known as connectionist AI or neural network-based AI, is the type of AI that uses numerical values and mathematical operations to model complex phenomena. Sub-symbolic AI relies on learning, adaptation, and optimization techniques to solve problems. Examples of sub-symbolic AI include artificial neural networks, evolutionary algorithms, fuzzy logic, etc.
- AI can also be classified into two main domains: applied AI and cognitive AI.
  - Applied AI, also known as engineering AI or practical AI, is the type of AI that focuses on developing systems and applications that can solve real-world problems and provide useful services. Applied AI can use any combination of weak or strong AI, and symbolic or sub-symbolic AI, depending on the task and the available data. Examples of applied AI include self-driving cars, recommender systems, chatbots, etc.
  - Cognitive AI, also known as scientific AI or theoretical AI, is the type of AI that focuses on understanding the nature and mechanisms of intelligence, both natural and artificial. Cognitive AI can use any combination of weak or strong AI, and symbolic or sub-symbolic AI, depending on the model and the hypothesis. Examples of cognitive AI include cognitive architectures, cognitive robotics, artificial life, etc.



# Origins and challenges of NLP

- Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.
- NLP has its origins in various disciplines, such as philosophy, logic, psychology, linguistics, mathematics, and engineering.
- Some of the early milestones in NLP include:
  - The development of formal languages and grammars by Noam Chomsky and others in the 1950s and 1960s.
  - The creation of the first machine translation systems in the 1950s and 1960s, such as the Georgetown-IBM experiment and the ALPAC report.
  - The emergence of the field of computational linguistics in the 1960s and 1970s, which focused on the analysis and generation of natural language texts using symbolic and rule-based methods.
  - The introduction of the concept of logical levels by Alfred Korzybski in the 1930s, which influenced the development of NLP techniques such as meta-modeling and reframing.
- NLP faces many challenges due to the complexity, diversity, ambiguity, and dynamism of natural language data .
- Some of the major challenges of NLP include:
  - Dealing with the sparsity, high-dimensionality, and noise of natural language data, which require efficient and robust representation and learning methods .
  - Handling the variability and inconsistency of natural language expressions, such as synonyms, homonyms, idioms, metaphors, and slang, which require sophisticated semantic and pragmatic analysis .
  - Coping with the context-dependence and subjectivity of natural language meanings, such as anaphora, ellipsis, presupposition, implicature, and sentiment, which require advanced reasoning and inference methods .
  - Adapting to the evolving and diverse nature of natural language data, such as new words, domains, genres, and languages, which require flexible and scalable NLP systems .
- NLP has also witnessed many advances and breakthroughs in recent years, such as:
  - The development of statistical and neural NLP methods, which leverage large-scale data and computational resources to learn from data rather than relying on handcrafted rules.
  - The emergence of subfields and applications of NLP, such as information extraction, question answering, text summarization, sentiment analysis, machine translation, speech recognition, and natural language generation .
  - The improvement of NLP performance and accuracy, which are measured by rigorous evaluation methods and benchmarks, such as BLEU, ROUGE, GLUE, and SQuAD .



# Language Modeling

- Language modeling is the task of estimating the probability of a sequence of words or a word given some context  .
- Language models are useful for various natural language processing applications, such as speech recognition, machine translation, text summarization, text generation, etc.
- Language models can be classified into two types: **generative** and **discriminative**.
  - Generative models learn the joint probability of the input and the output, and can generate new samples from the learned distribution. For example, a generative language model can generate a sentence given a topic or a keyword.
  - Discriminative models learn the conditional probability of the output given the input, and can predict the most likely output for a given input. For example, a discriminative language model can predict the next word given the previous words in a sentence.
- Language models can also be categorized based on the **order** of the words they consider.
  - **N-gram models** are the simplest and most widely used language models. They assume that the probability of a word depends only on the previous n-1 words, where n is a fixed parameter. For example, a bigram model (n=2) assumes that the probability of a word depends only on the previous word.
  - **Neural network models** are more advanced and powerful language models. They use neural networks to learn complex and non-linear relationships between words. They can consider longer contexts and capture semantic and syntactic information. For example, a recurrent neural network (RNN) model can process a sequence of words one by one and update its hidden state at each step.
- Language models can be evaluated using different metrics, such as **perplexity**, **accuracy**, **bleu score**, etc.
  - Perplexity measures how well a language model predicts a test set. It is the inverse of the average probability assigned to each word in the test set. A lower perplexity means a better language model.
  - Accuracy measures the percentage of correct predictions made by a language model. It is the ratio of the number of correct predictions to the total number of predictions. A higher accuracy means a better language model.
  - Bleu score measures the quality of a generated text by comparing it to one or more reference texts. It is based on the number of matching n-grams between the generated text and the reference texts. A higher bleu score means a better language model.



# Grammar-based LM for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A **language model (LM)** is a system that assigns a probability to a sequence of words or tokens in a natural language.
- A **grammar-based LM** is a type of LM that uses a formal grammar to generate and score sentences in a natural language.
- A **grammar** is a set of rules that specify how words and phrases can be combined to form sentences in a language.
- A **formal grammar** is a mathematical representation of a grammar that can be manipulated by algorithms.
- Some examples of formal grammars are **regular grammars**, **context-free grammars**, **context-sensitive grammars**, and **unrestricted grammars**.
- A grammar-based LM can be seen as a **generative model** that produces sentences according to the rules of the grammar and assigns probabilities to them based on some criteria.
- A grammar-based LM can also be seen as a **discriminative model** that evaluates the likelihood of a given sentence based on how well it conforms to the rules of the grammar.
- A grammar-based LM can be used for various natural language processing (NLP) tasks, such as **speech recognition**, **machine translation**, **text summarization**, **question answering**, **sentiment analysis**, etc .
- A grammar-based LM can capture the **syntactic** and **semantic** structure of a language, as well as the **context** and **pragmatics** of a discourse.
- A grammar-based LM can also handle **ambiguity**, **anaphora**, **ellipsis**, **coordination**, **subordination**, **agreement**, **negation**, **modality**, etc.
- A grammar-based LM can be **learned** from a corpus of sentences in a language, or **constructed** by experts based on linguistic knowledge.
- A grammar-based LM can be **evaluated** by comparing its predictions with human judgments, or by measuring its performance on a specific NLP task.
- A grammar-based LM can be **improved** by incorporating more data, more features, more rules, more parameters, or more feedback.
- A grammar-based LM can be **combined** with other types of LMs, such as **n-gram LMs**, **neural LMs**, **topic LMs**, etc .
- A grammar-based LM can be **adapted** to different domains, genres, styles, registers, or dialects of a language.



# Statistical Language Model for Natural Language Processing

- A statistical language model (SLM) is a mathematical representation of the probability distribution of sequences of words or symbols in a natural language.
- SLMs are used to generate or evaluate natural language texts in various natural language processing (NLP) tasks, such as speech recognition, machine translation, natural language generation, etc.
- SLMs are based on the assumption that the probability of a word or symbol depends on its previous words or symbols, which is called the Markov property.
- SLMs can be classified into different types based on the number of previous words or symbols they consider, which is called the order or the n-gram size of the model.
- An n-gram is a sequence of n words or symbols in a text. For example, "language" is a unigram (n = 1), "language model" is a bigram (n = 2), "statistical language model" is a trigram (n = 3), and so on.
- A unigram model is the simplest type of SLM, which assumes that each word or symbol is independent of its context. The probability of a text is the product of the probabilities of each word or symbol in the text.
- A bigram model is a type of SLM that assumes that each word or symbol depends only on its immediate predecessor. The probability of a text is the product of the conditional probabilities of each word or symbol given its previous word or symbol in the text.
- A trigram model is a type of SLM that assumes that each word or symbol depends only on its previous two words or symbols. The probability of a text is the product of the conditional probabilities of each word or symbol given its previous two words or symbols in the text.
- In general, an n-gram model is a type of SLM that assumes that each word or symbol depends only on its previous n-1 words or symbols. The probability of a text is the product of the conditional probabilities of each word or symbol given its previous n-1 words or symbols in the text.
- The higher the order of the n-gram model, the more context information it can capture, but also the more data and computation it requires.
- SLMs can be estimated from a large corpus of natural language texts, which is called the training data. The most common method of estimation is the maximum likelihood estimation (MLE), which assigns the probability of an n-gram to its relative frequency in the training data.
- SLMs often suffer from the problem of data sparsity, which means that some n-grams may not occur in the training data, resulting in zero probabilities. To overcome this problem, various smoothing techniques are used to assign non-zero probabilities to unseen n-grams by redistributing some probability mass from seen n-grams.
- SLMs can be evaluated by various metrics, such as perplexity, which measures how well the model predicts a test set of natural language texts. The lower the perplexity, the better the model.
- SLMs can also be extended or modified by incorporating various features, such as syntax, semantics, morphology, etc., to improve their performance and applicability.



# Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.

## Examples of Regular Expressions

- Regular Expressions | Regular Set
- (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … }
- (0*10*) | {1, 01, 10, 010, 0010, …}
- (0 + ε) (1 + ε) | {ε, 0, 1, 01}
- (a+b)* | It would be set of strings of a’s and b’s

## Simple Regular Expressions

- In this section, we will see the building blocks for simple regular expressions, along with a selection of linguistic examples.
- A simple regular expression consists of one or more of the following components:
  - A literal character, such as a, b, c, etc.
  - A wildcard character, such as ., which matches any single character
  - A character class, such as [a-z], which matches any character in the specified range
  - A negated character class, such as [^a-z], which matches any character not in the specified range
  - A repetition operator, such as *, +, ?, {n}, {n,m}, which specifies how many times the preceding component can be repeated
  - A grouping operator, such as ( ), which groups components together for applying repetition or alternation
  - An alternation operator, such as |, which matches either the component before or after it
  - An anchor, such as ^ or $, which matches the beginning or end of a string, respectively
- Some examples of simple regular expressions and their meanings are:
  - ^a.*b$ | matches any string that starts with a and ends with b
  - [A-Z][a-z]+ | matches any capitalized word
  - [^aeiou] | matches any consonant
  - (a|b)* | matches any string of a's and b's
  - \d{3}-\d{4} | matches any phone number of the form xxx-xxxx



# Finite-State Automata for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Finite-state automata (FSA) are abstract machines that can recognize and generate patterns of symbols, such as strings of characters or words .
- FSA have a finite number of states, a set of input symbols, a start state, a set of final states, and a transition function that maps each state and input symbol to a next state .
- FSA can be deterministic (DFA) or non-deterministic (NFA). DFA have exactly one transition for each state and input symbol, while NFA can have zero, one, or more transitions for each state and input symbol .
- FSA can be used for various natural language processing (NLP) tasks, such as tokenization, morphological analysis, part-of-speech tagging, named entity recognition, and speech recognition   .
- FSA can also be extended to finite-state transducers (FST), which can produce an output symbol for each input symbol. FST can be used for tasks such as spelling correction, text normalization, phonetic transcription, and machine translation  .
- FSA and FST have several advantages in NLP, such as efficiency, modularity, transparency, and expressiveness  . However, they also have some limitations, such as inability to handle long-distance dependencies, context-sensitive rules, and recursive structures .



# English Morphology

## Unit 1 - INTRODUCTION

- Morphology is the study of the internal structure of words and how they are formed from smaller units called morphemes.
- Morphemes are the smallest meaningful units of language. They can be roots, prefixes, suffixes, or infixes.
- For example, the word "unhappy" consists of two morphemes: the prefix "un-" and the root "happy". The prefix "un-" changes the meaning of the root "happy" to its opposite.
- Morphology is a core part of linguistic study because it helps us understand how words are related to each other and how they convey meaning in different contexts.
- Morphology is also important for natural language processing, which is the field of computer science that deals with analyzing and generating natural language data, such as text and speech.
- Natural language processing applications, such as spell checkers, speech recognition, machine translation, and information retrieval, rely on morphology to identify and process words and their parts.
- Morphology can be divided into two main branches: inflectional morphology and derivational morphology.
- Inflectional morphology deals with the changes in the form of words that indicate grammatical information, such as number, person, tense, case, gender, or mood.
- For example, the word "books" is inflected from the word "book" to indicate plural number. The word "walked" is inflected from the word "walk" to indicate past tense.
- Derivational morphology deals with the creation of new words from existing words or morphemes by adding prefixes, suffixes, or other affixes.
- For example, the word "happiness" is derived from the word "happy" by adding the suffix "-ness". The word "replay" is derived from the word "play" by adding the prefix "re-".
- Derivational morphology can change the meaning or the part of speech of a word. For example, the word "happy" is an adjective, but the word "happiness" is a noun. The word "play" is a verb, but the word "replay" can be a verb or a noun.



# Transducers for Lexicon

- A transducer is a device or a model that converts one form of data into another. In natural language processing (NLP), a transducer can map between different levels of linguistic representation, such as surface forms, lexical forms, syntactic structures, semantic representations, etc.
- A lexical transducer is a special type of finite-state transducer that maps inflected surface forms to lexical forms, and vice versa . A surface form is a word as it appears in a text, with its morphological features such as tense, number, case, etc. A lexical form is a word as it is stored in a lexicon, with its base form and its part-of-speech tag.
- For example, a lexical transducer can map the surface form "walked" to the lexical form "walk_VBD", where VBD stands for past tense verb. Conversely, it can map the lexical form "walk_VB" to the surface form "walk", where VB stands for base form verb.
- A lexical transducer can be constructed using finite-state methods, such as regular expressions, rewrite rules, or weighted finite-state machines. Such methods can capture the regularities and irregularities of natural language morphology, and allow for efficient analysis and generation of word forms .
- A lexical transducer can be used for various NLP applications, such as spell checking, text normalization, machine translation, speech recognition, information extraction, etc. It can also be composed with other finite-state transducers, such as context dependency transducers, n-gram language models, syntactic parsers, etc., to form complex language processing pipelines .



# Tokenization

Tokenization is the process of breaking down a piece of text into small units called tokens. A token may be a word, part of a word or just characters like punctuation. It is one of the most foundational NLP task and a difficult one, because every language has its own grammatical constructs, which are often difficult to write down as rules.

## Why is tokenization important?

Tokenization is important for a number of reasons:

- It is the first step in any NLP pipeline. It has an important effect on the rest of your pipeline.
- It can help to improve the accuracy of other NLP tasks, such as part-of-speech tagging, text classification, sentiment analysis, topic modeling, and machine translation, by providing more context for each word.
- It can help to reduce the size of the vocabulary and the dimensionality of the feature space, which can improve the efficiency and performance of NLP models.
- It can help to normalize the text and remove noise, such as punctuation, whitespace, and case.

## How does tokenization work?

There are different types of tokenization, depending on the level of granularity and the language of the text. Some of the common types are:

- **Word tokenization**: This is the most common type of tokenization, where the text is split into words based on whitespace and punctuation. For example, the sentence "Hello, world!" would be tokenized into ["Hello", ",", "world", "!"].
- **Subword tokenization**: This is a type of tokenization where the text is split into smaller units than words, such as syllables, morphemes, or characters. This can help to deal with rare words, spelling variations, and languages that do not have clear word boundaries. For example, the word "tokenization" could be tokenized into ["tok", "en", "iz", "a", "tion"] using character-level tokenization, or into ["token", "ization"] using morpheme-level tokenization.
- **Sentence tokenization**: This is a type of tokenization where the text is split into sentences based on punctuation and linguistic cues. For example, the paragraph "Hello, world! This is a test. How are you?" would be tokenized into ["Hello, world!", "This is a test.", "How are you?"].

## What are the challenges of tokenization?

Tokenization is not a trivial task, and there are many challenges and complexities involved, such as:

- **Ambiguity**: There may be cases where the text can be tokenized in more than one way, depending on the context and the intended meaning. For example, the word "can" can be a noun, a verb, or a modal auxiliary, and the punctuation "." can be a period, a decimal point, or an abbreviation marker.
- **Variation**: There may be cases where the text has different forms or spellings, depending on the dialect, the register, the domain, or the medium. For example, the word "color" can be spelled as "colour" in British English, or the word "lol" can be an acronym for "laugh out loud" or a word meaning "fun" in Dutch.
- **Language-specificity**: There may be cases where the text has language-specific features or rules that are not applicable to other languages. For example, some languages, such as Chinese, Japanese, and Thai, do not have clear word boundaries, and some languages, such as Arabic, Hebrew, and Urdu, are written from right to left.

## What are some examples of tokenization tools?

There are many tools and libraries that can perform tokenization for different languages and purposes. Some of the popular ones are:

- **NLTK**: This is a Python library that provides a wide range of tokenizers for different languages and levels of granularity. It also provides other NLP functionalities, such as stemming, lemmatization, and parsing.
- **SpaCy**: This is another Python library that provides fast and accurate tokenizers for many languages, as well as other NLP functionalities, such as named entity recognition, dependency parsing, and word vectors.
- **Stanford CoreNLP**: This is a Java library that provides tokenizers for many languages, as well as other NLP functionalities, such as part-of-speech tagging, sentiment analysis, and coreference resolution.
- **OpenNLP**: This is another Java library that provides tokenizers for many languages, as well as other NLP functionalities, such as chunking, parsing, and machine learning.



# Detecting and Correcting Spelling Errors

- Spelling errors are a common source of noise and ambiguity in natural language processing (NLP) tasks, such as information retrieval, machine translation, text summarization, etc.
- Spelling errors can be classified into two types: non-word errors and real-word errors.
- Non-word errors are those that result in a word that does not exist in the language, such as *teh* for *the*, *recieve* for *receive*, etc.
- Real-word errors are those that result in a word that exists in the language, but is not the intended one, such as *form* for *from*, *their* for *there*, etc.
- Non-word errors can be detected by checking the word against a predefined lexicon or dictionary, and corrected by using edit distance, n-gram models, or rule-based methods .
- Real-word errors are more challenging to detect and correct, as they require semantic and contextual information to identify the intended word. Some methods for real-word error correction are based on statistical language models, word embeddings, or neural networks  .
- Spelling correction methods can be evaluated by using metrics such as precision, recall, accuracy, and F1-score, on datasets that contain both correct and incorrect sentences.



# Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are, based on the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, each with a certain cost.
- For example, the minimum edit distance between "cat" and "bat" is 1, because we can substitute "c" with "b" with a cost of 1. The minimum edit distance between "cat" and "cart" is also 1, because we can insert "r" with a cost of 1.
- To compute the minimum edit distance between two strings, we can use a dynamic programming algorithm that fills a matrix with the optimal costs for each substring pair.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of deleting or inserting each character from the source or target string.
  - For each cell in the matrix, compute the minimum cost of transforming the substring up to that cell, by taking the minimum of three possible options:
    - The cost of the cell above plus the cost of deleting a character from the source string.
    - The cost of the cell to the left plus the cost of inserting a character to the target string.
    - The cost of the cell diagonally above and to the left plus the cost of substituting a character if the source and target characters are different, or zero if they are the same.
  - The minimum edit distance is the value of the bottom-right cell of the matrix.

- For example, the matrix for computing the minimum edit distance between "intention" and "execution" is:

|   |   | e | x | e | c | u | t | i | o | n |
|---|---|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| i | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| n | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 7 |
| t | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
| e | 4 | 3 | 4 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| n | 5 | 4 | 5 | 4 | 5 | 6 | 7 | 7 | 8 | 8 |
| t | 6 | 5 | 6 | 5 | 6 | 7 | 6 | 7 | 9 | 9 |
| i | 7 | 6 | 7 | 6 | 7 | 8 | 7 | 6 | 8 | 9 |
| o | 8 | 7 | 8 | 7 | 8 | 9 | 8 | 7 | 7 | 8 |
| n | 9 | 8 | 9 | 8 | 9 | 10| 9 | 8 | 8 | 8 |

- The minimum edit distance is 8, which corresponds to the following sequence of operations:

  - Substitute "i" with "e"
  - Substitute "n" with "x"
  - Delete "t"
  - Substitute "e" with "c"
  - Substitute "n" with "u"
  - Insert "t"
  - Delete "i"
  - Insert "o"

- Minimum edit distance can be used for various applications in natural language processing, such as spelling correction, speech recognition, machine translation, and text summarization.



# Unit 2 - WORD LEVEL ANALYSIS

Word level analysis is the process of identifying and describing the structure and meaning of words in a text. It involves the following aspects:

- Morphology: the study of the internal structure of words and how they are formed from smaller units called morphemes. Morphemes are the smallest meaningful units of language, such as roots, prefixes, suffixes, etc. For example, the word "unhappy" consists of two morphemes: the prefix "un-" and the root "happy".
- Lexicology: the study of the vocabulary of a language, including its origin, history, meaning, usage, and relationships with other words. Lexicology also covers the classification of words into different categories, such as parts of speech, synonyms, antonyms, homonyms, etc. For example, the word "bank" can be a noun, a verb, or an adjective, depending on the context and the meaning.
- Semantics: the study of the meaning of words and how they convey information and express ideas. Semantics also deals with the relationships between words and the world, such as reference, truth, implication, entailment, etc. For example, the word "dog" refers to a specific type of animal, and the sentence "Dogs bark" is true in most situations.



# Unsmoothed N-grams

- An **n-gram** is a sequence of **n** words or tokens in a text. For example, "natural language processing" is a **trigram** (n = 3), "machine learning" is a **bigram** (n = 2), and "statistics" is a **unigram** (n = 1).
- An **n-gram model** is a probabilistic model that estimates the probability of a word or token given the previous **n - 1** words or tokens. For example, a **bigram model** estimates the probability of a word given the previous word, and a **trigram model** estimates the probability of a word given the previous two words.
- An **unsmoothed n-gram model** is a simple way of calculating the probabilities of n-grams using the **maximum likelihood estimation (MLE)**. The MLE of an n-gram is the ratio of its frequency in the text to the frequency of its prefix (the previous n - 1 words or tokens). For example, the MLE of a bigram is the ratio of its frequency to the frequency of its first word, and the MLE of a trigram is the ratio of its frequency to the frequency of its first two words.
- An **unsmoothed n-gram model** has some limitations and drawbacks, such as:
  - It assigns **zero probability** to any n-gram that does not occur in the text, which is unrealistic and problematic for language modeling and generation tasks.
  - It is **data sparsity** problem, which means that many n-grams have very low frequencies or do not occur at all in the text, especially for higher values of n. This makes the model unreliable and inaccurate.
  - It is **overfitting** problem, which means that the model is too dependent on the specific text and does not generalize well to new or unseen texts. This reduces the model's performance and applicability.
- To overcome these limitations and drawbacks, various **smoothing techniques** are used to adjust the probabilities of n-grams and avoid zero probabilities. Some of the common smoothing techniques are **additive smoothing**, **Good-Turing smoothing**, **Kneser-Ney smoothing**, and **interpolation**.



# Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams can be used for various natural language processing tasks, such as language modeling, text generation, spelling correction, machine translation, speech recognition, etc.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical regularities of natural language and how well they generalize to unseen data.
- There are two main types of evaluation metrics for n-grams: intrinsic and extrinsic.

## Intrinsic evaluation

- Intrinsic evaluation measures the internal properties of n-grams, such as how well they fit the training data and how diverse they are.
- Intrinsic evaluation is usually faster and easier to perform than extrinsic evaluation, but it does not directly reflect the performance of n-grams on downstream tasks.
- Some common intrinsic evaluation metrics for n-grams are:

  - Perplexity: the inverse of the average probability assigned by the n-gram model to each word in a test set. Lower perplexity means higher probability and better fit.
  - Entropy: the average amount of information or uncertainty in the n-gram model. Higher entropy means more diversity and less predictability.
  - Coverage: the percentage of n-grams in a test set that are also present in the training set. Higher coverage means better generalization and less data sparsity.

## Extrinsic evaluation

- Extrinsic evaluation measures the impact of n-grams on the performance of a specific downstream task, such as text generation, machine translation, speech recognition, etc.
- Extrinsic evaluation is usually more costly and time-consuming than intrinsic evaluation, but it reflects the actual usefulness of n-grams for a given application.
- Some common extrinsic evaluation metrics for n-grams are:

  - BLEU: the geometric mean of the precision of n-grams in a generated text compared to one or more reference texts. Higher BLEU means higher similarity and better quality.
  - ROUGE: the recall of n-grams in a generated summary compared to one or more reference summaries. Higher ROUGE means higher coverage and better informativeness.
  - WER: the percentage of word errors (insertions, deletions, substitutions) in a transcribed speech compared to a reference transcription. Lower WER means higher accuracy and better recognition.



# Smoothing for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Smoothing is the process of flattening a probability distribution implied by a language model so that all reasonable word sequences can occur with some probability .
- Smoothing is important in natural language processing, as some words may have zero or close to zero probabilities such as the out-of-vocabulary words (words that do not exist in the vocabulary), but the same rare words may not have the same values in test data.
- Smoothing often involves broadening the distribution by redistributing weight from high probability regions to zero probability regions .
- Smoothing techniques in NLP are used to address scenarios related to determining probability / likelihood estimate of a sequence of words (say, a sentence) occurring together when one or more words individually (unigram) or N-grams such as bigram or trigram in the given set have never occurred in the past.
- Some common smoothing techniques are:
  - Additive smoothing: adding a small constant to all counts, such as Laplace smoothing or Lidstone smoothing.
  - Backoff smoothing: using lower order n-grams when higher order n-grams have zero counts, such as Katz backoff or Kneser-Ney smoothing.
  - Interpolation smoothing: combining different order n-grams with different weights, such as Jelinek-Mercer smoothing or Witten-Bell smoothing.
  - Discounting smoothing: reducing the counts of observed n-grams and assigning the mass to unobserved n-grams, such as Good-Turing smoothing or Absolute discounting smoothing.
- Smoothing can help performance whenever data sparsity is an issue, and data sparsity is almost always an issue in statistical modeling.
- Smoothing can also allow expanding the model, such as by moving to a higher n-gram model, to capture more complex patterns in the data.



# Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models in natural language processing.
- N-gram language models assign probabilities to sequences of words based on their frequency in a corpus of text.
- Smoothing is a technique to deal with the problem of data sparseness, which occurs when some n-grams are not observed in the training data, but may appear in the test data.
- Interpolation and backoff are both based on the idea of using lower-order n-grams to estimate the probabilities of higher-order n-grams when there is insufficient evidence for the latter.

## Interpolation

- Interpolation is a method that combines the probabilities of n-grams of different orders using weighted coefficients that sum to one.
- For example, a trigram interpolation model can be written as:

$$P(w_i|w_{i-2}w_{i-1}) = \lambda_1 P(w_i|w_{i-2}w_{i-1}) + \lambda_2 P(w_i|w_{i-1}) + \lambda_3 P(w_i)$$

- Where $\lambda_1$, $\lambda_2$, and $\lambda_3$ are the interpolation coefficients that satisfy $\lambda_1 + \lambda_2 + \lambda_3 = 1$.
- The coefficients can be learned from a held-out corpus using various methods, such as maximum likelihood estimation or expectation-maximization algorithm.
- Interpolation has the advantage of using all the available information from different n-gram orders, but it also requires more computation and storage.

## Backoff

- Backoff is a method that uses a lower-order n-gram model when the higher-order n-gram model has zero probability or low confidence.
- For example, a trigram backoff model can be written as:

$$P(w_i|w_{i-2}w_{i-1}) = \begin{cases} P(w_i|w_{i-2}w_{i-1}), & \text{if } C(w_{i-2}w_{i-1}w_i) > 0 \\ \alpha(w_{i-2}w_{i-1})P(w_i|w_{i-1}), & \text{otherwise} \end{cases}$$

- Where $C(w_{i-2}w_{i-1}w_i)$ is the count of the trigram $w_{i-2}w_{i-1}w_i$ in the training data, and $\alpha(w_{i-2}w_{i-1})$ is a discounting factor that ensures the probabilities sum to one.
- The discounting factor can be computed using various methods, such as Good-Turing estimation or Kneser-Ney smoothing.
- Backoff has the advantage of being simpler and faster than interpolation, but it also discards some information from higher-order n-grams.



# Word Classes

Word classes are categories of words that share some common characteristics, such as grammatical function, morphology, or meaning. Word classes are also known as parts of speech or lexical categories. Word classes are useful for natural language processing (NLP) tasks, such as parsing, tagging, and generating sentences.

Some common word classes in English are:

- Nouns: words that denote entities, such as people, places, things, or concepts. Examples: dog, book, city, love.
- Verbs: words that denote actions, states, or events. Examples: run, see, think, happen.
- Adjectives: words that modify nouns, expressing qualities, properties, or attributes. Examples: big, red, happy, smart.
- Adverbs: words that modify verbs, adjectives, or other adverbs, expressing manner, degree, time, place, or reason. Examples: quickly, very, yesterday, here, because.
- Pronouns: words that substitute for nouns or noun phrases, referring to entities that are already known or can be inferred from the context. Examples: he, she, it, they, this, that.
- Prepositions: words that introduce prepositional phrases, expressing the relation between a noun and another word. Examples: in, on, at, with, from.
- Conjunctions: words that connect words, phrases, or clauses, expressing logical or temporal relations. Examples: and, but, or, because, although.
- Determiners: words that precede nouns, specifying their quantity, definiteness, or possession. Examples: a, the, some, many, his, her.
- Interjections: words that express emotions, feelings, or attitudes, usually followed by an exclamation mark. Examples: wow, ouch, hey, oops.

Different languages may have different word classes, or different criteria for defining them. For example, some languages have grammatical gender, case, or number, which affect the form and function of nouns and pronouns. Some languages have more or fewer word classes than English, or different ways of categorizing them.

One of the challenges of NLP is to identify the word classes of words in a given text, and to use this information for further analysis or generation. This task is called part-of-speech tagging, and it involves assigning a label to each word according to its word class. For example, the sentence "She loves dogs and cats." can be tagged as:

She/PRON loves/VERB dogs/NOUN and/CONJ cats/NOUN ./PUNCT

Part-of-speech tagging can be done manually by human annotators, or automatically by computer programs. Automatic part-of-speech tagging can use various methods, such as rule-based, statistical, or neural network models. Automatic part-of-speech tagging is not always accurate, especially for ambiguous words that can belong to more than one word class depending on the context. For example, the word "book" can be a noun or a verb, and the word "well" can be an adverb or an adjective.

Word classes are not fixed or static, but can change over time or across domains. New words can be created, or existing words can change their meaning or function. For example, the word "google" was originally a noun, but now it is also a verb, meaning to search something on the internet. Word classes can also vary depending on the style, register, or genre of the text. For example, the word "lol" is an interjection in informal texts, but it is not a word class in formal texts.

Word classes are an important aspect of natural language, and they can help us understand the structure, meaning, and use of language. Word classes can also help us perform various NLP tasks, such as parsing, tagging, and generating sentences. Word classes are not the only way to categorize words, but they are one of the most common and useful ones.



# Part-of-Speech Tagging

- Part-of-speech (POS) tagging is the process of assigning a grammatical category to each word in a sentence or text, such as noun, verb, adjective, adverb, etc.   
- POS tagging is an important task in natural language processing (NLP), as it can help to analyze the structure and meaning of a sentence, and to perform other tasks such as parsing, named entity recognition, sentiment analysis, machine translation, etc.   
- POS tagging can be done manually by human annotators, or automatically by computer programs. Manual POS tagging is more accurate, but time-consuming and costly. Automatic POS tagging is faster and cheaper, but prone to errors and ambiguity. 
- There are different methods and techniques for automatic POS tagging, such as rule-based, statistical, and neural network-based approaches. Rule-based methods use predefined rules and dictionaries to assign tags based on the word form and context. Statistical methods use probabilistic models and machine learning algorithms to learn from annotated corpora and predict tags based on the word frequency and distribution. Neural network-based methods use deep learning architectures and embeddings to capture the semantic and syntactic features of words and their contexts.   
- One of the most widely used statistical methods for POS tagging is the Hidden Markov Model (HMM), which is a probabilistic model that assumes that the tag of a word depends only on the tag of the previous word, and that the word itself depends only on its tag. The HMM can be trained on a tagged corpus using the maximum likelihood estimation or the expectation-maximization algorithm, and can be used to tag new sentences using the Viterbi algorithm or the forward-backward algorithm.  
- POS tagging is not a trivial task, as there are many challenges and difficulties involved, such as the ambiguity of words that can have multiple tags depending on the context, the variation of words due to morphology, spelling, and punctuation, the lack of standardization and consistency of tag sets and annotation schemes, and the scarcity and quality of annotated data for different languages and domains.   
- POS tagging is an active and evolving research area in NLP, as there are many applications and improvements that can be made, such as developing more accurate and robust models, incorporating linguistic knowledge and external resources, adapting to different languages and domains, and evaluating and comparing different methods and systems.



# Rule-based Word Level Analysis

- Word level analysis is the process of identifying and categorizing the words in a natural language text according to their structure, meaning, and function.
- Rule-based word level analysis is a method that uses predefined rules and patterns to perform word level analysis, such as regular expressions, finite state automata, and context-free grammars.
- Rule-based word level analysis can be used for various tasks, such as:

  - Tokenization: splitting a text into smaller units called tokens, such as words, punctuation marks, numbers, etc.
  - Morphological analysis: identifying the morphemes (smallest meaningful units) and their features (such as part of speech, number, gender, tense, etc.) in a word, such as `cats` = `cat` + `s` (noun, plural).
  - Stemming: reducing a word to its base or root form, such as `running` -> `run`.
  - Lemmatization: finding the canonical or dictionary form of a word, such as `ran` -> `run`.
  - Part-of-speech tagging: assigning a part of speech (such as noun, verb, adjective, etc.) to each word in a text, based on its morphology and context.
  - Named entity recognition: identifying and classifying the proper names (such as persons, locations, organizations, etc.) in a text.
  - Word sense disambiguation: determining the meaning of a word in a given context, based on its definition, synonyms, antonyms, etc.

- Rule-based word level analysis has some advantages and disadvantages, such as:

  - Advantages:

    - It is fast and efficient, as it does not require large amounts of data or complex computations.
    - It is transparent and interpretable, as it can explain the logic and reasoning behind its decisions.
    - It can handle domain-specific and rare words, as it can incorporate expert knowledge and domain-specific rules.

  - Disadvantages:

    - It is brittle and inflexible, as it cannot handle exceptions, variations, and ambiguities that are not covered by the rules.
    - It is labor-intensive and error-prone, as it requires manual creation and maintenance of the rules and patterns.
    - It is not scalable and adaptable, as it cannot learn from new data or generalize to new domains and languages.



# Stochastic Word Level Analysis

- Word level analysis is the process of identifying and categorizing the words in a natural language text according to their morphology, syntax, and semantics.
- Stochastic word level analysis is the use of probabilistic models and methods to perform word level analysis, such as part-of-speech tagging, word segmentation, and spelling correction.
- Stochastic word level analysis can handle ambiguity, noise, and variation in natural language texts more effectively than rule-based approaches, which rely on predefined grammars and dictionaries.
- Some of the common stochastic models and methods used for word level analysis are:

  - Hidden Markov Models (HMMs): A HMM is a probabilistic finite state machine that can generate a sequence of observable symbols (words) based on a sequence of hidden states (tags). A HMM can be trained on a corpus of tagged texts to learn the transition probabilities between states and the emission probabilities of symbols given states. A HMM can then be used to assign the most likely tag sequence to a new text using the Viterbi algorithm.
  - Maximum Entropy Models (MEMs): A MEM is a probabilistic model that can assign a probability to any possible outcome (tag) given a set of features (word, context, etc.). A MEM can be trained on a corpus of tagged texts to learn the weights of the features using an optimization technique such as gradient descent. A MEM can then be used to assign the most likely tag to a new word given its features using the softmax function.
  - Conditional Random Fields (CRFs): A CRF is a probabilistic graphical model that can assign a probability to a sequence of outcomes (tags) given a sequence of observations (words). A CRF can be trained on a corpus of tagged texts to learn the potential functions of the features using an optimization technique such as gradient descent. A CRF can then be used to assign the most likely tag sequence to a new text using the Viterbi algorithm.
  - Neural Networks (NNs): A NN is a computational model that can learn complex nonlinear mappings between inputs (words) and outputs (tags) using a network of artificial neurons. A NN can be trained on a corpus of tagged texts to learn the weights of the connections between neurons using an optimization technique such as gradient descent. A NN can then be used to assign the most likely tag to a new word given its input vector using the softmax function.
  - Reinforcement Learning (RL): A RL is a learning paradigm that can optimize the behavior of an agent (tagger) based on the feedback (reward) from the environment (text). A RL can be trained on a corpus of tagged texts to learn a policy (action selection) and a value function (expected reward) using an algorithm such as Q-learning. A RL can then be used to assign the most likely tag to a new word given its state (context) and action (tag) using the policy and the value function.



# Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill.
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from examples and transforms one state to another state by using transformation rules .
- The basic idea of transformation-based tagging is to start with a simple initial tagging and then iteratively apply correction rules that improve the accuracy of the tagging.
- The initial tagging can be based on the most frequent tag for each word, or a default tag (such as noun) for unknown words.
- The correction rules are learned from a tagged corpus, using an error-driven learning algorithm that selects the rule that reduces the most errors at each step.
- The correction rules are of the form: change the tag of a word from X to Y, if condition Z is met.
- The condition Z can be based on the word itself, its surrounding words, or their tags.
- For example, a rule could be: change the tag of a word from noun to verb, if the previous word is "to".
- The advantage of transformation-based tagging is that it allows us to have linguistic knowledge in a readable form, and it can handle unknown words and ambiguity by using contextual information .
- The disadvantage of transformation-based tagging is that it can be slow, as it requires applying many rules sequentially, and it can be sensitive to the order of the rules.
- Transformation-based tagging can also be applied to other levels of textual analysis, such as chunking, which is the task of identifying non-recursive phrases (such as noun phrases) in a text.



# Issues in PoS tagging

- Part-of-speech (PoS) tagging is the task of assigning a word category (such as noun, verb, adjective, etc.) to each word in a text based on its definition and context.
- PoS tagging is useful for many natural language processing (NLP) applications, such as syntactic parsing, semantic analysis, information extraction, machine translation, and text summarization.
- PoS tagging is not a trivial task, as it faces several challenges and difficulties, such as:
  - **Ambiguity**: Many words can have more than one PoS depending on the context. For example, the word "book" can be a noun or a verb, and the word "down" can be a preposition, an adverb, or an adjective. A PoS tagger has to resolve this ambiguity accurately based on the surrounding words and the sentence structure.
  - **Unknown words**: A PoS tagger may encounter words that are not in its vocabulary, such as new words, proper names, abbreviations, foreign words, or misspellings. A PoS tagger has to assign a reasonable PoS to these words based on some heuristics, such as word morphology, capitalization, or suffixes.
  - **Tagset variation**: Different PoS taggers may use different sets of tags to represent the word categories. Some tagsets are coarse-grained and have fewer than 20 tags, while others are fine-grained and have more than 400 tags. A PoS tagger has to be consistent with the tagset it uses and be able to map its tags to other tagsets if needed.
  - **Domain adaptation**: A PoS tagger may perform well on one domain or genre of text, but poorly on another. For example, a PoS tagger trained on news articles may not be able to handle informal text, such as tweets or chats. A PoS tagger has to be able to adapt to different domains and styles of text and learn from new data.



# Hidden Markov and Maximum Entropy models for word level analysis in natural language processing

- Hidden Markov models (HMMs) are a powerful probabilistic tool for modeling sequential data, such as words in a sentence or speech signals.
- HMMs assume that the data are generated by a stochastic process that has some hidden or latent states, and that the observed data depend only on the current state.
- HMMs can be used for various word level analysis tasks, such as part-of-speech tagging, named entity recognition, text segmentation and information extraction .
- HMMs can be trained using the Baum-Welch algorithm, which is a special case of the Expectation-Maximization algorithm, or using supervised methods, such as maximum likelihood estimation or maximum a posteriori estimation.
- HMMs can be decoded using the Viterbi algorithm, which finds the most likely sequence of hidden states given the observed data, or using other methods, such as forward-backward algorithm or posterior decoding.

- Maximum Entropy models (MaxEnt) are another probabilistic tool for modeling data that have some uncertainty or ambiguity.
- MaxEnt models assume that the data are generated by a distribution that satisfies some constraints, such as feature expectations or prior knowledge, and that the distribution is otherwise as uniform as possible.
- MaxEnt models can be used for various word level analysis tasks, such as part-of-speech tagging, named entity recognition, text segmentation and information extraction .
- MaxEnt models can be trained using iterative scaling algorithms, such as improved iterative scaling or generalized iterative scaling, or using gradient-based methods, such as limited-memory BFGS or stochastic gradient descent.
- MaxEnt models can be decoded using the argmax operation, which finds the most likely label or class given the observed data, or using other methods, such as softmax or log-linear models.

- Maximum Entropy Markov models (MEMMs) are a hybrid of HMMs and MaxEnt models, which combine the advantages of both models.
- MEMMs assume that the data are generated by a stochastic process that has some hidden or latent states, and that the observed data depend on the current state and some features of the data.
- MEMMs can be used for various word level analysis tasks, such as part-of-speech tagging, named entity recognition, text segmentation and information extraction .
- MEMMs can be trained using the same methods as MaxEnt models, such as iterative scaling or gradient-based methods.
- MEMMs can be decoded using the same methods as HMMs, such as Viterbi or forward-backward algorithms.



## Unit 3 - SYNTACTIC ANALYSIS

- Syntactic analysis is the process of analyzing the structure and grammar of a natural language sentence or program code.
- Syntactic analysis can be performed by using formal methods such as grammars, parsers, and automata, or by using statistical methods based on data and probabilities.
- Syntactic analysis can be used for various applications, such as natural language processing, compiler design, code analysis, and artificial intelligence.
- Syntactic analysis can be divided into two main phases: lexical analysis and parsing.
- Lexical analysis is the process of breaking down a sentence or code into its smallest meaningful units, called tokens. Tokens can be words, symbols, numbers, or identifiers.
- Parsing is the process of arranging the tokens into a hierarchical structure, called a parse tree, that represents the syntactic rules and relationships of the language.
- A parse tree can be represented by using brackets, diagrams, or abstract syntax trees.
- A parse tree can be used to check the syntactic correctness, ambiguity, and completeness of a sentence or code.
- A parse tree can also be used to perform semantic analysis, which is the process of determining the meaning and validity of a sentence or code based on its syntax and context.



# Context Free Grammars

- A context-free grammar (CFG) is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a left-hand side, which identifies a syntactic category, and a right-hand side, which defines its alternative component parts, reading from left to right.
- A syntactic category is a label for a group of words or phrases that have similar grammatical properties, such as noun, verb, adjective, etc.
- A context-free grammar is called so because the rules can be applied regardless of the surrounding context of the words or phrases.
- A context-free grammar can be represented by a tuple (N, T, P, S), where:
  - N is a set of non-terminal symbols, which are the syntactic categories that can be expanded by the rules.
  - T is a set of terminal symbols, which are the words or tokens that cannot be expanded by the rules.
  - P is a set of production rules, which are of the form A -> B, where A is a non-terminal symbol and B is a sequence of terminal and/or non-terminal symbols.
  - S is a special non-terminal symbol, called the start symbol, which represents the whole sentence or program.
- A context-free grammar can be used to generate or parse sentences or programs in a language .
- To generate a sentence or program, we start with the start symbol and apply the rules recursively until we reach a sequence of terminal symbols.
- To parse a sentence or program, we start with the sequence of terminal symbols and apply the rules in reverse until we reach the start symbol.
- A context-free grammar can be visualized by a parse tree, which is a hierarchical representation of the syntactic structure of a sentence or program.
- A parse tree has the following properties:
  - The root node is labeled with the start symbol.
  - The leaf nodes are labeled with the terminal symbols.
  - The internal nodes are labeled with the non-terminal symbols.
  - The children of each node are labeled with the right-hand side of the rule that was applied to expand the node.
- A context-free grammar can be used to model the constituent structure of natural language, which is the way words and phrases are grouped together to form larger units of meaning.
- A context-free grammar can capture some of the syntactic regularities and variations of natural language, such as word order, agreement, recursion, etc.
- However, a context-free grammar cannot capture some of the syntactic dependencies and constraints of natural language, such as pronoun resolution, long-distance dependencies, cross-serial dependencies, etc.
- Therefore, natural languages are not strictly context-free, but rather mildly context-sensitive, which means they require some additional mechanisms or extensions to handle the complex phenomena that context-free grammars cannot account for.
- Some examples of such mechanisms or extensions are tree-adjoining grammars, feature structures, unification, etc.



# Grammar rules for English for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Syntactic analysis is the process of analyzing natural language with the rules of formal grammar.
- Syntactic analysis assigns a semantic structure to text, which helps to understand how words fit together to form meaningful sentences .
- Syntactic analysis involves the following steps:
  - Segmentation I: Identifying clause boundaries and word boundaries
  - Classification I: Determining the parts of speech
  - Segmentation II: Identifying constituents
  - Classification II: Determining the syntactic categories for the constituents
  - Determining the grammatical functions of the constituents
  - Drawing the syntactic structure
- Syntactic rules are the principles that govern the structure of sentences and clauses in a language.
- Syntactic rules in English set forth a specific order for grammatical elements like subjects, verbs, direct and indirect objects, etc.
- For example, if a sentence has a verb, direct object, and subject, the proper order is subject → verb → direct object.
- Syntactic rules also determine whether a sentence should have a subject, verb, and object, or if it should be in the active or passive voice.
- Syntactic rules can vary across languages, dialects, and registers.
- Syntactic rules can be used to create various rhetorical or literary effects, such as parallelism, inversion, ellipsis, etc.



# Treebanks

- A treebank is a collection of sentences annotated with syntactic structures, such as phrase structure trees or dependency graphs .
- Treebanks are useful for natural language processing (NLP) because they provide gold-standard data for training and evaluating systems such as part-of-speech taggers, parsers, semantic analyzers and machine translation systems  .
- Treebanks also enable linguistic research on various aspects of syntax, such as word order, grammatical categories, subcategorization, coordination, ellipsis, etc  .
- Treebanks can be constructed manually, semi-automatically or automatically, depending on the level of accuracy and consistency required .
- Manual treebanking involves human annotators who follow a set of guidelines and use annotation tools to assign syntactic structures to sentences .
- Semi-automatic treebanking involves using a pre-parser or a tagger to generate initial annotations, which are then corrected or refined by human annotators .
- Automatic treebanking involves using a parser or a tagger to generate annotations without human intervention, which may result in lower quality or less reliable data .
- Treebanks can vary in size, domain, language, annotation scheme and level of detail  .
- Some examples of well-known treebanks are the Penn Treebank for English, the Prague Dependency Treebank for Czech, the Universal Dependencies Treebank for multiple languages, and the Chinese Treebank for Mandarin  .
- Treebanks are often evaluated in terms of coverage, consistency, accuracy and usability  .
- Coverage refers to the amount and variety of data included in the treebank, such as genres, registers, domains, etc  .
- Consistency refers to the degree of agreement among annotators or between annotations and guidelines, which affects the reliability and comparability of the data  .
- Accuracy refers to the correctness and completeness of the annotations, which affects the performance and generalization of the NLP systems  .
- Usability refers to the availability and accessibility of the data, such as formats, licenses, tools, etc  .



# Normal Forms for Grammar

- Normal forms for grammar are ways of transforming a grammar into a simpler or more restricted form without changing the language it generates.
- Normal forms are useful for natural language processing (NLP) because they make parsing and analyzing natural language sentences easier using efficient algorithms.
- There are different types of normal forms for grammar, such as Chomsky normal form, Greibach normal form, and Kuroda normal form. Each normal form has its own rules and properties.
- Chomsky normal form (CNF) is a normal form for context-free grammars (CFGs) that requires every production rule to be of the form A -> BC or A -> a, where A, B, and C are non-terminal symbols and a is a terminal symbol.
- Greibach normal form (GNF) is a normal form for CFGs that requires every production rule to be of the form A -> aB1B2...Bn, where A and Bi are non-terminal symbols and a is a terminal symbol.
- Kuroda normal form (KNF) is a normal form for context-sensitive grammars (CSGs) that requires every production rule to be of the form A -> B, AB -> CD, A -> BC, or a -> b, where A, B, C, and D are non-terminal symbols and a and b are terminal symbols.



# Dependency Grammar

- Dependency grammar is a descriptive and theoretical tradition in linguistics that can be traced back to antiquity.
- It has long been influential in the European linguistics tradition and has more recently become a mainstream approach to representing syntactic and semantic structure in natural language processing.
- Dependency grammar states that words of a sentence are dependent upon other words of the sentence.
- Dependency grammar is based on the concept that there is a direct link between every linguistic unit of a sentence.
- Dependency grammar uses dependency relations to indicate how words are related to each other in a sentence.
- Dependency relations are binary, asymmetric and labeled relations between a head and a dependent.
- A head is a word that governs the form and/or position of one or more dependents.
- A dependent is a word that is governed by a head and modifies or complements the head.
- For example, in the sentence "The dog barked loudly", the word "dog" is the head of the noun phrase "the dog", and the word "the" is the dependent of "dog". The word "barked" is the head of the verb phrase "barked loudly", and the word "loudly" is the dependent of "barked".
- Dependency grammar can be represented by dependency trees, which are directed graphs that show the dependency relations between words in a sentence.
- Dependency trees have a single root node, which is usually the main verb of the sentence, and each node has at most one incoming edge, which indicates the head-dependent relation.
- For example, the dependency tree for the sentence "The dog barked loudly" is:

```
  barked
  /   \
the   loudly
 |
dog
```

- Dependency grammar has several advantages over other grammatical frameworks, such as phrase structure grammar or constituency grammar.
- Dependency grammar is more economical, as it does not require intermediate nodes or categories to represent syntactic structure.
- Dependency grammar is more flexible, as it can handle word order variations, discontinuous constituents, and non-projective structures more easily.
- Dependency grammar is more expressive, as it can capture semantic relations and roles more directly and explicitly.
- Dependency grammar is more universal, as it can account for the diversity and commonality of languages more adequately.
- Dependency grammar is more compatible with natural language processing, as it can facilitate parsing, generation, translation, and other tasks that require syntactic and semantic analysis.



# Syntactic Parsing

- Syntactic parsing is the process of analyzing natural language with the rules of a formal grammar .
- Formal grammar is a system of symbols and rules that defines the syntax of a language, i.e., how words and phrases can be combined to form sentences.
- Syntactic parsing aims to uncover the syntactic structure of an input sentence, such as a constituent or dependency tree.
- A constituent tree represents the hierarchical grouping of words into phrases and clauses, based on the categories and functions of each word.
- A dependency tree represents the grammatical relations between words, such as subject, object, modifier, etc., based on the dependencies and roles of each word.
- Syntactic parsing is one of the important tasks in computational linguistics and natural language processing, and has been a subject of research since the mid-20th century with the advent of computers.
- Syntactic parsing can be used for various downstream tasks, such as semantic parsing, relation extraction, machine translation, etc., that require understanding the meaning and structure of natural language .
- Syntactic parsing can be performed using different methods, such as rule-based, statistical, neural, or unsupervised approaches .
- Rule-based parsing relies on manually crafted grammar rules and lexicons to parse sentences, but it can be brittle and incomplete.
- Statistical parsing uses probabilistic models and machine learning algorithms to learn grammar rules and parameters from annotated data, but it can be noisy and domain-specific.
- Neural parsing uses deep neural networks and embeddings to learn syntactic representations and parse sentences, but it can be data-hungry and computationally expensive.
- Unsupervised parsing does not require any annotated data, but instead relies on linguistic assumptions and heuristics to induce syntactic structures, but it can be inaccurate and inconsistent.



# Ambiguity

- Ambiguity is the property of a sentence or phrase that can have more than one meaning or interpretation.
- Ambiguity can arise at different levels of language processing, such as lexical, syntactic, semantic, pragmatic, or discourse.
- Ambiguity can cause problems for natural language processing systems, as they may not be able to resolve the intended meaning of the input or output.
- Ambiguity can also be a source of creativity and humor in natural language, as it allows for multiple interpretations and associations.

## Lexical Ambiguity

- Lexical ambiguity occurs when a word or phrase has more than one sense or meaning in a given context.
- For example, the word "bank" can mean a financial institution, a river shore, or a verb meaning to tilt or turn.
- Lexical ambiguity can be resolved by using context clues, word sense disambiguation techniques, or external knowledge sources.

## Syntactic Ambiguity

- Syntactic ambiguity occurs when a sentence or phrase has more than one possible structure or parse tree.
- For example, the sentence "I saw the man with the telescope" can have two different structures, depending on whether "with the telescope" modifies "the man" or "saw".
- Syntactic ambiguity can be resolved by using grammatical rules, syntactic parsing techniques, or semantic information.

## Semantic Ambiguity

- Semantic ambiguity occurs when a sentence or phrase has more than one possible meaning or interpretation, even after resolving lexical and syntactic ambiguity.
- For example, the sentence "He fed her cat food" can have two different meanings, depending on whether "cat food" is the object or the complement of "fed".
- Semantic ambiguity can be resolved by using pragmatic cues, semantic analysis techniques, or world knowledge.

## Pragmatic Ambiguity

- Pragmatic ambiguity occurs when a sentence or phrase has more than one possible implication or inference, depending on the context and the speaker's intention.
- For example, the sentence "Can you pass the salt?" can have two different implications, depending on whether it is a request or a question.
- Pragmatic ambiguity can be resolved by using conversational maxims, pragmatic analysis techniques, or common sense.

## Discourse Ambiguity

- Discourse ambiguity occurs when a sentence or phrase has more than one possible relation or function within a larger text or dialogue.
- For example, the sentence "She was happy" can have different relations, depending on whether it is a main clause, a subordinate clause, or a discourse marker.
- Discourse ambiguity can be resolved by using discourse structure, discourse analysis techniques, or discourse coherence.



# Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences.
- It is based on the idea of storing and reusing partial results of the parsing process, rather than recomputing them.
- It can reduce the time complexity of parsing from exponential to polynomial, depending on the grammar and the input sentence.
- Dynamic programming parsing requires the grammar to be in a restricted form, such as Chomsky Normal Form (CNF), where each rule has at most two symbols on the right-hand side.
- One of the most popular dynamic programming parsing algorithms is the Cocke-Kasami-Younger (CKY) algorithm, which is a bottom-up chart parser that fills a triangular table with the possible constituents for each span of the input sentence.
- The CKY algorithm works as follows:
  - Initialize the table with the part-of-speech tags of the words at the diagonal cells.
  - For each span length from 2 to n, where n is the length of the sentence, iterate over all possible start and end positions of the span.
  - For each span, iterate over all possible split points, and check if there is a grammar rule that can combine the constituents at the left and right subspans.
  - If there is such a rule, add the left-hand side symbol of the rule to the cell corresponding to the span.
  - If the cell at the top-right corner of the table contains the start symbol of the grammar, the sentence is accepted and the table contains the parse tree. Otherwise, the sentence is rejected.
- The CKY algorithm has a time complexity of O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar. It has a space complexity of O(n^2 * |G|), since it stores all possible constituents for each span.



# Shallow parsing

Shallow parsing, also known as chunking or light parsing, is a technique in natural language processing that aims to identify the constituent parts of sentences and link them to higher order units that have discrete grammatical meanings. Shallow parsing does not produce a complete parse tree of a sentence, but rather a partial one that only shows the main phrases and their boundaries.

Some of the applications of shallow parsing are:

- Semantic role labeling: assigning labels to words or phrases in a sentence that indicate their semantic role, such as agent, patient, instrument, etc. For example, in the sentence "John ate an apple with a fork", John is the agent, apple is the patient, and fork is the instrument.
- Information extraction: extracting relevant information from unstructured text, such as names, dates, locations, etc. For example, in the sentence "Barack Obama was born on August 4, 1961 in Honolulu, Hawaii", Barack Obama is a person name, August 4, 1961 is a date, and Honolulu, Hawaii is a location.
- Text summarization: generating a concise summary of a longer text, such as a news article or a book review. For example, a possible summary of the sentence "The movie Joker is a dark and disturbing portrayal of a mentally ill man who becomes a violent criminal" is "Joker: a movie about a madman".

Shallow parsing can be performed using various methods, such as:

- Rule-based: using a set of predefined rules or patterns to identify and label the phrases in a sentence. For example, a rule might be that a noun phrase consists of a determiner followed by zero or more adjectives followed by a noun.
- Machine learning: using a supervised or unsupervised learning algorithm to learn the features and labels of the phrases in a sentence from a large corpus of annotated data. For example, a classifier might be trained to predict whether a word is the beginning, inside, or outside of a phrase, based on its part of speech, context, and other features.
- Hybrid: combining rule-based and machine learning methods to improve the accuracy and coverage of shallow parsing. For example, a rule-based system might be used to generate initial candidates for phrases, and then a machine learning system might be used to refine or filter them.



# Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probability of a rule is the conditional probability of expanding the left-hand side nonterminal into the right-hand side symbols, given the left-hand side nonterminal.
- The probability of a parse tree is the product of the probabilities of the rules used to generate it.
- The probability of a sentence is the sum of the probabilities of all possible parse trees for that sentence.
- PCFGs can be used to model natural languages and perform syntactic analysis, such as parsing and disambiguation.
- PCFGs can be learned from annotated corpora, such as treebanks, by counting the occurrences of each rule and normalizing by the occurrences of each nonterminal.
- PCFGs can be parsed by algorithms such as the CKY algorithm, which is a bottom-up dynamic programming algorithm that fills a chart with the most probable parses for each substring of the input sentence.
- PCFGs have some limitations, such as the independence assumption, which ignores the dependencies between different parts of the sentence, and the sparsity problem, which results from the lack of data for some rare rules or words.



# Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible substrings of the input sentence being generated by all possible nonterminals in a table.
- The algorithm fills the table in a bottom-up fashion, starting from the smallest substrings (single words) and moving up to the largest substring (the whole sentence).
- The algorithm considers every possible split of a substring into two smaller substrings, and computes the probability of the substring being generated by a nonterminal using the probabilities of the smaller substrings and the production rules.
- The algorithm returns the highest probability of the whole sentence being generated by the start symbol of the grammar, and the corresponding parse tree.
- The algorithm can be modified to use log-probabilities instead of probabilities to avoid underflow issues when multiplying many small probabilities together.



# Probabilistic Lexicalized CFGs

- Probabilistic Lexicalized CFGs (L-PCFGs) are a type of probabilistic context-free grammars (PCFGs) that incorporate lexical information into the grammar rules.
- PCFGs are CFGs that assign probabilities to each rule, such that the sum of the probabilities of all rules with the same left-hand side is 1. PCFGs can be used to model the likelihood of different syntactic structures for a given sentence, and to perform statistical parsing.
- Lexicalized CFGs (L-CFGs) are CFGs that annotate each non-terminal node in the parse tree with a head word, which is the most important word in the corresponding phrase. L-CFGs can capture more syntactic dependencies and preferences than standard CFGs, and can improve parsing accuracy.
- L-PCFGs combine the advantages of PCFGs and L-CFGs by assigning probabilities to L-CFG rules, which depend on both the syntactic category and the head word of the left-hand side non-terminal. L-PCFGs can model more fine-grained syntactic variations and ambiguities than PCFGs, and can also incorporate lexical information into the parsing process.
- L-PCFGs can be learned from a treebank, which is a corpus of sentences annotated with parse trees and head words. The parameters of an L-PCFG can be estimated by counting the occurrences of different L-CFG rules in the treebank, and normalizing them by the occurrences of the left-hand side non-terminals.
- L-PCFGs can be used for parsing by applying the probabilistic version of the CKY algorithm, which is a dynamic programming algorithm that finds the most probable parse tree for a given sentence. The algorithm builds the parse tree bottom-up, by computing the probabilities of all possible sub-trees for each span of the sentence, and selecting the best ones according to the L-PCFG rules. The algorithm returns the parse tree with the highest probability for the whole sentence.



# Feature structures for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Natural Language Processing (NLP) is a branch of artificial intelligence that attempts to bridge the gap between what a machine recognizes as input and the human language.
- NLP combines artificial intelligence and computational linguistics so that computers and humans can talk seamlessly.
- NLP involves various tasks, such as speech recognition, natural language understanding, natural language generation, machine translation, sentiment analysis, text summarization, etc.
- Syntactic analysis is one of the main components of NLP, which deals with the structure and grammar of natural language sentences.
- Syntactic analysis involves parsing, which is the process of assigning a syntactic structure to a given sentence according to a set of rules or a grammar.
- A syntactic structure can be represented in various ways, such as a tree, a bracketed expression, or a feature structure.
- A feature structure is a set of attribute-value pairs that describe the properties of a linguistic unit, such as a word, a phrase, or a sentence.
- A feature structure can capture various types of information, such as part-of-speech, number, gender, case, tense, mood, etc.
- A feature structure can also represent the relations between different linguistic units, such as agreement, subcategorization, dependency, etc.
- A feature structure can be represented graphically as a box with labeled slots for each attribute and its corresponding value.
- A feature structure can also be represented textually as a list of attribute-value pairs enclosed in brackets, separated by commas, and optionally indented for readability.
- For example, the feature structure for the word "book" as a noun can be represented as:

```
[NP
  head: [N
    form: book
    number: sg
  ]
  det: [D
    form: the
  ]
]
```

- This feature structure indicates that the word "book" is the head of a noun phrase (NP), which has a determiner (det) with the form "the". The word "book" itself is a noun (N) with the form "book" and the number singular (sg).
- Feature structures can be unified, which is the process of combining two or more feature structures into a single one, if they are compatible.
- Compatibility means that the feature structures have the same attribute names and values for the corresponding slots, or that the values are variables that can be instantiated.
- Unification can be used to check the grammaticality of a sentence, by unifying the feature structures of its constituents according to the grammar rules.
- For example, the feature structure for the verb "read" as a past tense verb can be represented as:

```
[VP
  head: [V
    form: read
    tense: past
    subcat: <NP, NP>
  ]
]
```

- This feature structure indicates that the word "read" is the head of a verb phrase (VP), which has the form "read", the tense past, and the subcategorization frame <NP, NP>, which means that it requires two noun phrases as its arguments.
- To check the grammaticality of the sentence "The boy read the book", we can unify the feature structures of the noun phrase "the boy" and the verb phrase "read the book", and see if the result is a valid sentence feature structure.
- The result of the unification is:

```
[S
  subj: [NP
    head: [N
      form: boy
      number: sg
    ]
    det: [D
      form: the
    ]
  ]
  pred: [VP
    head: [V
      form: read
      tense: past
      subcat: <>
    ]
    obj: [NP
      head: [N
        form: book
        number: sg
      ]
      det: [D
        form: the
      ]
    ]
  ]
]
```

- This feature structure indicates that the sentence is composed of a subject (subj) and a predicate (pred), which are the noun phrase "the boy" and the verb phrase "read the book", respectively. The verb phrase has an object (obj), which is the noun phrase "the book". The subcategorization frame of the verb is empty, which means that it has consumed



# Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- A feature structure is a set of attribute-value pairs, where the attributes are symbols and the values are either symbols or other feature structures.
- For example, the feature structure for a noun phrase can be written as:

```
[CAT: NP
 NUM: SG
 CASE: NOM
 HEAD: [CAT: N
        NUM: SG
        STEM: dog]]
```

- Unification is a (partial) operation on feature structures. Intuitively, it is the operation of combining two feature structures such that the new feature structure contains all the information of the original two, and nothing more.
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- For example, the unification of the feature structures `[CAT: NP NUM: SG]` and `[CAT: NP CASE: NOM]` is `[CAT: NP NUM: SG CASE: NOM]`.
- Unification can fail if the feature structures are incompatible, i.e., if they contain contradictory information. For example, the unification of `[CAT: NP NUM: SG]` and `[CAT: NP NUM: PL]` fails because the NUM feature has different values.
- Unification is widely used in natural language processing (NLP) for various tasks, such as parsing, generation, and semantic interpretation.
- Unification can be extended to E-unification, which allows the use of equations to express relations between feature values. E-unification of feature structures has, to the best of our knowledge, never been used in NLP, but it can be useful for capturing linguistic phenomena such as agreement, anaphora, and ellipsis .



## Unit 4 - SEMANTICS AND PRAGMATICS

- Semantics and pragmatics are two important branches of linguistics that study the meaning of language  .
- Semantics studies the meaning of words and sentences in a general and abstract way, without considering the context or the speaker's intention  .
- Pragmatics studies the meaning of words and sentences in a specific and concrete way, taking into account the context, the speaker's intention, and the listener's inference  .
- Semantics is context-independent, while pragmatics is context-dependent . For example, the sentence "It's raining" has the same semantic meaning in any situation, but it can have different pragmatic meanings depending on who says it, where, when, and why.
- Semantics has a narrower scope than pragmatics, as it only deals with the truth-conditional aspect of language, that is, the conditions under which a sentence is true or false . Pragmatics has a broader scope, as it also deals with the non-truth-conditional aspect of language, that is, the implications, assumptions, and effects of using language in communication .
- Semantics and pragmatics are complementary to each other, as they both contribute to the understanding of meaning in language . However, they also have different methods, assumptions, and goals, and they sometimes conflict or overlap with each other .

Some of the main topics and concepts in semantics and pragmatics are:

- Lexical semantics: the study of the meaning and relations of words, such as synonyms, antonyms, hyponyms, etc. .
- Compositional semantics: the study of how the meaning of a sentence is derived from the meaning of its parts and the way they are combined .
- Logical semantics: the study of the logical structure and validity of arguments and inferences based on language .
- Speech acts: the study of how language is used to perform actions, such as requesting, promising, apologizing, etc. .
- Implicature: the study of how speakers imply more than what they literally say, and how listeners infer the intended meaning .
- Presupposition: the study of what speakers assume or take for granted when they use language, and what listeners have to accept as true for the sentence to make sense .
- Deixis: the study of how words and expressions refer to different things depending on the context, such as pronouns, demonstratives, tense, etc. .
- Politeness: the study of how language is used to show respect, deference, or distance between speakers and listeners, and how it affects the interpretation of meaning .



# Requirements for representation for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Semantics is the study of meaning in natural language, and pragmatics is the study of meaning in context.
- A representation for semantics and pragmatics should capture the following aspects of natural language meaning:
  - **Lexical semantics**: the meaning of words and how they relate to each other, such as synonyms, antonyms, hyponyms, hypernyms, meronyms, etc. 
  - **Compositional semantics**: the meaning of phrases and sentences and how they are derived from the meaning of their constituents and the rules of syntax. 
  - **Discourse semantics**: the meaning of texts and dialogues and how they are structured by coherence relations, such as topic, focus, contrast, etc. 
  - **Pragmatic inference**: the meaning of utterances and how they are influenced by the speaker's intention, the listener's expectation, the common ground, the context, and the world knowledge. 
  - **Pragmatic ambiguity**: the phenomenon that the same utterance can have different meanings depending on the context and the speaker's intention. 
- A representation for semantics and pragmatics should also satisfy the following requirements:
  - **Formal**: the representation should be based on a well-defined syntax and semantics, and be amenable to automated reasoning and computation. 
  - **Expressive**: the representation should be able to capture the richness and diversity of natural language meaning, and handle various phenomena such as quantification, modality, anaphora, presupposition, implicature, etc. 
  - **Interoperable**: the representation should be compatible with other levels of natural language processing, such as syntax, morphology, phonology, etc., and with other modalities, such as speech, vision, etc. 
  - **Learnable**: the representation should be able to be acquired from data, either supervised or unsupervised, and be adaptable to new domains and tasks.



# First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL is more expressive than propositional logic, which can only represent the truth values of atomic sentences.
- FOL can represent complex sentences that involve quantifiers, variables, predicates, and functions.
- FOL can also capture the meaning of natural language sentences more precisely and systematically than informal methods.

## Syntax of FOL

- The syntax of FOL defines the rules for constructing well-formed formulas (WFFs) from a set of symbols.
- The symbols of FOL include:
  - Logical constants: `true`, `false`
  - Logical connectives: `and`, `or`, `not`, `implies`, `iff`
  - Quantifiers: `forall`, `exists`
  - Variables: `x`, `y`, `z`, ...
  - Predicates: `P`, `Q`, `R`, ...
  - Functions: `f`, `g`, `h`, ...
  - Constants: `a`, `b`, `c`, ...
- The grammar of FOL is as follows:

  - A term is either a variable, a constant, or a function applied to one or more terms.
  - An atomic formula is a predicate applied to one or more terms.
  - A formula is either an atomic formula, a logical constant, or a complex formula formed by applying a logical connective to one or more formulas, or by applying a quantifier to a formula with a variable.
  - A sentence is a formula that contains no free variables (i.e., variables that are not bound by a quantifier).

- Examples of terms: `x`, `a`, `f(x)`, `g(a, b)`
- Examples of atomic formulas: `P(x)`, `Q(a, b)`, `R(f(x), g(a, b))`
- Examples of formulas: `P(x)`, `not Q(a, b)`, `P(x) and Q(a, b)`, `forall x P(x)`, `exists x (P(x) and Q(x))`
- Examples of sentences: `P(a)`, `not Q(a, b)`, `forall x P(x)`, `exists x (P(x) and Q(x))`, `forall x (P(x) implies Q(x))`

## Semantics of FOL

- The semantics of FOL defines the rules for assigning truth values to formulas based on a model of the domain of discourse.
- A model consists of:
  - A domain: a non-empty set of objects that the terms can refer to.
  - An interpretation: a mapping from the symbols of FOL to the domain or to truth values.
- The interpretation assigns:
  - A unique object in the domain to each constant symbol.
  - A truth value (`true` or `false`) to each logical constant symbol.
  - A function from the domain to the domain to each function symbol of arity n (i.e., a function that takes n arguments).
  - A relation on the domain to each predicate symbol of arity n (i.e., a relation that holds for n objects).
- The truth value of a formula in a model is determined by:
  - The truth value of an atomic formula is the truth value of the corresponding relation applied to the corresponding objects in the domain.
  - The truth value of a logical constant is the truth value assigned by the interpretation.
  - The truth value of a complex formula is the truth value of the corresponding logical connective applied to the truth values of the subformulas.
  - The truth value of a quantified formula is the truth value of the corresponding quantifier applied to the truth values of the formula with different assignments of objects to the variable.
- A formula is satisfiable if there exists a model in which it is true.
- A formula is valid if it is true in every model.
- A formula entails another formula if the latter is true in every model in which the former is true.
- Examples of models:

  - Domain: `{1, 2, 3}`
  - Interpretation:
    - `a` -> `1`
    - `b` -> `2`
    - `c` -> `3`
    - `true` -> `true`
    - `false` -> `false`
    - `f` -> `+1` (i.e., a function that adds one to its argument)
    - `g` -> `*` (i.e.,



# Description Logics for Natural Language Processing

- Description logics (DLs) are a family of logic-based knowledge representation languages that allow for the formalization of concepts, roles, and individuals in a domain of interest .
- DLs can be used for various applications, such as the representation of ontologies, natural language processing, and formal verification  .
- In natural language processing (NLP), DLs can be used to represent the semantics of natural language expressions, such as sentences, phrases, and words  .
- DLs can also be used to perform reasoning tasks on natural language expressions, such as entailment, consistency, and satisfiability checking  .
- DLs can be integrated with other NLP components, such as parsers, lexicons, and dialogue systems, to provide a coherent and comprehensive framework for natural language understanding and generation  .
- Some examples of DL-based systems for NLP are:
  - Loom, a system that uses a DL called KL-ONE to represent and reason about natural language semantics.
  - LOLITA, a system that uses a DL called ALC to represent and reason about natural language semantics and pragmatics.
  - DIALOG, a system that uses a DL called ALCQ to represent and reason about natural language dialogue and discourse.
  - ACE, a system that uses a DL called SHOIN to represent and reason about natural language ontologies.



# Syntax-Driven Semantic Analysis

- Syntax-driven semantic analysis is the process of deriving the meaning of natural language sentences from their syntactic structure, using the rules of a formal grammar.
- Syntax-driven semantic analysis involves two main steps: parsing and interpretation.
- Parsing is the process of assigning a syntactic structure to a sentence, based on the rules of a grammar. A grammar is a set of rules that define how words can be combined to form sentences. A parser is a program that takes a sentence as input and outputs a parse tree, which is a hierarchical representation of the syntactic structure of the sentence.
- Interpretation is the process of assigning a semantic representation to a parse tree, based on the rules of a semantic theory. A semantic theory is a set of rules that define how syntactic structures can be mapped to meanings. A semantic representation is a formal expression that captures the meaning of a sentence in a logical language, such as predicate logic or lambda calculus.
- Syntax-driven semantic analysis can be performed using different types of grammars and semantic theories, such as context-free grammars and compositional semantics, or lexical-functional grammars and glue semantics. The choice of grammar and semantic theory depends on the goals and applications of the analysis, as well as the linguistic phenomena that need to be accounted for.
- Syntax-driven semantic analysis can be used for various natural language processing tasks, such as information extraction, question answering, machine translation, text summarization, and natural language understanding. Syntax-driven semantic analysis can help to disambiguate sentences that have multiple possible meanings, resolve anaphora and coreference, infer implicit information, and reason about the truth or falsity of sentences.



# Semantic attachments for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Semantic analysis is a subfield of natural language processing that helps machines to recognize and interpret the context and meaning of any text sample.
- Semantic analysis can be divided into two broad parts: lexical semantic analysis and compositional semantic analysis.
- Lexical semantic analysis involves understanding the meaning of each word of the text individually, based on its dictionary definition and its part of speech.
- Compositional semantic analysis involves understanding the meaning of larger units of text, such as phrases, sentences, and paragraphs, based on the syntactic structure and the logical relations among the words.
- Semantic attachments are a way of representing the meaning of text units using formal languages, such as logic, algebra, or programming languages.
- Semantic attachments can be used to link the syntactic structure of a text unit with its semantic representation, using rules or functions that map the syntactic categories to the semantic domains.
- Semantic attachments can be useful for various natural language processing applications, such as information extraction, question answering, natural language generation, and natural language understanding.
- Semantic attachments can be implemented using different methods, such as attribute grammars, lambda calculus, feature structures, or semantic networks.
- Semantic attachments can also be learned from data, using machine learning techniques, such as neural networks, probabilistic models, or semantic parsing.
- Semantic attachments can face some challenges, such as ambiguity, vagueness, anaphora, presupposition, and pragmatics, which require additional knowledge and reasoning to resolve.



# Word Senses

- A word sense is a representation of one aspect of a word's meaning.
- A word can have multiple senses, depending on the context in which it is used. For example, the word "bank" can mean a financial institution, a sloping mound, a biological repository, or a building where a bank does its business.
- Word sense disambiguation (WSD) is the task of assigning the appropriate sense to a given word in a text or discourse  .
- WSD is a challenging problem in natural language processing (NLP) because natural language is ambiguous, and many words can be interpreted in multiple ways depending on the context  .
- WSD is important for many NLP applications, such as machine translation, information retrieval, text summarization, question answering, sentiment analysis, etc. For example, translating the word "bank" from English to French requires knowing whether it means "banque" or "rive" in the source text .
- WSD can be performed using various methods, such as rule-based, knowledge-based, supervised, semi-supervised, or unsupervised approaches . Each method has its own advantages and disadvantages, depending on the availability of resources, the domain of the text, the granularity of the senses, etc.
- sense2vec is a fast and accurate method for word sense disambiguation, based on neural word representations. It models each word sense as a vector, and uses a large corpus of text annotated with part-of-speech tags to learn the sense vectors. It can handle both coarse-grained and fine-grained senses, and can be easily integrated with other NLP systems.



# Relations between Senses

- In natural language processing (NLP), word sense disambiguation (WSD) is the task of determining the meaning of a word in a given context, when the word has multiple possible meanings .
- WSD is important for NLP applications such as machine translation, information retrieval, text summarization, question answering, and sentiment analysis, as the meaning of a word can affect the interpretation and understanding of the whole text .
- WSD can be performed using various methods, such as rule-based, knowledge-based, supervised, semi-supervised, or unsupervised approaches.
- WSD is closely related to other NLP tasks, such as part-of-speech tagging, named entity recognition, semantic role labeling, and coreference resolution.
- WSD is also related to the linguistic fields of semantics and pragmatics, which study the meaning and use of language in context .
- Semantics is the branch of linguistics that deals with the meaning of words, phrases, sentences, and texts, while pragmatics is the branch of linguistics that deals with the meaning of language in relation to the situation, the speaker, the hearer, and the world.
- Semantics and pragmatics are interrelated, as the meaning of a word or a sentence can depend on the context, the intention, the inference, the presupposition, the implicature, and the speech act of the speaker or the hearer.
- For example, the word "bank" can have different senses, such as a financial institution, a river shore, or a verb meaning to tilt or turn, depending on the context and the usage.
- Similarly, the sentence "Can you pass the salt?" can have different meanings, such as a request, a question, or a sarcasm, depending on the tone, the gesture, and the situation of the speaker or the hearer.
- Therefore, WSD, semantics, and pragmatics are essential for NLP systems to understand and generate natural language accurately and appropriately    .



# Thematic Roles

Thematic roles are the semantic roles that the arguments of a verb play in a sentence. They describe the relationship between the verb and its arguments, such as who did what to whom, how, when, where, why, etc. Thematic roles are also called theta roles or case roles.

Some of the major thematic roles are:

- **Agent**: The entity that intentionally carries out the action of the verb. For example, in "John opened the door", John is the agent.
- **Experiencer**: The entity that undergoes an emotion, a state of being, or a perception expressed by the verb. For example, in "Mary saw a bird", Mary is the experiencer.
- **Theme**: The entity that directly receives the action of the verb. For example, in "John opened the door", the door is the theme.
- **Instrument**: The entity by which the action of the verb is carried out. For example, in "John opened the door with a key", the key is the instrument.
- **Source**: The entity from which the action of the verb originates. For example, in "John came from Paris", Paris is the source.
- **Goal**: The entity to which the action of the verb is directed. For example, in "John went to London", London is the goal.
- **Location**: The entity where the action of the verb takes place. For example, in "John lives in New York", New York is the location.
- **Beneficiary**: The entity for whose benefit the action of the verb is performed. For example, in "John baked a cake for Mary", Mary is the beneficiary.
- **Cause**: The entity that causes the action of the verb to happen. For example, in "The storm broke the window", the storm is the cause.

Thematic roles are important for natural language processing because they help to understand the meaning of a sentence and to perform tasks such as semantic parsing, semantic role labeling, question answering, information extraction, etc. Thematic roles can be identified by using syntactic cues, such as word order, case marking, prepositions, etc., or by using semantic knowledge, such as selectional restrictions, verb classes, etc.



# Selectional Restrictions

Selectional restrictions are semantic constraints that limit the possible arguments of a predicate. They account for the implausibility or ungrammaticality of sentences such as:

- Colorless green ideas slept furiously.
- The chair ate the sandwich.
- She drank the music.

Selectional restrictions are used in natural language processing for:

- Disambiguation: resolving the meaning of words or phrases that have multiple senses or interpretations.
- Pronoun resolution: identifying the referent of a pronoun in a given context.
- Lexical insertion: choosing the appropriate word to fill a syntactic slot in a sentence.

Selectional restrictions can be represented as:

- Sets of semantic features that a verb requires of its arguments, such as [+animate], [-abstract], or [+human].
- Types or categories that encode individuation conditions, such as e for entities, t for truth values, or s for situations.
- Distributional vectors that capture the co-occurrence patterns of words in large corpora, such as word2vec or GloVe.

Selectional restrictions can be violated for various reasons, such as:

- Metaphor: using words in a non-literal sense, such as He devoured the book.
- Humor: creating absurd or incongruous combinations, such as The cow jumped over the moon.
- Creativity: introducing novel or unconventional expressions, such as She painted the town red.

Selectional restrictions are not absolute or universal, but depend on the context, the genre, and the speaker's intention.




# Word Sense Disambiguation

- Word sense disambiguation (WSD) is the problem of determining which "sense" (meaning) of a word is activated by the use of the word in a particular context, a process which appears to be largely unconscious in people.
- WSD is a subfield of natural language processing (NLP) that deals with identifying the intended meaning of a word in a given context. It is the process of selecting the correct sense of a word from a set of possible senses, based on the context in which the word appears.
- WSD is an important research problem in NLP because lexical ambiguity, syntactic or semantic, is one of the very first problems that any NLP system faces. Lexical ambiguity occurs when a word has more than one possible meaning, such as "bank" (financial institution or river shore), "bat" (flying mammal or wooden club), or "crane" (bird or lifting machine).
- WSD can improve the performance of various NLP applications, such as machine translation, information retrieval, text summarization, question answering, sentiment analysis, etc. For example, in machine translation, WSD can help to choose the appropriate translation of a word based on the context, such as "interest" (curiosity or money paid for borrowing) or "date" (fruit or calendar day).
- WSD can be classified into two main types: supervised and unsupervised. Supervised WSD uses labeled data, such as sense-annotated corpora or dictionaries, to train a classifier that can assign a sense to a word based on its features, such as surrounding words, part-of-speech tags, syntactic structure, etc. Unsupervised WSD does not use labeled data, but relies on clustering or similarity measures to group words into senses based on their co-occurrence patterns, semantic relations, or other criteria.
- WSD faces some difficulties, such as the lack of standard sense inventories, the granularity of senses, the scarcity of sense-annotated data, the domain specificity of senses, the context dependence of senses, the subjectivity of senses, etc. Sense inventories are the collection of abbreviations and acronyms with their meanings, such as WordNet, BabelNet, etc. The granularity of senses refers to the level of detail or specificity of the senses, such as fine-grained or coarse-grained. The scarcity of sense-annotated data means that there are not enough examples of words with their senses in different contexts to train or evaluate WSD systems. The domain specificity of senses means that the same word may have different senses in different domains, such as "mouse" (computer device or animal) or "chip" (electronic component or food item). The context dependence of senses means that the same word may have different senses in different contexts, even within the same domain, such as "cold" (temperature or illness) or "light" (brightness or weight). The subjectivity of senses means that different people may have different interpretations of the same word, depending on their background knowledge, preferences, opinions, etc.
- WSD is a challenging and open problem in NLP, and there is still room for improvement and innovation in developing new methods, resources, and applications for WSD. Some of the current research directions in WSD include: using deep learning and neural networks to capture complex and non-linear features of words and contexts, using multilingual and cross-lingual data to leverage the information from different languages and cultures, using knowledge graphs and ontologies to enrich the semantic representation of words and senses, using common sense and world knowledge to infer the implicit and pragmatic meaning of words, using multimodal data, such as images, audio, or video, to complement the textual information, and using user feedback and interactive learning to adapt and personalize the WSD system to the user's needs and preferences.



# WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the supervised learning algorithms that have been applied to WSD are decision trees, naive Bayes, support vector machines, neural networks, etc  .
- Supervised WSD methods have the advantage of being able to learn from large amounts of data and achieve high accuracy on the same domain and genre as the training data.
- However, supervised WSD methods also have some limitations, such as the scarcity of sense-annotated data, the domain and genre dependence of the models, and the difficulty of adapting to new senses or words  .



# Dictionary & Thesaurus for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Natural language processing (NLP) is the application of machine learning algorithms to the analysis, understanding, and manipulation of written or spoken examples of human language.
- Semantics is the study of the meaning of words, phrases, and sentences in natural language, while pragmatics is the study of how context affects the interpretation and use of language.
- A dictionary is a resource that provides information about the spelling, pronunciation, part of speech, definition, and usage of words in a language. A dictionary can be used for various NLP tasks, such as word sense disambiguation, spelling correction, text summarization, and sentiment analysis.
- A thesaurus is a resource that provides synonyms and antonyms of selected words in a language. A thesaurus can be used for NLP tasks that require lexical variation, such as text generation, paraphrasing, query expansion, and information retrieval.
- Some of the challenges and limitations of using dictionaries and thesauruses for NLP are:
  - They may not cover all the words and senses in a language, especially new, rare, or domain-specific terms.
  - They may introduce ambiguity and noise, as words can have multiple meanings and synonyms depending on the context and usage.
  - They may not capture the nuances and connotations of words, such as emotional, stylistic, or pragmatic aspects.
  - They may not reflect the dynamic and evolving nature of natural language, as new words and senses emerge and old ones become obsolete over time.
- Some of the methods and techniques to overcome these challenges and improve the quality and usefulness of dictionaries and thesauruses for NLP are:
  - Using corpus-based methods to extract and update word information from large collections of text data, such as frequency, collocations, and co-occurrences.
  - Using knowledge-based methods to enrich and organize word information using external sources, such as ontologies, taxonomies, and semantic networks.
  - Using machine learning methods to learn and infer word information from data, such as word embeddings, neural networks, and probabilistic models.
  - Using evaluation methods to measure and compare the performance and accuracy of different dictionary and thesaurus resources and applications for NLP.



# Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods are useful for natural language processing (NLP) tasks that require semantic or pragmatic knowledge, such as word sense disambiguation, relation extraction, named entity recognition, etc.
- Bootstrapping methods in NLP generally follow the same format:
  - Start with an empty list of things (e.g., words, phrases, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., manually annotated examples, heuristics, dictionaries, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using pattern matching, similarity measures, clustering, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more new things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two types:
  - Self-training: The model learns from its own predictions on the unlabeled data and adds the most confident ones to the labeled data.
  - Co-training: The model consists of two or more classifiers that learn from different views or features of the data and mutually reinforce each other by adding the most confident predictions to the labeled data.
- Bootstrapping methods can also be combined with other learning techniques, such as rule-based methods, active learning, ensemble methods, etc.
- Bootstrapping methods have some advantages and disadvantages:
  - Advantages: They can reduce the need for manual annotation, exploit the large amount of unlabeled data, and improve the performance of the model.
  - Disadvantages: They can suffer from semantic drift, noise propagation, and data sparsity. Semantic drift refers to the deviation of the learned concepts from the original seeds due to errors or ambiguities. Noise propagation refers to the accumulation of errors or inconsistencies in the labeled data due to the model's predictions. Data sparsity refers to the lack of sufficient or diverse examples for some concepts or categories.



# Word Similarity using Thesaurus and Distributional methods

- Word similarity is a measure of how closely related two words are in terms of their meaning, usage, or association.
- Word similarity can be computed using different methods, such as thesaurus-based methods and distributional methods.
- Thesaurus-based methods rely on manually curated lexical resources, such as WordNet, that group words into synonym sets (synsets) and link them with semantic relations, such as hypernymy, hyponymy, meronymy, etc.
- Distributional methods rely on large corpora of text, where words are represented as vectors based on their co-occurrence patterns with other words in a given context window.
- Thesaurus-based methods have the advantage of capturing fine-grained semantic distinctions and relations, but they are limited by the coverage and quality of the lexical resources, and they may not reflect the current usage and sense of words in natural language.
- Distributional methods have the advantage of being data-driven and scalable, but they may not capture the nuances and subtleties of word meaning, and they may be sensitive to noise and sparsity in the data.
- Word similarity can be used for various natural language processing tasks, such as word sense disambiguation, semantic role labeling, information retrieval, text summarization, etc.



## Unit 5 - BASIC CONCEPTS of Speech Processing

Speech processing is the study of how humans produce, perceive, and understand speech, as well as how machines can emulate, recognize, and synthesize speech. Speech processing involves several subfields, such as speech production, speech perception, speech recognition, speech synthesis, speech analysis, speech enhancement, speech coding, and speech translation.

Some of the basic concepts of speech processing are:

- Speech production: This is the process by which humans generate speech sounds using the vocal tract and the respiratory system. Speech production involves three major levels of processing: conceptualization, formulation, and articulation. Conceptualization is the stage where the speaker decides what to say and selects the appropriate words and grammatical structures. Formulation is the stage where the speaker encodes the words into phonological and prosodic units. Articulation is the stage where the speaker produces the speech sounds by coordinating the movements of the vocal cords, the tongue, the lips, and the jaw.
- Speech perception: This is the process by which humans decode and interpret speech sounds using the auditory system and the brain. Speech perception involves several stages, such as auditory processing, phonetic processing, lexical processing, syntactic processing, semantic processing, and pragmatic processing. Auditory processing is the stage where the listener receives and analyzes the acoustic signal. Phonetic processing is the stage where the listener identifies the speech sounds and their features. Lexical processing is the stage where the listener accesses the stored knowledge of words and their meanings. Syntactic processing is the stage where the listener parses the sentence structure and assigns grammatical roles. Semantic processing is the stage where the listener derives the literal meaning of the sentence. Pragmatic processing is the stage where the listener infers the speaker's intention and the context of the utterance.
- Speech recognition: This is the process by which machines convert speech sounds into text or commands. Speech recognition involves several steps, such as feature extraction, acoustic modeling, language modeling, decoding, and post-processing. Feature extraction is the step where the machine extracts relevant information from the speech signal, such as spectral, temporal, and prosodic features. Acoustic modeling is the step where the machine learns the statistical relationship between the features and the speech units, such as phonemes, words, or sentences. Language modeling is the step where the machine learns the statistical relationship between the speech units and the language, such as the probability of a word given the previous words. Decoding is the step where the machine searches for the most likely sequence of speech units that matches the features. Post-processing is the step where the machine corrects or enhances the output, such as by using spelling, grammar, or context information.
- Speech synthesis: This is the process by which machines generate speech sounds from text or commands. Speech synthesis involves several steps, such as text analysis, text-to-speech conversion, and speech generation. Text analysis is the step where the machine analyzes the input text and extracts relevant information, such as the language, the style, the emotion, and the prosody. Text-to-speech conversion is the step where the machine converts the text into a sequence of speech units, such as phonemes, words, or sentences, and assigns appropriate features, such as pitch, duration, and stress. Speech generation is the step where the machine produces the speech sounds by using a speech database, a speech model, or a speech synthesizer.
- Speech analysis: This is the process by which machines extract useful information from speech sounds, such as the speaker identity, the speaker emotion, the speaker accent, the speech quality, the speech content, and the speech context. Speech analysis involves several techniques, such as speech segmentation, speech classification, speech clustering, speech verification, speech identification, speech enhancement, speech coding, and speech translation. Speech segmentation is the technique where the machine divides the speech signal into smaller units, such as frames, segments, or syllables. Speech classification is the technique where the machine assigns a label to each speech unit, such as voiced or unvoiced, consonant or vowel, or male or female. Speech clustering is the technique where the machine groups similar speech units together, such as by using k-means, Gaussian mixture models, or neural networks. Speech verification is the technique where the machine confirms or rejects the identity of the speaker, such as by using biometric features, such as voiceprints, or behavioral features, such as passwords. Speech identification is the technique where the machine recognizes the identity of the speaker, such as by using speaker models, such as hidden Markov models, or speaker embeddings, such as i-vectors. Speech enhancement is the



# Speech Fundamentals

Speech is the most natural and common way of human communication. Speech processing is the study of how to analyze, understand, and generate speech using computational methods. Speech processing is a subfield of natural language processing (NLP), which is the branch of artificial intelligence that deals with human language in general.

Some of the basic concepts of speech processing are:

- **Speech recognition**: This is the process of turning spoken voice data into text data. Speech recognition systems use acoustic models to map sounds to phonetic units, and language models to map phonetic units to words and sentences. Speech recognition can be used for various applications, such as voice assistants, dictation, transcription, and authentication.

- **Word sense disambiguation**: This is the process of determining the meaning of a word in a given context. Many words in natural languages have multiple meanings, depending on how they are used. For example, the word "bank" can mean a financial institution, a river shore, or a verb meaning to tilt or turn. Word sense disambiguation algorithms use lexical, syntactic, semantic, and pragmatic cues to infer the intended sense of a word.

- **Coreference resolution**: This is the process of identifying and linking words or phrases that refer to the same entity in a text or speech. For example, in the sentence "Alice went to the park with her dog. She loves it there.", the pronouns "she" and "it" refer to Alice and her dog, respectively. Coreference resolution helps to resolve ambiguity and improve the coherence and understanding of a text or speech.

- **Sentiment analysis**: This is the process of extracting the attitude, opinion, or emotion of a speaker or writer from a text or speech. Sentiment analysis can be done at different levels, such as word, phrase, sentence, or document level. Sentiment analysis can be used for various applications, such as customer feedback, social media analysis, product reviews, and market research.

- **Speech synthesis**: This is the process of generating natural-sounding speech from text data. Speech synthesis systems use text analysis, prosody modeling, and acoustic modeling to produce speech signals that match the content, style, and emotion of the input text. Speech synthesis can be used for various applications, such as text-to-speech, audiobooks, voiceovers, and accessibility.

- **Speech enhancement**: This is the process of improving the quality and intelligibility of speech signals in noisy or reverberant environments. Speech enhancement techniques include noise reduction, echo cancellation, dereverberation, and beamforming. Speech enhancement can be used for various applications, such as teleconferencing, hearing aids, speech recognition, and speech synthesis.

- **Speech coding**: This is the process of compressing speech signals to reduce the bandwidth and storage requirements for transmission and storage. Speech coding techniques include waveform coding, source coding, and hybrid coding. Speech coding can be used for various applications, such as telephony, internet telephony, voice mail, and multimedia.

- **Speech segmentation**: This is the process of dividing a speech signal into smaller units, such as words, syllables, phonemes, or features. Speech segmentation can be done based on acoustic, linguistic, or statistical criteria. Speech segmentation can be used for various applications, such as speech recognition, speech synthesis, speech analysis, and speech indexing.

- **Speech alignment**: This is the process of aligning a speech signal with a corresponding text or transcription. Speech alignment can be done at different levels, such as word, syllable, phoneme, or feature level. Speech alignment can be used for various applications, such as speech synthesis, speech recognition, speech editing, and speech annotation.

- **Speech translation**: This is the process of translating speech from one language to another. Speech translation systems can be divided into two types: cascaded systems and end-to-end systems. Cascaded systems use speech recognition, machine translation, and speech synthesis as separate modules, while end-to-end systems use a single neural network to directly map speech signals from one language to another. Speech translation can be used for various applications, such as cross-lingual communication, education, tourism, and entertainment.



# Articulatory Phonetics

- Articulatory phonetics is the branch of phonetics that studies how speech sounds are produced by the human vocal tract .
- Speech sounds are produced by the movements and/or positions of the vocal organs, such as the tongue, lips, teeth, palate, velum, glottis, etc. These are called articulators .
- Articulatory phonetics is concerned with the transformation of aerodynamic energy (airflow through the vocal tract) into acoustic energy (sound waves) .
- Articulatory phonetics is also interested in the physical and cognitive factors that determine what are possible speech sounds and sound patterns in the world's languages .
- Articulatory phonetics can be divided into two main subfields: segmental phonetics and suprasegmental phonetics .
  - Segmental phonetics deals with the production and classification of speech sounds as discrete units, such as consonants and vowels.
  - Suprasegmental phonetics deals with the production and perception of features that span over multiple segments, such as stress, intonation, tone, and duration.
- Articulatory phonetics uses various methods and tools to observe and measure the articulatory processes, such as x-ray, ultrasound, electropalatography, magnetic resonance imaging, etc.  .
- Articulatory phonetics is closely related to other branches of phonetics, such as acoustic phonetics (the study of the physical properties of speech sounds) and auditory phonetics (the study of the perception of speech sounds)  .



# Production And Classification Of Speech Sounds

- Speech sounds are the basic units of human communication that convey meaning and emotion through variations in sound waves.
- Speech sounds are produced by the coordinated action of the respiratory, phonatory, and articulatory systems, which are also known as the speech organs.
- Speech sounds are classified into two main categories: vowels and consonants, based on the degree of constriction or obstruction in the vocal tract during their production.
- Vowels are speech sounds that are produced with a relatively open vocal tract, allowing the air to flow freely. Vowels are typically voiced, meaning that the vocal folds vibrate during their production. Vowels are also characterized by their tongue height, tongue backness, lip rounding, and tenseness.
- Consonants are speech sounds that are produced with a relatively closed vocal tract, creating some degree of friction or turbulence in the air flow. Consonants can be voiced or voiceless, depending on whether the vocal folds vibrate or not. Consonants are also characterized by their place of articulation, manner of articulation, and secondary articulation.
- Place of articulation refers to the location of the constriction or obstruction in the vocal tract, such as bilabial, labiodental, dental, alveolar, palatal, velar, or glottal.
- Manner of articulation refers to the type of constriction or obstruction in the vocal tract, such as plosive, fricative, affricate, nasal, lateral, approximant, or trill.
- Secondary articulation refers to the modification of the primary articulation by another part of the vocal tract, such as labialization, palatalization, velarization, or pharyngealization.
- Speech sounds can be represented by symbols that correspond to their articulatory features, such as the International Phonetic Alphabet (IPA), which is a standardized system of symbols for all the sounds of human languages.



# Acoustic Phonetics

- Acoustic phonetics is the study of the acoustic characteristics of speech, including an analysis and description of speech in terms of its physical properties, such as frequency, intensity, and duration .
- Acoustic phonetics is an instrumental science that depends on ways to store, replicate, visualize, and analyze the speech signal. Acoustic phonetics is also a cumulative science in which older research continues to be influential.
- Acoustic phonetics investigates time domain features such as the mean squared amplitude of a waveform, its duration, its fundamental frequency, or frequency domain features such as the frequency spectrum, or even combined spectrotemporal features and the relationship of these properties to other branches of phonetics (e.g. articulatory or auditory phonetics), and to abstract linguistic concepts such as phonemes, phrases, or utterances.
- Some of the main topics of acoustic phonetics are:
  - The source-filter theory of speech production, which describes how the vocal tract shapes the glottal source into speech sounds.
  - The acoustic analysis of vowels, consonants, and suprasegmentals, such as stress, intonation, and tone.
  - The acoustic cues for speech perception, which are the features of the speech signal that allow listeners to identify and distinguish speech sounds.
  - The acoustic correlates of speech disorders, such as dysarthria, apraxia, stuttering, and cleft palate.
  - The acoustic characteristics of different languages, dialects, accents, and styles of speech.
  - The acoustic modeling of speech, which involves the use of mathematical and computational methods to represent and simulate the speech signal.



# Acoustics of Speech Production

- Acoustics of speech production is the study of how speech sounds are generated and modified by the human vocal tract and the physical properties of the resulting sound waves.
- Speech production involves three main components: a source of sound energy, a source of sound modulation, and a filter that shapes the sound spectrum.
- The source of sound energy is usually the air pressure from the lungs, which is controlled by the respiratory system and the diaphragm.
- The source of sound modulation is usually the vocal folds, which are two bands of muscle and tissue that vibrate when air passes through them. The vibration frequency of the vocal folds determines the pitch of the voice. The vocal folds can also be adjusted to produce different types of voice quality, such as breathy, creaky, or modal.
- The filter that shapes the sound spectrum is the vocal tract, which consists of the pharynx, the oral cavity, the nasal cavity, and the articulators. The articulators are the movable parts of the mouth and throat, such as the tongue, the lips, the teeth, the jaw, and the soft palate. The articulators can change the shape and size of the vocal tract, creating different resonances and formants that characterize different speech sounds, such as vowels and consonants.
- The acoustic theory of speech production is a mathematical model that describes how the source and the filter interact to produce the speech signal. The model assumes that the source and the filter are independent and linear, meaning that they do not affect each other and that their effects are additive. The model also assumes that the vocal tract can be approximated by a series of tubes with varying cross-sectional areas and lengths.
- The acoustic theory of speech production can be used to analyze and synthesize speech sounds, as well as to understand the acoustic cues that listeners use to perceive speech. The theory can also be applied to other animals and machines that produce speech-like sounds.



# Review Of Digital Signal Processing Concepts for the notes of the Unit 5 - BASIC CONCEPTS of Speech Processing in the subject of Natural Language Processing

- Speech processing is the study of how speech signals are acquired, manipulated, stored, transferred and output.
- Speech signals are usually processed in a digital representation, so speech processing can be regarded as a special case of digital signal processing (DSP), applied to speech signals.
- DSP is concerned with both a discrete signal representation, and with the theory, design and implementation of numerical procedures for processing discrete representation.
- Some of the basic concepts and algorithms of DSP that are relevant for speech processing are:

  - Sampling and quantization: the process of converting a continuous-time signal into a discrete-time signal by taking samples at regular intervals and assigning them numerical values.
  - Fourier transform and spectrum: the process of decomposing a signal into its frequency components and representing them as a function of frequency.
  - Z-transform and filter: the process of transforming a discrete-time signal into a complex function of a complex variable and applying linear operations to modify its frequency response.
  - Discrete cosine transform and cepstrum: the process of transforming a signal into a sum of cosine functions and applying a logarithm and an inverse Fourier transform to obtain a representation of its spectral envelope.
  - Linear prediction and LPC coefficients: the process of estimating the current sample of a signal as a linear combination of its past samples and obtaining a set of parameters that characterize its spectral shape.
  - Windowing and framing: the process of dividing a signal into short segments and applying a weighting function to reduce the discontinuities at the edges.
  - Short-time Fourier transform and spectrogram: the process of applying the Fourier transform to each frame of a signal and obtaining a time-frequency representation of its energy distribution.
  - Mel-frequency cepstral coefficients and MFCCs: the process of applying a filter bank that mimics the human auditory system to the spectrum of a signal and obtaining a set of features that are widely used for speech recognition and synthesis.

- Some of the applications of DSP in speech processing are:

  - Speech synthesis: the process of generating artificial speech signals from text or other symbolic inputs.
  - Speech recognition: the process of converting speech signals into text or other symbolic outputs.
  - Speech enhancement: the process of improving the quality of speech signals by reducing noise, reverberation, distortion or other degradations.
  - Speech coding: the process of compressing speech signals for efficient transmission or storage.
  - Speech analysis: the process of extracting information from speech signals such as speaker identity, emotion, language, accent, etc..



# Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique for analyzing the frequency content of a signal over time .
- It is based on applying a window function to a segment of the signal and then computing the Fourier transform of the windowed segment .
- The window function is usually shifted by a certain amount (called the hop size) to obtain the next segment, and the process is repeated until the entire signal is covered .
- The result of the STFT is a two-dimensional representation of the signal, where the horizontal axis is time and the vertical axis is frequency .
- The STFT can be used to perform various tasks on speech signals, such as feature extraction, filtering, enhancement, modification, and recognition .
- The STFT can also be visualized as a spectrogram, which is a plot of the magnitude or power of the STFT coefficients as a function of time and frequency  .
- The spectrogram can reveal the spectral characteristics of speech sounds, such as formants, pitch, and harmonics .
- The STFT has some limitations, such as the trade-off between time and frequency resolution, the assumption of stationarity within each window, and the dependence on the choice of the window function and the hop size .
- To overcome some of these limitations, other time-frequency transforms have been proposed, such as the wavelet transform, the constant-Q transform, and the Mel-frequency cepstral coefficients (MFCCs)  .



# Filter Bank And LPC Methods

Filter bank and LPC methods are two techniques for analyzing and synthesizing speech signals. They are based on different models of how speech is produced and perceived.

## Filter Bank Methods

Filter bank methods are based on the idea that speech is composed of different frequency components that can be separated by a set of filters. Each filter passes a narrow band of frequencies and attenuates the others. The output of each filter is called a subband signal, and the set of subband signals is called a filter bank.

Filter bank methods can be used for both speech analysis and synthesis. For speech analysis, the filter bank is applied to the input speech signal and the subband signals are extracted. The subband signals can be further processed to obtain features such as the mel-frequency cepstral coefficients (MFCCs), which are widely used for speech recognition. MFCCs are obtained by applying a discrete cosine transform (DCT) to the logarithm of the subband energies.

For speech synthesis, the filter bank is applied in reverse. The subband signals are generated from the features and then combined to form the output speech signal. This can be done by using a simple filter that equalizes the variance of the cepstral coefficients, as proposed by Ravindran and Demiroglu.

## LPC Methods

LPC methods are based on the idea that speech is produced by a source-filter model. The source is the vocal cords, which produce a periodic signal (buzz) for voiced sounds or a random signal (hiss) for unvoiced sounds. The filter is the vocal tract, which shapes the source signal by resonating at certain frequencies called formants.

LPC methods can also be used for both speech analysis and synthesis. For speech analysis, the LPC method estimates the formants and the source signal from the input speech signal. This can be done by using various algorithms, such as the autocorrelation method, the covariance method, the lattice method, or the inverse filter formulation. The output of the LPC analysis is a set of coefficients that represent the filter and a residual signal that represents the source.

For speech synthesis, the LPC method reverses the process. The source signal is generated from the residual signal and the filter is generated from the coefficients. The source signal is then passed through the filter to produce the output speech signal.



## Unit 6 - SPEECH-ANALYSIS

Speech-analysis is the process of examining the acoustic features and linguistic structures of speech to identify, interpret, and evaluate its meaning, purpose, and effectiveness.

Some of the objectives of speech-analysis are:

- To understand the speaker's intention, message, and audience.
- To identify the speaker's tone, mood, attitude, and emotion.
- To evaluate the speaker's credibility, logic, evidence, and persuasion techniques.
- To appreciate the speaker's style, language, and rhetorical devices.
- To compare and contrast different speeches or speakers on the same or related topics.

Some of the steps of speech-analysis are:

- Listen to or read the speech carefully and attentively.
- Identify the main idea, thesis, or claim of the speech.
- Analyze the structure, organization, and transitions of the speech.
- Examine the content, arguments, and supporting details of the speech.
- Evaluate the sources, reliability, and validity of the information and data used in the speech.
- Assess the speaker's delivery, voice, gestures, and nonverbal cues.
- Identify the speaker's purpose, audience, and context.
- Determine the speaker's tone, mood, attitude, and emotion.
- Identify and explain the speaker's use of rhetorical appeals (ethos, pathos, logos), strategies, and devices.
- Summarize the main points, strengths, and weaknesses of the speech.
- Provide your own opinion, feedback, or critique of the speech.



# Features for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotions, intent, and the content of the speech.
- Speech analysis is a subfield of natural language processing (NLP), which is the branch of artificial intelligence that deals with understanding and generating natural language.
- Speech analysis involves various techniques and applications, such as speech recognition, speech synthesis, speech segmentation, speech enhancement, speech coding, speech translation, speech summarization, speech emotion recognition, speaker identification, and speech diarization.
- Speech analysis can be performed at different levels of linguistic representation, such as phonetic, phonological, morphological, syntactic, semantic, pragmatic, and discourse.
- Speech analysis can also be performed using different approaches, such as rule-based, statistical, neural, or hybrid.
- Speech analysis can benefit from various features that capture the characteristics of speech signals, such as acoustic, prosodic, lexical, syntactic, and semantic features.
- Acoustic features are based on the physical properties of speech signals, such as pitch, intensity, duration, formants, and spectral features.
- Prosodic features are based on the variations of acoustic features over time, such as intonation, stress, rhythm, and pause.
- Lexical features are based on the words and phrases used in speech, such as vocabulary size, word frequency, word length, and n-grams.
- Syntactic features are based on the grammatical structure of speech, such as part-of-speech tags, parse trees, dependency relations, and grammatical errors.
- Semantic features are based on the meaning and context of speech, such as polarity, sentiment, topic, keywords, and named entities.
- Speech analysis can be used for various purposes, such as human-computer interaction, speech-to-text conversion, text-to-speech synthesis, speech enhancement, speech compression, speech translation, speech summarization, speech emotion recognition, speaker identification, speech diarization, and speech forensics.



# Feature Extraction And Pattern Comparison Techniques for Speech Analysis

## Introduction

Speech analysis is the process of extracting meaningful information from speech signals, such as the speaker identity, the spoken language, the speech content, the emotion, the accent, etc. Speech analysis is an important task in natural language processing, as it enables applications such as speech recognition, speaker verification, speech synthesis, speech enhancement, speech translation, etc.

Speech analysis involves two main steps: feature extraction and pattern comparison. Feature extraction is the process of transforming the speech signal into a compact and representative set of parameters that capture the relevant characteristics of the speech. Pattern comparison is the process of matching the extracted features with a predefined set of models or templates, in order to identify the speech category or class.

## Feature Extraction Techniques

Feature extraction techniques aim to reduce the dimensionality and complexity of the speech signal, while preserving the essential information for the analysis task. Feature extraction techniques can be classified into two categories: temporal and spectral.

Temporal techniques use the speech waveform itself as the feature vector, and analyze the variations of the amplitude, energy, zero-crossing rate, etc. over time. Temporal techniques are simple and fast, but they are sensitive to noise and variations in the speech signal.

Spectral techniques use the frequency-domain representation of the speech signal as the feature vector, and analyze the spectrum, cepstrum, filterbank, etc. of the speech. Spectral techniques are more robust and discriminative, but they are more complex and computationally intensive.

Some of the commonly used feature extraction techniques are:

- Linear Predictive Coding (LPC): LPC is a technique that models the speech signal as a linear combination of past samples, and estimates the coefficients of the linear predictor using the autocorrelation method or the covariance method. LPC features are the predictor coefficients, the residual error, and the gain. LPC features are good for speech synthesis and speaker recognition, but they are not suitable for speech recognition, as they are sensitive to pitch variations and noise.

- Mel-Frequency Cepstral Coefficients (MFCC): MFCC is a technique that applies a mel-scale filterbank to the speech spectrum, and computes the discrete cosine transform (DCT) of the log-energy of the filterbank outputs. MFCC features are the DCT coefficients, and they represent the envelope of the speech spectrum. MFCC features are good for speech recognition and speaker identification, as they are robust to noise and speaker variations, but they are not suitable for speech synthesis, as they lose the phase information of the speech signal.

- Perceptual Linear Prediction (PLP): PLP is a technique that applies a perceptual weighting filter to the speech spectrum, and computes the LPC coefficients of the weighted spectrum. PLP features are the LPC coefficients, the residual error, and the gain. PLP features are similar to MFCC features, but they incorporate the human auditory system characteristics, such as the critical bands, the equal-loudness curve, and the intensity-loudness power law. PLP features are good for speech recognition and speaker identification, as they are more perceptually relevant and robust to noise.

## Pattern Comparison Techniques

Pattern comparison techniques aim to measure the similarity or distance between the extracted features and a set of reference models or templates, in order to assign the speech signal to a specific category or class. Pattern comparison techniques can be classified into two categories: template-based and model-based.

Template-based techniques use a set of stored feature vectors as the reference templates, and compare the extracted features with each template using a distance metric, such as the Euclidean distance, the Mahalanobis distance, the cosine similarity, etc. Template-based techniques are simple and intuitive, but they require a large storage space and a high computational cost, and they are sensitive to variations in the speech signal.

Model-based techniques use a set of statistical models as the reference models, and compute the likelihood or probability of the extracted features given each model using a probabilistic framework, such as the Bayes' rule, the maximum likelihood, the maximum a posteriori, etc. Model-based techniques are more flexible and efficient, but they require a training phase and a parameter estimation process, and they are sensitive to the model assumptions and the data distribution.

Some of the commonly used pattern comparison techniques are:

- Dynamic Time Warping (DTW): DTW is a template-based technique that aligns the extracted features with the reference templates using a dynamic programming algorithm, and computes the optimal distance between them. DTW can handle the temporal variations in the speech signal, such as the different speaking rates, pauses, insertions, deletions, etc. DTW is good for isolated word recognition



# Speech Distortion Measures

Speech distortion measures are quantitative methods to evaluate the quality and intelligibility of speech signals that have been affected by noise, hearing loss, or processing algorithms. Speech distortion measures can be classified into two categories: signal-based and perception-based.

- Signal-based measures compare the original speech signal with the distorted speech signal using mathematical operations, such as mean squared error, signal-to-noise ratio, or spectral distance. Signal-based measures are easy to compute and do not require human listeners, but they may not reflect the perceptual effects of distortion on speech comprehension.

- Perception-based measures assess the subjective impression of speech quality or intelligibility by human listeners, using rating scales, word recognition tests, or speech reception thresholds. Perception-based measures are more reliable and valid than signal-based measures, but they are more time-consuming and costly to conduct.

Some examples of speech distortion measures are:

- Articulation Index (AI): a signal-based measure that estimates the proportion of speech information that is audible to a listener with a given hearing loss. AI ranges from 0 (no speech information) to 1 (all speech information).

- Speech Intelligibility Index (SII): a signal-based measure that is similar to AI, but accounts for the effects of noise and speech level on speech audibility. SII also ranges from 0 to 1.

- Speech Transmission Index (STI): a signal-based measure that evaluates the degradation of speech signals due to noise and reverberation. STI ranges from 0 (poor transmission) to 1 (excellent transmission).

- Mean Opinion Score (MOS): a perception-based measure that rates the overall quality of speech signals on a 5-point scale, from 1 (bad) to 5 (excellent).

- Word Recognition Score (WRS): a perception-based measure that calculates the percentage of words that are correctly identified by listeners from a list of words presented in noise or distortion.

- Speech Reception Threshold (SRT): a perception-based measure that determines the lowest signal-to-noise ratio at which listeners can understand 50% of the words in a sentence.



# Mathematical and Perceptual Speech Analysis

- Speech analysis is the process of extracting information from speech signals, such as the linguistic content, the speaker identity, the emotion, etc.
- Speech analysis can be done from different perspectives, such as mathematical, perceptual, linguistic, or cognitive.
- Mathematical speech analysis involves using mathematical models and methods to represent and manipulate speech signals, such as Fourier analysis, linear prediction, spectral analysis, etc.
- Perceptual speech analysis involves using psychological and physiological principles of human hearing to model and interpret speech signals, such as critical-band filtering, equal-loudness weighting, intensity-loudness mapping, etc.
- Mathematical and perceptual speech analysis are related and complementary, as they both aim to capture the essential features of speech signals and their perception by human listeners.
- Mathematical and perceptual speech analysis can be applied to various tasks and domains of speech technology, such as speech recognition, speech synthesis, speech enhancement, speech coding, speech emotion recognition, etc.
- Mathematical and perceptual speech analysis can also be used to study the cognitive and linguistic aspects of speech production and comprehension, such as the structure and meaning of language, the mechanisms and strategies of verbal and mathematical thinking, the relationship between speech and gesture, etc.



# Log–Spectral Distance

- The log-spectral distance (LSD), also referred to as log-spectral distortion or root mean square log-spectral distance, is a distance measure between two spectra .
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as p-norm:

$$
D_{LS} = \left(\frac{1}{2\pi}\int_{-\pi}^{\pi}\left[10\log_{10}\frac{P(\omega)}{P^(\omega)}\right]^p d\omega\right)^{1/p}
$$

- Unlike the Itakura–Saito distance, the log-spectral distance is symmetric .
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum .
- The log-spectral distance can be used to measure the quality of speech synthesis or speech recognition systems by comparing the spectra of the original and the synthesized or recognized speech signals.



# Cepstral Distances for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstrum is a transformation of the spectrum of a signal that reveals periodicities in the signal, such as the fundamental frequency of speech or the pitch of a musical note.
- Cepstral distance is a measure of the similarity or dissimilarity between two cepstra, which can be used to compare two speech frames, two speech signals, or two speech models .
- Cepstral distance can be computed in different ways, such as the Euclidean distance, the Mahalanobis distance, the Kullback-Leibler divergence, or the Itakura-Saito distance .
- Cepstral distance can be used for various applications in speech analysis, such as speech recognition, speaker recognition, emotion recognition, voice quality assessment, and endpoint detection  .
- Cepstral distance can be influenced by factors such as the number and type of cepstral coefficients, the window size and shape, the pre-emphasis and liftering, and the noise and distortion in the speech signals .
- Cepstral distance can be normalized or weighted to account for the perceptual relevance and variability of different cepstral coefficients, such as the mel frequency cepstral coefficients (MFCC) or the linear predictive cepstral coefficients (LPCC) .



# Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log spectrum of the signal.
- Cepstral distance is often used in speech recognition and speaker recognition systems to compare the input speech with the reference templates or models.
- A simple cepstral distance measure is the Euclidean distance between the cepstral vectors of two speech frames, but this may not be optimal for speech recognition because it does not account for the different importance and variability of the cepstral coefficients.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to the cepstral coefficients according to some criteria, such as the inverse variance, the log-index, or the perceptual relevance of the coefficients.
- A weighted cepstral distance measure can improve the performance of speech recognition systems by reducing the mismatch between the input speech and the reference templates or models, and by enhancing the discriminative power of the cepstral features.
- A weighted cepstral distance measure can be computed as follows:

  - Let x and y be two cepstral vectors of dimension N, and w be a weight vector of dimension N.
  - The weighted cepstral distance between x and y is given by:

    - d(x, y) = sqrt(sum(w_i * (x_i - y_i)^2) for i = 1 to N)

  - The weight vector w can be determined by different methods, such as:

    - Inverse variance weighting: w_i = 1 / var(x_i) or w_i = 1 / var(y_i), where var(x_i) or var(y_i) is the variance of the i-th cepstral coefficient across the training data or the reference data.
    - Log-index weighting: w_i = log(i), where i is the index of the cepstral coefficient, assuming that the lower-index coefficients are more important and less variable than the higher-index coefficients.
    - Perceptual weighting: w_i = a * e^(-b * i), where a and b are constants that control the shape of the exponential decay function, assuming that the lower-index coefficients are more perceptually relevant and less affected by noise than the higher-index coefficients.

- Filtering is a process of modifying the speech signal or the cepstral coefficients to reduce the effects of noise, channel distortion, or speaker variability, and to enhance the features that are relevant for speech recognition or speaker recognition.
- Filtering can be applied in different domains, such as the time domain, the frequency domain, or the cepstral domain, and can use different techniques, such as linear filtering, nonlinear filtering, or adaptive filtering.
- Some examples of filtering methods for speech analysis are:

  - Pre-emphasis: a high-pass filtering of the speech signal in the time domain to boost the high-frequency components and to compensate for the spectral tilt caused by the vocal tract.
  - Mel-frequency cepstral coefficients (MFCCs): a nonlinear filtering of the speech signal in the frequency domain to convert the linear spectrum into a mel-scale spectrum that mimics the human auditory system, and then applying a discrete cosine transform to obtain the cepstral coefficients.
  - Cepstral mean normalization (CMN): a linear filtering of the cepstral coefficients in the cepstral domain to subtract the mean of the cepstral coefficients from each cepstral vector, to reduce the effects of channel distortion or speaker variability.
  - Cepstral mean and variance normalization (CMVN): a linear filtering of the cepstral coefficients in the cepstral domain to subtract the mean and divide by the standard deviation of the cepstral coefficients from each cepstral vector, to reduce the effects of channel distortion or speaker variability and to normalize the dynamic range of the cepstral features.
  - Cepstral liftering: a nonlinear filtering of the cepstral coefficients in the cepstral domain to multiply each cepstral coefficient by a lifter function, such as a cosine function or a Hamming window, to emphasize or de-emphasize certain cepstral coefficients according to their importance or variability.



# Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the similarity or dissimilarity between two short-time spectra of speech signals, which are often used in speech recognition systems to compare the input speech with the stored templates or models.
- Likelihood distortions can be derived from the likelihood function of a statistical model of speech, such as the Gaussian model, which assumes that the speech spectrum follows a multivariate normal distribution.
- Likelihood distortions can be classified into two types: log likelihood ratio (LLR) and likelihood ratio (LR). The LLR distortion is defined as the negative logarithm of the LR distortion, which is the ratio of the likelihoods of the two spectra under the same model.
- LLR distortion has some desirable properties, such as being symmetric, additive, and invariant to scaling and translation of the spectra. However, LLR distortion is also sensitive to noise and spectral mismatch, and does not account for the perceptual relevance of the spectral differences.
- To overcome these limitations, some perceptually based likelihood distortions have been proposed, such as the weighted likelihood ratio (WLR) and the weighted slope metric (WSM) distortions, which incorporate some aspects of human auditory perception, such as the critical band frequency scale, the loudness function, and the masking effect.
- The performance of different likelihood distortions in speech recognition depends on various factors, such as the speech database, the feature extraction method, the template or model selection, and the recognition algorithm. Some empirical studies have shown that the LLR and WSM distortions tend to perform better than the other distortions, while the Itakura-Saito (IS) distortion, which is based on the minimum prediction error criterion, tends to perform worse  .



# Spectral Distortion Using A Warped Frequency Scale

- Spectral distortion is the difference between the original and the reconstructed spectra of a speech signal, usually measured in decibels (dB).
- Spectral distortion can affect the quality and intelligibility of speech, especially when the speech signal is processed by a low-order linear predictive coding (LPC) model or a discrete cosine transform (DCT) model.
- A warped frequency scale is a nonlinear transformation of the frequency axis that changes the resolution and spacing of the frequency bins according to some perceptual or acoustic criteria.
- A warped frequency scale can improve the spectral representation of speech by emphasizing the important features and reducing the noise effects.
- A common example of a warped frequency scale is the Bark scale, which is based on the critical band rate of the human auditory system. The Bark scale compresses the high frequencies and expands the low frequencies, reflecting the frequency resolution of the ear.
- Another example of a warped frequency scale is the Mel scale, which is based on the just noticeable differences in frequency perception. The Mel scale is similar to the Bark scale, but it has a linear segment at low frequencies and a logarithmic segment at high frequencies.
- To apply a warped frequency scale to a speech signal, one can use a frequency warping function that maps the original frequency to the warped frequency. The frequency warping function can be parameterized by a warping factor that controls the degree of warping.
- A frequency warping function can be applied to the speech signal in the time domain or in the frequency domain. In the time domain, the speech signal is resampled according to the frequency warping function, resulting in a warped speech signal with a different sampling rate. In the frequency domain, the speech signal is transformed to the warped frequency domain by a warped DCT or a warped LPC, resulting in a warped spectrum with a different number of frequency bins.
- The spectral distortion between the original and the warped spectra can be measured by various distance measures, such as the cepstral distance, the log-spectral distance, the Itakura-Saito distance, or the likelihood ratio distance. These distance measures can be modified to account for the frequency warping function and the warping factor.
- The spectral distortion using a warped frequency scale can be used for speech analysis, synthesis, recognition, and verification. By using a warped frequency scale, one can achieve a better match between the spectral features and the perceptual or acoustic characteristics of speech, and thus improve the performance and robustness of speech processing systems.



# LPC for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- LPC stands for Linear Predictive Coding, which is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model .
- LPC is the most widely used method in speech coding and speech synthesis, as it can model the human vocal tract and produce natural sounding speech with low bit rates.
- LPC analyzes the speech signal by estimating the formants, which are the resonant frequencies of the vocal tract, and removing their effects from the speech signal, and estimating the intensity and frequency of the remaining buzz, which is the source of voiced sounds.
- The process of removing the formants is called inverse filtering, and the remaining signal after the subtraction of the filtered modeled signal is called the residue.
- The residue contains the information about the pitch and the glottal pulses, which are the periodic vibrations of the vocal folds.
- The inverse filtering can be done by using a linear prediction model, which assumes that each sample of the speech signal can be approximated by a linear combination of the previous samples .
- The linear prediction model can be represented by a difference equation, which can be converted into a transfer function, which can be used to compute the reflection coefficients, which are the parameters that describe the shape of the vocal tract .
- The reflection coefficients can be converted into other equivalent representations, such as the LPC coefficients, the line spectral frequencies, or the cepstral coefficients, which can be used for different purposes, such as speech recognition, speaker identification, or speech enhancement .
- The LPC coefficients can be used to reconstruct the spectral envelope of the speech signal, which can be combined with the residue to synthesize the speech signal .
- The synthesis can be done by using a source-filter model, which assumes that the speech signal can be modeled by a source of excitation, such as a periodic pulse train for voiced sounds or a white noise for unvoiced sounds, and a filter that represents the vocal tract .
- The source-filter model can be implemented by using a synthesis filter, which is the inverse of the analysis filter, and a pitch-synchronous overlap-add (PSOLA) method, which can modify the pitch and duration of the speech signal .
- LPC analysis and synthesis can be used for various applications, such as speech compression, speech encryption, speech modification, speech enhancement, speech coding, and speech synthesis  .



# PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction, which is the computation of a set of parameters that represent the characteristics of the speech signal.
- Feature extraction methods aim to reduce the dimensionality of the speech signal and capture the relevant information for the task at hand.
- Some of the most widely used feature extraction methods for speech analysis are PLP and MFCC.

## PLP (Perceptual Linear Prediction)

- PLP is a feature extraction method that mimics the human auditory system and incorporates psychoacoustic principles.
- PLP applies a frequency warping and an equal-loudness curve to the speech spectrum, followed by an inverse Fourier transform and an autoregressive modeling.
- PLP produces a set of coefficients that represent the spectral envelope of the speech signal, which is related to the vocal tract shape and the articulation of the speaker.
- PLP is robust to noise and channel distortion, and can capture the speaker-specific and phonetic information in speech.

## MFCC (Mel Frequency Cepstral Coefficients)

- MFCC is another feature extraction method that mimics the human auditory system and incorporates psychoacoustic principles.
- MFCC applies a mel-scale filter bank to the speech spectrum, followed by a logarithmic compression and a discrete cosine transform.
- MFCC produces a set of coefficients that represent the cepstral representation of the speech signal, which is related to the spectral shape and the energy distribution of the speech signal.
- MFCC is also robust to noise and channel distortion, and can capture the speaker-specific and phonetic information in speech.

## Comparison of PLP and MFCC

- PLP and MFCC are both popular and effective feature extraction methods for speech analysis, and they have many similarities and differences.
- Similarities:
  - Both methods mimic the human auditory system and incorporate psychoacoustic principles.
  - Both methods produce a set of coefficients that represent the spectral or cepstral representation of the speech signal.
  - Both methods are robust to noise and channel distortion, and can capture the speaker-specific and phonetic information in speech.
- Differences:
  - PLP applies a frequency warping and an equal-loudness curve to the speech spectrum, while MFCC applies a mel-scale filter bank to the speech spectrum.
  - PLP performs an inverse Fourier transform and an autoregressive modeling, while MFCC performs a logarithmic compression and a discrete cosine transform.
  - PLP coefficients represent the spectral envelope of the speech signal, while MFCC coefficients represent the cepstral representation of the speech signal.
  - PLP coefficients are more correlated than MFCC coefficients, and may require further processing such as cepstral or linear discriminant analysis.



# Time Alignment And Normalization for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Time alignment is the process of finding the correspondence between the frames of two speech signals, usually from different speakers or different utterances.
- Time alignment is useful for many applications of speech analysis, such as speech recognition, text-to-speech conversion, voice conversion, speaker verification, and speech synthesis.
- Time alignment can be done by using methods such as dynamic time warping (DTW), hidden Markov models (HMMs), or neural networks.
- Time alignment can be improved by using some modifications to DTW, such as adding constraints, penalties, or weights to the alignment path, or using multiple features or multiple reference signals.
- Normalization is the process of reducing the variability of speech signals due to factors such as speaker, channel, environment, or recording conditions.
- Normalization can be done in different domains, such as amplitude, frequency, or time.
- Normalization can be done by using methods such as automatic gain control, automatic spectrum normalization, cepstral mean subtraction, vocal tract length normalization, or speaker adaptation.
- Normalization can improve the performance of speech analysis systems by making the speech signals more comparable and consistent.



# Dynamic Time Warping for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Dynamic Time Warping (DTW) is an algorithm for measuring similarity between two temporal sequences, which may vary in speed or length.
- DTW can be used for speech recognition, data mining, financial markets, and other domains where temporal alignment is important.
- DTW works by finding the optimal alignment between two sequences, such that the distance between them is minimized.
- DTW uses a dynamic programming approach to compute a matrix of distances between all possible pairs of elements from the two sequences.
- DTW then finds the optimal path through the matrix, which corresponds to the best alignment.
- DTW can handle different types of distortions, such as stretching, shrinking, shifting, or skipping of elements in the sequences.
- DTW can also be extended to handle multiple sequences, multidimensional sequences, or sequences with different features.
- DTW can be improved by using different distance measures, pruning techniques, or constraints to reduce the computational complexity and improve the accuracy.
- DTW is a powerful and flexible technique for comparing temporal sequences, but it also has some limitations, such as sensitivity to noise, lack of robustness to outliers, or difficulty in interpreting the results.



# Multiple Time – Alignment Paths for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications of speech analysis, such as speech recognition, speech synthesis, voice conversion, speech enhancement, and speech to lips synchronization  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or temporal variations .
- One common technique for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the cumulative distance between the frames.
- DTW can be implemented using various algorithms, such as the classical dynamic programming, the ordered graph search, or the multiview temporal alignment by dependence maximization in the latent space .
- DTW can also be modified or extended to handle different types of time series, such as non-parallel, multi-modal, or multi-channel data .
- Multiple time-alignment paths are possible when there are multiple ways to align two time series with similar distances or costs.
- Multiple time-alignment paths can be useful for finding alternative or robust alignments, or for exploring the variability or diversity of the time series.
- Multiple time-alignment paths can be obtained by using different algorithms, such as the N-best DTW, the multiple path DTW, or the probabilistic DTW.
- Multiple time-alignment paths can also be evaluated or compared using different criteria, such as the alignment accuracy, the alignment diversity, or the alignment consistency.



# Unit 7 - SPEECH MODELING

- Speech modeling is the process of using speech and language to help the development of speech and language skills in others, especially children or users of augmentative and alternative communication (AAC) tools .
- Speech modeling can be used for different purposes, such as:
  - Teaching new words, phrases, or sentence structures
  - Expanding vocabulary and grammar
  - Encouraging communication and interaction
  - Providing feedback and reinforcement
  - Correcting errors or misconceptions
- Speech modeling can be done in various ways, such as:
  - Imitating the target speech or language
  - Expanding or extending the target speech or language
  - Recasting or reformulating the target speech or language
  - Prompting or eliciting the target speech or language
  - Narrating or describing the target speech or language
- Speech modeling can be applied to various domains, such as:
  - Speech recognition: the task of converting speech signals into text or commands
  - Speech synthesis: the task of generating speech signals from text or commands
  - Natural language processing: the task of understanding and generating natural language from speech or text
  - Speech translation: the task of translating speech from one language to another
- Speech modeling can be enhanced by using machine learning techniques, such as:
  - Neural networks: a type of artificial intelligence that can learn from data and perform complex tasks
  - Universal speech model: a family of state-of-the-art speech models that can recognize and understand speech across different languages and accents 
  - Neural text to speech: a type of speech synthesis that can produce realistic and expressive voices



# Hidden Markov Models for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- A hidden Markov model (HMM) is a statistical model that can be used to represent the probabilistic behavior of a system that undergoes transitions between a finite set of states, where each state is associated with a probability distribution over a finite set of observations.
- HMMs are widely used for speech recognition, speech synthesis, speech segmentation, speech enhancement, and speech coding.
- HMMs can capture the temporal and sequential dependencies of speech signals, as well as the variability and uncertainty of speech production and perception.
- HMMs consist of three main components: states, observations, and parameters.
  - States are the discrete variables that represent the underlying states of the system. Each state has a self-transition probability and a transition probability to other states. The sequence of states is called the state sequence or the hidden sequence, and it is not directly observable.
  - Observations are the discrete or continuous variables that represent the observable outputs of the system. Each observation is generated by a state according to a probability distribution that depends on the state. The sequence of observations is called the observation sequence or the visible sequence, and it is the only available data for HMMs.
  - Parameters are the numerical values that define the HMM, such as the number of states, the number of observations, the initial state probabilities, the state transition probabilities, and the observation probabilities. The parameters can be estimated from training data using various methods, such as the maximum likelihood estimation or the expectation-maximization algorithm.
- HMMs can be used to perform three main tasks: evaluation, decoding, and learning.
  - Evaluation is the task of computing the probability of an observation sequence given an HMM. This can be done efficiently using the forward algorithm or the backward algorithm, which are dynamic programming techniques that exploit the Markov property and the independence assumptions of HMMs.
  - Decoding is the task of finding the most likely state sequence given an observation sequence and an HMM. This can be done using the Viterbi algorithm, which is another dynamic programming technique that finds the optimal path through the state space.
  - Learning is the task of estimating the parameters of an HMM given a set of observation sequences. This can be done using the Baum-Welch algorithm, which is an iterative method that applies the expectation-maximization algorithm to HMMs. The algorithm alternates between computing the expected counts of state transitions and observations (E-step) and updating the parameters to maximize the likelihood of the data (M-step).
- HMMs can be extended and modified in various ways to improve their performance and applicability, such as using multiple observation streams, multiple mixture components, continuous density functions, hierarchical structures, context-dependent states, and discriminative training criteria.



# Markov Processes

- A Markov process is a random process indexed by time, and with the property that the future is independent of the past, given the present.
- Markov processes are the natural stochastic analogs of the deterministic processes described by differential and difference equations.
- Markov processes are often applicable to decision problems, where the states represent the possible outcomes and the probabilities represent the likelihood of transitions between the states.
- Markov processes can be classified into discrete-time and continuous-time, depending on whether the time index is discrete or continuous.
- Discrete-time Markov processes are also called Markov chains, and they are characterized by a transition matrix that gives the probabilities of moving from one state to another in one time step.
- Continuous-time Markov processes are characterized by a transition rate matrix that gives the rates of transitions between states per unit time.
- Examples of discrete-time Markov processes are the partial sum process associated with a sequence of independent, identically distributed random variables, and the weather process that models the daily changes in weather conditions.
- Examples of continuous-time Markov processes are the diffusion processes that model the random motion of particles, and the Poisson and Wiener processes that model the occurrence of events over time.



# HMMs for Speech Modeling

- Hidden Markov Models (HMMs) are a statistical model that consists of two components: a set of hidden states, and a set of observations .
- Each hidden state has a probability distribution over the possible observations, and each observation is assumed to be generated by one of the hidden states .
- The hidden states form a Markov chain, meaning that the current state depends only on the previous state .
- HMMs can be used to model sequential data, such as speech signals, by assuming that the speech signal is a sequence of observations generated by an underlying HMM   .
- Speech recognition is the task of converting a speech signal into a textual representation, such as a word or a sentence .
- HMMs can be used for speech recognition by finding the most likely sequence of hidden states that corresponds to a given speech signal, and then mapping the hidden states to the corresponding words or phonemes   .
- HMMs have some advantages for speech recognition, such as:
  - They can capture the temporal dynamics and variability of speech .
  - They can be trained from data using efficient algorithms, such as the Baum-Welch algorithm or the Viterbi algorithm    .
  - They can handle noisy or incomplete data by using probabilistic inference  .
  - They can be combined with other models, such as language models or acoustic models, to improve the performance of speech recognition   .
- HMMs also have some disadvantages for speech recognition, such as:
  - They make some unrealistic assumptions, such as the independence of observations given the hidden states, or the stationarity of the state transition probabilities  .
  - They have a high computational complexity, especially for large vocabulary continuous speech recognition (LVCSR) systems, which require a large number of hidden states and observations   .
  - They have a limited expressive power, meaning that they cannot capture some complex features or dependencies of speech, such as prosody, coarticulation, or context  .
  - They are sensitive to the choice of parameters, such as the number of hidden states, the observation features, or the initialization of the model  .



# Evaluation for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Speech modeling is the process of representing speech signals in a mathematical or statistical way, such as using acoustic features, phonetic units, or word sequences.
- Speech modeling can be used for various applications, such as speech recognition, speech synthesis, speech enhancement, speech compression, speech analysis, and speech translation.
- Speech modeling can be divided into two main categories: parametric and non-parametric models.
  - Parametric models assume that speech signals follow a certain distribution or structure, and use a finite set of parameters to describe them. Examples of parametric models are linear predictive coding (LPC), hidden Markov models (HMMs), and deep neural networks (DNNs).
  - Non-parametric models do not make any assumptions about the underlying distribution or structure of speech signals, and use data-driven methods to learn them from a large corpus of speech data. Examples of non-parametric models are Gaussian mixture models (GMMs), dynamic time warping (DTW), and support vector machines (SVMs).
- Speech modeling can also be classified based on the level of abstraction or granularity of the speech units, such as waveform, spectral, cepstral, phonetic, syllabic, lexical, or semantic.
  - Waveform models operate on the raw speech signals, and try to preserve the temporal and amplitude information of the speech waveforms. Examples of waveform models are waveform interpolation (WI) and waveform coding (WC).
  - Spectral models operate on the frequency domain representation of speech signals, and try to capture the spectral envelope and fine structure of the speech spectra. Examples of spectral models are Fourier transform (FT), discrete cosine transform (DCT), and mel-frequency cepstral coefficients (MFCCs).
  - Cepstral models operate on the logarithmic representation of speech spectra, and try to separate the source and filter components of speech production. Examples of cepstral models are linear predictive cepstral coefficients (LPCCs), perceptual linear prediction (PLP), and mel-frequency cepstral coefficients (MFCCs).
  - Phonetic models operate on the discrete units of speech sounds, such as vowels, consonants, and diphthongs, and try to capture the articulatory and acoustic characteristics of speech production. Examples of phonetic models are phonetic decision trees, phonetic feature vectors, and phonetic hidden Markov models (PHMMs).
  - Syllabic models operate on the units of speech rhythm, such as syllables, stress, and intonation, and try to capture the prosodic and suprasegmental features of speech. Examples of syllabic models are syllable-based hidden Markov models (SHMMs), syllable-based neural networks (SNNs), and syllable-based prosody models (SPMs).
  - Lexical models operate on the units of speech meaning, such as words, phrases, and sentences, and try to capture the lexical and syntactic features of speech. Examples of lexical models are n-gram language models, statistical parsing models, and neural network language models (NNLMs).
  - Semantic models operate on the units of speech understanding, such as concepts, topics, and intents, and try to capture the semantic and pragmatic features of speech. Examples of semantic models are latent semantic analysis (LSA), topic models, and dialogue models.



# Optimal State Sequence for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Speech modeling is the process of representing speech signals as sequences of discrete symbols or states, such as phonemes, words, or sentences.
- Speech modeling is useful for speech recognition, speech synthesis, speech enhancement, and speech analysis.
- One of the most common speech models is the hidden Markov model (HMM), which is a probabilistic model that assumes that the speech signal is generated by a stochastic process that transitions between a finite number of hidden states, each emitting an observable output.
- The optimal state sequence is the most likely sequence of hidden states that explains the observed speech signal, given the HMM parameters and the prior probabilities of the states.
- The optimal state sequence can be decoded using various algorithms, such as the Viterbi algorithm, the forward-backward algorithm, or the expectation-maximization (EM) algorithm.
- The optimal state sequence can be used for various purposes, such as:
  - Aligning the speech signal with the corresponding transcription or annotation, which is useful for speech recognition and speech synthesis training.
  - Segmenting the speech signal into smaller units, such as phonemes, syllables, or words, which is useful for speech analysis and speech synthesis.
  - Extracting features or parameters from the speech signal, such as pitch, energy, or spectral coefficients, which can be used for speech enhancement, speech synthesis, or speech recognition.
  - Modifying or transforming the speech signal, such as changing the speaker identity, the emotion, or the accent, which can be done by mapping the optimal state sequence from one HMM to another HMM.
- The optimal state sequence can be improved by incorporating additional information or constraints, such as:
  - The context or the history of the previous or the following states, which can capture the temporal dependencies and the coarticulation effects in speech.
  - The linguistic or the semantic information, such as the grammar, the syntax, or the meaning of the speech, which can reduce the ambiguity and the errors in speech recognition or speech synthesis.
  - The prosodic or the expressive information, such as the stress, the intonation, or the emphasis of the speech, which can enhance the naturalness and the intelligibility of speech synthesis or speech recognition.
  - The statistical or the variational information, such as the posterior probabilities, the confidence scores, or the regularization terms, which can smooth the state likelihoods and avoid overfitting or underfitting the speech signal .



# Viterbi Search for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Speech modeling is the process of representing speech signals using mathematical models, such as hidden Markov models (HMMs), that capture the statistical properties of speech sounds and their sequences.
- Speech recognition is the task of converting speech signals into text or commands, using speech models and algorithms that search for the best matching sequence of words or phonemes.
- Viterbi search is a widely used algorithm for speech recognition, based on the Viterbi algorithm, which is a dynamic programming technique for finding the most likely sequence of hidden states in a Markov process, given a sequence of observations.
- The Viterbi search algorithm works as follows :
  - Create a state list with one cell for each state in the speech model, such as an HMM.
  - Initialize the state list with the initial states for the first observation frame, and assign them the initial probabilities and back pointers.
  - For each subsequent observation frame, clear the state list and compute the transitions from the previous state list, using the observation likelihoods and the transition probabilities.
  - If a new state is reached, update its score and back pointer with the best previous state and its score.
  - If an existing state is reached, compare its score with the new score from the previous state, and update it if the new score is better, along with the back pointer.
  - Repeat this process until the last observation frame is processed, and then trace back the best path from the final state list, using the back pointers.
- The Viterbi search algorithm can be applied to different levels of speech modeling, such as word-level, phoneme-level, or feature-level  .
  - At the word-level, the speech model consists of a set of word HMMs, each representing a word in the vocabulary, and the Viterbi search algorithm finds the best sequence of words that matches the speech signal.
  - At the phoneme-level, the speech model consists of a set of phoneme HMMs, each representing a basic speech sound, and the Viterbi search algorithm finds the best sequence of phonemes that matches the speech signal.
  - At the feature-level, the speech model consists of a set of feature HMMs, each representing a distinctive acoustic feature, such as voicing, nasality, or frication, and the Viterbi search algorithm finds the best sequence of features that matches the speech signal.
- The Viterbi search algorithm has several advantages for speech recognition, such as :
  - It is efficient and optimal, as it avoids exhaustive search and guarantees to find the best path in polynomial time.
  - It is robust and flexible, as it can handle noisy and incomplete observations, and can be adapted to different speech models and constraints.
  - It is scalable and modular, as it can be applied to large vocabularies and complex models, and can be combined with other techniques, such as pruning, beam search, or n-gram language models.



# Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a Hidden Markov Model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulas.
- The forward-backward procedure computes the posterior probabilities of the hidden states given the observations, using the current parameters of the HMM.
- The re-estimation formulas update the parameters of the HMM using the posterior probabilities computed in the previous step.
- The re-estimation formulas are derived by applying the principle of maximum likelihood, which aims to maximize the probability of the observations given the model.
- The re-estimation formulas depend on the type of HMM, such as discrete or continuous, and the type of distribution used to model the observation probabilities, such as multinomial or Gaussian.
- The re-estimation formulas for the discrete HMM with multinomial observation probabilities are as follows :

  - The initial state probabilities are re-estimated as the expected frequency of being in state 1 at time 1, averaged over all observation sequences.
  - The state transition probabilities are re-estimated as the expected number of transitions from state i to state j, divided by the expected number of transitions from state i, averaged over all observation sequences.
  - The observation probabilities are re-estimated as the expected number of times state i emits symbol k, divided by the expected number of times state i is visited, averaged over all observation sequences.

- The re-estimation formulas for the continuous HMM with Gaussian observation probabilities are as follows:

  - The initial state probabilities are re-estimated as the expected frequency of being in state 1 at time 1, averaged over all observation sequences.
  - The state transition probabilities are re-estimated as the expected number of transitions from state i to state j, divided by the expected number of transitions from state i, averaged over all observation sequences.
  - The mean vectors are re-estimated as the weighted average of the observation vectors, where the weights are the posterior probabilities of being in state i, averaged over all observation sequences.
  - The covariance matrices are re-estimated as the weighted average of the squared deviations of the observation vectors from the mean vectors, where the weights are the posterior probabilities of being in state i, averaged over all observation sequences.

- The Baum-Welch algorithm can be applied to train HMMs for various applications, such as speech recognition, speech synthesis, speech segmentation, and speech modeling.



# Implementation Issues for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Speech modeling is the process of representing speech signals in a mathematical or statistical way, such as using acoustic features, phonetic units, or word sequences.
- Speech modeling is essential for natural language processing (NLP) applications that involve speech recognition, speech synthesis, speech translation, speech emotion analysis, etc.
- Some of the implementation issues for speech modeling are:

  - Choosing the appropriate level of abstraction for the speech representation, such as waveform, spectrum, cepstrum, or feature vectors.
  - Choosing the appropriate unit of analysis for the speech modeling, such as phonemes, syllables, words, or sentences.
  - Choosing the appropriate modeling technique for the speech representation, such as hidden Markov models, neural networks, deep learning, or probabilistic graphical models.
  - Choosing the appropriate evaluation metric for the speech modeling, such as accuracy, error rate, perplexity, or likelihood.
  - Dealing with the variability and uncertainty of speech signals, such as noise, speaker, accent, dialect, emotion, or context.
  - Dealing with the complexity and scalability of speech modeling, such as computational cost, memory requirement, data availability, or domain adaptation.

