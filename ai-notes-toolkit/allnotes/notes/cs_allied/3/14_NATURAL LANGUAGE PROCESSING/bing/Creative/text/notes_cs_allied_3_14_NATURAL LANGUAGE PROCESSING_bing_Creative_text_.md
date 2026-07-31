

# NATURAL LANGUAGE PROCESSING

- Natural language processing (NLP) is a subfield of artificial intelligence (AI) that deals with the interactions between computers and human language .
- NLP helps machines process and understand the human language so that they can automatically perform repetitive tasks .
- Examples of NLP applications include machine translation, summarization, ticket classification, spell check, sentiment analysis, chatbots, and speech recognition .
- NLP combines computational linguistics, which is the rule-based modeling of human language, with statistical, machine learning, and deep learning methods, which are data-driven approaches to learn from large amounts of text and speech data .
- NLP faces many challenges, such as ambiguity, diversity, and complexity of natural language, as well as the need for domain knowledge, common sense, and world knowledge to understand the context and meaning of human communication.
- NLP is a rapidly evolving and expanding field, with new research, applications, and tools emerging every day. NLP is also closely related to other disciplines, such as natural language generation, natural language understanding, information retrieval, text mining, and knowledge representation and reasoning.



## Unit 1 - INTRODUCTION

- This unit introduces the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and software that can perform tasks that normally require human intelligence, such as reasoning, learning, planning, decision making, natural language processing, computer vision, etc.
- AI can be classified into two main categories: weak AI and strong AI.
  - Weak AI, also known as narrow AI, is the type of AI that can perform specific tasks or solve specific problems, but does not have general intelligence or understanding of the world. Examples of weak AI include speech recognition, face recognition, chess playing, etc.
  - Strong AI, also known as artificial general intelligence (AGI), is the type of AI that can perform any intellectual task that a human can, and has human-like consciousness, self-awareness, and common sense. Examples of strong AI include HAL 9000 from 2001: A Space Odyssey, Data from Star Trek, etc. Strong AI is still a hypothetical and controversial concept, and has not been achieved yet.
- AI can also be classified into two main approaches: symbolic AI and sub-symbolic AI.
  - Symbolic AI, also known as classical AI or rule-based AI, is the type of AI that uses symbols and rules to represent and manipulate knowledge. Symbolic AI relies on logic, search, and knowledge representation and reasoning techniques to solve problems. Examples of symbolic AI include expert systems, theorem provers, natural language understanding, etc.
  - Sub-symbolic AI, also known as connectionist AI or neural network AI, is the type of AI that uses numerical values and mathematical operations to model complex phenomena. Sub-symbolic AI relies on learning, adaptation, and emergence to solve problems. Examples of sub-symbolic AI include artificial neural networks, evolutionary algorithms, fuzzy logic, etc.
- AI can also be classified into two main goals: human-inspired AI and human-imitative AI.
  - Human-inspired AI, also known as cognitive AI or artificial psychology, is the type of AI that tries to understand and model the mechanisms and processes of human cognition, such as perception, memory, attention, emotion, etc. Human-inspired AI aims to create machines and software that can think and behave like humans, but not necessarily in the same way. Examples of human-inspired AI include cognitive architectures, cognitive robotics, artificial neural networks, etc.
  - Human-imitative AI, also known as artificial intelligence engineering or artificial intelligence applications, is the type of AI that tries to replicate and surpass the performance and capabilities of humans in specific domains, such as games, medicine, education, etc. Human-imitative AI aims to create machines and software that can do what humans can do, but better, faster, or cheaper. Examples of human-imitative AI include chess playing, speech recognition, face recognition, etc.



### Origins and challenges of NLP

- Natural language processing (NLP) is a field of computer science, artificial intelligence (also called machine learning), and linguistics concerned with the interactions between computers and human (natural) languages.
- The origins of NLP can be traced back to the early attempts to use computers for translating natural languages, such as the Georgetown experiment in 1954, which translated 60 Russian sentences into English.
- The history of NLP also comes from many other sources, such as linguistics, psychology, philosophy, logic, mathematics, and cognitive science. Some of the influential figures in the development of NLP include Noam Chomsky, Alan Turing, Marvin Minsky, John McCarthy, and Richard Montague.
- The main goal of NLP is to enable computers to understand, generate, and communicate natural language, as well as to perform tasks that require natural language processing, such as information retrieval, text summarization, sentiment analysis, question answering, dialogue systems, and speech recognition.
- The challenges of NLP stem from the complexity, diversity, ambiguity, and dynamism of natural language, as well as the limitations of current algorithms and data sources . Some of the major challenges of NLP include:
  - Dealing with the sparsity, high dimensionality, and noise of natural language data, which require efficient and robust methods for feature extraction, representation, and selection .
  - Handling the syntactic, semantic, pragmatic, and discourse aspects of natural language, which involve multiple levels of analysis and interpretation, as well as common sense and world knowledge .
  - Adapting to the variability, diversity, and evolution of natural language, which require flexible and scalable methods for learning from heterogeneous and dynamic data sources, such as social media, web pages, and speech .
  - Evaluating the performance and quality of NLP systems, which require appropriate metrics, benchmarks, and human feedback, as well as ethical and social considerations .
- The power of NLP lies in its potential to enable new applications and insights that can benefit various domains and industries, such as education, health care, business, entertainment, and social good. Some of the current and future applications of NLP include:
  - Enhancing human-computer interaction and communication, such as through voice assistants, chatbots, and conversational agents.
  - Extracting and synthesizing information and knowledge from large and diverse text and speech data, such as through search engines, recommender systems, and summarizers.
  - Analyzing and generating natural language, such as through sentiment analysis, text classification, natural language generation, and machine translation.
  - Improving and supporting human learning and decision making, such as through educational technology, natural language understanding, and natural language inference.



### Language Modeling for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Language modeling is the task of estimating the probability of a sequence of words or symbols in a natural language .
- Language models are statistical tools that analyze the pattern of human language for the prediction of words.
- Language models are the core component of modern natural language processing (NLP), which is the branch of computer science and artificial intelligence concerned with giving computers the ability to understand text and spoken words .
- Language models have a large number of applications in NLP, such as speech recognition, machine translation, text summarization, text generation, question answering, sentiment analysis, spam filtering, etc.  .
- Language models can be classified into two types: n-gram models and neural models .
- N-gram models are based on counting the frequency of n consecutive words or symbols in a large corpus of text, and using the chain rule of probability to estimate the probability of the next word or symbol given the previous n-1 words or symbols.
- Neural models are based on using deep neural networks, such as recurrent neural networks (RNNs), long short-term memory (LSTM), gated recurrent units (GRU), transformers, etc., to learn the probability distribution of the next word or symbol given the previous words or symbols in a sequence.
- Neural models have the advantage of being able to capture long-range dependencies and semantic relationships between words or symbols, and being able to generate more fluent and coherent text than n-gram models.
- However, neural models also have some challenges, such as requiring large amounts of data and computational resources, being prone to overfitting and generating repetitive or nonsensical text, and being difficult to interpret and explain.



### Grammar-based LM for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A language model (LM) is a mathematical representation of the probability of a sequence of words or symbols in a natural language .
- A LM can be used to generate or evaluate natural language sentences, such as in speech recognition, machine translation, spelling correction, text summarization, etc .
- A grammar-based LM is a type of LM that uses the rules and structure of a natural language to estimate the probability of a sentence.
- A grammar-based LM can be formal or probabilistic, depending on whether it uses deterministic or stochastic methods to assign probabilities .
- A formal grammar-based LM is based on the grammar and parsing of a natural language, where grammar checks the permissible structure of the sentence and parsing analyses the sentence to check whether the structure is compliant with the grammar.
- A formal grammar-based LM can be context-free or context-sensitive, depending on whether the rules of the grammar depend on the surrounding context or not.
- A probabilistic grammar-based LM is based on the statistical analysis of a large corpus of natural language text, where the probability of a sentence is estimated from the frequency of its occurrence or its subparts in the corpus .
- A probabilistic grammar-based LM can be n-gram or neural, depending on whether it uses fixed-length or variable-length sequences of words to estimate the probability of the next word .
- A n-gram probabilistic grammar-based LM is based on the Markov assumption, which states that the probability of the next word depends only on the previous n-1 words, where n is the order of the model .
- A neural probabilistic grammar-based LM is based on the use of artificial neural networks, which learn the distributed representations of words and their contexts from the corpus and use them to estimate the probability of the next word .



### Statistical Language Model for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A statistical language model (SLM) is a mathematical tool that assigns probabilities to sequences of words or symbols in a natural language, such as English, Chinese, or Hindi.
- SLMs are used to generate or analyze natural language texts for various applications, such as speech recognition, machine translation, natural language generation, information retrieval, and text summarization.
- SLMs are based on the assumption that the probability of a word or symbol depends on its previous words or symbols, or its context. For example, the probability of the word "apple" is higher after the word "red" than after the word "blue".
- SLMs can be classified into two main types: n-gram models and neural network models.
- N-gram models are the simplest and most widely used SLMs. They estimate the probability of a word or symbol based on the previous n-1 words or symbols, where n is a fixed number. For example, a bigram model (n=2) estimates the probability of a word based on the previous word, while a trigram model (n=3) estimates the probability of a word based on the previous two words.
- Neural network models are more complex and powerful SLMs. They use artificial neural networks to learn the probability distribution of words or symbols from large amounts of text data. They can capture long-range dependencies and semantic similarities between words or symbols, which n-gram models cannot. For example, a neural network model can learn that the word "apple" is more likely to appear after the word "fruit" than after the word "animal".
- SLMs are the core component of modern natural language processing (NLP), which is the automatic manipulation of natural languages that provides machines with the ability to read, understand, and derive meaning from human languages. NLP changes many industries for the better, such as education, healthcare, entertainment, and e-commerce.



### Regular Expressions

- Regular expressions are a powerful and concise way of specifying patterns of text, such as words, characters, or symbols.
- Regular expressions can be used for various tasks in natural language processing, such as tokenization, stemming, lemmatization, spelling correction, text normalization, and information extraction.
- Regular expressions are composed of literals and metacharacters. Literals are characters that match themselves, such as `a`, `b`, or `c`. Metacharacters are characters that have special meanings, such as `*`, `+`, `?`, `|`, `^`, `$`, `.`, `[`, `]`, `(`, `)`, `{`, `}`, and `\`.
- Metacharacters can be used to specify different types of patterns, such as:
  - Alternation: `|` means "or", and can be used to match any one of the alternatives, such as `cat|dog` matches either `cat` or `dog`.
  - Repetition: `*` means "zero or more", `+` means "one or more", and `?` means "zero or one". They can be used to match repeated occurrences of a pattern, such as `a*` matches zero or more `a`s, `a+` matches one or more `a`s, and `a?` matches zero or one `a`.
  - Grouping: `(` and `)` can be used to group a subpattern and treat it as a single unit, such as `(ab)+` matches one or more repetitions of `ab`.
  - Character classes: `[` and `]` can be used to specify a set of characters to match, such as `[aeiou]` matches any vowel, and `[^aeiou]` matches any non-vowel. Ranges of characters can also be specified, such as `[a-z]` matches any lowercase letter, and `[0-9]` matches any digit.
  - Anchors: `^` and `$` can be used to match the beginning and the end of a string, respectively, such as `^a` matches any string that starts with `a`, and `a$` matches any string that ends with `a`.
  - Wildcard: `.` can be used to match any single character, except for the newline character `\n`, such as `a.b` matches any three-character string that starts with `a` and ends with `b`.
  - Escape: `\` can be used to escape the special meaning of a metacharacter and match it literally, such as `\.` matches a dot, and `\\` matches a backslash.
- Regular expressions can also be modified by flags, which are options that change the behavior of the matching process, such as:
  - Case-insensitive: `i` makes the matching case-insensitive, such as `a` matches both `a` and `A`.
  - Dotall: `s` makes the dot `.` match any character, including the newline `\n`, such as `a.b` matches any three-character string that starts with `a` and ends with `b`, even if `b` is on a new line.
  - Multiline: `m` makes the anchors `^` and `$` match the beginning and the end of each line, rather than the whole string, such as `^a` matches any line that starts with `a`, and `a$` matches any line that ends with `a`.
  - Unicode: `u` makes the regular expression use Unicode character properties, such as `\w` matches any Unicode word character, and `\d` matches any Unicode digit character.
- Regular expressions can be implemented in various programming languages, such as Python, Java, Perl, and Ruby, using built-in or external libraries or modules. Each language may have slightly different syntax and features for regular expressions, so it is important to consult the documentation for the specific language and library.



### Finite-State Automata for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Finite-state automata (FSA) are abstract machines that can recognize and generate patterns of symbols, such as words, sentences, or phonetic sequences .
- FSA have a finite number of states, and can change from one state to another based on the input symbol and a transition function .
- FSA can be deterministic (DFA) or non-deterministic (NFA). DFA have exactly one transition for each input symbol and state, while NFA can have zero, one, or more transitions for each input symbol and state .
- FSA can be used to model various aspects of natural language processing (NLP), such as morphology, syntax, phonology, and semantics  .
- FSA can also be extended to finite-state transducers (FST), which can produce an output symbol along with changing the state for each input symbol .
- FST can be used to perform various transformations and operations on natural language, such as tokenization, stemming, lemmatization, spelling correction, transliteration, and translation  .
- FSA and FST have several advantages in NLP, such as efficiency, modularity, compositionality, and transparency .
- FSA and FST also have some limitations in NLP, such as inability to handle long-distance dependencies, recursion, and ambiguity .



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content in markdown format on the topic of English Morphology for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING. Here is what I have written:

### English Morphology

- Morphology is the study of the internal structure and formation of words in a language.
- Words are composed of smaller units called morphemes, which are the smallest meaningful units in a language.
- Morphemes can be classified into two types: free and bound.
  - Free morphemes can stand alone as words, such as cat, dog, happy, etc.
  - Bound morphemes cannot stand alone as words, but must be attached to other morphemes, such as -s, -ed, -ing, etc.
- Morphemes can also be classified into two types based on their function: roots and affixes.
  - Roots are the core of the word, carrying the main meaning and lexical category, such as cat, dog, happy, etc.
  - Affixes are the modifiers of the word, changing its meaning or grammatical function, such as -s, -ed, -ing, etc.
- Affixes can be further classified into four types based on their position and function: prefixes, suffixes, infixes and circumfixes.
  - Prefixes are affixes that are attached to the beginning of the root, such as un-, re-, pre-, etc.
  - Suffixes are affixes that are attached to the end of the root, such as -s, -ed, -ing, etc.
  - Infixes are affixes that are inserted into the root, such as -um- in flummoxed, -iz- in realizability, etc.
  - Circumfixes are affixes that are attached to both the beginning and the end of the root, such as en-...-en in enlighten, be-...-ed in beloved, etc.
- The process of combining morphemes to form words is called word formation. There are different types of word formation processes, such as derivation, compounding, conversion, blending, clipping, acronymy, etc.
  - Derivation is the process of creating new words by adding affixes to existing words, such as happy + -ness = happiness, teach + -er = teacher, etc.
  - Compounding is the process of creating new words by combining two or more existing words, such as blackboard, snowman, toothbrush, etc.
  - Conversion is the process of creating new words by changing the lexical category of existing words, such as noun to verb (bottle, google, etc.), verb to noun (run, cut, etc.), adjective to noun (poor, rich, etc.), etc.
  - Blending is the process of creating new words by combining parts of two or more existing words, such as brunch (breakfast + lunch), smog (smoke + fog), motel (motor + hotel), etc.
  - Clipping is the process of creating new words by shortening existing words, such as phone (telephone), gym (gymnasium), flu (influenza), etc.
  - Acronymy is the process of creating new words by using the initial letters of a phrase or a name, such as NASA (National Aeronautics and Space Administration), AIDS (Acquired Immune Deficiency Syndrome), LOL (Laugh Out Loud), etc.

I hope this content is helpful for you. If you have any questions or feedback, please let me know.😊



### Transducers for lexicon

- A transducer is a device or a model that converts one form of data into another. In natural language processing (NLP), a transducer can be used to map between different levels of linguistic representation, such as surface forms and lexical forms  .
- A surface form is the actual word that appears in a text, such as "dogs". A lexical form is the abstract representation of a word that includes its lemma and morphological features, such as "dog+N+PL". A transducer can convert a surface form to a lexical form, or vice versa, depending on the direction of the mapping.
- A lexical transducer is a special type of finite-state transducer (FST) that performs the mapping between surface forms and lexical forms. An FST is a finite-state automaton (FSA) that has two tapes, one for input and one for output, and a set of rules that define how to read from one tape and write to the other. An FSA is a mathematical model of computation that has a finite number of states and transitions between them  .
- A lexical transducer can be constructed using regular expressions and rewrite rules that capture the morphological patterns of a language. For example, a rule that adds an "s" to a noun to form its plural can be written as: N -> N + "s" / _#. This rule means that a noun (N) can be rewritten as itself (N) followed by an "s" when it occurs at the end of a word (_#). A lexical transducer can apply this rule in either direction, depending on the input and output tapes .
- A lexical transducer can be used for various NLP tasks, such as morphological analysis, morphological generation, spelling correction, text normalization, and finite-state parsing. Morphological analysis is the task of converting a surface form to a lexical form, while morphological generation is the reverse. Spelling correction is the task of finding and correcting spelling errors in a text, using a lexicon and a set of rules. Text normalization is the task of converting non-standard or noisy text, such as SMS messages or tweets, to a standard form. Finite-state parsing is the task of analyzing the syntactic structure of a sentence, using a grammar that is represented as an FST  .
- A lexical transducer can be composed with other FSTs to form a more complex transducer that performs multiple tasks. For example, a virtual keyboard pipeline, used for decoding on mobile devices, can consist of a context dependency transducer C, a lexicon L, and an n-gram language model G. A bikey C transducer maps between two consecutive key presses and a set of possible words. A lexicon L transducer maps between words and their lexical forms. An n-gram language model G transducer assigns probabilities to sequences of words. The composition of these three transducers, C o L o G, can be used to predict the most likely word or phrase given a sequence of key presses .



### Tokenization

- Tokenization is the process of breaking down a piece of text into small units called tokens   .
- A token may be a word, part of a word or just characters like punctuation.
- Tokenization is the first step in any NLP pipeline. It has an important effect on the rest of the pipeline.
- A tokenizer breaks unstructured data and natural language text into chunks of information that can be considered as discrete elements.
- The token occurrences in a document can be used directly as a vector representing that document.
- Tokenization is useful for a number of tasks in natural language processing, including sentiment analysis, topic modeling, and machine translation.
- One of the main advantages of tokenization is that it can help to improve the accuracy of these tasks by providing more context for each word.
- Tokenization is a crucial step in many NLP tasks, such as part-of-speech tagging and text classification.
- Tokenization is also used in speech recognition, where it means splitting up speech into words or sentences.
- Tokenization is a difficult task, because every language has its own grammatical constructs, which are often difficult to write down as rules.
- There are different types of tokenization, such as word tokenization, sentence tokenization, subword tokenization, and character tokenization .
- Word tokenization is the process of splitting a text into words based on whitespace and punctuation.
- Sentence tokenization is the process of splitting a text into sentences based on punctuation and capitalization.
- Subword tokenization is the process of splitting a word into smaller units based on morphology or frequency .
- Character tokenization is the process of splitting a text into individual characters.
- There are different challenges in tokenization, such as handling abbreviations, contractions, hyphenated words, compound words, and multi-word expressions .
- There are different tools and libraries for tokenization, such as NLTK, spaCy, Stanford CoreNLP, and BERT .
- Tokenization is an essential step in natural language processing, as it transforms raw text into meaningful units that can be further analyzed and processed   .



### Detecting and Correcting Spelling Errors

- Spelling errors are common in natural language texts, especially in informal domains such as social media, chat messages, or user-generated content.
- Spelling errors can affect the performance of natural language processing (NLP) systems, such as parsers, taggers, or machine translation systems, by introducing noise and ambiguity.
- Detecting and correcting spelling errors is a challenging task that requires knowledge of the language, the context, and the possible sources of errors.
- Some common sources of spelling errors are:
  - Typographical errors: Mistakes made while typing, such as hitting the wrong key, omitting a letter, or transposing two letters. For example, `form` instead of `from`, `hte` instead of `the`, or `recieve` instead of `receive`.
  - Cognitive errors: Mistakes made due to confusion or lack of knowledge of the spelling rules, such as homophones, irregular verbs, or silent letters. For example, `there` instead of `their`, `loose` instead of `lose`, or `wierd` instead of `weird`.
  - Phonological errors: Mistakes made due to the influence of the pronunciation or dialect of the speaker, such as dropping or adding sounds, or using non-standard spellings. For example, `gonna` instead of `going to`, `wanna` instead of `want to`, or `nite` instead of `night`.
  - Morphological errors: Mistakes made due to the incorrect use of prefixes, suffixes, or inflections, such as plural, tense, or case. For example, `alot` instead of `a lot`, `happend` instead of `happened`, or `childs` instead of `children`.
- Some common methods for detecting and correcting spelling errors are:
  - Dictionary-based methods: These methods compare each word in the text with a list of valid words (a dictionary) and flag the words that are not found in the list as errors. Then, they generate a list of candidate corrections for each error by applying some rules or heuristics, such as deleting, inserting, substituting, or transposing letters. Finally, they select the best correction for each error by using some criteria, such as frequency, edit distance, or context. For example, the word `writting` can be corrected to `writing` by deleting one `t`, or to `written` by substituting `t` with `e`.
  - Statistical methods: These methods use probabilistic models to estimate the likelihood of a word being correct or incorrect, and the likelihood of a correction being appropriate or not, based on the evidence from large corpora of texts. They use techniques such as n-gram models, hidden Markov models, or noisy channel models to capture the patterns and dependencies of words and letters in the language. For example, the word `teh` can be corrected to `the` by using a bigram model that assigns a higher probability to `the` than to `teh` given the previous word.
  - Machine learning methods: These methods use supervised or unsupervised learning algorithms to learn the features and rules that distinguish correct and incorrect words, and to generate and rank the corrections. They use techniques such as decision trees, neural networks, or support vector machines to classify, cluster, or rank the words and corrections based on the features extracted from the text, such as orthographic, phonetic, syntactic, or semantic features. For example, the word `definately` can be corrected to `definitely` by using a neural network that learns the spelling patterns and the context of the word.



### Minimum Edit Distance

- Minimum edit distance is a measure of how similar or dissimilar two strings are by counting the minimum number of operations required to transform one string into another .
- The operations are typically insertion, deletion, and substitution of a single character, or transposition of two adjacent characters.
- Minimum edit distance can be used for various natural language processing tasks, such as spelling correction, text classification, information extraction, and machine translation .
- Minimum edit distance can be computed using a dynamic programming algorithm that fills a matrix with the costs of the optimal alignments between the prefixes of the two strings  .
- The algorithm works as follows  :
  - Initialize the first row and column of the matrix with the costs of inserting or deleting the characters of the first string or the second string, respectively.
  - For each cell in the matrix, compute the minimum cost of aligning the prefixes of the two strings up to that cell, by taking the minimum of three possible costs:
    - The cost of the cell above plus the cost of deleting a character from the first string.
    - The cost of the cell to the left plus the cost of inserting a character to the second string.
    - The cost of the cell diagonally above and to the left plus the cost of substituting a character if the characters at the current position are different, or zero if they are the same.
  - The minimum edit distance is the value of the bottom-right cell of the matrix.
  - Optionally, the optimal alignment can be traced back by following the pointers from the bottom-right cell to the top-left cell, indicating which operation was chosen at each step.
- The costs of the operations can be assigned arbitrarily, depending on the application and the language . For example, some common choices are:
  - Assign a cost of 1 for each operation, regardless of the characters involved. This is also known as the Levenshtein distance.
  - Assign a cost of 2 for substitution and 1 for insertion and deletion. This is also known as the restricted Damerau-Levenshtein distance.
  - Assign a cost of 0.5 for transposition and 1 for the other operations. This is also known as the optimal string alignment distance.
  - Assign different costs for different characters, based on their frequency, similarity, or keyboard layout . For example, substituting 'e' with 'i' may have a lower cost than substituting 'e' with 'z' in English.



### WORD LEVEL ANALYSIS

Word level analysis is the process of analyzing natural language at the level of individual words or tokens. It involves identifying the basic units of meaning and structure in a text, such as morphemes, words, parts of speech, and punctuation marks. Word level analysis can help us to understand the lexical and syntactic properties of natural language, as well as to perform tasks such as text normalization, tokenization, stemming, lemmatization, and spell checking.

Some of the techniques and tools used for word level analysis are:

- **Regular expressions**: A regular expression (RE) is a language for specifying text search strings. RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern. RE can be used to perform tasks such as finding and replacing text, extracting information, validating input, and splitting text into tokens.
- **Morphological analysis**: Morphological analysis deals with the identification and analysis of the smallest units of meaning in a word, called morphemes. A morpheme can be a root, a prefix, a suffix, or an infix. Morphological analysis can help us to determine the meaning, category, and inflection of a word, as well as to generate new words from existing ones.
- **Part-of-speech tagging**: Part-of-speech (POS) tagging is the process of assigning a grammatical category to each word in a text, such as noun, verb, adjective, adverb, etc. POS tagging can help us to understand the syntactic role and function of words in a sentence, as well as to perform tasks such as parsing, named entity recognition, and sentiment analysis.
- **Word embeddings**: Word embeddings are numerical representations of words that capture their semantic and syntactic similarities and differences. Word embeddings are learned from large corpora of text using neural network models, such as word2vec, GloVe, and fastText. Word embeddings can help us to perform tasks such as word similarity, analogy, clustering, and classification.

Word level analysis is an essential component of natural language processing, as it provides the foundation for higher-level analysis and applications. Word level analysis can help us to extract useful information and insights from natural language, as well as to generate new and creative text.



### Unsmoothed N-grams

- An n-gram is a sequence of n words or tokens in a text. For example, "natural language processing" is a trigram (n = 3).
- N-grams are used to model the probability of a word given its previous words or context. For example, P(processing | natural language) is the probability of the word "processing" given the previous words "natural language".
- N-gram models are based on the assumption of the Markov property, which states that the probability of a word only depends on a fixed number of previous words. For example, a bigram model assumes that P(w_n | w_1, ..., w_n-1) = P(w_n | w_n-1), where w_n is the nth word in a sequence.
- To estimate the n-gram probabilities, we can use the maximum likelihood estimation (MLE), which counts the frequency of each n-gram in a corpus and divides it by the frequency of the (n-1)-gram. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C(.) is the count function.
- Unsmoothed n-gram models are simple and easy to implement, but they have some drawbacks. One of them is data sparsity, which means that some n-grams may not occur in the training corpus, leading to zero probabilities. Another one is overfitting, which means that the model may memorize the training data and fail to generalize to unseen data.



### Evaluating N-grams

- N-grams are sequences of words or characters that are used to model natural language.
- N-grams can be used for various tasks, such as text generation, spelling correction, machine translation, speech recognition, etc.
- N-grams are typically extracted from a large corpus of text, and their probabilities are estimated based on their frequency of occurrence.
- N-grams can be evaluated based on different criteria, such as:

  - **Coverage**: the percentage of n-grams in a test set that are also present in a training set. Higher coverage means better generalization and less data sparsity.
  - **Perplexity**: the inverse of the average probability of a test set, given a trained n-gram model. Lower perplexity means better fit and less uncertainty.
  - **Entropy**: the average amount of information contained in an n-gram. Higher entropy means more diversity and richness of language.
  - **Likelihood**: the probability of a test set, given a trained n-gram model. Higher likelihood means better fit and more evidence.
  - **Cross-entropy**: the average amount of information needed to encode a test set, given a trained n-gram model. Lower cross-entropy means better fit and less redundancy.

- N-grams can be evaluated using different methods, such as:

  - **Held-out estimation**: a portion of the training data is set aside as a validation set, and the n-gram model is trained on the remaining data. The n-gram model is then evaluated on the validation set using one or more of the criteria mentioned above.
  - **Bootstrap sampling**: the n-gram model is trained on the entire training data, and then a number of samples are drawn from the training data with replacement. The n-gram model is then evaluated on each sample using one or more of the criteria mentioned above, and the results are averaged.
  - **Cross-validation**: the training data is divided into k folds, and the n-gram model is trained on k-1 folds and evaluated on the remaining fold. This process is repeated for each fold, and the results are averaged.
  - **Extrinsic evaluation**: the n-gram model is used as a component of a larger system, such as a machine translation system or a speech recognition system, and the performance of the system is measured on a test set using some task-specific metric, such as BLEU score or word error rate.



### Smoothing for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Smoothing is the process of flattening a probability distribution implied by a language model so that all reasonable word sequences can occur with some probability .
- Smoothing often involves broadening the distribution by redistributing weight from high probability regions to zero probability regions .
- Smoothing is very important in natural language processing, as some words may have zero or close to zero probabilities such as the out-of-vocabulary words (words that do not exist in the vocabulary), but the same rare words may not have the same values in test data.
- Smoothing techniques in NLP are used to address scenarios related to determining probability / likelihood estimate of a sequence of words (say, a sentence) occuring together when one or more words individually (unigram) or N-grams such as bigram or trigram in the given set have never occured in the past.
- Smoothing can help performance whenever data sparsity is an issue, and data sparsity is almost always an issue in statistical modeling.
- Smoothing can also allow expanding the model, such as by moving to a higher n-gram model, to improve the accuracy of the language model.
- Some examples of smoothing techniques are add-one smoothing, add-k smoothing, Good-Turing smoothing, Kneser-Ney smoothing, etc.



### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram models in natural language processing.
- Smoothing is a technique to assign non-zero probabilities to unseen n-grams and reduce the probabilities of seen n-grams.
- Interpolation and backoff are based on the idea of using lower-order n-grams when higher-order n-grams are unreliable or sparse.
- Interpolation is a method that combines the probabilities of n-grams of different orders using some weights. For example, the probability of a trigram can be interpolated as:

$$
P(w_i|w_{i-2}w_{i-1}) = \lambda_1 P(w_i|w_{i-2}w_{i-1}) + \lambda_2 P(w_i|w_{i-1}) + \lambda_3 P(w_i)
$$

where $\lambda_1 + \lambda_2 + \lambda_3 = 1$ and $\lambda_i \geq 0$ for $i = 1, 2, 3$.

- The weights $\lambda_i$ can be estimated using various methods, such as maximum likelihood estimation, expectation-maximization, or cross-validation.
- Interpolation has the advantage of using all the available information from different n-gram orders, but it also requires more parameters and computation.
- Backoff is a method that uses a higher-order n-gram only if it has sufficient frequency or evidence, otherwise it backs off to a lower-order n-gram. For example, the probability of a trigram can be computed as:

$$
P(w_i|w_{i-2}w_{i-1}) = \begin{cases}
P^*(w_i|w_{i-2}w_{i-1}) & \text{if } C(w_{i-2}w_{i-1}w_i) > 0 \\
\alpha(w_{i-2}w_{i-1})P(w_i|w_{i-1}) & \text{otherwise}
\end{cases}
$$

where $P^*(w_i|w_{i-2}w_{i-1})$ is a discounted probability of the trigram, $C(w_{i-2}w_{i-1}w_i)$ is the count of the trigram, and $\alpha(w_{i-2}w_{i-1})$ is a scaling factor to ensure that the probabilities sum to one.
- Backoff has the advantage of being simpler and faster than interpolation, but it also discards some information from higher-order n-grams when backing off.
- In general, interpolation works better than backoff, but both methods are widely used in natural language processing applications.



### Word Classes for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Word classes, also known as **parts of speech**, are categories of words that share similar syntactic and semantic properties in a language.
- Word classes can be divided into two types: **open** and **closed**. Open word classes are those that can accept new members, such as nouns, verbs, adjectives, and adverbs. Closed word classes are those that have a fixed set of members, such as pronouns, prepositions, conjunctions, and determiners.
- Word classes can also be further subdivided into more specific categories, such as proper nouns, common nouns, count nouns, mass nouns, transitive verbs, intransitive verbs, modal verbs, comparative adjectives, superlative adjectives, etc.
- Word classes are important for natural language processing (NLP) because they provide information about the structure and meaning of sentences. For example, knowing the word class of a word can help determine its possible syntactic roles, such as subject, object, modifier, etc. Knowing the word class of a word can also help infer its possible semantic relations, such as synonymy, antonymy, hyponymy, etc.
- One of the tasks of NLP is to automatically assign word classes to words in a text, which is called **part-of-speech tagging**. Part-of-speech tagging can be done using various methods, such as rule-based, statistical, or neural network-based approaches. Part-of-speech tagging is useful for many downstream NLP applications, such as parsing, named entity recognition, sentiment analysis, machine translation, etc.



### Part-of-Speech Tagging

- Part-of-speech (POS) tagging is the automatic assignment of part-of-speech tags to words in a sentence .
- A POS tag is a grammatical category that indicates the function and form of a word, such as noun, verb, adjective, adverb, etc.  .
- POS tagging is an important natural language processing (NLP) task that helps to analyze the syntactic structure and semantic meaning of a sentence  .
- POS tagging can be useful for various NLP applications, such as parsing, machine translation, information extraction, sentiment analysis, text summarization, etc.  .
- POS tagging can be performed using different methods, such as rule-based, statistical, or neural network-based approaches   .
- Rule-based methods use predefined rules and dictionaries to assign POS tags based on the word form and context .
- Statistical methods use probabilistic models and machine learning algorithms to learn the POS tag distribution from a large corpus of annotated data .
- Neural network-based methods use deep learning architectures and techniques to learn the POS tag representation from raw text features  .
- POS tagging is a challenging task due to the ambiguity and variability of natural language, such as homographs, heteronyms, idioms, slang, etc.  .
- POS tagging can be evaluated using different metrics, such as accuracy, precision, recall, and F1-score, which measure the agreement between the predicted and the true POS tags  .



### Rule-based

- Rule-based natural language processing (NLP) is an approach that uses predefined rules and patterns to analyze and manipulate natural language data.
- Rule-based NLP relies on linguistic knowledge, such as syntax, semantics, morphology, and pragmatics, to define the rules and patterns for various NLP tasks, such as tokenization, stemming, lemmatization, part-of-speech tagging, parsing, named entity recognition, sentiment analysis, etc.
- Rule-based NLP can be implemented using regular expressions, finite state automata, context-free grammars, or other formal methods.
- Rule-based NLP has some advantages, such as:
  - It can handle well-formed and structured language data with high accuracy and precision.
  - It can capture domain-specific and expert knowledge that may not be available in large corpora or statistical models.
  - It can be transparent and interpretable, as the rules and patterns are explicitly defined and can be inspected and modified.
- Rule-based NLP also has some limitations, such as:
  - It can be labor-intensive and time-consuming to manually craft and maintain the rules and patterns for different languages, domains, and tasks.
  - It can be brittle and inflexible, as it may fail to generalize to new or unseen language data that do not match the rules and patterns.
  - It can be difficult to scale and integrate with other NLP systems, as it may require a lot of computational resources and human intervention.



### Stochastic for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Stochastic means involving randomness or probability.
- Stochastic methods are widely used in natural language processing (NLP) to deal with uncertainty and ambiguity in natural languages .
- Stochastic methods can be applied at different levels of NLP, such as:
  - Stochastic grammar: a grammar that assigns probabilities to grammar rules, and can be used to parse sentences and generate sentences .
  - Stochastic semantic analysis: a semantic analysis that uses segments of words as basic semantic units, and can be used to understand the meaning of sentences and generate sentences.
  - Stochastic language modeling: a language model that assigns probabilities to sequences of words, and can be used to generate text and perform tasks such as machine translation, question answering, and speech recognition .
- Stochastic methods can be based on different types of models, such as:
  - Probabilistic models: models that use probability theory to represent uncertainty and learn from data .
  - Statistical models: models that use statistical inference to estimate parameters and test hypotheses from data .
  - Machine learning models: models that use algorithms to learn from data and improve their performance .
- Stochastic methods can have various advantages and challenges, such as:
  - Advantages: they can handle large and complex data, they can cope with noise and variation, they can generalize to unseen data, they can provide confidence scores and rankings  .
  - Challenges: they can require a lot of data and computational resources, they can be sensitive to data quality and bias, they can be difficult to interpret and explain, they can raise ethical and social issues .



### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill .
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns a series of transformation rules from a set of labeled data .
- The transformation rules are applied in a sequential order to modify the initial state of the data until no more rules can be applied or a predefined number of iterations is reached .
- The initial state of the data is usually obtained by assigning the most frequent or default tag to each word, such as noun for unknown words .
- The transformation rules are of the form: change tag a to tag b when condition c is met .
- The condition c can be based on the word itself, its surrounding words, its previous or following tags, or any other contextual information .
- The transformation rules are learned by iteratively finding the rule that reduces the most errors on the training data, applying it, and repeating the process until no more rules can be found or a predefined number of rules is reached .
- The learned rules are then applied to the test data in the same order as they were learned .
- Transformation-based tagging has the advantages of being fast, simple, interpretable, and adaptable to different domains and languages .
- It also has the disadvantages of being sensitive to the order of the rules, requiring a large amount of labeled data, and having difficulties with rare or ambiguous words .



### Issues in PoS tagging

- PoS tagging is the task of assigning a part-of-speech (PoS) label to each word in a sentence, such as noun, verb, adjective, etc.
- PoS tagging is useful for many natural language processing (NLP) applications, such as syntactic parsing, semantic analysis, information extraction, machine translation, etc.
- PoS tagging is not a trivial task, as there are many issues and challenges involved, such as:

  - **Ambiguity**: Many words can have more than one possible PoS tag, depending on the context. For example, the word "book" can be a noun or a verb, and the word "can" can be a modal verb or a noun. PoS taggers need to resolve this ambiguity by using linguistic rules or statistical models.
  - **Sparsity**: Many words are rare or unseen in the training data, and PoS taggers need to handle them appropriately. For example, proper nouns, acronyms, foreign words, etc. PoS taggers can use morphological, syntactic, or semantic clues to infer the PoS tag of unknown words, or use a default tag for them.
  - **Variation**: Different languages, domains, genres, and styles can have different PoS tag sets, conventions, and frequencies. For example, some languages have more PoS categories than others, and some domains have more technical terms than others. PoS taggers need to adapt to these variations and use appropriate resources and models for different scenarios.
  - **Evaluation**: PoS tagging is not a well-defined task, as there can be more than one correct PoS tag for a word, depending on the level of granularity, the annotation scheme, and the intended application. For example, some PoS tag sets distinguish between different types of nouns, verbs, or adjectives, while others do not. PoS taggers need to be evaluated against a consistent and reliable gold standard, and use appropriate metrics, such as accuracy, precision, recall, or F1-score.



### Hidden Markov and Maximum Entropy models for natural language processing

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions) .
- HMM assumes that the hidden states follow a Markov chain, which means that the current state depends only on the previous state, and the emissions depend only on the current state .
- HMM can be used for various natural language processing tasks, such as part-of-speech tagging, speech recognition, named entity recognition, and machine translation  .
- HMM can be represented by five parameters: the set of hidden states, the set of emissions, the initial state probabilities, the state transition probabilities, and the emission probabilities .
- HMM can be trained using the Baum-Welch algorithm, which is a special case of the Expectation-Maximization algorithm, and can be used to find the most likely sequence of hidden states using the Viterbi algorithm, which is a dynamic programming technique .
- Maximum Entropy Markov Model (MEMM) is a discriminative model that extends a standard maximum entropy classifier by assuming that the unknown values to be learnt are connected in a Markov chain rather than being conditionally independent of each other .
- MEMM can also be used for natural language processing tasks, such as part-of-speech tagging and information extraction  .
- MEMM can overcome some of the limitations of HMM, such as the inability to incorporate rich features and the label bias problem, which occurs when some states have very low transition probabilities and tend to dominate the predictions  .
- MEMM can be represented by a set of features and weights, which are used to calculate the conditional probability of a state given an observation and a previous state .
- MEMM can be trained using the Generalized Iterative Scaling algorithm or the Improved Iterative Scaling algorithm, which are both iterative methods that adjust the weights to maximize the likelihood of the training data .
- MEMM can be used to find the most likely sequence of states using the Viterbi algorithm, but with some modifications to account for the conditional probabilities .



## Unit 2 - SYNTACTIC ANALYSIS

- Syntactic analysis is the process of analyzing the structure and grammar of a natural language sentence or program code.
- Syntactic analysis involves parsing, which is the process of assigning a hierarchical representation to the input, such as a parse tree or an abstract syntax tree.
- Syntactic analysis can be performed by different types of parsers, such as top-down parsers, bottom-up parsers, or hybrid parsers.
- Syntactic analysis can be used for various applications, such as natural language processing, compiler design, code analysis, and code generation.
- Syntactic analysis can be influenced by various factors, such as the grammar formalism, the lexicon, the ambiguity, the error handling, and the efficiency of the parser.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of context free grammars for the unit 2 - syntactic analysis in the subject of natural language processing.

### Context Free Grammars

- A context free grammar (CFG) is a set of rules that define how words and phrases can be combined to form sentences in a language.
- A CFG consists of four components: a set of terminals, a set of non-terminals, a start symbol, and a set of production rules.
- Terminals are the basic symbols or words of the language, such as nouns, verbs, adjectives, etc.
- Non-terminals are the syntactic categories or phrases that can be further expanded by the production rules, such as noun phrase, verb phrase, sentence, etc.
- The start symbol is a special non-terminal that represents the whole sentence or the root of the parse tree.
- Production rules are the rules that specify how a non-terminal can be rewritten as a sequence of terminals and/or non-terminals, such as S -> NP VP, NP -> Det N, VP -> V NP, etc.
- A CFG can generate a language, which is the set of all sentences that can be derived from the start symbol by applying the production rules repeatedly.
- A CFG can also parse a sentence, which is the process of finding a derivation or a parse tree that shows how the sentence can be generated by the CFG.
- A CFG is called context free because the production rules only depend on the non-terminal being rewritten, and not on the surrounding symbols or context.
- A CFG can capture the hierarchical structure and the recursive nature of natural language syntax, but it also has some limitations, such as ambiguity, overgeneration, and inability to handle long-distance dependencies.



### Grammar rules for English for the notes of the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Grammar rules are the conventions that govern how words and phrases are arranged to form sentences in a language.
- Syntactic analysis is the process of identifying the structure and meaning of sentences based on grammar rules.
- There are different types of grammar rules for English, such as:
  - **Morphological rules**: These rules determine how words are formed from smaller units called morphemes, such as prefixes, suffixes, and roots. For example, the word "unhappy" is formed by adding the prefix "un-" to the root "happy".
  - **Phonological rules**: These rules determine how sounds are pronounced and combined in a language. For example, the sound /t/ is pronounced differently in "top" and "stop".
  - **Lexical rules**: These rules determine the meaning and category of words in a language. For example, the word "book" can be a noun or a verb depending on the context.
  - **Syntactic rules**: These rules determine how words are grouped and ordered to form phrases and clauses in a language. For example, the word order in English is usually subject-verb-object (SVO), such as "She reads a book".
  - **Semantic rules**: These rules determine the meaning and relation of phrases and clauses in a language. For example, the phrase "a red apple" means an apple that is red, not a red that is apple.
  - **Pragmatic rules**: These rules determine the use and interpretation of language in different situations and contexts. For example, the sentence "Can you pass the salt?" can be a request or a question depending on the tone and intention of the speaker.
- Syntactic analysis can be performed at different levels of granularity, such as:
  - **Word level**: This level focuses on the morphological and lexical properties of words, such as their spelling, pronunciation, meaning, and part of speech. For example, the word "running" can be a verb, a noun, or an adjective depending on the context.
  - **Phrase level**: This level focuses on the syntactic and semantic properties of phrases, such as their structure, function, and meaning. For example, the phrase "the old man" is a noun phrase that consists of a determiner, an adjective, and a noun, and it acts as the subject of a sentence.
  - **Clause level**: This level focuses on the syntactic and semantic properties of clauses, such as their structure, type, and meaning. For example, the clause "He saw her" is a declarative clause that consists of a subject, a verb, and an object, and it expresses a fact.
  - **Sentence level**: This level focuses on the syntactic and semantic properties of sentences, such as their structure, coherence, and meaning. For example, the sentence "He saw her and she smiled" is a compound sentence that consists of two independent clauses joined by a conjunction, and it expresses a sequence of events.
  - **Discourse level**: This level focuses on the pragmatic and rhetorical properties of sentences, such as their use, purpose, and effect. For example, the sentence "He saw her and she smiled" can be used to convey different messages depending on the context, such as happiness, surprise, or sarcasm.



### Treebanks

- A treebank is a collection of sentences annotated with syntactic structures, such as phrase structure trees or dependency graphs .
- Treebanks are useful for natural language processing (NLP) because they provide gold-standard data for training and evaluating systems such as part-of-speech taggers, parsers, semantic analyzers and machine translation systems  .
- Treebanks also enable linguistic research on various aspects of syntax, such as word order, grammatical categories, argument structure, and long-distance dependencies  .
- Treebanks can be constructed manually by linguists, automatically by parsers, or semi-automatically by combining both methods .
- Treebanks can vary in their size, domain, language, annotation scheme, and level of detail .
- Some examples of well-known treebanks are the Penn Treebank for English, the Prague Dependency Treebank for Czech, the Universal Dependencies Treebank for multiple languages, and the Chinese Treebank for Mandarin .



### Normal Forms for Grammar

- Normal forms for grammar are ways of transforming a grammar into a simpler or more restricted form without changing the language it generates.
- Normal forms are useful for parsing and analyzing natural language sentences using efficient algorithms.
- There are different types of normal forms for grammar, such as Chomsky normal form, Greibach normal form, Kuroda normal form, etc.
- Each normal form has its own rules and properties that define how the grammar can be rewritten.
- For example, Chomsky normal form (CNF) is a normal form for context-free grammars that requires every production rule to be of the form A -> BC or A -> a, where A, B, and C are non-terminal symbols and a is a terminal symbol.
- Any context-free grammar can be converted to CNF using a series of steps, such as eliminating epsilon-rules, unit rules, useless symbols, and long rules.
- CNF is widely used in natural language processing for parsing and analyzing natural language sentences using the CYK algorithm.



### Dependency Grammar

- Dependency grammar is a descriptive and theoretical tradition in linguistics that can be traced back to antiquity.
- It has long been influential in the European linguistics tradition and has more recently become a mainstream approach to representing syntactic and semantic structure in natural language processing.
- Dependency grammar is based on the idea that linguistic units, such as words, are connected by directed links called dependencies.
- Dependencies express the grammatical relations between words, such as subject, object, modifier, etc.
- Dependencies are represented by labeled directed graphs, where nodes are words and edges are dependencies.
- The root node of the graph is usually the main verb or predicate of the sentence.
- Dependency grammar differs from other syntactic frameworks, such as phrase structure grammar, in that it does not use phrase categories or constituent structure.
- Instead, it relies on the notion of valency or the number and type of arguments that a word can take.
- Dependency grammar can capture both the linear and hierarchical structure of natural language, as well as the semantic roles and functions of words.
- Dependency grammar can be implemented using various algorithms and models, such as transition-based, graph-based, or neural network-based dependency parsers .
- Dependency parsing is a natural language processing task that aims to automatically produce dependency graphs for given sentences.
- Dependency parsing is useful for many downstream applications, such as information extraction, machine translation, sentiment analysis, question answering, etc.



### Syntactic Parsing

- Syntactic parsing is the process of analyzing the structure and meaning of a natural language sentence based on a formal grammar.
- A grammar is a set of rules that define the syntax and semantics of a language, i.e., how words can be combined into phrases and sentences, and what they mean.
- A parser is a program that takes a sentence as input and outputs a parse tree, which is a hierarchical representation of the syntactic structure and meaning of the sentence.
- A parse tree consists of nodes and edges, where nodes are labeled with syntactic categories (such as noun, verb, adjective, etc.) or semantic roles (such as agent, patient, theme, etc.), and edges are labeled with grammatical relations (such as subject, object, modifier, etc.).
- A parse tree can be represented in different formats, such as bracketed notation, tree diagrams, or dependency graphs.
- Syntactic parsing can be divided into two main types: constituency parsing and dependency parsing.
- Constituency parsing is based on the idea that sentences are composed of nested constituents, i.e., groups of words that function as a unit. For example, in the sentence "The dog chased the cat", the noun phrase "the dog" is a constituent that acts as the subject of the verb phrase "chased the cat".
- Dependency parsing is based on the idea that sentences are composed of words that depend on each other in terms of syntactic and semantic functions. For example, in the same sentence, the word "dog" depends on the word "chased" as its subject, and the word "cat" depends on the word "chased" as its object.
- Syntactic parsing can be performed using different methods, such as rule-based, probabilistic, or neural network-based approaches.
- Rule-based parsing relies on manually crafted grammars and algorithms that apply the rules to generate or select the best parse tree for a given sentence. For example, a top-down parser starts from the root node of the tree and tries to expand it using the grammar rules until it matches the input sentence.
- Probabilistic parsing relies on statistical models that learn the probabilities of grammar rules and parse trees from a large corpus of annotated sentences. For example, a probabilistic context-free grammar (PCFG) assigns a probability to each rule based on its frequency in the corpus, and a probabilistic parser uses these probabilities to find the most likely parse tree for a given sentence.
- Neural network-based parsing relies on artificial neural networks that learn to encode the input sentence into a vector representation and decode it into a parse tree. For example, a recurrent neural network (RNN) can process the input sentence word by word and update its hidden state, which can then be used to generate or select the parse tree.



### Ambiguity

- Ambiguity is the property of a sentence or phrase that can have more than one meaning or interpretation.
- Ambiguity can arise at different levels of language processing, such as lexical, syntactic, semantic, or pragmatic.
- Lexical ambiguity occurs when a word or phrase has multiple senses or meanings, such as "bank" (financial institution or river shore) or "bat" (flying mammal or wooden club).
- Syntactic ambiguity occurs when the structure or grammar of a sentence allows for more than one possible grouping of words or phrases, such as "I saw the man with the telescope" (who has the telescope?) or "They are flying planes" (who is flying?).
- Semantic ambiguity occurs when the meaning of a sentence or phrase depends on the context or the world knowledge of the speaker or listener, such as "He is in the park" (which park?) or "She is looking for a match" (for lighting a fire or for dating?).
- Pragmatic ambiguity occurs when the intended message or implication of a sentence or phrase is unclear or ambiguous, such as "Can you pass the salt?" (is it a request or a question?) or "You're not bad" (is it a compliment or an insult?).
- Ambiguity can cause problems or challenges for natural language processing systems, such as parsers, translators, or dialogue agents, as they need to resolve or disambiguate the possible meanings or interpretations of a given input.



### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient parsing of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- The idea is to store the results of subproblems (i.e., whether a substring can be derived from a nonterminal symbol) in a table or chart, and reuse them to solve larger problems (i.e., whether the whole sentence can be derived from the start symbol).
- The most common algorithm for dynamic programming parsing is the Cocke-Kasami-Younger (CKY) algorithm, which has a time complexity of O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar.
- The CKY algorithm works as follows:
  - Initialize an n x n upper triangular chart, where each cell (i, j) corresponds to the substring from word i to word j (inclusive) of the input sentence.
  - For each word i, fill the cell (i, i) with the nonterminal symbols that can directly generate that word, according to the grammar rules.
  - For each span length l from 2 to n, and for each start position i from 1 to n - l + 1, fill the cell (i, i + l - 1) with the nonterminal symbols that can generate the substring from word i to word i + l - 1, by applying the following rule: 
    - If A -> BC is a grammar rule, and B is in cell (i, k) and C is in cell (k + 1, i + l - 1) for some k between i and i + l - 1, then add A to cell (i, i + l - 1).
  - Check if the start symbol of the grammar is in the cell (1, n). If yes, then the sentence is accepted by the grammar. If no, then the sentence is rejected by the grammar.
  - Optionally, backtrack from the cell (1, n) to construct a parse tree for the sentence, by following the pointers that indicate which grammar rules and which cells were used to fill each cell.



### Shallow parsing

- Shallow parsing (also called chunking or light parsing) is an analysis of a sentence which first identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and then links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.).
- Shallow parsing is different from deep parsing, which aims to produce a complete and detailed syntactic structure of a sentence, such as a parse tree or a dependency graph.
- Shallow parsing is useful for natural language processing tasks that do not require full syntactic analysis, such as information extraction, named entity recognition, sentiment analysis, etc.
- Shallow parsing can be seen as a set of cascaded classification problems, where separate classifiers are used for tagging, chunk boundary detection, chunk labeling, relation finding, etc.
- Shallow parsing can also be used to assign semantic roles to words or phrases in a sentence, such as that of an agent, goal, or result. This is also called semantic role labeling or slot-filling.
- Shallow parsing can be performed using various methods, such as rule-based systems, statistical models, machine learning algorithms, etc. Some popular tools for shallow parsing are NLTK, spaCy, Stanford CoreNLP, etc.



### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probabilities of the rules are estimated from a corpus of sentences and their parse trees, called a treebank.
- A PCFG can be used to model the syntactic structure of natural languages, and to perform probabilistic parsing, which is the task of finding the most likely parse tree for a given sentence.
- A PCFG is defined by a tuple (N, Σ, R, S, P), where:
  - N is a set of nonterminal symbols (also called syntactic categories or labels)
  - Σ is a set of terminal symbols (also called words or tokens)
  - R is a set of production rules of the form A → α, where A ∈ N and α ∈ (N ∪ Σ)*
  - S ∈ N is the start symbol
  - P is a function that assigns a probability to each rule in R, such that for any A ∈ N, the sum of P(A → α) over all α ∈ (N ∪ Σ)* is 1.
- A PCFG generates a sentence w ∈ Σ* and its parse tree t by applying a sequence of rules starting from S, such that the yield of t is w and the product of the probabilities of the rules is the probability of t.
- The probability of a sentence w is the sum of the probabilities of all possible parse trees for w.
- A PCFG can be converted to Chomsky normal form (CNF), which is a restricted form of CFG where each rule has either two nonterminals or one terminal on the right-hand side. This simplifies the parsing algorithm and reduces the number of parameters to estimate.
- A common algorithm for probabilistic parsing with PCFGs is the CKY algorithm, which is a bottom-up dynamic programming algorithm that fills a chart with the probabilities of all possible subtrees for each span of the sentence, and then backtracks to find the most probable parse tree.



### Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees for each substring of the input sentence in a table.
- The algorithm works as follows:

  - Initialize the table with the probabilities of the terminal symbols for each word in the sentence.
  - For each substring of length 2 or more, consider all possible ways of splitting it into two smaller substrings, and all possible rules of the form A -> BC that can generate the substring.
  - For each such rule, multiply the probabilities of the subtrees for B and C, and the probability of the rule itself, and store the maximum value in the table for A.
  - Repeat until the table is filled.
  - The probability of the most likely parse tree for the whole sentence is the maximum value in the table for the start symbol of the grammar.
  - The most likely parse tree can be reconstructed by tracing back the table entries from the start symbol to the terminal symbols.



### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule in a CFG.
- The probability of a rule A -> α is the conditional probability of expanding A to α given A, written as P(A -> α | A) or P(A -> α).
- The probability of a derivation or a parse tree is the product of the probabilities of all the rules used in the derivation.
- PCFGs can be used to model the syntactic structure of natural language sentences, and to perform parsing tasks such as finding the most probable parse tree for a given sentence.
- Lexicalized PCFGs (L-PCFGs) are a type of PCFGs that incorporate lexical information into the nonterminal symbols of the grammar.
- L-PCFGs use a head-driven approach, where each nonterminal symbol is annotated with the head word of its constituent, and the probabilities of the rules depend on the head words of the parent and the children.
- L-PCFGs can capture more fine-grained syntactic and semantic dependencies between words, and can improve the accuracy and efficiency of parsing.
- Neural bi-lexicalized PCFGs (NBL-PCFGs) are a type of L-PCFGs that use neural networks to parameterize the probabilities of the rules based on the embeddings of the head words.
- NBL-PCFGs can learn richer and more expressive representations of the head words, and can handle unseen words and rare rules better than traditional L-PCFGs.
- NBL-PCFGs can also perform unsupervised grammar induction, where they learn the grammar rules and the probabilities from unannotated sentences.



### Feature structures for the notes of the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Natural Language Processing (NLP) is a branch of artificial intelligence that attempts to bridge the gap between what a machine recognizes as input and the human language.
- NLP combines artificial intelligence, computational linguistics and machine learning to enable computers and humans to communicate seamlessly.
- NLP can be divided into three main tasks: speech recognition, natural language understanding and natural language generation.
- Syntactic analysis is the process of analyzing the structure and meaning of sentences in natural language.
- Feature structures are a way of representing syntactic information in a hierarchical and modular way.
- Feature structures are composed of features and values, where features are atomic symbols and values can be atomic symbols, sets or other feature structures.
- Feature structures can be visualized as labeled graphs, where nodes are features and edges are values.
- For example, the following feature structure represents some information about a word:

```
[POS = N
 NUM = SG
 GND = FEM
 SEM = [CAT = ANIMAL
        NAME = 'Fido']]
```

- This feature structure can be graphically represented as:

```
    POS
     |
     N
    /|\
   / | \
  /  |  \
 /   |   \
NUM GND  SEM
 |   |    |
 SG FEM  [CAT = ANIMAL
          NAME = 'Fido']
```

- Feature structures can be manipulated by the operation of unification, which allows us to combine the information contained in two different feature structures.
- Unification is the process of finding the most general feature structure that is consistent with both of the input feature structures.
- Unification can fail if there is a contradiction between the input feature structures, such as different values for the same feature.
- For example, the unification of the following two feature structures:

```
[POS = N
 NUM = SG]
```

and

```
[POS = N
 GND = FEM]
```

results in the following feature structure:

```
[POS = N
 NUM = SG
 GND = FEM]
```

- However, the unification of the following two feature structures:

```
[POS = N
 NUM = SG]
```

and

```
[POS = V
 TNS = PRES]
```

fails because the values of the feature POS are different.



### Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- Unification is a (partial) operation on feature structures. Intuitively, it is the operation of combining two feature structures such that the new feature structure contains all the information of the original two, and nothing more.
- Unification can be used for various purposes in natural language processing (NLP), such as parsing, generation, semantic interpretation, and grammar development.
- Unification can be classified into two types: structural unification and E-unification .
- Structural unification is the standard form of unification that operates on feature structures without any additional constraints or equations .
- E-unification is a generalization of structural unification that allows the use of an E-theory, which is a set of equations that can be applied to feature structures during unification .
- E-unification can be useful for expressing linguistic phenomena that are difficult or impossible to capture with structural unification, such as agreement, anaphora, ellipsis, and coordination .
- E-unification of feature structures has, to the best of our knowledge, never been used in NLP, but it has been studied in logic and artificial intelligence .
- E-unification is more expressive and powerful than structural unification, but it is also more complex and computationally expensive .
- E-unification is undecidable in general, but it can be decidable for some restricted classes of E-theories .
- E-unification can be implemented by a universal E-unification procedure, which is a generalization of the standard unification algorithm that can handle arbitrary E-theories .
- E-unification can also be implemented by specialized algorithms that are tailored for specific E-theories, which can be more efficient and tractable than the universal procedure .
- E-unification of feature structures is a promising research direction for NLP, as it can offer more flexibility and expressiveness for linguistic modeling and analysis .



## Unit 3 - SEMANTICS AND PRAGMATICS

- Semantics is the study of meaning in language, especially the relationship between words and sentences and the situations they refer to.
- Pragmatics is the study of how language is used in context, especially the relationship between speakers and hearers and the assumptions they make about each other.
- Some of the main topics in semantics and pragmatics are:
  - Reference and sense: how words and phrases relate to the entities and concepts they denote or imply.
  - Truth conditions: how the meaning of a sentence depends on the facts of the world and the possible worlds.
  - Entailment and presupposition: how the meaning of a sentence affects or depends on the meaning of another sentence.
  - Implicature and inference: how speakers and hearers use additional information and reasoning to communicate more than what is literally said.
  - Speech acts and illocutionary force: how speakers and hearers use language to perform actions and express intentions.
  - Politeness and face: how speakers and hearers use language to show respect and avoid offense.
  - Context and relevance: how the meaning of a sentence is influenced by the situation and the goals of the communication.



### Requirements for representation for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- The representation of semantics and pragmatics in natural language processing (NLP) is the process of deriving the meaning and the use of natural language expressions from their linguistic and contextual features.
- The representation of semantics and pragmatics requires the following components :
  - A formal language for expressing the semantic and pragmatic information of natural language expressions, such as logic, lambda calculus, or feature structures.
  - A lexicon that provides the semantic and pragmatic properties of words and phrases, such as their meanings, senses, relations, and roles.
  - A grammar that specifies the syntactic and semantic rules for combining words and phrases into larger units, such as sentences, paragraphs, and discourses.
  - A parser that analyzes the syntactic and semantic structure of natural language expressions and produces their representations in the formal language.
  - A semantic interpreter that evaluates the representations of natural language expressions and computes their truth values, entailments, and implicatures.
  - A pragmatic analyzer that uses the contextual information and the world knowledge to infer the speaker's intentions, goals, and beliefs, and to resolve ambiguities, anaphora, and presuppositions.
  - A discourse model that represents the structure and coherence of multi-sentence texts and dialogues, and tracks the topics, themes, and focus of the discourse.
  - A dialogue manager that handles the interaction between the speaker and the hearer, and manages the turn-taking, feedback, and repair mechanisms.
- The representation of semantics and pragmatics faces the following challenges  :
  - The variability and ambiguity of natural language expressions, which can have different meanings and uses depending on the context, the speaker, and the hearer.
  - The incompleteness and inconsistency of natural language expressions, which can omit or contradict some relevant information or assumptions.
  - The creativity and flexibility of natural language expressions, which can introduce new words, metaphors, idioms, and rhetorical devices.
  - The dynamism and evolution of natural language expressions, which can change over time and across domains, genres, and cultures.
  - The integration and coordination of natural language expressions with other modalities, such as speech, gesture, and vision.



### First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL is more expressive than propositional logic, which can only represent the truth values of atomic sentences.
- FOL can represent complex sentences that involve quantifiers, variables, functions, and predicates.
- FOL can also capture the meaning of natural language sentences more precisely and systematically than propositional logic.
- FOL is widely used in natural language processing, artificial intelligence, mathematics, and philosophy.

#### Syntax of FOL

- The basic symbols of FOL are:
  - **Constants**: symbols that denote specific objects in the domain, such as `a`, `b`, `c`, `John`, `Mary`, etc.
  - **Variables**: symbols that can take the value of any object in the domain, such as `x`, `y`, `z`, etc.
  - **Functions**: symbols that map objects to objects, such as `f`, `g`, `h`, `father`, `mother`, etc.
  - **Predicates**: symbols that map objects to truth values, such as `P`, `Q`, `R`, `Animal`, `Organism`, etc.
  - **Connectives**: symbols that combine sentences to form more complex sentences, such as `^` (and), `v` (or), `~` (not), `->` (implies), `<->` (if and only if), etc.
  - **Quantifiers**: symbols that express the scope of variables, such as `forall` (for all), `exists` (there exists), etc.
  - **Parentheses**: symbols that group subexpressions, such as `(` and `)`.
- The grammar of FOL is defined by the following rules:
  - A **term** is either a constant, a variable, or a function applied to one or more terms, such as `a`, `x`, `f(x)`, `g(a,b)`, etc.
  - An **atomic sentence** is a predicate applied to one or more terms, such as `P(a)`, `Q(x,y)`, `Animal(x)`, `Organism(f(x))`, etc.
  - A **sentence** is either an atomic sentence, or a sentence formed by applying a connective to one or more sentences, or a sentence formed by applying a quantifier to a variable and a sentence, such as `P(a)`, `~Q(x,y)`, `P(a) ^ Q(x,y)`, `forall x (Animal(x) -> Organism(x))`, `exists y (P(a) ^ Q(x,y))`, etc.
- The **scope** of a variable is the part of the sentence where the variable is bound by a quantifier, such as `forall x (Animal(x) -> Organism(x))`, where the scope of `x` is `(Animal(x) -> Organism(x))`.
- A **free variable** is a variable that is not bound by any quantifier, such as `x` in `P(x)`.
- A **closed sentence** is a sentence that has no free variables, such as `forall x (Animal(x) -> Organism(x))`.
- An **open sentence** is a sentence that has one or more free variables, such as `P(x)`.

#### Semantics of FOL

- The **interpretation** of FOL is a mapping from the symbols of FOL to the objects and truth values in a given domain.
- The interpretation consists of two components:
  - A **domain** is a set of objects that the constants, variables, and functions refer to, such as `{a, b, c, d, e}`.
  - A **valuation** is a function that assigns a value to each symbol, such as `a -> a`, `b -> b`, `c -> c`, `d -> d`, `e -> e`, `x -> a`, `y -> b`, `z -> c`, `f -> a function that maps a to b and b to c`, `g -> a function that maps a and b to d and c and d to e`, `P -> a predicate that is true for a and b and false for c, d, and e`, `Q -> a predicate that is true for b and c and false for a, d, and e`, `R -> a predicate that is true for c and d and false for a, b, and e`, etc.
- The



### Description Logics for Natural Language Processing

- Description logics (DLs) are a family of logic-based knowledge representation formalisms that allow for the representation of concepts, roles, and individuals, and their relationships .
- DLs are used for various applications, such as ontology engineering, semantic web, natural language processing (NLP), and formal verification .
- In NLP, DLs can be used to model the semantics of natural language expressions, such as sentences, phrases, and words, and to reason about their meaning and entailment .
- DLs can also be used to integrate natural language and knowledge bases, by providing a common representation language and a common inference mechanism .
- Some of the advantages of using DLs for NLP are :
  - They provide a clear and precise semantics for natural language expressions, based on set-theoretic and model-theoretic notions.
  - They allow for the representation of complex and structured concepts, such as modifiers, quantifiers, and negation, and their interactions.
  - They support various forms of reasoning, such as subsumption, consistency, satisfiability, and abduction, which can be used for tasks such as semantic analysis, query answering, and information extraction.
  - They are modular and extensible, meaning that different DLs can be defined by adding or removing expressive features, depending on the application requirements and the computational resources available.
  - They have efficient and sound algorithms for reasoning, implemented in various systems and tools, such as Racer, Pellet, and FaCT++.
- Some of the challenges of using DLs for NLP are :
  - They have limited expressivity compared to other logic-based formalisms, such as first-order logic or higher-order logic, which can capture more aspects of natural language semantics, such as intensionality, modality, and context.
  - They have high computational complexity, meaning that reasoning with DLs can be intractable or undecidable for some expressive features, such as disjunction, number restrictions, or transitive roles.
  - They have a mismatch between the syntax and the semantics of natural language and DLs, meaning that natural language expressions cannot be directly translated into DLs, and vice versa, without losing some information or introducing some ambiguity.
  - They have a lack of linguistic resources, such as lexicons, grammars, and corpora, that are annotated or aligned with DLs, which can facilitate the development and evaluation of NLP applications based on DLs.



### Syntax-Driven Semantic Analysis

- Syntax-driven semantic analysis is the process of assigning a semantic structure to a natural language sentence based on its syntactic structure and grammatical rules  .
- Semantic structure is the representation of the meaning of a sentence that can be manipulated by logical and inferential operations.
- Syntax-driven semantic analysis involves two main steps: syntactic parsing and semantic interpretation.
- Syntactic parsing is the process of analyzing the grammatical structure of a sentence and assigning a syntactic category (such as noun, verb, adjective, etc.) and a syntactic role (such as subject, object, modifier, etc.) to each word or phrase in the sentence  .
- Semantic interpretation is the process of mapping the syntactic structure and the syntactic categories and roles of the words and phrases in the sentence to a semantic representation that captures their meaning and their relationships in the context of the sentence   .
- Syntax-driven semantic analysis can be performed using different methods and formalisms, such as:
  - Constituency-based methods, which use phrase structure rules and tree structures to represent the syntactic and semantic structure of a sentence.
  - Dependency-based methods, which use dependency relations and graphs to represent the syntactic and semantic structure of a sentence.
  - Feature-based methods, which use feature structures and unification operations to represent the syntactic and semantic structure of a sentence.
  - Logic-based methods, which use logical forms and inference rules to represent the syntactic and semantic structure of a sentence.
- Syntax-driven semantic analysis is useful for natural language processing tasks that require understanding and reasoning about the meaning of natural language, such as:
  - Question answering, which involves finding the answer to a natural language question from a given text or knowledge base.
  - Information extraction, which involves extracting relevant information from a natural language text and storing it in a structured format.
  - Text summarization, which involves generating a concise and coherent summary of a natural language text.
  - Natural language generation, which involves producing a natural language text from a given semantic representation or input.



### Semantic attachments for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Semantic attachments are **rules or functions** that map the syntactic structures of a natural language to their **semantic representations** .
- Semantic representations are **formal expressions** that capture the **meaning** of natural language sentences or texts .
- Semantic attachments can be used for various **natural language processing (NLP) tasks**, such as information extraction, question answering, text summarization, machine translation, etc .
- Semantic attachments can be **defined manually** by experts or **learned automatically** from data using machine learning techniques .
- Semantic attachments can be based on different **semantic theories** or **frameworks**, such as first-order logic, lambda calculus, conceptual graphs, frame semantics, etc  .
- Semantic attachments can be **implemented** using different **programming languages** or **tools**, such as Prolog, Lisp, Python, NLTK, etc .
- Semantic attachments can be **evaluated** using different **metrics** or **criteria**, such as accuracy, coverage, consistency, efficiency, etc .
- Semantic attachments can be **challenged** by various **linguistic phenomena** or **problems**, such as ambiguity, anaphora, presupposition, implicature, etc  .
- Semantic attachments can be **enhanced** by incorporating **pragmatic information** or **context**, such as speaker's intention, listener's expectation, common knowledge, discourse structure, etc  .



### Word Senses

- A word sense is a representation of one aspect of a word's meaning.
- A word can have multiple senses, depending on the context in which it is used. For example, the word "bank" can mean a financial institution, a sloping mound, a biological repository, or a building where a bank does its business.
- Word sense disambiguation (WSD) is the task of assigning the appropriate sense to a given word in a text or discourse  .
- WSD is a challenging problem in natural language processing (NLP) because natural language is ambiguous, and many words can be interpreted in multiple ways depending on the context .
- WSD is important for many NLP applications, such as machine translation, information retrieval, text summarization, question answering, and sentiment analysis, because the correct interpretation of a word can affect the overall meaning and quality of the output .
- WSD can be performed using various methods, such as rule-based, knowledge-based, supervised, semi-supervised, or unsupervised approaches .
- Neural word representations, such as word embeddings, have proven useful in WSD because they can efficiently model complex semantic and syntactic word relationships.
- However, most word embedding techniques model only one representation per word, despite the fact that a single word can have multiple senses.
- Sense2vec is a method for word sense disambiguation that leverages word embeddings and part-of-speech tags to create multiple representations for each word, corresponding to different senses.
- Sense2vec can achieve fast and accurate WSD by using a simple nearest neighbor approach to find the most similar sense representation for a given word in a context.



### Relations between Senses

- In natural language processing (NLP), the meaning of a word can vary depending on the context in which it is used. This phenomenon is called **lexical ambiguity** or **polysemy** .
- To resolve lexical ambiguity, NLP systems need to identify the correct **sense** of a word in a given sentence. This task is called **word sense disambiguation (WSD)** .
- A sense is a specific meaning or usage of a word, usually defined by a dictionary or a lexical resource such as WordNet .
- Senses can have different types of relations with each other, such as **synonymy**, **antonymy**, **hyponymy**, **hypernymy**, **meronymy**, **holonymy**, **troponymy**, **entailment**, **implicature**, etc .
- These relations can help NLP systems to infer the meaning of words, expand the vocabulary, and perform various tasks such as information retrieval, machine translation, text summarization, sentiment analysis, etc  .
- Some examples of sense relations are:

  - Synonymy: Two words have the same or very similar meaning, e.g., big and large, happy and glad, sofa and couch, etc.
  - Antonymy: Two words have opposite or contrasting meanings, e.g., hot and cold, up and down, true and false, etc.
  - Hyponymy: A word is a more specific instance of another word, e.g., dog is a hyponym of animal, rose is a hyponym of flower, etc.
  - Hypernymy: A word is a more general category of another word, e.g., animal is a hypernym of dog, flower is a hypernym of rose, etc.
  - Meronymy: A word is a part of another word, e.g., finger is a meronym of hand, wheel is a meronym of car, etc.
  - Holonymy: A word is a whole that contains another word, e.g., hand is a holonym of finger, car is a holonym of wheel, etc.
  - Troponymy: A word is a manner or degree of another word, e.g., whisper is a troponym of speak, jog is a troponym of run, etc.
  - Entailment: A word implies another word, e.g., snore entails sleep, buy entails pay, etc.
  - Implicature: A word suggests another word, e.g., bachelor implicates male, doctor implicates educated, etc.



### Thematic Roles

- Thematic roles are the semantic relationships between a verb and its arguments (the noun phrases that appear with the verb)  .
- Thematic roles describe the role or function of each argument in the event or state expressed by the verb .
- Thematic roles are also called theta roles or semantic roles .
- Thematic roles are different from grammatical roles (such as subject or object), which are based on the syntactic position of the arguments .
- Thematic roles are assigned by the verb to each of its obligatory arguments, according to the theta criterion, which states that each argument must receive exactly one thematic role, and each thematic role must be assigned to exactly one argument .
- Thematic roles are important for natural language processing because they provide a level of semantic analysis that can help with tasks such as information extraction, question answering, and machine translation .

Some of the major thematic roles are:

- Agent: the entity that intentionally performs the action of the verb . Example: Tom broke the window with a rock. (Tom is the agent of break)
- Patient: the entity that undergoes the action or is affected by the state of the verb . Example: Tom broke the window with a rock. (window is the patient of break)
- Experiencer: the entity that perceives or feels the state or event expressed by the verb . Example: Tom saw the window break. (Tom is the experiencer of see)
- Theme: the entity that is involved or moved by the action or state of the verb . Example: Tom gave a book to Mary. (book is the theme of give)
- Instrument: the entity that is used to perform the action of the verb . Example: Tom broke the window with a rock. (rock is the instrument of break)
- Beneficiary: the entity that benefits from or is adversely affected by the action or state of the verb . Example: Tom bought a book for Mary. (Mary is the beneficiary of buy)
- Source: the entity from which an action or state originates . Example: Tom took the book from Mary. (Mary is the source of take)
- Goal: the entity to which an action or state is directed . Example: Tom took the book to the library. (library is the goal of take)
- Location: the entity where an action or state takes place . Example: Tom read the book in the park. (park is the location of read)

: Lecture 24: Semantic Role Labeling and Verb Semantics, CS447: Natural Language Processing, https://courses.grainger.illinois.edu/cs447/fa2019/Slides/Lecture24.pdf
: What Is Natural Language Processing, and How Does It Work? - How-To Geek, https://www.howtogeek.com/665702/what-is-natural-language-processing-and-how-does-it-work/
: Semantics: Thematic Roles - Linguistics Network, https://www.linguisticsnetwork.com/semantics-thematic-roles/
: Natural Language Processing - University of California, Berkeley, https://people.ischool.berkeley.edu/~dbamman/nlp21_slides/18_semantic_roles.pdf



### Selectional restrictions

- Selectional restrictions are semantic constraints that limit the possible arguments of a word or a phrase  .
- They account for the implausibility or ungrammaticality of sentences that violate the expected semantic features of the arguments, such as "Colorless green ideas slept furiously" or "The chair ate the sandwich"  .
- They are often represented as sets of semantic features or categories that specify the legal combinations of senses that can co-occur  .
- For example, the verb "eat" may have a selectional restriction that its subject must be [+animate] and its object must be [+edible], while the verb "admire" may have a selectional restriction that its subject and object must be [+human] or [+intelligent].
- Selectional restrictions are useful for natural language processing tasks such as disambiguation, pronoun resolution, lexical insertion, and semantic composition    .
- They can also be modeled using distributional semantics, which measures the similarity of words based on their co-occurrence patterns in large corpora.
- However, selectional restrictions are not absolute and can be violated for various reasons, such as metaphor, humor, creativity, or error  .
- For example, the sentence "The chair ate the sandwich" may be a metaphor for a greedy person, a joke, a novel expression, or a mistake.
- Therefore, natural language processing systems should be able to handle both the regular and the irregular cases of selectional restrictions, and use contextual cues and world knowledge to interpret them correctly.



### Word Sense Disambiguation

- Word sense disambiguation (WSD) is the problem of determining which "sense" (meaning) of a word is activated by the use of the word in a particular context, a process which appears to be largely unconscious in people.
- WSD is an important research problem in the field of natural language processing (NLP) because lexical ambiguity, syntactic or semantic, is one of the very first problems that any NLP system faces.
- WSD is a subfield of NLP that deals with identifying the intended meaning of a word in a given context from a set of possible senses, based on the context in which the word appears.
- WSD can be useful for many NLP applications, such as machine translation, information retrieval, text summarization, sentiment analysis, question answering, etc.
- WSD can be classified into two main types: supervised and unsupervised. Supervised WSD uses annotated data to train a classifier that can assign senses to words in new contexts. Unsupervised WSD does not use annotated data, but relies on clustering or similarity measures to group words with similar meanings.
- WSD can also be classified into two main levels: fine-grained and coarse-grained. Fine-grained WSD aims to assign the most specific sense of a word from a large inventory of senses, such as WordNet. Coarse-grained WSD aims to assign a more general sense of a word from a smaller inventory of senses, such as domain labels or semantic classes.
- WSD faces some difficulties, such as the lack of standard sense inventories, the variability of word meanings across domains and genres, the sparsity of annotated data, the complexity of word sense representation, and the evaluation of WSD systems .
- WSD is an active and challenging research area in NLP, with many open problems and opportunities for improvement. Some of the current research directions include using deep learning models, incorporating contextual and world knowledge, exploiting multilingual and cross-lingual resources, and developing more realistic and robust evaluation methods.



### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as the surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the common supervised WSD algorithms are:
  - Naive Bayes: This is a probabilistic classifier that assigns the most likely sense to a word based on the frequencies of the features in the training data.
  - Decision Trees: This is a rule-based classifier that splits the feature space into regions based on the values of the features, and assigns the most frequent sense in each region to the word.
  - Support Vector Machines: This is a linear classifier that finds the optimal hyperplane that separates the feature vectors of different senses, and assigns the sense that corresponds to the side of the hyperplane where the word's feature vector lies.
  - Neural Networks: This is a non-linear classifier that learns a complex function that maps the feature vectors to the senses, and assigns the sense that has the highest output value for the word's feature vector.
- Supervised WSD methods have the advantage of being able to learn from large amounts of data and achieve high accuracy, but they also have some limitations, such as:
  - They require a lot of manually annotated data, which is costly and time-consuming to obtain .
  - They suffer from the data sparsity problem, which means that they may not have enough examples for rare or fine-grained senses, or for new words that are not in the training data .
  - They are domain-dependent, which means that they may not generalize well to different domains or genres of text, where the word usage and sense distribution may vary .

: http://nlpprogress.com/english/word_sense_disambiguation.html
: https://www.ijsr.net/archive/v4i2/SUB151598.pdf
: https://aclanthology.org/2020.textgraphs-1.6.pdf
: http://www.scholarpedia.org/article/Word_sense_disambiguation
: https://www.tutorialspoint.com/natural_language_processing/natural_language_processing_word_sense_disambiguation.htm
: https://link.springer.com/article/10.1007/s12046-019-1206-x



### Dictionary & Thesaurus for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- A **dictionary** is a collection of words and their meanings, pronunciations, usage examples, and other information. A dictionary can be used to look up the meaning of a word, to check its spelling, or to find synonyms or antonyms.
- A **thesaurus** is a specialized dictionary that stores synonyms and antonyms of selected words in a language. A thesaurus can be used to find alternative words with similar or opposite meanings, to enrich the vocabulary, or to avoid repetition.
- In natural language processing (NLP), a dictionary and a thesaurus can be useful resources for various tasks, such as:
  - **Word sense disambiguation**: the process of identifying the correct meaning of a word in a given context, among multiple possible meanings. A dictionary can provide the definitions of different senses, and a thesaurus can provide the related words for each sense.
  - **Text summarization**: the process of creating a concise and informative summary of a longer text. A thesaurus can help to find synonyms or paraphrases for the key words or phrases in the text, to reduce redundancy and increase diversity.
  - **Text generation**: the process of creating natural language text from some input, such as a prompt, a query, or a data source. A dictionary can provide the spelling and grammar rules for the target language, and a thesaurus can provide the word choices and variations for the generated text.
  - **Text analysis**: the process of extracting information and insights from natural language text, such as sentiment, topics, entities, relations, etc. A dictionary can provide the basic linguistic information for the text, such as part-of-speech, morphology, and syntax, and a thesaurus can provide the semantic information, such as synonyms, antonyms, and categories.



### Bootstrapping methods for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods can be applied to various natural language processing (NLP) tasks, such as part-of-speech tagging, named entity recognition, relation extraction, sentiment analysis, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., tags, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., rules, patterns, examples, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., by matching, expanding, scoring, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more things are found, a threshold is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Generative bootstrapping: the model learns a probabilistic distribution over the data and uses it to generate new labels or examples.
  - Discriminative bootstrapping: the model learns a classifier or a function that discriminates between different labels or examples and uses it to assign new labels or examples.
- Bootstrapping methods can benefit from the following advantages :
  - They can reduce the cost and effort of manual annotation.
  - They can exploit the redundancy and diversity of the unlabeled data.
  - They can adapt to new domains or tasks with minimal supervision.
  - They can improve the performance and robustness of the model or the task.
- Bootstrapping methods can also face the following challenges :
  - They can suffer from semantic drift, which is the deviation of the learned things from the original seeds due to noise or ambiguity in the data.
  - They can be sensitive to the quality and quantity of the seeds, which can affect the initial and final results of the bootstrapping process.
  - They can be prone to overfitting or underfitting, which can lead to poor generalization or low coverage of the model or the task.



### Word Similarity using Thesaurus and Distributional methods

- Word similarity is the degree to which two words share a common meaning or are semantically related.
- Thesaurus and distributional methods are two approaches to measure word similarity based on different sources of information.
- Thesaurus methods rely on manually constructed lexical resources, such as WordNet, that group words into synonym sets and organize them into a hierarchical structure of semantic relations.
- Distributional methods rely on large corpora of text, and use the principle that words that occur in similar contexts tend to have similar meanings.
- Thesaurus methods have the advantage of capturing fine-grained semantic distinctions and relations, but they are limited by the coverage and quality of the lexical resources.
- Distributional methods have the advantage of being data-driven and scalable, but they are limited by the sparsity and ambiguity of the word co-occurrences.
- Both methods can be combined to leverage the complementary strengths of each approach.
- Some examples of word similarity tasks are:
  - Finding synonyms and antonyms of a given word
  - Clustering words into semantic categories
  - Creating thesauri and bilingual dictionaries
  - Disambiguating word senses
  - Expanding search queries with related terms



## Unit 4 - BASIC CONCEPTS of Speech Processing

- Speech processing is the study of how humans produce, perceive, and understand speech, as well as how speech can be processed by machines.
- Speech processing involves three major levels of processing: conceptualization, formulation, and articulation.
  - Conceptualization is the process of selecting the words and concepts that convey the intended meaning.
  - Formulation is the process of organizing the words into grammatical and phonological structures.
  - Articulation is the process of producing the sounds of speech using the vocal apparatus.
- Speech production is influenced by various factors, such as the speaker's age, gender, dialect, mood, and context.
- Speech production can be modeled by various theories, such as the motor theory, the cohort theory, and the interactive activation model.
- Speech perception is the process of decoding the acoustic signals of speech and recognizing the words and meanings.
- Speech perception involves various stages, such as auditory processing, phonetic processing, lexical access, and semantic integration.
- Speech perception is influenced by various factors, such as the listener's knowledge, expectations, attention, and context.
- Speech perception can be modeled by various theories, such as the trace model, the fuzzy logical model, and the Bayesian model.
- Speech processing can be applied to various domains, such as speech recognition, speech synthesis, speech enhancement, speech coding, speech analysis, and speech translation.



### Speech Fundamentals

- Speech is a natural mode of communication for humans, and one of the main sources of linguistic data for natural language processing (NLP).
- Speech processing is the subfield of NLP that deals with the analysis, synthesis, and recognition of speech signals and the understanding of spoken language.
- Speech processing involves multiple levels of representation and analysis, such as:
  - Acoustic level: the physical properties of sound waves, such as frequency, amplitude, and duration.
  - Phonetic level: the basic units of speech sounds, such as vowels, consonants, and tones.
  - Phonological level: the patterns and rules of how speech sounds are organized and combined, such as stress, intonation, and syllable structure.
  - Morphological level: the smallest units of meaning in words, such as roots, prefixes, and suffixes.
  - Lexical level: the words and their meanings, such as nouns, verbs, and adjectives.
  - Syntactic level: the structure and order of words in sentences, such as phrases, clauses, and modifiers.
  - Semantic level: the meaning and interpretation of sentences, such as propositions, arguments, and relations.
  - Pragmatic level: the use and function of language in context, such as speech acts, discourse, and dialogue.
- Speech processing tasks can be divided into two main categories: speech synthesis and speech recognition.
  - Speech synthesis is the process of generating speech signals from text or other symbolic inputs, such as emotions, gestures, or images.
  - Speech recognition is the process of converting speech signals into text or other symbolic outputs, such as commands, queries, or actions.
- Speech processing applications include:
  - Text-to-speech (TTS): generating natural-sounding speech from text, such as for reading aloud, assistive technology, or entertainment.
  - Speech-to-text (STT): transcribing speech into text, such as for dictation, captioning, or documentation.
  - Speech translation: translating speech from one language to another, such as for communication, education, or tourism.
  - Speech understanding: extracting information or intent from speech, such as for question answering, dialogue systems, or voice assistants.
  - Speech enhancement: improving the quality or intelligibility of speech, such as for noise reduction, speaker identification, or emotion detection.
  - Speech synthesis and recognition are challenging tasks that require sophisticated models and algorithms, as well as large and diverse datasets of speech and text. Some of the main challenges include:
  - Variability: speech signals vary depending on the speaker, the environment, the channel, the dialect, the accent, the emotion, the style, and the context.
  - Ambiguity: speech signals can have multiple interpretations or meanings, depending on the word, the sentence, the domain, the situation, and the listener.
  - Complexity: speech signals have multiple levels of representation and analysis, each with its own rules and constraints, and often interacting with each other.
  - Creativity: speech signals can be novel, expressive, and dynamic, reflecting the richness and diversity of human language and communication.



### Articulatory Phonetics

- Articulatory phonetics is the branch of phonetics that studies how speech sounds are produced by the human vocal tract .
- Articulatory phonetics is concerned with the movements and positions of the vocal organs (articulators), such as the tongue, lips, jaw, velum, glottis, etc. .
- Articulatory phonetics is also concerned with the airflow through the vocal tract and how it is modulated by the articulators to create different speech sounds .
- Articulatory phonetics can be used to describe and classify speech sounds based on their articulatory features, such as place of articulation, manner of articulation, voicing, etc. .
- Articulatory phonetics can also be used to analyze the phonetic patterns and processes that occur in different languages, such as assimilation, coarticulation, lenition, etc. .
- Articulatory phonetics is an important part of speech processing, as it provides the link between the physical production of speech and the acoustic and perceptual properties of speech sounds .
- Articulatory phonetics can also help in speech synthesis, speech recognition, speech enhancement, speech pathology, and speech education.



### Production And Classification Of Speech Sounds

- Speech sounds are the basic units of human communication that are produced by the vocal organs and perceived by the auditory system.
- The production of a speech sound involves four interrelated processes :
  - Initiation: the generation of an air stream, usually by the lungs, that provides the energy for speech.
  - Phonation: the vibration of the vocal folds in the larynx, which modulates the air stream and creates voiced or voiceless sounds.
  - Oro-nasal process: the opening or closing of the velum, which directs the air stream into either the oral cavity or the nasal cavity, or both, and affects the resonance of the sound.
  - Articulation: the shaping of the air stream by the tongue, lips, teeth, and other articulators in the oral cavity, which creates different types of sounds such as stops, fricatives, affricates, nasals, liquids, and glides.
- Speech sounds are classified into two broad phonetic categories: vowels and consonants.
  - Vowels are speech sounds that are produced with no obstruction or narrowing of the air stream in the vocal tract, and are characterized by their height, backness, roundedness, and length.
  - Consonants are speech sounds that are produced with some degree of constriction or closure of the air stream in the vocal tract, and are characterized by their place, manner, and voicing of articulation.
- Speech sounds are also classified into phonemic categories, which are based on the contrastive function of sounds in a language. Phonemes are the smallest units of sound that can distinguish meaning in a language, and are represented by symbols enclosed in slashes, such as /p/, /b/, /i/, /u/, etc.
- Speech sounds can also be grouped into natural classes, which are sets of sounds that share one or more phonetic features, such as [+voice], [-nasal], [+high], etc. Natural classes are useful for describing the patterns and rules of speech sound distribution and alternation in a language.



### Acoustic Phonetics

- Acoustic phonetics is the branch of phonetics that studies the acoustic properties of speech sounds, such as their frequency, intensity, and duration .
- Acoustic phonetics relies on instruments and methods to record, store, visualize, and analyze the speech signal, such as sound spectrographs, oscilloscopes, and computer software.
- Acoustic phonetics can be used to describe and classify speech sounds in terms of their acoustic features, such as formants, pitch, amplitude, and duration.
- Acoustic phonetics can also be used to investigate the relationship between the acoustic features of speech and other aspects of speech production and perception, such as articulation, phonology, prosody, and dialect variation .
- Acoustic phonetics is an interdisciplinary field that draws on knowledge and methods from physics, mathematics, engineering, psychology, and linguistics .



### Acoustics of Speech Production

- Acoustics of speech production is the study of how speech sounds are generated and modified by the human vocal tract and how they are perceived by the listener.
- Speech production involves a complex interaction of physical, physiological, and cognitive processes that transform linguistic intentions into acoustic signals.
- The acoustic theory of speech production is a model that describes speech as a result of a source of sound energy (e.g., the larynx) modulated by a filter function determined by the shape of the supralaryngeal vocal tract (e.g., the tongue, lips, palate, etc.).
- The source-filter model assumes that the source and the filter are independent of each other, meaning that the source can vary in frequency and intensity without affecting the filter, and vice versa.
- The source of speech can be either voiced or voiceless, depending on whether the vocal folds vibrate or not. Voiced sounds (e.g., vowels, nasals, liquids, etc.) have a periodic source with a fundamental frequency (F0) and harmonics, while voiceless sounds (e.g., fricatives, stops, etc.) have a noise-like source with a flat spectrum.
- The filter function of the vocal tract is determined by its resonant frequencies, which are called formants. Formants are peaks of energy in the speech spectrum that reflect the shape and size of the vocal tract cavities. The first three formants (F1, F2, F3) are usually sufficient to distinguish most speech sounds, especially vowels.
- The filter function can be changed by articulating different speech sounds, such as vowels and consonants. Vowels are produced by varying the position and shape of the tongue and the jaw, which affect the formant frequencies. Consonants are produced by creating constrictions or closures in the vocal tract, which affect the airflow and the source spectrum.
- Speech acoustics can be analyzed using various methods and tools, such as spectrograms, waveforms, pitch contours, intensity curves, etc. These methods can reveal the acoustic features and patterns of speech sounds, such as duration, amplitude, frequency, periodicity, etc.
- Speech acoustics can also be modeled using mathematical equations and computer simulations, such as the source-filter model, the linear predictive coding (LPC) model, the articulatory synthesis model, etc. These models can help understand the relationship between the speech production and perception processes, as well as the effects of noise, distortion, and variability on speech quality and intelligibility.



### Review Of Digital Signal Processing Concepts

Digital signal processing (DSP) is the use of digital processing, such as by computers or more specialized digital signal processors, to perform a wide variety of signal processing operations. The digital signals processed in this manner are a sequence of numbers that represent samples of a continuous variable in a domain such as time, space, frequency, or wavelet.

Some of the basic concepts of DSP are:

- **Data digitizing** – Convert continuous signals to finite discrete digital signals by sampling, quantizing, and encoding . Sampling is the process of taking periodic snapshots of the signal at a fixed rate called the sampling frequency. Quantizing is the process of approximating the sampled values to a finite set of levels called the quantization levels. Encoding is the process of assigning a binary code to each quantization level.
- **Signal analysis** – Analyze the properties and characteristics of the digital signal, such as its amplitude, frequency, phase, spectrum, energy, power, autocorrelation, cross-correlation, etc. Signal analysis can be done in the time domain or the frequency domain. The time domain analysis deals with the signal as a function of time, while the frequency domain analysis deals with the signal as a function of frequency. The Fourier transform is a mathematical tool that can convert a signal from the time domain to the frequency domain and vice versa.
- **Signal processing** – Modify, enhance, or extract information from the digital signal by applying various mathematical operations and algorithms. Some of the common signal processing techniques are filtering, modulation, demodulation, compression, encryption, decryption, error correction, etc. Filtering is the process of removing or attenuating unwanted components from the signal, such as noise, interference, or distortion. Modulation is the process of changing one or more parameters of a carrier signal according to the information signal, such as amplitude, frequency, or phase. Demodulation is the reverse process of modulation, which recovers the information signal from the modulated carrier signal. Compression is the process of reducing the amount of data required to represent the signal, while preserving the essential information. Encryption is the process of transforming the signal into a secret form that can only be understood by authorized parties. Decryption is the reverse process of encryption, which restores the original signal from the encrypted form. Error correction is the process of detecting and correcting errors that may occur during the transmission or storage of the signal.
- **Signal synthesis** – Generate a new digital signal from the existing signal or from scratch by using various methods and algorithms. Some of the common signal synthesis techniques are interpolation, extrapolation, resampling, reconstruction, etc. Interpolation is the process of estimating the values of the signal between the sampled points. Extrapolation is the process of estimating the values of the signal beyond the sampled points. Resampling is the process of changing the sampling rate of the signal, either by increasing or decreasing it. Reconstruction is the process of converting the discrete digital signal back to a continuous analog signal by using a low-pass filter called the reconstruction filter.

These are some of the basic concepts of DSP that are useful for understanding and applying the techniques of speech processing. Speech processing is a subfield of DSP that deals with the analysis, synthesis, recognition, and enhancement of human speech signals. Speech processing has many applications in natural language processing, such as speech recognition, speech synthesis, speech translation, speech coding, speech enhancement, speech emotion recognition, etc.



### Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique for analyzing the frequency content of a signal over time.
- It involves dividing the signal into overlapping segments, applying a window function to each segment, and computing the discrete Fourier transform (DFT) of the windowed segments.
- The result is a two-dimensional representation of the signal, where each point in the time-frequency plane corresponds to the complex amplitude of a particular frequency component at a particular time instant.
- The STFT is useful for speech and audio processing because it can capture the non-stationary and time-varying characteristics of these signals, such as pitch, formants, harmonics, and noise.
- The STFT can also be used as a basis for various signal processing operations, such as filtering, enhancement, compression, recognition, and synthesis.
- The STFT has some limitations, such as the trade-off between time and frequency resolution, the leakage effect due to windowing, and the redundancy of the representation.

Some key concepts and formulas related to the STFT are:

- The window function $w[n]$ is a sequence of length $N$ that is multiplied with each segment of the signal. It should have desirable properties such as being symmetric, smooth, and having a narrow main lobe and low side lobes in the frequency domain. Some common window functions are rectangular, Hamming, Hanning, and Blackman.
- The hop size $H$ is the number of samples between the start of two consecutive segments. It determines the degree of overlap between the segments. A smaller hop size gives a finer time resolution but a larger computational cost. A larger hop size gives a coarser time resolution but a smaller computational cost. A typical choice is $H = N/2$, where $N$ is the window length.
- The analysis frame $x_m[n]$ is the $m$-th segment of the signal $x[n]$, obtained by multiplying the signal with the window function shifted by $mH$ samples, i.e., $x_m[n] = x[n+mH]w[n]$ for $n = 0, 1, \dots, N-1$.
- The STFT $X[m, k]$ is the DFT of the analysis frame $x_m[n]$, i.e., $X[m, k] = \sum_{n=0}^{N-1} x_m[n] e^{-j2\pi nk/N}$ for $k = 0, 1, \dots, N-1$. It can be interpreted as the complex amplitude of the $k$-th frequency bin at the $m$-th time frame.
- The magnitude spectrum $|X[m, k]|$ is the absolute value of the STFT, which indicates the strength of the $k$-th frequency component at the $m$-th time frame. It can be used to visualize the spectral content of the signal over time.
- The phase spectrum $\angle X[m, k]$ is the argument of the STFT, which indicates the phase of the $k$-th frequency component at the $m$-th time frame. It can be used to reconstruct the signal from the STFT using the inverse DFT (IDFT).
- The inverse STFT $x[n]$ is the signal reconstructed from the STFT using the IDFT and the overlap-add method, i.e., $x[n] = \sum_{m=-\infty}^{\infty} x_m[n-mH] = \frac{1}{N} \sum_{m=-\infty}^{\infty} \sum_{k=0}^{N-1} X[m, k] e^{j2\pi nk/N}$ for $n = 0, 1, \dots, L-1$, where $L$ is the length of the signal. The inverse STFT is exact if the window function satisfies the constant overlap-add (COLA) condition, i.e., $\sum_{m=-\infty}^{\infty} w[n-mH] = 1$ for all $n$.



### Filter Bank and LPC Methods for Speech Processing

- Filter bank and LPC methods are two common techniques for extracting features from speech signals for speech recognition or synthesis applications.
- Filter bank methods divide the speech signal into frequency bands and compute the energy or power spectrum of each band. The most popular filter bank method is the mel-frequency cepstral coefficients (MFCC) method, which uses a set of triangular filters that are spaced according to the mel scale, which approximates the human perception of frequency. The MFCC method consists of the following steps:
  - Pre-emphasize the speech signal by applying a high-pass filter to reduce the effect of the vocal tract and enhance the high-frequency components.
  - Divide the speech signal into overlapping frames of 20-40 ms duration, and apply a window function (such as Hamming) to each frame to reduce the discontinuities at the edges.
  - Compute the discrete Fourier transform (DFT) of each frame and obtain the magnitude spectrum.
  - Apply the mel filter bank to the magnitude spectrum and sum the energy in each filter.
  - Take the logarithm of the filter bank energies to mimic the human perception of loudness.
  - Apply the discrete cosine transform (DCT) to the log filter bank energies and retain the first few coefficients (typically 12-20) as the MFCC features. Optionally, append the energy of the frame and the first and second derivatives of the MFCC features to form a feature vector.
- LPC methods model the speech signal as the output of a linear filter driven by an excitation signal. The linear filter represents the vocal tract, and the excitation signal represents the glottal source or the noise source. The LPC method consists of the following steps:
  - Divide the speech signal into frames of 10-30 ms duration, and apply a window function to each frame.
  - Estimate the LPC coefficients of each frame by minimizing the mean squared error between the original signal and the predicted signal. This can be done by solving the Yule-Walker equations or using the Levinson-Durbin algorithm.
  - Use the LPC coefficients to obtain the frequency response of the filter, which corresponds to the formant frequencies of the speech signal.
  - Inverse filter the speech signal by passing it through the inverse of the LPC filter, and obtain the residual signal, which corresponds to the excitation signal.
  - Quantize the LPC coefficients and the residual signal using appropriate coding schemes, such as vector quantization or adaptive differential pulse code modulation (ADPCM).
  - To synthesize the speech signal, reverse the process by using the quantized LPC coefficients and the residual signal to generate the filter and the excitation signal, and pass the excitation signal through the filter.

- Filter bank and LPC methods have different advantages and disadvantages for speech processing. Some of the comparisons are :
  - Filter bank methods are more robust to noise and channel distortions, while LPC methods are more sensitive to these factors.
  - Filter bank methods require more computation and storage than LPC methods, especially for high-dimensional feature vectors.
  - Filter bank methods capture the spectral envelope of the speech signal, while LPC methods capture the spectral peaks of the speech signal.
  - Filter bank methods are more suitable for speaker-independent recognition, while LPC methods are more suitable for speaker-dependent recognition.
  - Filter bank methods are more compatible with hidden Markov models (HMMs), which are widely used for speech recognition, while LPC methods are more compatible with dynamic time warping (DTW), which is an older technique for speech recognition.



## Unit 5 - SPEECH-ANALYSIS

- Speech-analysis is the process of examining spoken language to identify its features, such as words, sounds, intonation, rhythm, and meaning.
- Speech-analysis can be done for various purposes, such as:
  - Transcribing speech into text or other formats
  - Recognizing speakers or languages
  - Synthesizing speech from text or other inputs
  - Analyzing emotions, attitudes, or intentions of speakers
  - Evaluating the quality, clarity, or effectiveness of speech
  - Enhancing or modifying speech signals
- Speech-analysis involves different levels of representation and processing, such as:
  - Acoustic level: the physical properties of speech sounds, such as frequency, amplitude, and duration
  - Phonetic level: the articulatory and perceptual characteristics of speech sounds, such as place, manner, and voicing of consonants, and height, backness, and roundness of vowels
  - Phonological level: the patterns and rules of speech sounds in a language, such as stress, tone, and syllable structure
  - Morphological level: the structure and formation of words from smaller units, such as roots, prefixes, and suffixes
  - Lexical level: the meaning and usage of words in a language, such as synonyms, antonyms, and collocations
  - Syntactic level: the structure and formation of sentences from words, such as word order, agreement, and case
  - Semantic level: the meaning and interpretation of sentences in a language, such as truth conditions, entailment, and presupposition
  - Pragmatic level: the meaning and use of sentences in a context, such as speech acts, implicature, and politeness
- Speech-analysis requires various methods and techniques, such as:
  - Signal processing: the manipulation and transformation of speech signals, such as filtering, sampling, and encoding
  - Feature extraction: the identification and measurement of relevant features from speech signals, such as pitch, energy, and formants
  - Pattern recognition: the classification and matching of speech features to predefined categories, such as phonemes, words, or speakers
  - Statistical modeling: the representation and estimation of speech features and patterns using mathematical models, such as hidden Markov models, neural networks, or Bayesian networks
  - Natural language processing: the analysis and generation of natural language from speech features and patterns, such as parsing, semantic analysis, or text-to-speech synthesis
  - Machine learning: the adaptation and improvement of speech-analysis methods and models using data and feedback, such as supervised learning, unsupervised learning, or reinforcement learning



### Features for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, intention, and content.
- Speech analysis is a subfield of natural language processing (NLP), which is the branch of computer science and artificial intelligence that deals with understanding and generating natural language  .
- Speech analysis involves various techniques and applications, such as speech recognition, speech synthesis, speech segmentation, speech enhancement, speech coding, speech translation, speech summarization, speech emotion recognition, speaker identification, and speech diarization.
- Speech analysis can be performed at different levels of linguistic representation, such as acoustic, phonetic, phonological, lexical, syntactic, semantic, pragmatic, and discourse.
- Speech analysis can benefit from various features extracted from speech signals, such as pitch, intensity, duration, formants, spectral properties, prosody, voice quality, articulation, and pauses.
- Speech analysis can also use features derived from natural language processing techniques, such as part-of-speech tags, word embeddings, n-grams, parse trees, named entities, sentiment scores, and topic models.
- Speech analysis can be applied to various domains and tasks, such as human-computer interaction, voice assistants, speech therapy, education, health care, security, forensics, entertainment, and social media .



### Feature Extraction And Pattern Comparison Techniques for Speech Analysis

- Feature extraction is the process of transforming the speech signal into a set of features that represent the characteristics of the speech and the speaker.
- Feature extraction is important for speech analysis because it reduces the dimensionality and complexity of the speech signal, and enhances the discriminative and robust aspects of the speech.
- Some of the common feature extraction techniques for speech analysis are:
  - Linear Predictive Coding (LPC): This technique models the speech signal as a linear combination of past samples, and estimates the coefficients of the linear predictor using the autocorrelation method or the Levinson-Durbin algorithm . The LPC coefficients capture the spectral envelope of the speech signal, and can be used for speech synthesis, speech coding, and speaker recognition.
  - Mel-Frequency Cepstral Coefficients (MFCC): This technique computes the cepstral coefficients of the speech signal after applying a mel-scale filter bank to the spectrum of the signal . The MFCC coefficients represent the spectral shape of the speech signal, and are widely used for speech recognition, speaker recognition, and speech enhancement.
  - Linear Predictive Cepstral Coefficients (LPCC): This technique computes the cepstral coefficients of the speech signal using the LPC coefficients as the input. The LPCC coefficients are similar to the MFCC coefficients, but have a lower computational complexity and a higher sensitivity to noise.
  - Unique Mapped Real Transform (UMRT): This technique transforms the speech signal into a set of real-valued coefficients using a complex-valued filter bank and a mapping function. The UMRT coefficients are invariant to the phase of the speech signal, and can be used for speaker recognition and speech recognition.
  - Real Cepstral Coefficients (RCC): This technique computes the cepstral coefficients of the speech signal using the real part of the spectrum of the signal. The RCC coefficients are also invariant to the phase of the speech signal, and can be used for speaker recognition and speech recognition.

- Pattern comparison is the process of matching the features of an unknown speech signal with the features of a known speech signal, and computing a similarity or distance measure between them.
- Pattern comparison is important for speech analysis because it enables the identification or verification of the speech or the speaker, and the recognition or understanding of the speech content.
- Some of the common pattern comparison techniques for speech analysis are:
  - Dynamic Time Warping (DTW): This technique aligns two sequences of features by finding the optimal warping path that minimizes the cumulative distance between them . DTW can handle the variations in the temporal and spectral aspects of the speech signal, and can be used for speech recognition and speaker recognition.
  - Gaussian Mixture Model (GMM): This technique models the distribution of features of a speech signal as a weighted sum of multivariate Gaussian components, and estimates the parameters of the model using the expectation-maximization algorithm . GMM can capture the statistical characteristics of the speech signal, and can be used for speaker recognition and speech recognition.
  - Support Vector Machine (SVM): This technique finds the optimal hyperplane that separates the features of two classes of speech signals, and uses the hyperplane as a decision boundary for classification . SVM can handle the nonlinear and high-dimensional aspects of the speech signal, and can be used for speaker recognition and speech recognition.
  - Neural Network (NN): This technique consists of a network of interconnected nodes that process the features of a speech signal using nonlinear activation functions and learning algorithms . NN can learn the complex and dynamic patterns of the speech signal, and can be used for speech recognition, speaker recognition, and speech synthesis.
  - Vector Quantization (VQ): This technique partitions the feature space of a speech signal into a finite number of regions or clusters, and assigns a representative vector or codebook to each cluster . VQ can reduce the redundancy and variability of the speech signal, and can be used for speech coding, speech recognition, and speaker recognition.



### Speech Distortion Measures

- Speech distortion measures are methods to quantify the amount and type of distortion that occurs in speech signals due to various factors, such as hearing loss, noise, hearing aids, or speech processing algorithms.
- Speech distortion measures can be classified into two categories: subjective and objective.
  - Subjective measures are based on human perception and evaluation of speech quality, intelligibility, or naturalness. They require listening tests with human subjects, which can be time-consuming, costly, and variable.
  - Objective measures are based on mathematical or statistical calculations that compare the original and distorted speech signals, or their features, such as spectra, cepstra, or pitch. They do not require human listeners, but they may not always correlate well with subjective measures or reflect the actual impact of distortion on speech communication.
- Some examples of speech distortion measures are:
  - Signal-to-noise ratio (SNR): the ratio of the average power of the speech signal to the average power of the noise signal, expressed in decibels (dB). A higher SNR indicates less noise and better speech quality.
  - Segmental SNR: the SNR calculated for short segments of speech, such as frames or syllables, rather than for the whole speech signal. It can capture the local variations of noise and speech levels, and reflect the perceptual importance of different speech segments.
  - SNR loss: the difference between the SNR of the original speech signal and the SNR of the distorted speech signal, expressed in dB. It represents the amount of distortion introduced by a factor, such as hearing loss or hearing aid. A higher SNR loss indicates more distortion and worse speech quality.
  - Spectral distortion: the difference between the spectra of the original and distorted speech signals, measured by various metrics, such as log spectral distance, spectral tilt, or spectral slope. It reflects the changes in the frequency content and envelope of the speech signal due to distortion.
  - Cepstral distortion: the difference between the cepstra of the original and distorted speech signals, measured by various metrics, such as cepstral distance, cepstral mean, or cepstral variance. It reflects the changes in the spectral shape and dynamics of the speech signal due to distortion.
  - Pitch distortion: the difference between the pitch values or contours of the original and distorted speech signals, measured by various metrics, such as pitch error, pitch jitter, or pitch drift. It reflects the changes in the fundamental frequency and prosody of the speech signal due to distortion.
  - Articulation index (AI): a measure of the audibility of speech sounds in a given listening condition, based on the assumption that speech intelligibility depends on the amount of speech information that is audible to the listener. It ranges from 0 to 1, where 0 means no speech information is audible, and 1 means all speech information is audible. A higher AI indicates better speech intelligibility.
  - Speech intelligibility index (SII): a measure of the intelligibility of speech in a given listening condition, based on the assumption that speech intelligibility depends on the amount of speech information that is transmitted to the listener. It ranges from 0 to 1, where 0 means no speech information is transmitted, and 1 means all speech information is transmitted. A higher SII indicates better speech intelligibility. It is a generalization of the AI that can account for various factors, such as speech level, noise level, frequency weighting, and hearing loss.
  - Perceptual evaluation of speech quality (PESQ): a measure of the perceived quality of speech in a given listening condition, based on a model of human auditory perception and cognition. It ranges from -0.5 to 4.5, where -0.5 means very poor speech quality, and 4.5 means excellent speech quality. A higher PESQ indicates better speech quality. It is a standardized objective measure that can correlate well with subjective measures of speech quality.



### Mathematical And Perceptual Speech Analysis

- Mathematical speech analysis is the study of how human language and mathematics relate to each other and to the real world. It involves using mathematical models and methods to describe, explain, and predict various aspects of speech, such as phonology, morphology, syntax, and semantics .
- Perceptual speech analysis is the study of how human listeners perceive and process speech sounds and meanings. It involves using psychological and physiological principles to account for the effects of hearing, attention, memory, and cognition on speech perception and comprehension.
- Some of the topics and techniques that are relevant for mathematical and perceptual speech analysis are:

  - **Fourier analysis**: a method of decomposing a complex signal into a sum of simple sinusoidal waves, each with a different frequency, amplitude, and phase. Fourier analysis is useful for representing the spectral properties of speech sounds and for applying filters and transformations to speech signals.
  - **Markov models**: a type of probabilistic model that assumes that the state of a system at a given time depends only on the state of the system at the previous time. Markov models are useful for modeling the sequential and stochastic nature of speech production and recognition, as well as for capturing the statistical regularities of speech units, such as phonemes, words, and sentences.
  - **Linear predictive coding (LPC)**: a method of estimating the spectral envelope of a speech signal by finding the coefficients of a linear filter that minimizes the prediction error between the original signal and the filtered signal. LPC is useful for reducing the redundancy and noise in speech signals and for extracting the formant frequencies and bandwidths that characterize the vocal tract resonances.
  - **Perceptual linear predictive (PLP)**: a variant of LPC that incorporates three aspects of human auditory perception: the critical-band spectral resolution, the equal-loudness curve, and the intensity-loudness power law. PLP is useful for deriving an estimate of the auditory spectrum that is more consistent with how human listeners perceive speech sounds.
  - **Speech and gesture**: the study of how speakers use their hands and body movements to accompany and enhance their verbal communication. Speech and gesture are useful for analyzing how speakers convey and construct mathematical proofs, as well as how listeners interpret and evaluate them.



### Log–Spectral Distance

- The log-spectral distance (LSD), also referred to as log-spectral distortion or root mean square log-spectral distance, is a distance measure (expressed in dB) between two spectra .
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as :

$$
D_{LS} = \frac{1}{2\pi} \int_{-\pi}^{\pi} \left[ 10 \log_{10} \frac{P(\omega)}{P^(\omega)} \right]^2 d\omega
$$

- Unlike the Itakura–Saito distance, the log-spectral distance is symmetric .
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum .
- The log-spectral distance can be used to measure the quality of speech synthesis or speech recognition systems, by comparing the spectra of the original and the synthesized or recognized speech signals .
- The log-spectral distance can also be used to measure the similarity of speech signals from different speakers, by comparing the spectra of their vocal tract transfer functions .
- The log-spectral distance can be computed efficiently using the fast Fourier transform (FFT) or the discrete cosine transform (DCT) .



### Cepstral Distances for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Cepstral distance is a measure of the similarity or dissimilarity between two speech frames based on their cepstral coefficients.
- Cepstral coefficients are obtained by applying the inverse Fourier transform to the logarithm of the spectrum of a speech signal .
- Cepstral distance can be used for various applications in speech analysis, such as endpoint detection, emotion recognition, speaker identification, and voice quality assessment  .
- One of the most common cepstral distance measures is the Euclidean distance between mel frequency cepstral coefficients (MFCC), which are based on a perceptually motivated frequency scale.
- Cepstral distance can be combined with other features, such as speech energy, to improve the performance of speech analysis tasks.
- Cepstral distance can also be normalized or weighted to account for the perceptual significance of different cepstral coefficients.



### Weighted Cepstral Distances And Filtering for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log spectrum of the signal.
- Cepstral distance can be used for speech recognition, speaker recognition, speech enhancement, and speech synthesis applications.
- A simple cepstral distance measure is the Euclidean distance between the cepstral coefficients of two signals, but this may not be optimal for speech recognition because it does not account for the different importance and variability of each coefficient.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to each cepstral coefficient according to some criterion, such as the inverse variance, the log-index, or the perceptual relevance of the coefficient.
- A weighted cepstral distance measure can improve the performance of speech recognition systems by reducing the mismatch between the training and testing conditions, enhancing the discriminative power of the cepstral features, and reducing the computational complexity of the distance computation.
- A common method to obtain the weights for the cepstral coefficients is to use a statistical approach, such as the maximum likelihood estimation or the minimum classification error criterion, based on a training set of speech data.
- Another method to obtain the weights for the cepstral coefficients is to use a perceptual approach, such as the mel-scale or the bark-scale, based on the human auditory system.
- A weighted cepstral distance measure can be combined with other techniques, such as dynamic time warping, vector quantization, or hidden Markov models, to achieve robust and accurate speech recognition systems.



### Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the similarity or dissimilarity between two short-time spectra of speech signals .
- They are used to compare the observed speech signal with the reference speech signal in speech recognition systems .
- They are based on the assumption that the speech signal can be modeled by a probability distribution, such as a Gaussian distribution .
- Some common likelihood distortions are:
  - Log likelihood ratio (LLR): the negative logarithm of the ratio of the probability densities of the observed and reference spectra .
  - Likelihood ratio (LR): the ratio of the probability densities of the observed and reference spectra .
  - Itakura-Saito (IS): the difference between the logarithms of the probability densities of the observed and reference spectra, minus the logarithm of their ratio .
  - Cepstral (CEP): the squared Euclidean distance between the cepstral coefficients of the observed and reference spectra .
  - Weighted likelihood ratio (WLR): the LLR weighted by a perceptual weighting function that emphasizes the spectral regions that are more important for speech perception .
  - Weighted slope metric (WSM): the squared Euclidean distance between the slopes of the log spectra of the observed and reference spectra, weighted by a perceptual weighting function .
- The choice of the likelihood distortion affects the performance of the speech recognition system .
- Some factors that influence the performance are:
  - The spectral resolution and frequency warping of the spectra .
  - The inclusion or exclusion of suprasegmental information, such as energy, gain, and loudness .
  - The perceptual relevance and robustness of the distortion measure .
- According to a comparative study by Lee and Rabiner, the LLR and WSM distortion measures gave the highest recognition accuracy, while the IS distortion measure gave the lowest score .
- The WLR distortion measure did not perform as well as its unweighted counterpart .
- The addition of suprasegmental energy information helped the recognition performance, while the use of gain and loudness degraded the performance .
- The bark-scale frequency warping did not perform as well as its unwarped counterpart for the bandlimited telephone data set .



### Spectral Distortion Using A Warped Frequency Scale

- Spectral distortion is the difference between the original and the reconstructed speech spectrum, which affects the quality and intelligibility of speech.
- A warped frequency scale is a nonlinear transformation of the frequency axis that aims to match the human perception of sound, such as the mel scale or the bark scale.
- Warping the frequency scale can reduce the spectral distortion by emphasizing the important spectral features, such as formants, and de-emphasizing the less important ones, such as high-frequency noise.
- A common method to warp the frequency scale is to use an all-pass filter, which preserves the magnitude spectrum but changes the phase spectrum. The phase response of the all-pass filter defines the warped frequency scale.
- A popular technique to analyze and synthesize speech on a warped frequency scale is the cepstral analysis, which converts the speech spectrum into a set of cepstral coefficients that represent the spectral envelope and the excitation source.
- Cepstral analysis on a warped frequency scale can be performed by applying the inverse Fourier transform to the log-magnitude spectrum of the speech signal after warping the frequency axis by the all-pass filter.
- Cepstral synthesis on a warped frequency scale can be performed by applying the Fourier transform to the cepstral coefficients after unwarping the frequency axis by the inverse all-pass filter, and then exponentiating the result to obtain the magnitude spectrum of the speech signal.
- Cepstral analysis synthesis on a warped frequency scale can reduce the spectral distortion and the data rate compared to the conventional cepstral or linear predictive coding (LPC) vocoders, as well as improve the perceived quality of speech.



### LPC for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- LPC stands for Linear Predictive Coding, which is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model .
- LPC analyzes the speech signal by estimating the formants, which are the resonant frequencies of the vocal tract, and removing their effects from the speech signal, leaving behind the residual signal, which contains the pitch and the noise components.
- The process of removing the formants is called inverse filtering, and the residual signal is obtained by subtracting the filtered modeled signal from the original speech signal.
- The linear predictive model assumes that the current sample of the speech signal can be approximated as a linear combination of the previous samples, plus some error term .
- The coefficients of the linear combination are called the LPC coefficients, or the prediction coefficients, and they can be obtained by minimizing the mean squared error between the original signal and the predicted signal .
- The LPC coefficients can be used to reconstruct the spectral envelope of the speech signal, which is a smooth curve that approximates the peaks and valleys of the frequency spectrum .
- The LPC coefficients can also be converted to the reflection coefficients, which are the ratios of the backward and forward traveling waves in a lossless transmission line model of the vocal tract .
- The reflection coefficients have some advantages over the LPC coefficients, such as being more stable, having a smaller dynamic range, and being more suitable for quantization and transmission .
- The residual signal can be further processed to extract the pitch and the noise components, which can be used to synthesize the speech signal by adding them to the filtered modeled signal .
- The synthesis of the speech signal from the LPC coefficients, the pitch, and the noise is called LPC synthesis, and it can produce intelligible speech with a low bit rate .
- LPC is the most widely used method in speech coding and speech synthesis, and it has many applications, such as voice over IP, speech recognition, speech enhancement, and speech modification .



### PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting useful information from speech signals, such as the speaker identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction methods that can represent the speech signals in a compact and discriminative way, while capturing the relevant characteristics of the speech production and perception.
- PLP and MFCC are two popular feature extraction methods for speech analysis, based on different models of the human auditory system.
- PLP stands for Perceptual Linear Prediction, and it is a method that applies a linear predictive analysis to the frequency spectrum of the speech signal, after applying a psychoacoustic model that mimics the human hearing sensitivity and frequency resolution .
- MFCC stands for Mel Frequency Cepstral Coefficients, and it is a method that computes the cepstral coefficients of the speech signal, after applying a filter bank that approximates the human auditory system's nonlinear frequency scaling, known as the mel scale .
- Both PLP and MFCC aim to reduce the dimensionality of the speech signal and to enhance the features that are relevant for speech recognition and speaker identification.
- PLP and MFCC differ in the way they model the human auditory system, and in the way they compute the cepstral coefficients.
- PLP uses an all-pole model to represent the spectrum of the speech signal, while MFCC uses a discrete cosine transform (DCT) to obtain the cepstral coefficients .
- PLP also applies an equal-loudness curve and an intensity-loudness power law to the spectrum, to account for the human perception of loudness at different frequencies .
- MFCC applies a logarithmic function to the filter bank outputs, to account for the human perception of loudness as a logarithmic function of intensity .
- PLP and MFCC have different advantages and disadvantages for speech analysis, depending on the application and the data.
- PLP is more robust to noise and channel distortion, as it models the spectrum more accurately and smoothly .
- MFCC is more sensitive to fine spectral details, as it preserves the high-frequency information better than PLP .
- PLP and MFCC can be combined or modified to improve their performance, such as using PLP-RASTA, which applies a temporal filtering to the PLP coefficients to reduce the effects of noise and channel variation , or using delta and delta-delta features, which capture the dynamic information of the speech signal by computing the first and second derivatives of the cepstral coefficients .



### Time Alignment And Normalization for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Time alignment is the process of finding the optimal alignment between two speech signals that are related by some transformation, such as speaker variation, speaking rate variation, or noise distortion .
- Time alignment is useful for many applications of speech analysis, such as speaker recognition, voice conversion, speech synthesis, and speech recognition .
- Time alignment can be achieved by using a measure of dissimilarity between speech events, such as spectral distance, and minimizing the total dissimilarity between the aligned signals using a dynamic programming algorithm, such as dynamic time warping (DTW) or hidden Markov model (HMM)  .
- Time alignment can be improved by using some modifications, such as refinement, normalization, and comparisons between the preceding and the following frames, to reduce the alignment error and ensure sound correspondence between the signals.
- Normalization is the process of reducing the variability of speech signals that is due to speaker-specific factors, such as vocal tract size, pitch, and accent, and enhancing the variability that is due to linguistic factors, such as phonetic contrast and prosody.
- Normalization is important for speech analysis, as it allows listeners and machines to recognize words and meanings across different speakers and speaking conditions.
- Normalization can be achieved by using various methods, such as acoustic scaling, vocal tract length normalization, speaker adaptation, and perceptual normalization, that aim to transform the speech signals or the features extracted from them to a common or canonical representation .



### Dynamic Time Warping

- Dynamic Time Warping (DTW) is an algorithm for measuring the similarity between two temporal sequences, such as speech signals, that may vary in speed or length.
- DTW can align two sequences by finding the optimal warping path that minimizes the distance between them.
- DTW can be used for speech recognition, speaker verification, gesture recognition, data mining, financial markets, etc .
- DTW works by constructing a matrix of distances between each pair of elements from the two sequences, and then finding the shortest path from the first pair to the last pair that satisfies some constraints.
- The constraints are: 
  - Boundary condition: the path must start at the first pair and end at the last pair.
  - Continuity: the path can only move one step forward, one step diagonally, or one step downward at each step.
  - Monotonicity: the path cannot move backward in time.
- The optimal warping path can be found using dynamic programming, by computing the cumulative distance matrix and then backtracking from the last pair to the first pair.
- The similarity score between the two sequences is the total distance along the optimal warping path.
- DTW can handle non-linear distortions and different sampling rates, but it is computationally expensive and sensitive to noise.
- DTW can be improved by using different distance measures, pruning techniques, lower bounding methods, and dimensionality reduction methods.



### Multiple Time – Alignment Paths for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications, such as speech recognition, speech synthesis, voice conversion, speech to lips synchronization, and articulatory-to-acoustic mapping  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or temporal variations  .
- One common method for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the cumulative distance between the frames.
- DTW can be implemented using various algorithms, such as the classical dynamic programming, the ordered graph search, or the multiview temporal alignment by dependence maximization in the latent space .
- However, DTW may not be able to find the optimal alignment path when there are multiple possible paths with similar distances, or when there are nonlinear or non-monotonic relationships between the time series .
- Therefore, some methods have been proposed to find multiple time-alignment paths, such as the multi-path DTW, the multi-scale DTW, the multi-view DTW, or the multi-modal DTW .
- These methods aim to capture the diversity and variability of the time series, and to find the most relevant and consistent alignment paths among them .
- Multiple time-alignment paths can be useful for improving the performance and robustness of the applications that rely on time alignment, such as enhancing the quality and naturalness of the speech synthesis or voice conversion, or increasing the accuracy and reliability of the articulatory-to-acoustic mapping .



### SPEECH MODELING

- Speech modeling is the process of representing speech signals in a mathematical or statistical way that captures the relevant information and patterns in the speech data.
- Speech modeling is an important task in natural language processing (NLP), which is a branch of artificial intelligence that deals with the interaction between computers and human languages  .
- Speech modeling can be used for various applications, such as speech recognition, speech synthesis, speech enhancement, speech segmentation, speech emotion recognition, speaker identification, and speech translation  .
- Speech modeling can be divided into two main types: acoustic modeling and language modeling.
  - Acoustic modeling is the process of mapping speech signals to a sequence of acoustic units, such as phonemes, syllables, or words. Acoustic modeling involves extracting features from the speech signals, such as pitch, energy, spectral, and cepstral features, and using statistical models, such as hidden Markov models, Gaussian mixture models, or neural networks, to estimate the probability of each acoustic unit given the speech features.
  - Language modeling is the process of estimating the probability of a sequence of words or symbols in a natural language, such as English, Chinese, or Arabic. Language modeling involves collecting a large corpus of text or speech data, and using statistical models, such as n-gram models, neural network models, or transformer models, to learn the patterns and rules of the language, such as syntax, semantics, and pragmatics.
- Speech modeling can be evaluated using various metrics, such as accuracy, perplexity, word error rate, mean opinion score, and subjective tests, depending on the application and the goal of the speech modeling.



### Hidden Markov Models for Speech Analysis

- Hidden Markov Models (HMMs) are a statistical framework for modeling sequential data, such as speech signals, where the underlying states of the system are hidden or unobservable.
- HMMs can capture the probabilistic dependencies between the observed features and the hidden states, and allow for efficient inference and learning algorithms .
- HMMs are widely used for speech recognition tasks, where the goal is to convert a speech signal into a sequence of words or phonemes .
- HMMs for speech recognition consist of three main components:
  - An acoustic model, which defines the probability distribution of the observed features (such as spectral or cepstral coefficients) given a hidden state (such as a phoneme or a sub-phonetic unit).
  - A language model, which defines the probability distribution of the sequence of words or phonemes given the previous words or phonemes.
  - A lexicon, which defines the mapping between words and phonemes.
- HMMs for speech recognition can be trained using various methods, such as maximum likelihood estimation, expectation-maximization, or discriminative training .
- HMMs for speech recognition can be evaluated using various metrics, such as word error rate, phoneme error rate, or accuracy.
- HMMs for speech recognition have some advantages and disadvantages :
  - Advantages:
    - They can model complex and non-stationary speech signals with a relatively simple and compact representation.
    - They can handle variable-length and noisy speech signals with robustness and flexibility.
    - They can incorporate prior knowledge and constraints from the language model and the lexicon.
    - They can be easily extended and adapted to different tasks and domains.
  - Disadvantages:
    - They rely on the independence assumption, which means that the observed features and the hidden states are independent of each other given the previous state. This can limit the expressive power and accuracy of the model.
    - They require a large amount of labeled data for training, which can be costly and time-consuming to obtain.
    - They can suffer from overfitting or underfitting problems, depending on the choice of the model parameters and the training method.
    - They can be outperformed by newer and more advanced methods, such as deep neural networks, which can learn more complex and nonlinear features and dependencies from the data.



### Markov Processes for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- A Markov process is a stochastic process that models the evolution of a system that changes its state over time in a probabilistic way .
- A Markov process has two main properties :
  - The system can only be in one of a finite or countable number of states at any given time.
  - The transition from one state to another depends only on the current state and not on the previous history of the system. This is called the Markov property or memorylessness.
- A Markov process can be represented by a state diagram, where each node is a state and each edge is a transition with a probability .
- A Markov process can be classified into two types :
  - A Markov chain is a Markov process where the state space is discrete and the time parameter is discrete or continuous.
  - A Markov random field is a Markov process where the state space is continuous and the time parameter is discrete or continuous.
- Markov processes are widely used in natural language processing (NLP) to model the patterns and dependencies of natural language at different levels, such as characters, words, sentences, and documents   .
- Some of the applications of Markov processes in NLP are   :
  - Text generation: Markov processes can be used to generate realistic-looking text based on a sample document by using the probabilities of transitions between words or characters.
  - Part-of-speech tagging: Markov processes can be used to assign a grammatical category to each word in a sentence by using the probabilities of transitions between tags and words.
  - Speech recognition: Markov processes can be used to recognize the spoken words in an audio signal by using the probabilities of transitions between sounds and words.
  - Machine translation: Markov processes can be used to translate a text from one language to another by using the probabilities of transitions between words or phrases in different languages.
  - Information extraction: Markov processes can be used to extract relevant information from a text by using the probabilities of transitions between words or entities.
  - Text summarization: Markov processes can be used to generate a concise summary of a text by using the probabilities of transitions between sentences or concepts.
- One of the most popular Markov models used in NLP is the hidden Markov model (HMM), which is a Markov process that has two layers of states: the hidden states and the observed states  .
- The hidden states are the underlying states of the system that are not directly observable, but influence the observed states  .
- The observed states are the states of the system that are directly observable, but depend on the hidden states  .
- An HMM can be represented by a state diagram, where each node is a hidden state and each edge is a transition with a probability, and each hidden state is associated with a probability distribution over the observed states  .
- An HMM can be used to solve three main problems in NLP  :
  - Evaluation: Given an HMM and a sequence of observed states, compute the probability of the sequence being generated by the HMM.
  - Decoding: Given an HMM and a sequence of observed states, find the most likely sequence of hidden states that generated the observed states.
  - Learning: Given a sequence of observed states, find the optimal parameters of the HMM that maximize the probability of the sequence being generated by the HMM.
- An HMM can be trained using various algorithms, such as the forward-backward algorithm, the Viterbi algorithm, and the Baum-Welch algorithm  .



### HMMs for Speech Analysis

- Hidden Markov Models (HMMs) are a statistical framework for modeling time-varying spectral vector sequences, such as speech signals .
- HMMs assume that the speech signal is generated by a Markov process with unobservable (hidden) states, and that each state produces an observable output according to some probability distribution.
- HMMs can be used for speech recognition, speech synthesis, speech segmentation, and speech enhancement  .
- HMMs have some advantages, such as:
  - They can capture the temporal dynamics and variability of speech signals .
  - They can be trained from data using efficient algorithms, such as the Baum-Welch algorithm .
  - They can be adapted, interpolated, and modified to model different voice characteristics, speaking styles, or emotions .
- HMMs also have some limitations, such as:
  - They rely on the independence assumption, which means that the current state depends only on the previous state, and that the current observation depends only on the current state  .
  - They require a large amount of training data to estimate the model parameters accurately .
  - They may not capture the fine details and naturalness of speech signals, especially in speech synthesis  .



### Evaluation for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis can be divided into two main tasks: speech recognition and speech understanding.
- Speech recognition is the task of converting speech signals into text or other symbolic representations, such as phonetic transcriptions, word sequences, etc.
- Speech understanding is the task of interpreting the meaning and intention of the speech signals, such as the speaker's goal, attitude, sentiment, etc.
- Speech analysis can be performed using different methods, such as acoustic, linguistic, or statistical models, or a combination of them.
- Speech analysis can be applied to various domains, such as human-computer interaction, speech synthesis, speech translation, speech enhancement, speech verification, etc.
- Speech analysis can be evaluated using different metrics, such as accuracy, precision, recall, F1-score, word error rate, etc.
- Speech analysis can also be evaluated qualitatively, such as by human judges, user satisfaction, etc.



### Optimal State Sequence for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Speech analysis is the process of extracting meaningful information from speech signals, such as words, emotions, speaker identity, etc.
- Speech analysis can be performed using various techniques, such as signal processing, machine learning, natural language processing, etc.
- One of the common techniques for speech analysis is to use hidden Markov models (HMMs), which are probabilistic models that can capture the sequential and temporal dependencies of speech signals.
- HMMs consist of a set of states, each associated with a probability distribution over the observations, and a set of transition probabilities between the states.
- HMMs can be used to model speech signals as a sequence of observations, each generated by one of the states, and to infer the most likely sequence of states that produced the observations, which is called the optimal state sequence.
- The optimal state sequence can be useful for various speech-related tasks, such as speech recognition, speaker identification, speech segmentation, etc.
- The optimal state sequence can be computed using various algorithms, such as the Viterbi algorithm, the forward-backward algorithm, the Baum-Welch algorithm, etc.
- The Viterbi algorithm is a dynamic programming algorithm that finds the optimal state sequence by maximizing the joint probability of the observations and the state sequence, given the HMM parameters.
- The forward-backward algorithm is a recursive algorithm that computes the forward and backward probabilities, which are the probabilities of the partial state sequences up to and from a given time point, given the observations and the HMM parameters.
- The Baum-Welch algorithm is an iterative algorithm that estimates the HMM parameters by maximizing the likelihood of the observations, given the initial HMM parameters. It uses the forward-backward algorithm to compute the expected counts of the state transitions and the state emissions, and updates the parameters accordingly.
- The optimal state sequence can be affected by various factors, such as the number and type of states, the observation distribution, the transition probabilities, the initial state probabilities, the noise level, the length of the observation sequence, etc.
- The optimal state sequence can be evaluated using various metrics, such as the accuracy, the error rate, the perplexity, the log-likelihood, etc.



### Viterbi Search for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Viterbi search is an algorithm that finds the most likely sequence of hidden states in a Hidden Markov Model (HMM) given a sequence of observed events .
- Viterbi search is widely used in speech analysis applications, such as speech recognition, speech synthesis and speech enhancement  .
- Viterbi search is based on the principle of dynamic programming, which means that it breaks down the problem into smaller subproblems and stores the intermediate results in a table.
- Viterbi search consists of three main steps: initialization, recursion and termination.
  - Initialization: Set the initial probabilities for the first state of the sequence, based on the initial state distribution and the observation likelihood.
  - Recursion: For each subsequent state, compute the maximum probability of reaching that state from any previous state, based on the transition probabilities and the observation likelihood. Store the maximum probability and the corresponding previous state in the table.
  - Termination: Find the maximum probability and the corresponding state for the last state of the sequence. Trace back the previous states from the table to obtain the most likely sequence of hidden states.
- Viterbi search can be extended to handle multiple observations, such as microphone array signals, by using a 3-D Viterbi search that considers the spatial information of the sound sources.
- Viterbi search can be improved by using smoothing techniques, such as interpolation or back-off, to handle unknown or rare events.



### Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a Hidden Markov Model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulae.
- The forward-backward procedure computes the posterior probabilities of the hidden states given the observations using dynamic programming. These probabilities are also called the forward and backward variables, denoted by $\alpha_t(i)$ and $\beta_t(i)$, respectively.
- The re-estimation formulae update the parameters of the HMM using the forward and backward variables and the observed feature vectors. The parameters include the initial state probabilities $\pi_i$, the state transition probabilities $a_{ij}$, and the emission probabilities $b_j(k)$.
- The re-estimation formulae are derived by applying the principle of maximum likelihood and using the Lagrange multipliers to enforce the constraints on the probabilities.
- The re-estimation formulae are as follows :

$$\hat{\pi}_i = \frac{\alpha_1(i)\beta_1(i)}{\sum_{j=1}^N \alpha_1(j)\beta_1(j)}$$

$$\hat{a}_{ij} = \frac{\sum_{t=1}^{T-1} \alpha_t(i) a_{ij} b_j(x_{t+1}) \beta_{t+1}(j)}{\sum_{t=1}^{T-1} \alpha_t(i) \beta_t(i)}$$

$$\hat{b}_j(k) = \frac{\sum_{t=1}^T \alpha_t(j) \beta_t(j) \delta(x_t, k)}{\sum_{t=1}^T \alpha_t(j) \beta_t(j)}$$

where $\delta(x_t, k)$ is 1 if $x_t = k$ and 0 otherwise.

- The algorithm starts with an initial guess of the parameters and repeats the following steps until convergence or a predefined number of iterations is reached :

  - Step 1: For each observation sequence, compute the forward and backward variables using the current parameters.
  - Step 2: For each parameter, compute the re-estimation using the forward and backward variables and the observation sequences.
  - Step 3: Replace the current parameters with the re-estimated ones.

- The algorithm is guaranteed to increase the likelihood of the observation sequences at each iteration, and converges to a local maximum of the likelihood function.
- The algorithm can be applied to discrete or continuous HMMs, depending on the type of the emission probabilities.



### Implementation Issues

- Speech recognition is the process of converting spoken words into text or commands that can be understood by a computer system.
- Speech recognition has many applications, such as voice assistants, dictation, transcription, authentication, and accessibility.
- However, speech recognition also faces many challenges and issues that affect its performance and usability. Some of these issues are:

  - **Accuracy**: The accuracy of a speech recognition system depends on how well it can recognize and transcribe the speech input, regardless of the speaker, language, accent, dialect, vocabulary, grammar, pronunciation, speed, volume, tone, and context. Accuracy is measured by the word error rate (WER), which is the ratio of the number of errors (substitutions, deletions, and insertions) to the number of words in the reference transcript. A lower WER indicates a higher accuracy. However, achieving a high level of accuracy can be challenging, as speech recognition systems have to deal with various sources of variability and uncertainty, such as:

    - **Noise**: Noise is any unwanted sound that interferes with the speech signal, such as background music, traffic, wind, or other speakers. Noise can reduce the signal-to-noise ratio (SNR), which is the ratio of the power of the speech signal to the power of the noise. A lower SNR indicates a poorer quality of the speech signal, which can affect the accuracy of the speech recognition system. To overcome the noise problem, speech recognition systems can use techniques such as noise reduction, noise cancellation, beamforming, or microphone arrays, which aim to enhance the speech signal and suppress the noise.

    - **Speaker variability**: Speaker variability refers to the differences among speakers in terms of their physical, biological, and behavioral characteristics, such as age, gender, anatomy, physiology, health, emotion, mood, personality, style, attitude, intention, and preference. Speaker variability can affect the acoustic features of the speech signal, such as pitch, intensity, duration, formants, and spectral envelope, which can affect the accuracy of the speech recognition system. To overcome the speaker variability problem, speech recognition systems can use techniques such as speaker adaptation, speaker normalization, speaker identification, or speaker verification, which aim to adjust the system parameters or models to match the characteristics of the speaker.

    - **Language variability**: Language variability refers to the differences among languages or dialects in terms of their structure, grammar, syntax, semantics, pragmatics, vocabulary, and orthography. Language variability can affect the linguistic features of the speech signal, such as words, phrases, sentences, and meanings, which can affect the accuracy of the speech recognition system. To overcome the language variability problem, speech recognition systems can use techniques such as language identification, language modeling, or language translation, which aim to recognize, generate, or convert the language or dialect of the speech input.

  - **Data**: The data of a speech recognition system consists of the speech input, the reference transcript, and the system output. The data is essential for training, testing, and evaluating the speech recognition system, as well as for improving its performance and functionality. However, data also poses many challenges and issues, such as:

    - **Availability**: The availability of data refers to the quantity and quality of the data that is accessible and usable for the speech recognition system. The availability of data can affect the coverage and diversity of the speech recognition system, as well as its generalization and robustness. However, obtaining a large and high-quality dataset can be difficult, time-consuming, and costly, especially for low-resource languages or domains, which have limited or no data available. To overcome the data availability problem, speech recognition systems can use techniques such as data augmentation, data synthesis, data transfer, or data sharing, which aim to increase the amount or variety of the data.

    - **Reliability**: The reliability of data refers to the consistency and accuracy of the data that is provided and processed by the speech recognition system. The reliability of data can affect the validity and reliability of the speech recognition system, as well as its trustworthiness and credibility. However, ensuring a reliable dataset can be challenging, as data can be corrupted, distorted, incomplete, outdated, or inaccurate, due to human errors, technical errors, or malicious attacks. To overcome the data reliability problem, speech recognition systems can use techniques such as data cleaning, data verification, data correction, or data protection, which aim to improve the quality or security of the data.

  - **Privacy**: The privacy of data refers to the protection and control of the personal or sensitive information that is collected and used by the speech recognition system. The privacy of data

