

# Natural Language Processing

Natural language processing (NLP) is an interdisciplinary subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data.

Some of the main goals and applications of NLP are:

- To enable computers to understand, interpret and manipulate human language, such as text and speech, in much the same way human beings can.
- To develop systems that can perform tasks such as machine translation, speech recognition, sentiment analysis, information extraction, text summarization, question answering, natural language generation, and more.
- To advance the state of the art in natural language understanding and generation, by using techniques such as deep learning, rule-based modeling, statistical methods, and knowledge representation .
- To leverage the power of natural language processing to enhance various domains and industries, such as education, health care, business, social media, e-commerce, and more.

Some of the main challenges and limitations of NLP are:

- To deal with the ambiguity, variability, and complexity of natural language, which can have different meanings, structures, and contexts depending on the situation, speaker, and listener.
- To cope with the diversity and evolution of natural language, which can have different dialects, accents, idioms, slang, and neologisms depending on the culture, region, and time.
- To bridge the gap between natural language and formal logic, which can have different levels of abstraction, expressiveness, and inference depending on the domain, task, and goal.
- To balance the trade-off between generality and specificity, which can have different degrees of applicability, accuracy, and efficiency depending on the data, model, and algorithm.



## Unit 1 - INTRODUCTION

This unit provides an overview of the following topics:

- What is artificial intelligence (AI) and why is it important?
- What are the main subfields and applications of AI?
- What are the main challenges and limitations of AI?
- What are the ethical and social implications of AI?

### What is artificial intelligence (AI) and why is it important?

- Artificial intelligence (AI) is the study and design of intelligent agents that can perceive, learn, reason, and act in complex environments.
- AI is important because it can enhance human capabilities, automate tasks, solve problems, and create new opportunities in various domains.
- AI can also pose risks and challenges, such as ethical dilemmas, social impacts, and technical limitations.

### What are the main subfields and applications of AI?

- AI can be divided into four main subfields: machine learning, natural language processing, computer vision, and robotics.
- Machine learning is the study of algorithms and models that can learn from data and improve their performance over time.
- Natural language processing is the study of methods and systems that can understand, generate, and interact with natural languages, such as speech and text.
- Computer vision is the study of techniques and systems that can analyze, interpret, and manipulate visual information, such as images and videos.
- Robotics is the study of machines and devices that can sense, act, and communicate in physical environments.

- AI has many applications in various domains, such as health care, education, entertainment, business, security, and social good.
- Some examples of AI applications are:

  - Diagnosis and treatment of diseases
  - Personalized learning and tutoring
  - Recommendation and search systems
  - Face and voice recognition
  - Self-driving cars and drones
  - Chatbots and virtual assistants
  - Fraud detection and cybersecurity
  - Disaster response and humanitarian aid

### What are the main challenges and limitations of AI?

- AI faces many challenges and limitations, such as:

  - Data quality and availability: AI systems depend on large and diverse datasets to learn and perform well, but data can be noisy, incomplete, biased, or scarce.
  - Computational resources and efficiency: AI systems require high computational power and memory to process and store data, but these resources can be costly, limited, or energy-intensive.
  - Explainability and transparency: AI systems can be complex, opaque, or unpredictable, making it hard to understand how they work and why they make certain decisions or actions.
  - Robustness and reliability: AI systems can be vulnerable to errors, failures, or adversarial attacks, affecting their performance and safety in real-world scenarios.
  - Generalization and adaptation: AI systems can be specialized or optimized for specific tasks or domains, but they may struggle to transfer or adapt their knowledge and skills to new or changing situations.
  - Ethical and social values: AI systems can have positive or negative impacts on human values, such as fairness, privacy, accountability, and trust, depending on how they are designed, used, and regulated.

### What are the ethical and social implications of AI?

- AI has ethical and social implications, such as:

  - Beneficence and harm: AI can benefit or harm humans and other living beings, depending on its intended and unintended consequences, such as improving health, well-being, and productivity, or causing injury, death, or displacement.
  - Justice and fairness: AI can affect the distribution of benefits and burdens, opportunities and risks, rights and responsibilities, among different groups and individuals, such as creating or reducing inequalities, biases, or discrimination.
  - Autonomy and agency: AI can influence the freedom and control of humans and other agents, such as enhancing or diminishing their choices, preferences, and actions, or empowering or manipulating them.
  - Privacy and security: AI can affect the protection and access of personal and sensitive information, such as respecting or violating the confidentiality, integrity, and availability of data, or enabling or threatening the identity, reputation, and well-being of data subjects and owners.
  - Accountability and responsibility: AI can affect the attribution and evaluation of actions and outcomes, such as determining or obscuring the causes, effects, and consequences of AI behavior, or assigning or avoiding the blame, credit, or liability of AI agents and stakeholders.



### Origins and challenges of NLP

- Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.
- The origins of NLP can be traced back to the early attempts to create machines that can understand and generate natural language, such as the Turing test, the ELIZA program, and the SHRDLU system.
- The history of NLP is also influenced by various sources from psychology, philosophy, logic, linguistics, and cognitive science, such as Alfred Korzybski's theory of general semantics, Noam Chomsky's theory of generative grammar, and John Searle's Chinese room argument .
- The development of NLP has been driven by various applications and challenges, such as machine translation, information retrieval, speech recognition, sentiment analysis, question answering, text summarization, and natural language generation  .
- The challenges of NLP stem from the complexity, diversity, ambiguity, and dynamism of natural language, as well as the limitations of computational resources, algorithms, and evaluation methods .
- Some of the major challenges of NLP are:
  - Dealing with the sparsity, high-dimensionality, and noise of natural language data
  - Capturing the syntactic, semantic, pragmatic, and discourse aspects of natural language meaning
  - Handling the variability, inconsistency, and idiosyncrasy of natural language expressions
  - Adapting to the evolving and emerging trends, domains, and genres of natural language use
  - Incorporating the context, background knowledge, and common sense of natural language communication
  - Balancing the trade-off between simplicity, accuracy, efficiency, and scalability of NLP systems
  - Evaluating the performance, quality, and usability of NLP systems



# Language Modeling for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Language modeling is the task of estimating the probability of a sequence of words or tokens in a natural language .
- Language models are statistical tools that analyze the pattern of human language for the prediction of words.
- Language models are the core component of modern natural language processing (NLP), which is the branch of computer science and artificial intelligence concerned with giving computers the ability to understand text and spoken words .
- Language models have a large number of applications in NLP, such as speech recognition, machine translation, text summarization, text generation, question answering, sentiment analysis, spam filtering, etc.  .
- Language models can be classified into two types: n-gram models and neural models .
- N-gram models are based on counting the frequency of n consecutive words or tokens in a large corpus of text and using the chain rule of probability to estimate the probability of a word given its previous n-1 words.
- Neural models are based on using deep neural networks, such as recurrent neural networks (RNNs), long short-term memory (LSTM), gated recurrent units (GRU), transformers, etc., to learn the probability distribution of words or tokens in a natural language from a large corpus of text.
- Neural models have the advantage of being able to capture long-range dependencies and semantic relationships between words or tokens, which n-gram models cannot do well.
- Neural models also have the disadvantage of being more computationally expensive and requiring more data and resources to train and run.
- Language models can be evaluated using various metrics, such as perplexity, which measures how well a model predicts the next word or token in a sequence, or BLEU, which measures how well a model generates a natural language translation of a source text.



### Grammar-based LM

- Grammar-based language models (GLMs) are a type of language models that use the rules and structures of a natural language to generate and evaluate sentences.
- GLMs can be formal or probabilistic, depending on whether they use deterministic or stochastic methods to define the grammar and the parsing of a sentence.
- Formal GLMs are based on the syntax and semantics of a language, and they check whether a sentence is well-formed and meaningful according to the grammar rules. Examples of formal GLMs are context-free grammars (CFGs) and context-sensitive grammars (CSGs).
- Probabilistic GLMs are based on the frequency and likelihood of a sentence or a word sequence occurring in a given corpus or text data. They assign a probability to a sentence or a word sequence based on the observed occurrences in the corpus. Examples of probabilistic GLMs are n-gram models and probabilistic context-free grammars (PCFGs).
- GLMs are useful for natural language processing (NLP) tasks that require the generation or evaluation of natural language sentences, such as speech recognition, machine translation, spelling correction, text summarization, and natural language generation.



### Statistical Language Model for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A statistical language model (SLM) is a mathematical tool that assigns probabilities to sequences of words or symbols in a natural language.
- SLMs are used to generate or analyze natural language texts for various applications, such as speech recognition, machine translation, natural language generation, information retrieval, etc.
- SLMs are based on the assumption that the probability of a word or symbol depends on its previous words or symbols, i.e., its context.
- SLMs can be classified into two types: n-gram models and neural network models.
- N-gram models are the simplest and most widely used SLMs. They estimate the probability of a word or symbol based on its n-1 previous words or symbols, where n is a fixed parameter. For example, a bigram model (n=2) estimates the probability of a word based on its previous word, while a trigram model (n=3) estimates the probability of a word based on its previous two words.
- Neural network models are more complex and powerful SLMs. They use artificial neural networks to learn the probability distribution of words or symbols in a natural language. They can capture long-range dependencies and semantic similarities between words or symbols. For example, a recurrent neural network (RNN) model can process variable-length sequences of words or symbols, while a transformer model can encode the context and attention of words or symbols.
- SLMs are trained on large corpora of natural language texts, using various methods such as maximum likelihood estimation, smoothing techniques, backpropagation, etc.
- SLMs are evaluated on various metrics, such as perplexity, accuracy, recall, precision, etc. Perplexity measures how well a SLM predicts the next word or symbol in a sequence, while accuracy measures how often a SLM predicts the correct word or symbol. Recall measures how many relevant words or symbols a SLM retrieves, while precision measures how many retrieved words or symbols are relevant.



### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.
- RE is used in various tasks such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.

- Examples of Regular Expressions:

| Regular Expressions | Regular Set |
| ------------------- | ----------- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s |

- The syntax of RE consists of the following elements:

| Element | Meaning |
| ------- | ------- |
| a | Matches the character a |
| . | Matches any character |
| [abc] | Matches any character in the set {a, b, c} |
| [a-z] | Matches any character in the range a to z |
| [^abc] | Matches any character not in the set {a, b, c} |
| [^a-z] | Matches any character not in the range a to z |
| a* | Matches zero or more occurrences of a |
| a+ | Matches one or more occurrences of a |
| a? | Matches zero or one occurrence of a |
| a{m} | Matches exactly m occurrences of a |
| a{m,} | Matches at least m occurrences of a |
| a{m,n} | Matches at least m and at most n occurrences of a |
| a|b | Matches either a or b |
| (a) | Matches a and captures it as a group |
| (?:a) | Matches a but does not capture it as a group |
| \n | Matches the nth captured group |
| \a | Matches the character a if it is a metacharacter |
| ^ | Matches the beginning of a string or line |
| $ | Matches the end of a string or line |
| \b | Matches a word boundary |
| \B | Matches a non-word boundary |
| \d | Matches any digit |
| \D | Matches any non-digit |
| \s | Matches any whitespace |
| \S | Matches any non-whitespace |
| \w | Matches any word character |
| \W | Matches any non-word character |



### Finite-State Automata for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Finite-state automata (FSA) are abstract machines that can recognize and generate patterns of symbols, such as strings of characters or words.
- FSA have a finite number of states, and can change from one state to another based on the input symbol and a transition function.
- FSA can be deterministic (DFA) or non-deterministic (NFA). DFA have exactly one transition for each input symbol and state, while NFA can have zero, one, or more transitions for each input symbol and state.
- FSA can be used to model various aspects of natural language processing (NLP), such as morphology, syntax, semantics, and phonology.
- FSA can also be extended to finite-state transducers (FST), which can produce an output symbol for each input symbol, or vice versa. FST can be used to perform tasks such as morphological analysis, text normalization, and speech recognition.
- FSA and FST have several advantages in NLP, such as efficiency, simplicity, modularity, and expressiveness. They can also be combined with other techniques, such as probabilistic models, to handle uncertainty and ambiguity in natural language.



### English Morphology

- Morphology is the study of the internal structure and formation of words.
- Words are composed of smaller units called morphemes, which are the smallest meaningful units in a language.
- Morphemes can be classified into two types: free and bound.
  - Free morphemes can stand alone as words, such as cat, dog, happy, etc.
  - Bound morphemes cannot stand alone as words, but must be attached to other morphemes, such as -s, -ed, -ing, etc.
- Morphemes can also be classified into two types: roots and affixes.
  - Roots are the core of a word, carrying the main meaning and lexical category, such as cat, dog, happy, etc.
  - Affixes are morphemes that modify the meaning or category of a root, such as -s, -ed, -ing, etc.
- Affixes can be further classified into four types: prefixes, suffixes, infixes and circumfixes.
  - Prefixes are affixes that attach to the beginning of a root, such as un-, re-, pre-, etc.
  - Suffixes are affixes that attach to the end of a root, such as -s, -ed, -ing, etc.
  - Infixes are affixes that insert into the middle of a root, such as -um- in Tagalog (e.g. sulat 'write', sumulat 'wrote').
  - Circumfixes are affixes that attach to both the beginning and the end of a root, such as ge-...-t in German (e.g. spiel 'play', gespielt 'played').
- The process of combining morphemes to form words is called word formation.
- There are different types of word formation processes, such as derivation, inflection, compounding, blending, clipping, acronym, etc.
  - Derivation is the process of creating new words by adding affixes to existing words, such as happy + -ness = happiness, teach + -er = teacher, etc.
  - Inflection is the process of modifying existing words to indicate grammatical features, such as number, tense, person, case, etc. For example, cat + -s = cats, walk + -ed = walked, etc.
  - Compounding is the process of creating new words by combining two or more existing words, such as blackboard, toothbrush, etc.
  - Blending is the process of creating new words by combining parts of two or more existing words, such as brunch (breakfast + lunch), smog (smoke + fog), etc.
  - Clipping is the process of creating new words by shortening existing words, such as gym (gymnasium), flu (influenza), etc.
  - Acronym is the process of creating new words by using the initial letters of a phrase or a name, such as NASA (National Aeronautics and Space Administration), LOL (laugh out loud), etc.



### Transducers for lexicon

- A transducer is a device or a model that converts one form of data into another, such as sound to electrical signals, or text to speech.
- A lexical transducer is a specialized finite-state automaton that maps inflected surface forms to lexical forms, and vice versa .
- A lexical form is a representation of a word that contains its lemma (base form) and its morphological features, such as part of speech, number, gender, tense, etc.
- A surface form is a representation of a word that appears in a text, such as a spelling or a pronunciation.
- A lexical transducer can be used for various natural language processing tasks, such as morphological analysis, generation, normalization, correction, and parsing .
- A lexical transducer can be constructed using regular expressions, rewrite rules, or lexicon and grammar files .
- A lexical transducer can be composed with other transducers, such as context dependency transducers, language models, or speech recognizers, to form a complex language processing pipeline .
- A lexical transducer can be compressed using various techniques, such as minimization, factorization, pruning, or quantization, to reduce its size and improve its efficiency .



### Tokenization for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Tokenization is the process of breaking down a piece of text into small units called tokens.
- A token may be a word, part of a word or just characters like punctuation.
- Tokenization is the first step in any NLP pipeline. It has an important effect on the rest of the pipeline.
- Tokenization is used in natural language processing to split paragraphs and sentences into smaller units that can be more easily assigned meaning.
- The token occurrences in a document can be used directly as a vector representing that document.
- Tokenization is useful for a number of tasks in natural language processing, including sentiment analysis, topic modeling, and machine translation.
- One of the main advantages of tokenization is that it can help to improve the accuracy of these tasks by providing more context for each word.
- Tokenization is a crucial step in many NLP tasks, such as part-of-speech tagging and text classification.
- Tokenization is not a simple task, as different languages have different grammatical constructs, which are often difficult to write down as rules.
- Tokenization may also depend on the domain and the purpose of the text analysis.
- There are different types of tokenization, such as word tokenization, sentence tokenization, subword tokenization, and character tokenization.
- There are different tools and libraries that can perform tokenization, such as NLTK, spaCy, and BERT.
- Tokenization is an essential step in natural language processing, as it transforms unstructured data into a structured form that can be processed by other NLP components.



### Detecting and Correcting Spelling Errors

- Spelling errors are a common source of noise and ambiguity in natural language processing (NLP) tasks, such as information retrieval, machine translation, text summarization, etc.
- Spelling errors can be classified into two types: non-word errors and real-word errors.
- Non-word errors are those that result in a word that does not exist in the language, such as *teh* for *the*, *recieve* for *receive*, etc.
- Real-word errors are those that result in a word that exists in the language, but is not the intended one, such as *form* for *from*, *their* for *there*, etc.
- Detecting and correcting spelling errors involves two steps: error detection and error correction.
- Error detection is the task of identifying the words that are misspelled in a given text.
- Error correction is the task of finding the correct spelling for the misspelled words.
- There are different methods and techniques for detecting and correcting spelling errors, such as rule-based, dictionary-based, statistical, neural, and hybrid approaches.
- Rule-based methods use a set of predefined rules or patterns to detect and correct spelling errors, such as phonetic rules, orthographic rules, morphological rules, etc.
- Dictionary-based methods use a lexicon or a list of valid words to detect and correct spelling errors, such as edit distance, longest common subsequence, etc.
- Statistical methods use probabilistic models to detect and correct spelling errors, such as n-gram models, hidden Markov models, noisy channel models, etc.
- Neural methods use deep learning models to detect and correct spelling errors, such as recurrent neural networks, convolutional neural networks, attention mechanisms, etc.
- Hybrid methods use a combination of different methods to detect and correct spelling errors, such as rule-based and statistical, dictionary-based and neural, etc.
- Some of the challenges and limitations of spelling error detection and correction are: dealing with out-of-vocabulary words, handling homophones and homographs, coping with dialectal and regional variations, etc.



### Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are, based on the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, each with a certain cost.
- For example, the minimum edit distance between "cat" and "bat" is 1, because we can substitute "c" with "b" with a cost of 1. The minimum edit distance between "cat" and "cut" is also 1, because we can substitute "a" with "u" with a cost of 1.
- To compute the minimum edit distance between two strings, we can use a dynamic programming algorithm that fills a matrix with the optimal costs for each substring pair.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of deleting or inserting each character from the source or target string.
  - For each cell in the matrix, compute the minimum cost of transforming the substring up to that cell, based on the previous cells and the cost of substituting, inserting, or deleting the current character.
  - The minimum cost of transforming the whole strings is the value in the bottom-right cell of the matrix.
  - To find the optimal sequence of operations, we can backtrack from the bottom-right cell to the top-left cell, following the pointers that indicate which previous cell was used to compute the current cell.

- Here is an example of computing the minimum edit distance between "intention" and "execution", with a cost of 1 for each operation:

|   |   | e | x | e | c | u | t | i | o | n |
|---|---|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| i | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| n | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 7 |
| t | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
| e | 4 | 3 | 4 | 3 | 4 | 5 | 6 | 7 | 7 | 8 |
| n | 5 | 4 | 5 | 4 | 5 | 6 | 7 | 7 | 8 | 8 |
| t | 6 | 5 | 6 | 5 | 6 | 7 | 6 | 7 | 9 | 9 |
| i | 7 | 6 | 7 | 6 | 7 | 8 | 7 | 6 | 8 | 9 |
| o | 8 | 7 | 8 | 7 | 8 | 9 | 8 | 7 | 7 | 8 |
| n | 9 | 8 | 9 | 8 | 9 | 10| 9 | 8 | 8 | 8 |

- The minimum edit distance is 8, and one possible sequence of operations is:

  - Substitute "i" with "e"
  - Substitute "n" with "x"
  - Substitute "t" with "e"
  - Insert "c"
  - Insert "u"
  - Delete "n"
  - Delete "t"
  - Delete "i"

- Minimum edit distance can be used for various applications in natural language processing, such as spelling correction, speech recognition, machine translation, and text similarity.



### WORD LEVEL ANALYSIS

Word level analysis is a stage of natural language processing that deals with text at the individual word level. It involves the following tasks:

- **Tokenization**: The process of splitting a text into smaller units called tokens, such as words, punctuation marks, numbers, etc. Tokenization is usually the first step of any natural language processing pipeline, as it prepares the text for further analysis. Tokenization can be done using various methods, such as whitespace, regular expressions, or specialized libraries.
- **Morphological analysis**: The process of identifying the morphemes, the smallest meaningful units of a word, and their structure and function. Morphemes can be roots, stems, prefixes, suffixes, or inflections. Morphological analysis can help to determine the part of speech, number, tense, aspect, mood, voice, gender, case, or person of a word. Morphological analysis can be done using rules, dictionaries, or machine learning models.
- **Stemming and lemmatization**: The process of reducing a word to its base form, either by removing affixes (stemming) or by finding the canonical form (lemmatization). Stemming and lemmatization can help to normalize the text and reduce the vocabulary size. Stemming and lemmatization can be done using rules, dictionaries, or machine learning models.
- **Word sense disambiguation**: The process of determining the meaning of a word in a given context, among multiple possible meanings. Word sense disambiguation can help to improve the accuracy and relevance of natural language processing applications, such as information retrieval, machine translation, or text summarization. Word sense disambiguation can be done using rules, dictionaries, or machine learning models.



### Unsmoothed N-grams

- An n-gram is a sequence of n words or tokens in a text. For example, "natural language processing" is a trigram (n = 3).
- N-grams are used to model the probability of a word given its previous words or context. For example, P(processing | natural language) is the probability of the word "processing" given the previous words "natural language".
- N-gram models are based on the assumption of the Markov property, which states that the probability of a word only depends on a fixed number of previous words. For example, a bigram model assumes that P(w_n | w_1, ..., w_n-1) = P(w_n | w_n-1), where w_n is the nth word in a sequence.
- To estimate the n-gram probabilities, we can use the maximum likelihood estimation (MLE), which counts the frequency of each n-gram in a corpus and divides it by the frequency of its prefix. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C(.) is the count function.
- Unsmoothed n-gram models are simple and easy to implement, but they have some drawbacks. One of them is data sparsity, which means that some n-grams may not occur in the training corpus, leading to zero probabilities. Another one is overfitting, which means that the model may memorize the training data and fail to generalize to unseen data.



### Evaluating N-grams

- N-grams are sequences of words or characters that are used to model language and capture the probability of a word given its previous context.
- N-grams are evaluated based on how well they can predict unseen data, such as test sentences or documents, using the probabilities estimated from the training data.
- There are different methods to evaluate n-grams, such as:

  - **Perplexity**: a measure of how uncertain the model is about the next word, given the previous context. Perplexity is inversely proportional to the probability of the test data, and lower perplexity means better prediction. Perplexity can be calculated as:

    $$\text{Perplexity}(W) = P(w_1 w_2 \dots w_N)^{-\frac{1}{N}} = \sqrt[N]{\frac{1}{P(w_1 w_2 \dots w_N)}}$$

    where $W$ is the test data, $N$ is the number of words in the test data, and $P(w_1 w_2 \dots w_N)$ is the probability of the test data according to the n-gram model.

  - **Entropy**: a measure of how much information is needed to encode the test data, given the n-gram model. Entropy is proportional to the negative logarithm of the probability of the test data, and lower entropy means better compression. Entropy can be calculated as:

    $$\text{Entropy}(W) = -\frac{1}{N} \log_2 P(w_1 w_2 \dots w_N)$$

    where $W$ is the test data, $N$ is the number of words in the test data, and $P(w_1 w_2 \dots w_N)$ is the probability of the test data according to the n-gram model.

  - **Cross-entropy**: a measure of how much information is needed to encode the test data, given the n-gram model and a reference model. Cross-entropy is proportional to the negative logarithm of the probability of the test data, weighted by the reference model. Cross-entropy can be calculated as:

    $$\text{Cross-entropy}(W) = -\frac{1}{N} \sum_{i=1}^N q(w_i) \log_2 p(w_i)$$

    where $W$ is the test data, $N$ is the number of words in the test data, $q(w_i)$ is the probability of the $i$-th word according to the reference model, and $p(w_i)$ is the probability of the $i$-th word according to the n-gram model.

  - **Kullback-Leibler divergence**: a measure of how much the n-gram model differs from the reference model. Kullback-Leibler divergence is proportional to the difference between the cross-entropy and the entropy of the test data, and lower divergence means better similarity. Kullback-Leibler divergence can be calculated as:

    $$\text{Kullback-Leibler divergence}(W) = \text{Cross-entropy}(W) - \text{Entropy}(W)$$

    where $W$ is the test data, and $\text{Cross-entropy}(W)$ and $\text{Entropy}(W)$ are defined as above.

- N-gram evaluation methods have some limitations, such as:

  - They do not account for the semantic or syntactic quality of the generated text, only the statistical likelihood.
  - They are sensitive to the choice of the test data and the reference model, which may not reflect the true distribution of the language or the task.
  - They are affected by the smoothing techniques used to deal with zero or low probabilities of unseen n-grams. Different smoothing methods may result in different n-gram probabilities and evaluations.



### Smoothing

- Smoothing is the process of flattening a probability distribution implied by a language model so that all reasonable word sequences can occur with some probability .
- Smoothing often involves broadening the distribution by redistributing weight from high probability regions to zero probability regions .
- Smoothing is very important in natural language processing, as some words may have zero or close to zero probabilities such as the out-of-vocabulary words (words that do not exist in the vocabulary), but the same rare words may not have the same values in test data.
- Smoothing techniques in NLP are used to address scenarios related to determining probability / likelihood estimate of a sequence of words (say, a sentence) occurring together when one or more words individually (unigram) or N-grams such as bigram or trigram in the given set have never occurred in the past.
- Smoothing can help performance whenever data sparsity is an issue, and data sparsity is almost always an issue in statistical modeling.
- Smoothing can also allow expanding the model, such as by moving to a higher n-gram model, to improve the accuracy of the language model.
- Some common smoothing techniques are:
  - Additive smoothing (also known as Laplace smoothing): adding a small constant to all counts, usually 1.
  - Backoff smoothing: using lower order n-grams when higher order n-grams have zero counts.
  - Interpolation smoothing: combining different order n-grams with different weights.
  - Kneser-Ney smoothing: using a modified count that discounts the probability of n-grams that occur frequently and increases the probability of n-grams that occur rarely.
  - Good-Turing smoothing: using a formula to estimate the probability of unseen n-grams based on the frequency of n-grams that occur once.



# Interpolation and Backoff

- Interpolation and backoff are two methods of smoothing n-gram language models to deal with data sparsity and generalization problems.
- Interpolation: a linear combination of n-gram probabilities with different orders, weighted by coefficients that sum to one.
- Backoff: a conditional probability that falls back to a lower-order n-gram if the higher-order n-gram has zero count or low confidence.
- In general, interpolation works better than backoff, but requires more computation and parameter tuning.
- There are different ways of estimating the interpolation coefficients, such as held-out interpolation, deleted interpolation, or expectation-maximization (EM) algorithm.
- There are different ways of implementing the backoff strategy, such as Katz backoff, Witten-Bell backoff, or Kneser-Ney smoothing.



### Word Classes for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Word classes, also known as **part-of-speech (POS) tags**, are categories of words that share similar syntactic and morphological properties in a language. For example, nouns, verbs, adjectives, and adverbs are common word classes in English.
- Word classes are useful for natural language processing (NLP) tasks such as **parsing**, **text analysis**, **information extraction**, **machine translation**, and **speech recognition**. They help to identify the structure and meaning of sentences and texts, and to disambiguate words that have multiple possible interpretations.
- There are different ways to define and label word classes, depending on the level of granularity and the linguistic theory adopted. Some common word classes in English are:

  - **Noun (N)**: A word that denotes a person, place, thing, or concept. Examples: dog, book, John, happiness.
  - **Verb (V)**: A word that denotes an action, state, or occurrence. Examples: run, be, see, learn.
  - **Adjective (A)**: A word that modifies a noun or pronoun, expressing a quality or attribute. Examples: big, red, happy, smart.
  - **Adverb (Adv)**: A word that modifies a verb, adjective, or another adverb, expressing a manner, degree, time, place, or direction. Examples: quickly, very, yesterday, here, away.
  - **Pronoun (P)**: A word that substitutes for a noun or noun phrase, referring to a person or thing previously mentioned or understood. Examples: he, she, it, they, this, that.
  - **Preposition (P)**: A word that introduces a phrase, expressing the relation of a noun or pronoun to another word. Examples: in, on, at, with, from, to.
  - **Conjunction (C)**: A word that connects words, phrases, or clauses, expressing a logical or temporal relation. Examples: and, but, or, because, although, when.
  - **Determiner (D)**: A word that precedes a noun or noun phrase, expressing a quantity, possession, definiteness, or specificity. Examples: a, the, some, my, this, every.
  - **Interjection (I)**: A word that expresses a sudden emotion or reaction, usually followed by an exclamation mark. Examples: wow, ouch, hey, oops.

- Some word classes can be further divided into subcategories, such as **proper nouns**, **modal verbs**, **comparative adjectives**, **adverbs of frequency**, etc. Some words can belong to more than one word class, depending on their usage and context. For example, the word **book** can be a noun or a verb, and the word **well** can be an adverb or an adjective.
- Word classes can be automatically assigned to words in a text using a process called **part-of-speech tagging**, which is a common NLP task. Part-of-speech taggers use various methods, such as **rule-based**, **statistical**, or **neural network** approaches, to assign the most likely word class to each word, based on its form, context, and lexical resources. Part-of-speech tagging can improve the performance of other NLP tasks, such as **named entity recognition**, **sentiment analysis**, **text summarization**, etc.



### Part-of-Speech Tagging

- Part-of-speech (POS) tagging is the process of assigning a grammatical category to each word in a sentence or text, such as noun, verb, adjective, adverb, etc.   
- POS tagging is an important task in natural language processing (NLP), as it can help to analyze the structure and meaning of a sentence, and to perform other tasks such as parsing, named entity recognition, sentiment analysis, machine translation, etc.   
- POS tagging can be done manually by human annotators, or automatically by computer programs. Manual POS tagging is more accurate but time-consuming and costly, while automatic POS tagging is faster and cheaper but prone to errors. 
- There are different methods and techniques for automatic POS tagging, such as rule-based, statistical, and neural network-based approaches. Rule-based methods use predefined rules and dictionaries to assign tags based on word forms and contexts. Statistical methods use probabilistic models and machine learning algorithms to learn from annotated corpora and predict tags based on word frequencies and patterns. Neural network-based methods use deep learning architectures and embeddings to capture complex features and dependencies from large amounts of data.   
- There are also different types and levels of POS tagging, such as coarse-grained and fine-grained tagging, morphological tagging, and syntactic tagging. Coarse-grained tagging uses a small set of basic tags, such as noun, verb, adjective, etc. Fine-grained tagging uses a larger set of more specific tags, such as singular noun, plural noun, past tense verb, present tense verb, etc. Morphological tagging includes information about the word forms and inflections, such as number, gender, case, etc. Syntactic tagging includes information about the word functions and roles, such as subject, object, modifier, etc.  
- POS tagging is not a trivial task, as there are many challenges and difficulties involved, such as ambiguity, variation, and inconsistency. Ambiguity means that a word can have more than one possible tag depending on the context, such as "book" as a noun or a verb. Variation means that a word can have different forms or spellings in different dialects, registers, or domains, such as "color" or "colour". Inconsistency means that different taggers or annotators can use different standards or criteria to assign tags, such as "adverb" or "particle".  
- POS tagging is an active and evolving research area, as there are still many open problems and opportunities for improvement, such as dealing with unknown words, low-resource languages, multilingual texts, noisy texts, etc.



### Rule-based

- Rule-based natural language processing is an approach that relies on predefined rules and grammars to analyze and generate natural language.
- Rules can be based on syntax, semantics, morphology, pragmatics, or any other aspect of natural language.
- Rule-based systems can be deterministic or probabilistic, depending on whether they assign a single or multiple interpretations to a given input or output.
- Rule-based systems can be hand-crafted or learned from data, depending on whether the rules are manually defined by experts or automatically induced from corpora.
- Rule-based systems have some advantages and disadvantages compared to other approaches, such as statistical or neural methods.
  - Advantages:
    - They can capture linguistic knowledge and regularities explicitly and transparently.
    - They can handle rare or unseen cases that are not covered by data.
    - They can be more interpretable and explainable than black-box models.
  - Disadvantages:
    - They can be brittle and inflexible to cope with the variability and ambiguity of natural language.
    - They can be labor-intensive and domain-specific to develop and maintain.
    - They can be hard to scale and generalize to large and diverse datasets.



### Stochastic for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- Stochastic means involving randomness or probability.
- Stochastic methods are widely used in natural language processing (NLP) to deal with uncertainty and ambiguity in natural languages.
- Stochastic methods can be applied at different levels of NLP, such as morphology, syntax, semantics, and pragmatics.
- Some examples of stochastic methods in NLP are:

  - Stochastic grammar: a grammar that assigns probabilities to grammar rules, and uses them to parse sentences and generate language. Stochastic grammars can capture the frequency and preference of linguistic constructions, and handle ambiguity and noise in natural language .
  - Stochastic semantic analysis: an approach that uses segments of words as basic semantic units, and models their meaning and relations using probabilities. Stochastic semantic analysis can cope with polysemy, synonymy, and vagueness in natural language.
  - Statistical parsing: a technique that uses probabilistic models to analyze the syntactic structure of sentences. Statistical parsers can learn from large corpora of annotated or unannotated text, and achieve high accuracy and robustness.
  - Language modeling: a task that estimates the probability of a word or a sequence of words in a language. Language models can be used for various NLP applications, such as text generation, machine translation, question answering, and speech recognition.

- Stochastic methods in NLP require mathematical and computational tools, such as probability theory, statistics, machine learning, and optimization.
- Stochastic methods in NLP also face challenges, such as data sparsity, overfitting, scalability, and interpretability.



### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill.
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from examples and transforms one state to another state by using transformation rules .
- The basic idea of transformation-based tagging is to start with a simple initial tagging of the text, and then iteratively apply a set of rules that correct the errors in the tagging .
- The initial tagging can be based on the most frequent tag for each word, or a default tag (such as noun) for unknown words .
- The rules are learned from a tagged corpus, by finding the rule that reduces the most errors in each iteration .
- The rules are of the form: change the tag of the current word from X to Y, if condition Z is met .
- The condition Z can be based on the word itself, the surrounding words, the tags of the surrounding words, or any combination of these features .
- For example, a rule could be: change the tag of the current word from noun to verb, if the previous word is "to" and the next word is not a noun .
- The rules are applied in a fixed order, and the order can affect the accuracy of the tagging .
- Transformation-based tagging has been shown to achieve high accuracy for POS tagging, as well as other tasks such as text chunking  .
- It has the advantage of being fast, simple, and interpretable, as the rules are human-readable and can capture linguistic knowledge   .
- It has the disadvantage of being dependent on the quality and size of the tagged corpus, and the choice of the initial tagging and the rule order .
- It can also suffer from overfitting, as some rules may be too specific to the training data and not generalize well to new data .



### Issues in PoS tagging

- Part-of-speech (PoS) tagging is the process of assigning a grammatical category to each word in a text, such as noun, verb, adjective, etc. based on its definition and context.
- PoS tagging is an important task in natural language processing (NLP) as it can help in syntactic and semantic analysis, information extraction, machine translation, sentiment analysis, etc.
- However, PoS tagging is not a trivial task as it faces several challenges and difficulties, such as:
  - **Ambiguity**: Many words can have multiple PoS depending on the context and meaning. For example, the word "book" can be a noun or a verb in different sentences. A PoS tagger has to resolve this ambiguity accurately based on the surrounding words and the overall structure of the sentence  .
  - **Unknown words**: A PoS tagger may encounter words that are not in its vocabulary or training data, such as new words, proper names, foreign words, etc. A PoS tagger has to assign a reasonable PoS to these words based on some heuristics or rules, such as morphology, capitalization, suffixes, etc.
  - **Variation in tag sets**: Different PoS taggers may use different sets of tags to represent the grammatical categories of words. Some tag sets may be coarse-grained and have fewer tags, while others may be fine-grained and have more tags. For example, some tag sets may distinguish between past tense and past participle verbs, while others may not. A PoS tagger has to be consistent with the tag set it uses and be able to map between different tag sets if needed.
  - **Noise and errors**: A PoS tagger may have to deal with noisy or erroneous input, such as spelling mistakes, punctuation errors, slang, abbreviations, etc. A PoS tagger has to be robust and tolerant to these variations and still produce accurate and meaningful output.



### Hidden Markov and Maximum Entropy models for natural language processing

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions).
- HMMs are widely used in natural language processing, especially in speech recognition, part-of-speech tagging, named entity recognition, and machine translation. 
- HMMs are based on the assumption that the hidden state at a given time depends only on the previous hidden state, and the emission at a given time depends only on the current hidden state. This is known as the Markov property.
- HMMs can be represented by a set of parameters: the initial state distribution, the state transition matrix, and the emission probability matrix. These parameters can be estimated from training data using algorithms such as the Baum-Welch algorithm or the Viterbi training algorithm.
- HMMs can be used to perform two main tasks: decoding and learning. Decoding is the process of finding the most likely sequence of hidden states given a sequence of emissions. This can be done using algorithms such as the Viterbi algorithm or the forward-backward algorithm. Learning is the process of finding the optimal parameters of the HMM given a set of training data. This can be done using algorithms such as the Baum-Welch algorithm or the Viterbi training algorithm.
- Maximum Entropy Markov Model (MEMM) is a discriminative model that extends a standard maximum entropy classifier by assuming that the unknown values to be learnt are connected in a Markov chain rather than being conditionally independent of each other.
- MEMMs find applications in natural language processing, specifically in part-of-speech tagging and information extraction.
- MEMMs are based on the principle of maximum entropy, which states that the best model is the one that makes the least assumptions about the data, subject to some constraints. The constraints are derived from the features of the data, such as the previous state, the current word, the next word, etc.
- MEMMs can be represented by a set of parameters: the feature functions and the weights. The feature functions are binary functions that indicate the presence or absence of a certain feature in a given state and observation pair. The weights are real numbers that measure the importance of each feature. These parameters can be estimated from training data using algorithms such as the Improved Iterative Scaling algorithm or the Generalized Iterative Scaling algorithm.
- MEMMs can be used to perform the decoding task, which is the same as in HMMs. However, MEMMs have some advantages over HMMs, such as the ability to incorporate arbitrary features, the avoidance of the label bias problem, and the better generalization performance. MEMMs also have some disadvantages, such as the requirement of more training data, the difficulty of handling unseen observations, and the complexity of the inference algorithm.



```
## Unit 2 - SYNTACTIC ANALYSIS

- Syntactic analysis is the process of analyzing the structure and grammar of a natural language sentence or program code.
- Syntactic analysis can be performed by using formal methods, such as parsing algorithms, or by using heuristic methods, such as machine learning or rule-based systems.
- Syntactic analysis can be used for various applications, such as natural language processing, compiler design, code analysis, and text summarization.
- Syntactic analysis can be divided into two main phases: lexical analysis and parsing.
- Lexical analysis is the process of breaking down a sentence or code into its smallest meaningful units, called tokens or lexemes.
- Parsing is the process of building a hierarchical representation of the syntactic structure and relationships of the tokens or lexemes, called a parse tree or abstract syntax tree.
- Syntactic analysis can be further classified into two types: top-down parsing and bottom-up parsing.
- Top-down parsing is the process of starting from the root or the highest level of the parse tree and applying grammar rules to generate the tokens or lexemes.
- Bottom-up parsing is the process of starting from the tokens or lexemes and applying grammar rules to construct the parse tree or abstract syntax tree.
- Syntactic analysis can also be influenced by the type of grammar used to define the language, such as context-free grammar, context-sensitive grammar, or regular grammar.
- Syntactic analysis can encounter various challenges and limitations, such as ambiguity, recursion, left-recursion, backtracking, and complexity.
```



### Context Free Grammars

- A context-free grammar (CFG) is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a left-hand side, which identifies a syntactic category, and a right-hand side, which defines its alternative component parts, reading from left to right.
- A syntactic category is a label for a group of words or phrases that share some common properties, such as noun, verb, adjective, etc.
- A context-free grammar is called so because the rules can be applied regardless of the surrounding context of the words or phrases.
- A context-free grammar can be formally defined as a 4-tuple (N, Σ, R, S), where:
  - N is a finite set of non-terminal symbols, which represent syntactic categories.
  - Σ is a finite set of terminal symbols, which represent words or punctuation marks.
  - R is a finite set of production rules, which have the form A → α, where A ∈ N and α ∈ (N ∪ Σ)*.
  - S ∈ N is the start symbol, which represents the whole sentence.
- A context-free grammar can be used to generate or parse sentences in a language.
  - To generate a sentence, we start with the start symbol S and apply the rules recursively until we obtain a string of terminal symbols.
  - To parse a sentence, we start with the string of terminal symbols and try to find a sequence of rule applications that can derive it from the start symbol S.
- A context-free grammar can be represented by a parse tree, which is a graphical representation of the derivation process.
  - A parse tree has a root node labeled with the start symbol S and branches for each rule application.
  - The leaf nodes are labeled with the terminal symbols and the internal nodes are labeled with the non-terminal symbols.
  - A parse tree shows the hierarchical structure and the constituent parts of a sentence.
- A context-free grammar can be used to model the constituent structure of natural language, which is the way words and phrases are grouped together to form larger units of meaning.
  - A commonly used mathematical system for modelling constituent structure in natural language is context-free grammar (CFG), which was first defined for natural language in (Chomsky 1957) and was independently discovered for the description of the Algol programming language by Backus (backus 1959) and Naur (Naur et al. 1960).
  - A context-free grammar can capture some of the syntactic properties and regularities of natural language, such as recursion, coordination, subordination, etc.
  - A context-free grammar can also be used to define the high level structure of a programming language.
- However, a context-free grammar is not sufficient to account for all the aspects and complexities of natural language, such as agreement, anaphora, word order, etc.
  - Natural languages are really not context-free: e.g. pronouns more likely in Object rather than Subject of a sentence.
  - Parsing natural language with a context-free grammar is PSPACE-complete (Recognized by a Turing machine using a polynomial amount of memory, and unlimited time).
  - Often, more expressive and powerful grammars are needed, such as mildly context-sensitive grammars, tree-adjoining grammars, etc.



### Grammar rules for English

Grammar is a system of language rules that allows you to combine individual words to make complex meanings. By applying grammar rules to your writing, you’ll make it stronger, clearer, and more effective. Here are some basic grammar rules for English that you should learn and follow:

- A complete sentence must include a subject and a verb. A subject is the person, place, thing or idea that performs the action or is described by the verb. A verb is an action word or a state of being word. For example, "The bird flew." The subject is "the bird" and the verb is "flew".
- The first word in a sentence must start with a capital letter. This is a convention that signals the beginning of a new statement. For example, "She likes apples." The first word "She" is capitalized.
- A sentence must end with a punctuation mark, such as a period (.), a question mark (?), or an exclamation point (!). This is another convention that signals the end of a statement and the type of statement it is. For example, "Do you like apples?" The sentence ends with a question mark because it is a question.
- A singular subject in a sentence needs a singular verb. A singular subject is one that refers to a single person, place, thing or idea. A singular verb is one that agrees with a singular subject in number and person. For example, "He runs fast." The subject "he" is singular and the verb "runs" is singular.
- A plural subject in a sentence needs a plural verb. A plural subject is one that refers to more than one person, place, thing or idea. A plural verb is one that agrees with a plural subject in number and person. For example, "They run fast." The subject "they" is plural and the verb "run" is plural.
- A noun can be modified by an adjective or a determiner. A noun is a person, place, thing or idea. An adjective is a word that describes a noun. A determiner is a word that specifies a noun, such as a, the, this, that, etc. For example, "The red apple." The noun is "apple", the adjective is "red" and the determiner is "the".
- A verb can be modified by an adverb or a complement. An adverb is a word that modifies a verb, an adjective or another adverb. A complement is a word or phrase that completes the meaning of a verb. For example, "She runs quickly." The verb is "runs", the adverb is "quickly" and the complement is missing.
- A sentence can be linked with another sentence by a conjunction or a semicolon. A conjunction is a word that connects two sentences, such as and, but, or, etc. A semicolon is a punctuation mark that separates two sentences that are closely related in meaning. For example, "She likes apples; he likes oranges." The conjunction is missing and the semicolon is used.
- Commas should be correctly used in sentences to separate items in a list, to set off introductory words or phrases, to set off nonessential information, to indicate a pause or a change in tone, etc. For example, "However, she doesn't like bananas." The comma is used to set off the introductory word "however".
- Pronouns should agree with their antecedents in number, person and gender. A pronoun is a word that takes the place of a noun. An antecedent is the noun that the pronoun refers to. For example, "He likes his bike." The pronoun "he" agrees with the antecedent "he" in number (singular), person (third) and gender (male).

These are some of the grammar rules for English that you should learn and follow. There are many more rules and exceptions that you can study and practice to improve your language skills. You can also use online tools and resources, such as Grammarly or The Blue Book of Grammar and Punctuation, to check your grammar and punctuation. I hope this helps you with your notes for the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING.



### Treebanks

- A treebank is a corpus of natural language sentences annotated with syntactic structure, such as phrase structure trees or dependency graphs .
- Treebanks can be used for various purposes, such as:
  - Developing and evaluating natural language processing systems, such as part-of-speech taggers, parsers, semantic analyzers and machine translation systems .
  - Studying linguistic phenomena and testing linguistic hypotheses.
  - Providing rich linguistic resources for language education and learning.
- Treebanks can vary in their annotation schemes, granularity, size, domain, language and quality.
- Some examples of treebanks are:
  - The Penn Treebank, which annotates English sentences from the Wall Street Journal and other sources with phrase structure trees and part-of-speech tags.
  - The Universal Dependencies project, which aims to create cross-linguistically consistent treebanks for many languages using dependency graphs and universal part-of-speech tags.
  - The TIGER Treebank, which annotates German sentences from newspapers with dependency graphs and morphological information.
- Treebank annotation is a complex and labor-intensive task that requires linguistic expertise and annotation tools .
- Treebank quality can be measured by various criteria, such as coverage, consistency, accuracy, completeness and usability.



### Normal Forms for Grammar

- Normal forms for grammar are ways of transforming a grammar into a simpler or more restricted form without changing the language it generates.
- Normal forms are useful for simplifying the analysis and parsing of natural languages, as well as for proving properties of grammars and languages.
- There are different types of normal forms for different types of grammars, such as regular, context-free, context-sensitive, and unrestricted grammars.
- Some examples of normal forms for grammar are:

  - **Chomsky Normal Form (CNF)**: A context-free grammar is in CNF if every production is of the form A -> BC or A -> a, where A, B, and C are non-terminals and a is a terminal. CNF is useful for parsing natural languages using the CYK algorithm.
  - **Greibach Normal Form (GNF)**: A context-free grammar is in GNF if every production is of the form A -> aB1B2...Bn, where A and Bi are non-terminals and a is a terminal. GNF is useful for parsing natural languages using a top-down parser.
  - **Kuroda Normal Form (KNF)**: A context-sensitive grammar is in KNF if every production is of the form A -> B, A -> BC, AB -> CD, or ABC -> DE, where A, B, C, D, and E are non-terminals. KNF is useful for proving that context-sensitive languages are equivalent to linear bounded automata.
  - **Backus-Naur Form (BNF)**: A meta-syntax for describing context-free grammars, where productions are of the form <symbol> ::= <expression>, where <symbol> is a non-terminal and <expression> is a sequence of terminals and non-terminals. BNF is useful for defining the syntax of programming languages and natural languages.



### Dependency Grammar

- Dependency grammar is a descriptive and theoretical tradition in linguistics that can be traced back to antiquity.
- It has long been influential in the European linguistics tradition and has more recently become a mainstream approach to representing syntactic and semantic structure in natural language processing.
- Dependency grammar is based on the idea that linguistic units, such as words, are connected by directed links called dependencies.
- Dependencies express grammatical relations between words, such as subject, object, modifier, etc.
- Dependencies are represented by labeled directed graphs, where nodes are words and edges are dependencies.
- The root of the graph is usually the main verb or predicate of the sentence.
- The direction of the dependency indicates the head-dependent relation, where the head is the word that governs the dependent.
- For example, in the sentence "She likes apples", the verb "likes" is the head of the subject "she" and the object "apples", and the dependencies are labeled as nsubj (nominal subject) and dobj (direct object) respectively.
- Dependency grammar has several advantages over other syntactic frameworks, such as phrase structure grammar or constituency grammar :
  - It is more economical and parsimonious, as it does not require intermediate nodes or categories to represent syntactic structure.
  - It is more transparent and intuitive, as it directly reflects the semantic relations between words and avoids the ambiguity of phrase boundaries.
  - It is more flexible and adaptable, as it can handle various word orders, discontinuous constructions, and non-projective dependencies.
  - It is more compatible and consistent with the neural network models that are widely used in natural language processing, as it can be easily encoded as adjacency matrices or tensors.
- Dependency grammar has several applications in natural language processing, such as dependency parsing, semantic role labeling, information extraction, machine translation, and natural language understanding.
- Dependency parsing is the task of automatically analyzing the dependency structure of a given sentence, i.e., identifying the words, their dependencies, and their labels.
- Dependency parsing can be performed using various methods, such as rule-based, transition-based, graph-based, or neural network-based algorithms .
- Dependency parsing is an important step for many downstream natural language processing tasks, such as syntactic analysis, semantic analysis, sentiment analysis, question answering, and summarization .



# Syntactic Parsing

- Syntactic parsing is the process of analyzing natural language with the rules of a formal grammar .
- Syntactic parsing assigns a semantic structure to text, such as a constituent or dependency tree .
- Syntactic parsing applies grammatical rules only to categories and groups of words, not to individual words .
- Syntactic parsing is an important task in natural language processing, and has been a subject of research since the mid-20th century with the advent of computers.
- Syntactic parsing is useful for downstream tasks such as semantic parsing, relation extraction, and machine translation .
- Syntactic parsing can be performed using different methods, such as rule-based, probabilistic, or neural network-based approaches .
- Syntactic parsing can be supervised, semi-supervised, or unsupervised, depending on the availability and quality of annotated data.
- Syntactic parsing can be evaluated using different metrics, such as accuracy, precision, recall, or F1-score .
- Syntactic parsing can be challenging due to the ambiguity, complexity, and variability of natural language .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of ambiguity in syntactic analysis.

### Ambiguity

- Ambiguity is the property of a sentence or phrase that can have more than one meaning or interpretation.
- Ambiguity can arise at different levels of natural language processing, such as lexical, syntactic, semantic, or pragmatic.
- Syntactic ambiguity is the type of ambiguity that occurs when a sentence or phrase can have more than one syntactic structure or parse tree.
- Syntactic ambiguity can be caused by factors such as word order, punctuation, attachment of modifiers, coordination, or scope of operators.
- Syntactic ambiguity can affect the meaning and understanding of a sentence or phrase, as well as its translation, summarization, or generation.
- Syntactic ambiguity can be resolved by using various methods, such as context, world knowledge, discourse structure, or linguistic cues.
- Syntactic ambiguity can also be exploited for various purposes, such as humor, rhetoric, or poetry.

Some examples of syntactic ambiguity are:

- I saw the man with the telescope. (Who has the telescope?)
- They are flying planes. (Who are flying? What are planes?)
- The chicken is ready to eat. (Who is ready to eat?)
- He likes cooking his family and his dogs. (What does he like cooking?)



### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- It is based on the idea of storing and reusing partial results of the parsing process in a table or chart, rather than recomputing them.
- It is a bottom-up parsing strategy, meaning that it starts from the words (or tokens) of the input sentence and builds larger constituents (or phrases) using the grammar rules.
- It is also a dynamic programming algorithm, meaning that it solves a complex problem by breaking it down into simpler subproblems and solving them optimally.
- The most common dynamic programming parsing algorithm is the Cocke-Kasami-Younger (CKY) algorithm, which has a time complexity of O(n^3 * |G|), where n is the length of the input sentence and |G| is the size of the grammar.
- The CKY algorithm works as follows:

  - Initialize an n x n chart, where each cell (i, j) corresponds to a span of words from i to j in the input sentence.
  - For each word w_i in the input sentence, fill the cell (i, i) with the nonterminal symbols that can generate w_i according to the grammar rules. These are called the preterminal symbols.
  - For each span length l from 2 to n, and for each start position i from 1 to n - l + 1, fill the cell (i, i + l - 1) with the nonterminal symbols that can generate the span from i to i + l - 1 according to the grammar rules. These are called the intermediate symbols.
  - To fill a cell (i, j), consider all possible splits of the span from i to j into two smaller spans: from i to k and from k + 1 to j, where i <= k < j. For each split, check if there is a grammar rule of the form A -> B C, where B is in the cell (i, k) and C is in the cell (k + 1, j). If so, add A to the cell (i, j).
  - The chart is filled in a diagonal fashion, from bottom left to top right, ensuring that the smaller spans are filled before the larger ones.
  - The final cell (1, n) contains the nonterminal symbols that can generate the whole input sentence. If the start symbol of the grammar (usually S) is in this cell, then the sentence is accepted by the grammar and a parse tree can be constructed by tracing back the chart. If not, then the sentence is rejected by the grammar and no parse tree exists.



### Shallow parsing

- Shallow parsing (also called chunking or light parsing) is an analysis of a sentence which first identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and then links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.).
- Shallow parsing is different from deep parsing, which aims to produce a complete and detailed parse tree that represents the syntactic structure and semantic roles of a sentence.
- Shallow parsing is useful for natural language processing tasks that do not require full syntactic analysis, such as information extraction, named entity recognition, sentiment analysis, etc.
- Shallow parsing can be seen as a set of cascaded classification problems with separate classifiers for tagging, chunk boundary detection, chunk labeling, relation finding, etc.
- Shallow parsing can be performed using rule-based, statistical, or machine learning methods, or a combination of them.
- Shallow parsing can be evaluated using metrics such as precision, recall, and F1-score, which measure how well the system identifies and labels the chunks in a sentence.



# Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probabilities of the rules are estimated from a corpus of annotated sentences, called a treebank.
- A PCFG can be used to model the syntactic structure of natural languages, and to parse new sentences with a probabilistic parser.
- A probabilistic parser finds the most likely parse tree for a given sentence, or the probability distribution over all possible parse trees.
- A PCFG can be defined as a tuple (N, Σ, R, S, P), where:
  - N is a set of nonterminal symbols
  - Σ is a set of terminal symbols (words)
  - R is a set of production rules of the form A -> α, where A is a nonterminal and α is a string of nonterminals and terminals
  - S is the start symbol
  - P is a function that assigns a probability to each rule, such that for each nonterminal A, the sum of the probabilities of all rules with A on the left-hand side is 1.
- A PCFG can be converted to Chomsky Normal Form (CNF), where each rule has at most two nonterminals on the right-hand side, by introducing new nonterminals and rules.
- A PCFG in CNF can be parsed efficiently with the CKY algorithm, which is a dynamic programming algorithm that fills a chart with the probabilities of all possible sub-trees for each span of the sentence.
- The CKY algorithm can also be extended to handle unary rules, which have only one nonterminal on the right-hand side, by collapsing them into a single nonterminal with a combined probability.



### Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees for each substring of the input sentence in a table.
- The algorithm works as follows:

  - Initialize the table with the probabilities of the terminal symbols for each word in the sentence.
  - For each substring of length 2 or more, consider all possible ways of splitting it into two smaller substrings, and all possible rules that can generate the substring from two nonterminals.
  - For each rule A -> BC, compute the probability of the substring being generated by A as the product of the probability of the rule and the probabilities of the subtrees for B and C.
  - Store the maximum probability and the corresponding rule for each nonterminal A in the table entry for the substring.
  - Repeat until the table entry for the whole sentence is filled.
  - Trace back the table from the entry for the whole sentence to find the most likely parse tree.

- The probabilistic CYK algorithm can be used for parsing natural language sentences, given a suitable PCFG that models the syntax and the lexical preferences of the language.



### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule, such that the sum of the probabilities of all rules with the same left-hand side is 1.
- PCFGs can be used to model the likelihood of different syntactic structures for a given sentence, and to select the most probable parse tree among the possible ones.
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the non-terminal symbols, such that each non-terminal is associated with a head word that determines its subcategorization and selectional preferences.
- L-PCFGs can capture more fine-grained syntactic distinctions and dependencies than PCFGs, and can improve the accuracy of parsing and disambiguation.
- L-PCFGs can be learned from a treebank of annotated sentences, by extracting the head words of each non-terminal node and estimating the rule probabilities from the relative frequencies of the rules in the corpus.
- L-PCFGs can be parsed using the same algorithms as PCFGs, such as the CKY algorithm or the Earley algorithm, with some modifications to handle the lexicalization of the non-terminals.



### Feature structures for the notes of the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Natural Language Processing (NLP) is a branch of artificial intelligence that attempts to bridge the gap between what a machine recognizes as input and the human language.
- NLP combines artificial intelligence, computational linguistics and machine learning to enable computers and humans to communicate seamlessly.
- NLP can be divided into three main tasks: speech recognition, natural language understanding and natural language generation.
- Speech recognition is the translation of spoken language into text.
- Natural language understanding is the computer's ability to understand what we say.
- Natural language generation is the generation of natural language by a computer.
- Syntactic analysis is a subtask of natural language understanding that deals with the structure and rules of language.
- Syntactic analysis involves parsing sentences into their constituent parts and assigning grammatical categories and functions to them.
- Syntactic analysis can be done using different types of grammars, such as phrase structure grammars, dependency grammars and feature based grammars.
- Feature based grammars are a type of grammars that use features to describe the properties and relations of linguistic units.
- Features are atomic symbols or pairs of attribute-value that can be attached to linguistic units, such as words, phrases or sentences.
- Features can capture various aspects of language, such as number, gender, case, tense, mood, agreement, subcategorization, etc.
- Feature structures are sets of features that are organized in a hierarchical manner, using brackets and indentation.
- Feature structures can be used to represent the syntactic and semantic information of linguistic units in a compact and modular way.
- Feature structures can be manipulated using the operation of unification, which allows us to combine the information contained in two different feature structures.
- Unification is the process of finding a feature structure that is compatible with both input feature structures, or failing if there is no such feature structure.
- Unification can be used to check the grammaticality and the meaning of sentences, by unifying the feature structures of the words and phrases in the sentence.
- Unification can also be used to generate sentences, by unifying the feature structures of the desired meaning and the available lexical items.
- Feature based grammars can be implemented using various formalisms, such as head-driven phrase structure grammar (HPSG), lexical functional grammar (LFG) and constraint-based grammar (CBG).
- Feature based grammars can handle various linguistic phenomena, such as word order variation, coordination, ellipsis, anaphora, etc.



### Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- A feature structure is a set of attribute-value pairs, where the attributes are symbols and the values are either symbols or other feature structures.
- For example, the feature structure for a noun phrase "the dog" can be written as:

```
[cat: NP
 det: [cat: Det
       form: the]
 head: [cat: N
        form: dog]]
```

- Unification is a (partial) operation on feature structures. Intuitively, it is the operation of combining two feature structures such that the new feature structure contains all the information of the original two, and nothing more.
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- For example, the unification of the feature structures `[cat: NP, det: [cat: Det]]` and `[cat: NP, head: [cat: N]]` is `[cat: NP, det: [cat: Det], head: [cat: N]]`.
- Unification is used in natural language processing (NLP) for various tasks, such as parsing, generation, and semantic interpretation.
- Unification can be implemented using different data structures and algorithms, such as binding lists, feature matrices, or hash tables.
- Unification can also be extended to E-unification, which allows for the use of equations and variables in feature structures .
- E-unification can handle more complex linguistic phenomena, such as agreement, anaphora, and ellipsis.



## Unit 3 - SEMANTICS AND PRAGMATICS

- Semantics and pragmatics are two important branches of linguistics that study the meaning of language  .
- Semantics studies the meaning of words and sentences in a general and abstract way, without considering the context or the speaker's intention  .
- Pragmatics studies the meaning of words and sentences in a specific and concrete way, taking into account the context, the speaker's intention, and the listener's inference  .
- Semantics is context-independent, while pragmatics is context-dependent . For example, the sentence "It's raining" has the same semantic meaning in any situation, but it can have different pragmatic meanings depending on who says it, where, when, and why.
- Semantics has a narrower scope than pragmatics, as it only deals with the truth-conditional aspect of language, that is, the conditions under which a sentence is true or false . Pragmatics has a broader scope, as it also deals with the non-truth-conditional aspect of language, that is, the implications, assumptions, and effects of using language in communication .
- Semantics and pragmatics are complementary to each other, as they both contribute to the understanding of meaning in language . However, they are also distinct from each other, as they have different methods, goals, and phenomena of study .



### Requirements for representation for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Semantics is the study of meaning in natural language, while pragmatics is the study of meaning in context.
- A representation for semantics and pragmatics should capture the following aspects of natural language meaning:
  - **Lexical semantics**: the meaning of words and how they relate to each other, such as synonyms, antonyms, hyponyms, hypernyms, meronyms, etc.
  - **Compositional semantics**: the meaning of phrases and sentences and how they are derived from the meaning of their constituents, such as by applying rules of syntax and logic.
  - **Discourse semantics**: the meaning of texts and dialogues and how they are structured and connected, such as by using coherence, cohesion, anaphora, presupposition, etc.
  - **Pragmatic inference**: the meaning of utterances and how they are influenced by the speaker's intention, the listener's expectation, the situational context, the common ground, the speech acts, the implicatures, etc.
- A representation for semantics and pragmatics should also satisfy the following requirements:
  - **Expressiveness**: the representation should be able to capture the richness and diversity of natural language meaning, including ambiguity, vagueness, metaphor, irony, etc.
  - **Formality**: the representation should be based on a well-defined syntax and semantics, allowing for precise and consistent interpretation and manipulation of meaning.
  - **Computability**: the representation should be amenable to efficient and effective computation, enabling natural language processing tasks such as parsing, generation, translation, summarization, question answering, etc.
- Some examples of representations for semantics and pragmatics are:
  - **First-order logic**: a formal language that uses symbols, variables, constants, predicates, functions, quantifiers, and connectives to represent the meaning of natural language expressions.
  - **Semantic networks**: a graphical representation that uses nodes to represent concepts and links to represent relations between concepts, such as inheritance, causation, part-of, etc.
  - **Frames**: a data structure that uses slots to represent attributes and values of concepts, such as color, size, shape, etc.
  - **Scripts**: a data structure that uses slots to represent events and roles of concepts, such as agent, patient, instrument, etc.
  - **Conceptual graphs**: a graphical representation that combines semantic networks and frames, using nodes to represent concepts and links to represent relations and attributes of concepts.
  - **Discourse representation theory**: a formal theory that uses discourse representation structures to represent the meaning of texts and dialogues, including the entities, events, and situations involved, as well as their accessibility and anaphoric relations.
  - **Relevance theory**: a pragmatic theory that explains how speakers and listeners infer meaning from utterances based on the principle of relevance, which states that every utterance conveys a presumption of its own optimal relevance.



### First-Order Logic

First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects, events, and situations in natural language. FOL is also called predicate logic or first-order predicate calculus.

Some of the main features of FOL are:

- FOL has a simple syntax that consists of symbols for constants, variables, functions, predicates, logical connectives, and quantifiers.
- FOL has a well-defined semantics that assigns truth values to sentences based on a model, which is a set of objects and an interpretation of the symbols.
- FOL has a powerful inference mechanism that allows deriving new sentences from existing ones using rules of logic, such as modus ponens, universal instantiation, and resolution.
- FOL can express many aspects of natural language semantics, such as negation, conjunction, disjunction, implication, equivalence, quantification, and equality.

Some of the main limitations of FOL are:

- FOL cannot express some semantic phenomena that require higher-order logic, such as intensionality, modality, and anaphora.
- FOL cannot capture the ambiguity, vagueness, context-dependence, and pragmatics of natural language.
- FOL is undecidable, which means that there is no algorithm that can determine whether a given sentence is valid, satisfiable, or entailed by another sentence in general.

Some of the main applications of FOL in natural language processing are:

- FOL can be used as a target representation for semantic parsing, which is the task of mapping natural language sentences to formal representations that can be manipulated by a computer.
- FOL can be used as a source representation for natural language generation, which is the task of producing natural language sentences from formal representations that convey a desired meaning.
- FOL can be used as a medium for natural language understanding, which is the task of extracting and inferring relevant information from natural language texts using logical reasoning.

Some of the main challenges of FOL in natural language processing are:

- FOL requires a large and consistent lexicon and grammar that can map natural language words and phrases to logical symbols and structures.
- FOL requires a robust and efficient parser that can handle the complexity and variability of natural language syntax and semantics.
- FOL requires a reliable and scalable theorem prover that can perform logical inference on large and noisy datasets of natural language sentences.



# Description Logics for Natural Language Processing

- Description logics (DLs) are a family of logic-based knowledge representation languages that allow for the formalization of concepts, roles, and individuals in a domain of interest.
- DLs can be used for various applications in natural language processing (NLP), such as the representation of ontologies, the analysis of the semantics of natural language sentences, and the reasoning with natural language queries  .
- DLs are based on the notions of interpretation, satisfaction, and entailment. An interpretation assigns a set of individuals to each concept and a binary relation to each role. A concept or a role is satisfied by an interpretation if it is not empty. An interpretation entails a sentence if the sentence is true in the interpretation.
- DLs have different expressive power and computational complexity depending on the constructors and axioms they allow. For example, the DL ALC allows for conjunction, disjunction, negation, universal and existential quantification, and inclusion axioms. ALC is decidable and has a worst-case complexity of EXPTIME.
- DLs can be extended with various features, such as nominals, inverse roles, role hierarchies, number restrictions, transitive roles, role chains, and datatypes. These extensions increase the expressiveness and the complexity of DLs, and may require different reasoning algorithms.
- DLs can be used to represent ontologies, which are formal specifications of the concepts and relations in a domain. Ontologies can be used to annotate natural language texts, to extract information from texts, and to support natural language understanding and generation .
- DLs can also be used to analyze the semantics of natural language sentences, by mapping natural language expressions to DL concepts and roles. This can be done by using a lexicon that associates natural language words with DL symbols, and by using a grammar that specifies how natural language phrases and sentences are composed from words .
- DLs can also be used to reason with natural language queries, by translating natural language questions to DL queries, and by using a DL reasoner to compute the answers. This can be done by using a query language that allows for the specification of DL queries, and by using a query answering algorithm that exploits the structure and the semantics of DLs .



### Syntax-Driven Semantic Analysis

- Syntax-driven semantic analysis is a method of deriving the meaning of natural language sentences from their syntactic structure and lexical information.
- It involves applying rules of formal grammar to assign semantic structures to sentences or phrases, such as logical forms, predicate-argument structures, or semantic role labels.
- It assumes that there is a correspondence between the syntactic categories and the semantic types of words and phrases, and that the syntactic rules can be augmented with semantic rules to produce semantic representations.
- It can be implemented using various formalisms, such as lambda calculus, feature structures, or tree-adjoining grammar.
- It can be used for various natural language processing tasks, such as information extraction, question answering, or machine translation.
- It can also be combined with other sources of semantic information, such as ontologies, world knowledge, or pragmatics, to achieve more accurate and comprehensive semantic analysis.



### Semantic attachments for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Semantic attachments are a way of connecting the syntactic structure of a sentence with its semantic representation, such as a logical form or a meaning representation language.
- Semantic attachments are usually implemented as functions or rules that map syntactic categories or constituents to semantic expressions, based on the lexical semantics of the words and the compositional semantics of the phrases.
- Semantic attachments can be used for various natural language processing (NLP) tasks, such as semantic parsing, question answering, information extraction, text summarization, and natural language generation.
- Semantic attachments can be defined manually, learned automatically, or a combination of both, depending on the availability of annotated data and the complexity of the semantic representation.
- Semantic attachments can be classified into different types, such as:
  - Predicate-argument attachments: These map the syntactic arguments of a verb or a predicate to the semantic arguments of a logical predicate or a relation. For example, the sentence "John loves Mary" can be mapped to the logical form `love(John, Mary)`, where `love` is the predicate and `John` and `Mary` are the arguments.
  - Modifier attachments: These map the syntactic modifiers of a word or a phrase to the semantic modifiers of a logical expression or a concept. For example, the sentence "The red car is fast" can be mapped to the logical form `fast(car) ∧ red(car)`, where `fast` and `red` are the modifiers and `car` is the concept.
  - Quantifier attachments: These map the syntactic quantifiers of a noun phrase to the semantic quantifiers of a logical expression or a scope. For example, the sentence "Every student likes some teacher" can be mapped to the logical form `∀x(student(x) → ∃y(teacher(y) ∧ like(x, y)))`, where `∀` and `∃` are the quantifiers and `x` and `y` are the variables.
  - Anaphora attachments: These map the syntactic anaphoric expressions, such as pronouns or ellipses, to the semantic antecedents or referents of a logical expression or a discourse. For example, the sentence "He saw her yesterday" can be mapped to the logical form `see(x, y, yesterday)`, where `x` and `y` are the variables that refer to the antecedents of `he` and `her` respectively.



### Word Senses

- A word sense is the meaning of a word in a given context.
- A word can have multiple senses depending on how it is used in different sentences or situations.
- For example, the word "bank" can have the following senses:
  - A financial institution that holds money and provides loans.
  - The edge of a river or lake.
  - A set of similar things arranged in a row or a group.
  - An act of tilting or turning something sideways.
- Word sense disambiguation is the task of identifying the correct sense of a word in a given context.
- Word sense disambiguation can be done using various methods, such as:
  - Dictionary-based methods that use definitions and examples from a lexical resource, such as WordNet, to match the word with the most appropriate sense.
  - Corpus-based methods that use statistical information from large collections of texts, such as frequency, collocations, and co-occurrences, to determine the most likely sense of a word.
  - Knowledge-based methods that use external sources of information, such as ontologies, semantic networks, or common sense knowledge, to infer the meaning of a word from the context.
  - Supervised methods that use machine learning techniques to train a classifier or a neural network to predict the sense of a word based on features extracted from the context.
  - Unsupervised methods that use clustering algorithms to group words into senses based on their similarity or relatedness.
- Word sense disambiguation is important for natural language processing applications, such as:
  - Machine translation, where the correct sense of a word can affect the choice of the target word or phrase in another language.
  - Information retrieval, where the correct sense of a word can affect the relevance of a document or a query.
  - Information extraction, where the correct sense of a word can affect the extraction of entities, relations, or events from a text.
  - Text summarization, where the correct sense of a word can affect the selection and compression of the main points of a text.
  - Text generation, where the correct sense of a word can affect the coherence and fluency of the generated text.



### Relations between Senses

- Senses are the meanings of words or expressions in a given context or situation.
- Semantics is the study of the relations between senses and the objects or concepts they refer to.
- Pragmatics is the study of the relations between senses and the users or situations that produce or interpret them.
- The relations between senses can be classified into two types: paradigmatic and syntagmatic.
- Paradigmatic relations are the relations between senses that belong to the same category or class, such as synonyms, antonyms, hyponyms, etc.
- Syntagmatic relations are the relations between senses that can combine or co-occur with each other in a sentence or discourse, such as collocations, selectional restrictions, implicatures, etc.
- The relations between senses can be affected by various factors, such as context, intention, inference, culture, etc.
- The relations between senses can be used to analyze the meaning of words, sentences, and texts, as well as to generate or understand natural language.



# Thematic Roles

Thematic roles are the semantic relationships between a verb and its arguments. They describe the role or function of each argument in the event or state expressed by the verb. For example, in the sentence "John ate the apple", John is the agent (the one who performs the action of eating) and the apple is the theme (the one who undergoes the action of eating).

Thematic roles are important for natural language processing because they help to identify the meaning and structure of sentences. They can also be used for tasks such as semantic role labeling, which is the process of assigning thematic roles to the arguments of a verb in a sentence.

There are different types of thematic roles, and different theories may propose different inventories of them. However, some of the most common and widely accepted thematic roles are:

- Agent: The entity that intentionally performs the action of the verb. For example, in "Mary opened the door", Mary is the agent.
- Experiencer: The entity that undergoes an emotion, a state of being, or a perception expressed by the verb. For example, in "She loves him", she is the experiencer.
- Theme: The entity that directly receives the action of the verb or is affected by it. For example, in "He broke the vase", the vase is the theme.
- Instrument: The entity by which the action of the verb is carried out. For example, in "She cut the cake with a knife", the knife is the instrument.
- Goal: The entity towards which the action of the verb is directed. For example, in "He gave her a book", her is the goal.
- Source: The entity from which the action of the verb originates. For example, in "She took the book from him", him is the source.
- Location: The entity where the action of the verb takes place. For example, in "They live in Paris", Paris is the location.
- Beneficiary: The entity for whom the action of the verb is performed. For example, in "He cooked dinner for her", her is the beneficiary.
- Manner: The entity that describes how the action of the verb is performed. For example, in "She sang beautifully", beautifully is the manner.
- Cause: The entity that initiates or triggers the action of the verb. For example, in "The storm caused the flood", the storm is the cause.

Thematic roles are assigned by the verb to its arguments according to the theta criterion, which states that each argument must receive exactly one thematic role, and each thematic role must be assigned to exactly one argument. For example, in "She loves him", she and him each receive one thematic role (experiencer and theme, respectively), and each thematic role is assigned to one argument. However, some verbs may have optional arguments that do not receive a thematic role, such as adjuncts or modifiers. For example, in "She loves him dearly", dearly does not receive a thematic role, but modifies the verb.



### Selectional restrictions

- Selectional restrictions are semantic constraints that limit the possible arguments of a word or a phrase  .
- They account for the implausibility or ungrammaticality of sentences such as *Colorless green ideas slept furiously* or *The chair ate the cake* .
- They are based on the semantic features or categories of the arguments, such as animacy, gender, number, shape, color, etc  .
- They can be used in natural language processing for tasks such as disambiguation, pronoun resolution, lexical insertion, and sentence generation  .
- They can be violated for rhetorical or poetic effects, such as metaphor, irony, or humor.
- They can be modeled using distributional semantics, which captures the co-occurrence patterns of words in large corpora.



### Word Sense Disambiguation

- Word sense disambiguation (WSD) is the problem of determining which "sense" (meaning) of a word is activated by the use of the word in a particular context, a process which appears to be largely unconscious in people.
- WSD is a subfield of natural language processing (NLP) that deals with identifying the intended meaning of a word from a set of possible senses, based on the context in which the word appears.
- WSD is important for many NLP applications, such as machine translation, information retrieval, text summarization, question answering, sentiment analysis, etc.
- WSD is challenging because of the lexical ambiguity, syntactic or semantic, that is inherent in natural language. Lexical ambiguity is the phenomenon of a word having more than one meaning or sense.
- For example, the word "bank" can have different meanings depending on the context: a financial institution, a river shore, a verb meaning to tilt or turn, etc.
- WSD can be classified into two types: supervised and unsupervised. Supervised WSD uses labeled data, such as sense-annotated corpora, to train machine learning models that can predict the correct sense of a word given its context. Unsupervised WSD does not use labeled data, but relies on clustering, similarity measures, or knowledge bases to group words into senses based on their usage patterns.
- WSD also depends on the choice of sense inventory, which is the collection of abbreviations and acronyms with their meanings for a particular domain or language. Different sense inventories may have different levels of granularity, coverage, and consistency. Some examples of sense inventories are WordNet, BabelNet, Wikipedia, etc.
- WSD is an active and open research problem in NLP, as there is no definitive solution or evaluation method for it. Some of the current challenges and directions for WSD are: improving the quality and availability of sense-annotated data, developing domain-specific and cross-lingual WSD methods, integrating WSD with other NLP tasks, and exploring the cognitive and linguistic aspects of WSD.



### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the supervised learning algorithms that have been applied to WSD are decision trees, naive Bayes, support vector machines, neural networks, etc  .
- Supervised WSD methods have the advantage of being able to learn from large amounts of data and achieve high accuracy, but they also have some limitations, such as:
  - They require a lot of manually annotated data, which is costly and time-consuming to obtain .
  - They suffer from the data sparsity problem, which means that they may not have enough examples for rare or fine-grained senses .
  - They are domain-dependent, which means that they may not generalize well to new domains or genres that differ from the training data .



### Dictionary & Thesaurus for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- A dictionary is a resource that provides information about the meaning, spelling, pronunciation, and usage of words in a language.
- A thesaurus is a resource that provides synonyms and antonyms of selected words in a language, thus grouping words according to similarity.
- Both dictionaries and thesauruses are useful for natural language processing (NLP), which is the application of machine learning algorithms to the analysis, understanding, and manipulation of written or spoken examples of human language.
- Some of the benefits of using dictionaries and thesauruses for NLP are:
  - They can help to resolve ambiguity and improve accuracy in tasks such as word sense disambiguation, which is the process of identifying the correct meaning of a word in a given context.
  - They can help to enrich the vocabulary and diversity of language generation tasks, such as text summarization, paraphrasing, and dialogue systems.
  - They can help to provide semantic information and relations between words, such as synonyms, antonyms, hypernyms, hyponyms, meronyms, and holonyms, which can be useful for tasks such as semantic similarity, entailment, and inference.
- Some of the challenges of using dictionaries and thesauruses for NLP are:
  - They may not cover all the words and senses in a language, especially new or domain-specific terms, slang, or idioms.
  - They may introduce new ambiguity and complexity, as different dictionaries and thesauruses may have different definitions, classifications, and formats of word senses.
  - They may not capture the dynamic and contextual nature of language, as word meanings and usage may change over time and across domains, genres, and registers.
- Some of the methods and techniques of using dictionaries and thesauruses for NLP are:
  - Dictionary- and knowledge-based methods, which rely on text data like dictionaries, thesaurus, etc. to find related words and senses in the definitions. An example is the Lesk method, which compares the overlap of words between the definition of a target word and the surrounding context.
  - Supervised methods, which use annotated data to train machine learning models to learn the mapping between words and senses. An example is the Naive Bayes classifier, which uses the probability of a word given a sense to predict the most likely sense.
  - Unsupervised methods, which use unlabeled data to discover word senses and clusters based on similarity or co-occurrence. An example is the word2vec model, which uses a neural network to learn word embeddings that capture semantic and syntactic features of words.
  - Hybrid methods, which combine different sources of information and methods to improve the performance and robustness of NLP tasks. An example is the UWN method, which integrates a large-scale multilingual thesaurus with a probabilistic word sense disambiguation system.



### Bootstrapping methods for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods can be applied to various natural language processing (NLP) tasks, such as part-of-speech tagging, named entity recognition, relation extraction, sentiment analysis, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., words, phrases, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., manually annotated examples, heuristics, rules, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using pattern matching, classification, clustering, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more new things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Self-training: The model learns from its own predictions on the unlabeled data and adds the most confident ones to the labeled data.
  - Co-training: The model consists of two or more classifiers that learn from different views or features of the data and mutually teach each other by adding the most confident predictions to the labeled data.
- Bootstrapping methods can also be combined with other techniques, such as rule-based parsing, active learning, or ensemble learning, to improve the performance and robustness of the model.
- Bootstrapping methods have some advantages and disadvantages:
  - Advantages: They can reduce the need for manual annotation, which is costly and time-consuming. They can also exploit the large amount of unlabeled data available on the web or other sources.
  - Disadvantages: They can suffer from semantic drift, which is the deviation of the model from the original task or domain due to the accumulation of errors or noise in the unlabeled data. They can also be sensitive to the choice of seeds, which can affect the quality and diversity of the learned things.



### Word Similarity using Thesaurus and Distributional methods

- Word similarity is the degree to which two words share a common meaning or are semantically related.
- Thesaurus and distributional methods are two approaches to measure word similarity based on different sources of information.
- Thesaurus methods rely on manually constructed lexical resources, such as WordNet, Roget's Thesaurus, or BabelNet, that group words into synonym sets or semantic categories.
- Distributional methods rely on automatically extracted statistical information from large corpora, based on the assumption that words that occur in similar contexts are similar in meaning.
- Thesaurus methods have the advantage of capturing fine-grained semantic distinctions and relations, but they are limited by the coverage and quality of the available resources, and they may not reflect the current usage of words in natural language.
- Distributional methods have the advantage of being scalable, adaptable, and data-driven, but they may not capture the nuances and subtleties of word meanings, and they may be sensitive to the choice of parameters, such as similarity measures, frequency thresholds, and association scores.
- Similarity measures are mathematical functions that quantify the degree of similarity between two words based on their representations, such as vectors, matrices, or graphs.
- Frequency thresholds are minimum values that filter out words or contexts that occur too rarely or too frequently in the corpus, to reduce noise and sparsity.
- Association scores are numerical values that indicate the strength of the association between a word and a context, such as pointwise mutual information, log-likelihood ratio, or cosine similarity.
- To construct a distributional thesaurus, the contexts in which a target word occurs are extracted from a corpus, and the frequencies of the co-occurring word-context pairs are computed. Then, a similarity measure is applied to compare the target word with other words based on their contexts, and a list of semantically related neighbors is generated for each target word, ranked by decreasing similarity.



## Unit 4 - BASIC CONCEPTS of Speech Processing

Speech processing is the study of how humans produce, perceive, and understand speech, as well as how speech can be processed by machines. Speech processing involves three major levels of processing: production, perception, and analysis.

- Speech production is the process by which thoughts are translated into speech. This includes the selection of words, the organization of relevant grammatical forms, and then the articulation of the resulting sounds by the motor system using the vocal apparatus.
- Speech perception is the process by which the acoustic signals of speech are decoded and interpreted by the auditory system and the brain. This involves the recognition of speech sounds, words, phrases, and sentences, as well as the extraction of meaning and intention from speech.
- Speech analysis is the process by which speech signals are transformed into numerical or symbolic representations that can be manipulated by machines. This involves the extraction of features, such as pitch, intensity, duration, and spectral properties, from speech signals, as well as the application of algorithms and techniques, such as segmentation, classification, recognition, synthesis, and enhancement, to achieve various objectives in speech processing applications.

Some of the basic concepts of speech processing are:

- Speech is a complex and dynamic signal that varies in time and frequency. Speech signals can be represented as waveforms, which show the variation of air pressure over time, or as spectrograms, which show the variation of frequency and intensity over time.
- Speech is composed of basic units, such as phonemes, syllables, words, and phrases, that have different levels of linguistic and acoustic information. Phonemes are the smallest units of speech that can distinguish meaning, such as /p/ and /b/ in "pat" and "bat". Syllables are the units of speech that consist of one or more phonemes, such as /pæt/ and /bæt/. Words are the units of speech that have lexical meaning, such as "pat" and "bat". Phrases are the units of speech that have syntactic and semantic meaning, such as "pat the bat" and "bat the pat".
- Speech is influenced by various factors, such as speaker, language, dialect, accent, emotion, context, and noise. Speaker factors include the age, gender, health, and identity of the speaker, which affect the anatomy and physiology of the vocal tract, as well as the style and intention of the speech. Language factors include the vocabulary, grammar, and phonology of the language, which affect the choice and organization of words and sounds. Dialect and accent factors include the regional and social variations of the language, which affect the pronunciation and usage of words and sounds. Emotion factors include the mood and attitude of the speaker, which affect the prosody and expression of the speech. Context factors include the topic, purpose, and situation of the speech, which affect the content and structure of the speech. Noise factors include the background and environmental sounds, which affect the quality and intelligibility of the speech.



### Speech Fundamentals

- Speech is the natural mode of communication for humans, and speech processing is the study of how to analyze, understand, and generate speech using computational methods.
- Speech processing is a subfield of natural language processing (NLP), which is the branch of artificial intelligence that deals with the interaction between computers and human languages.
- Speech processing involves several tasks, such as:
  - Speech recognition: the process of converting spoken voice data into text data.
  - Speech synthesis: the process of generating speech from text data or other inputs.
  - Speech analysis: the process of extracting features, information, and meaning from speech signals.
  - Speech enhancement: the process of improving the quality and intelligibility of speech signals.
  - Speech coding: the process of compressing and decompressing speech signals for transmission or storage.
  - Speech translation: the process of translating speech from one language to another.
- Speech processing relies on various techniques and models, such as:
  - Acoustic modeling: the representation of the relationship between speech sounds and their corresponding acoustic features, such as frequency, amplitude, and duration.
  - Language modeling: the representation of the statistical properties and structure of natural languages, such as vocabulary, grammar, and syntax.
  - Hidden Markov models (HMMs): a probabilistic framework for modeling sequential data, such as speech signals, based on the assumption that the underlying system is a Markov process with hidden states.
  - Neural networks: a computational paradigm that mimics the structure and function of biological neurons, and can learn complex patterns and functions from data.
  - Deep learning: a subfield of machine learning that uses multiple layers of neural networks to learn high-level abstractions and features from data.
  - Attention mechanisms: a technique that allows neural networks to focus on relevant parts of the input or output, and to dynamically align them.
- Speech processing has many applications and benefits, such as:
  - Voice assistants: software agents that can perform tasks or services for users based on voice commands, such as Siri, Alexa, and Cortana.
  - Speech-to-text: software that can transcribe speech into text, such as Google Docs Voice Typing, Microsoft Dictate, and Dragon NaturallySpeaking.
  - Text-to-speech: software that can synthesize speech from text, such as Google Text-to-Speech, Microsoft Speech Synthesis, and Amazon Polly.
  - Speech analytics: software that can analyze speech data for various purposes, such as sentiment analysis, emotion recognition, speaker identification, and speech summarization.
  - Speech translation: software that can translate speech from one language to another, such as Google Translate, Microsoft Translator, and Skype Translator.
  - Speech therapy: software that can help people with speech disorders or impairments, such as stuttering, aphasia, and dysarthria, to improve their speech skills and quality of life.



# Articulatory Phonetics

- Articulatory phonetics is the branch of phonetics that studies how speech sounds are produced by the human vocal tract .
- Speech sounds are produced by the interaction of different physiological structures, such as the lungs, the larynx, the tongue, the lips, and the teeth.
- Articulatory phonetics is concerned with the transformation of aerodynamic energy (airflow) into acoustic energy (sound waves) by the movements and/or positions of the vocal organs (articulators) .
- Articulatory phonetics is also interested in the physical and cognitive factors that determine what are possible speech sounds and sound patterns in the world's languages.
- Articulatory phonetics uses various methods and tools to describe and measure the articulatory features of speech sounds, such as X-ray, ultrasound, MRI, electropalatography, and acoustic analysis .
- Articulatory phonetics can be divided into two main subfields: segmental phonetics and suprasegmental phonetics.
  - Segmental phonetics deals with the production and classification of individual speech sounds (segments), such as vowels and consonants.
  - Suprasegmental phonetics deals with the production and perception of features that span over more than one segment, such as stress, intonation, and tone.



# Production And Classification Of Speech Sounds

- Speech sounds are the basic units of human communication that convey meaning and emotion.
- Speech sounds are produced by the coordinated movement of various organs of speech, such as the lungs, larynx, velum, tongue, lips, etc.
- Speech sounds are classified into two main categories: vowels and consonants.
- Vowels are speech sounds that are produced with no obstruction or narrowing of the air stream in the vocal tract. Vowels are usually voiced, meaning that the vocal folds vibrate during their production. Vowels are characterized by their height, backness, roundness, and length.
- Consonants are speech sounds that are produced with some degree of constriction or closure of the air stream in the vocal tract. Consonants can be voiced or voiceless, depending on whether the vocal folds vibrate or not. Consonants are characterized by their place, manner, and voicing of articulation.
- Speech sounds can also be classified into phonemes and allophones. Phonemes are the smallest units of sound that can distinguish meaning in a language. Allophones are the different variants of a phoneme that occur in different contexts or environments. Allophones do not change the meaning of a word, but may affect its pronunciation or quality.



### Acoustic Phonetics

- Acoustic phonetics is the study of the acoustic characteristics of speech, including an analysis and description of speech in terms of its physical properties, such as frequency, intensity, and duration .
- Acoustic phonetics is an instrumental science that depends on ways to store, replicate, visualize, and analyze the speech signal. Acoustic phonetics is also a cumulative science in which older research continues to be influential.
- Acoustic phonetics investigates time domain features such as the mean squared amplitude of a waveform, its duration, its fundamental frequency, or frequency domain features such as the frequency spectrum, or even combined spectrotemporal features and the relationship of these properties to other branches of phonetics (e.g. articulatory or auditory phonetics), and to abstract linguistic concepts such as phonemes, phrases, or utterances.
- Acoustic phonetics can be used to identify the place and manner of articulation of speech sounds, the prosodic features of speech, the speaker's identity, the speaker's emotional state, the language or dialect spoken, and the speech errors or disorders.
- Acoustic phonetics can also be used to synthesize speech from text, to enhance speech signals, to recognize speech automatically, to convert speech to text, and to model speech production and perception.
- Acoustic phonetics relies on various tools and methods, such as sound spectrographs, oscilloscopes, waveform editors, pitch trackers, formant trackers, spectral analysis, acoustic models, acoustic measurements, acoustic features, acoustic cues, acoustic parameters, and acoustic databases .



### Acoustics of Speech Production

- Acoustics of speech production is the study of how speech sounds are generated and modified by the human vocal tract.
- Speech production involves a source of sound energy (e.g. the larynx) and a filter function (e.g. the vocal tract) that shapes the sound spectrum.
- The source of sound energy can be either voiced (produced by the vibration of the vocal folds) or unvoiced (produced by the turbulence of the airflow) depending on the type of speech sound.
- The filter function is determined by the shape and configuration of the vocal tract, which includes the oral cavity, the nasal cavity, and the pharynx.
- The vocal tract can be modeled as a series of connected tubes with varying cross-sectional areas and lengths, which affect the resonance frequencies and the formants of the speech signal .
- The acoustic characteristics of speech sounds depend on the interaction between the source and the filter, as well as the articulatory movements and gestures of the speech organs (e.g. the tongue, the lips, the jaw, etc.) .
- Acoustics of speech production can be analyzed using various methods and tools, such as spectrograms, waveforms, acoustic models, articulatory models, and acoustic phonetics .
- Acoustics of speech production is an important field of research for understanding the nature and function of human speech, as well as for developing applications such as speech recognition, speech synthesis, speech enhancement, and speech therapy .



### Review Of Digital Signal Processing Concepts

Digital signal processing (DSP) is the use of digital processing, such as by computers or more specialized digital signal processors, to perform a wide variety of signal processing operations. The digital signals processed in this manner are a sequence of numbers that represent samples of a continuous variable in a domain such as time, space, frequency, or image pixels.

Some of the basic concepts of DSP are:

- **Data digitizing** – Convert continuous signals to finite discrete digital signals by using analog-to-digital converters (ADCs). This allows the signals to be stored, transmitted, and manipulated by digital devices.
- **Sampling and quantization** – Sampling is the process of taking periodic snapshots of a continuous signal, while quantization is the process of assigning discrete values to the sampled signal. The sampling rate and the number of bits per sample determine the quality and resolution of the digital signal.
- **Signal representation** – A digital signal can be represented in different ways, such as in time domain, frequency domain, or z-domain. Each representation has its own advantages and disadvantages for analysis and processing. For example, the time domain representation shows the amplitude of the signal as a function of time, while the frequency domain representation shows the spectrum of the signal as a function of frequency.
- **Signal transformation** – A digital signal can be transformed from one domain to another by using mathematical operations such as Fourier transform, Laplace transform, or z-transform. These transformations allow the signal to be viewed from different perspectives and reveal different properties of the signal.
- **Signal filtering** – A digital signal can be filtered to remove unwanted noise, enhance certain features, or extract specific information from the signal. Filtering can be done by using linear or nonlinear operations, such as convolution, correlation, or thresholding. Filters can be classified into different types, such as low-pass, high-pass, band-pass, or notch filters, depending on their frequency response.
- **Signal modulation and demodulation** – A digital signal can be modulated or demodulated to change its frequency, amplitude, or phase, for the purpose of transmission, encryption, or compression. Modulation and demodulation can be done by using analog or digital techniques, such as amplitude modulation (AM), frequency modulation (FM), or phase modulation (PM).
- **Signal compression and decompression** – A digital signal can be compressed or decompressed to reduce its size, bandwidth, or complexity, for the purpose of storage, transmission, or processing. Compression and decompression can be done by using lossy or lossless techniques, such as Huffman coding, run-length encoding, or discrete cosine transform (DCT).
- **Signal detection and estimation** – A digital signal can be detected or estimated to infer the presence, absence, or value of a signal or a parameter of interest, such as speech, music, or temperature. Detection and estimation can be done by using statistical or probabilistic methods, such as hypothesis testing, maximum likelihood, or Bayesian inference.
- **Signal classification and recognition** – A digital signal can be classified or recognized to identify the type, category, or source of the signal or a feature of interest, such as speaker, language, or emotion. Classification and recognition can be done by using machine learning or artificial intelligence techniques, such as neural networks, support vector machines, or hidden Markov models.



### Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique to analyze the frequency and phase content of a signal as it changes over time .
- The STFT is computed by dividing a longer signal into shorter segments of equal length, applying a window function to each segment, and then taking the Fourier transform of each windowed segment  .
- The STFT produces a two-dimensional representation of the signal, where the horizontal axis is time, the vertical axis is frequency, and the amplitude or phase of the signal is encoded in the color or intensity of the plot .
- The STFT is useful for situations where the frequency components of a signal vary over time, such as speech, music, or environmental sounds .
- The STFT has some limitations, such as the trade-off between time and frequency resolution, the leakage of energy across frequency bins, and the lack of phase information in the magnitude spectrogram .
- The STFT can be modified or extended by using different window functions, different segment lengths, different overlap sizes, or different transformations, such as the discrete cosine transform or the wavelet transform .



### Filter Bank and LPC Methods for Speech Processing

- Speech processing is the study of how humans produce, perceive, and understand speech, and how to design machines that can perform these tasks.
- Speech processing involves various stages, such as speech analysis, speech synthesis, speech recognition, speech enhancement, speech coding, and speech translation.
- Speech analysis is the process of extracting features or parameters from the speech signal that represent its characteristics, such as pitch, energy, spectrum, and formants.
- Speech synthesis is the process of generating speech from text or other symbolic representations, such as phonetic symbols, prosodic features, or articulatory gestures.
- Speech recognition is the process of converting speech into text or other symbolic representations, such as commands, keywords, or semantic meanings.
- Speech enhancement is the process of improving the quality of speech by reducing noise, reverberation, or distortion.
- Speech coding is the process of compressing speech for efficient transmission or storage, while preserving its intelligibility and naturalness.
- Speech translation is the process of converting speech from one language to another, while preserving its meaning and style.

- Filter bank and LPC methods are two common techniques for speech analysis and speech coding, which are based on different models of speech production.
- Filter bank methods assume that speech is produced by a source-filter model, where the source is either a periodic pulse train (for voiced sounds) or a random noise (for unvoiced sounds), and the filter is a time-varying vocal tract that shapes the spectrum of the source.
- Filter bank methods use a bank of band-pass filters to divide the speech signal into frequency bands, and compute the energy or amplitude of each band. The filter bank can be designed to mimic the frequency response of the human auditory system, such as the mel-scale or the bark-scale.
- Filter bank methods can also apply a discrete cosine transform (DCT) or a discrete Fourier transform (DFT) to the filter bank outputs, to obtain a compact and decorrelated representation of the speech spectrum, such as the mel-frequency cepstral coefficients (MFCC) or the perceptual linear prediction (PLP) coefficients.
- Filter bank methods are widely used for speech recognition, speech enhancement, and speech synthesis, as they capture the perceptual and acoustic features of speech.
- LPC methods assume that speech is produced by an all-pole model, where the speech signal is approximated as a linear combination of past samples, and the coefficients of the linear combination are called the linear prediction coefficients (LPC).
- LPC methods use an autocorrelation method or a covariance method to estimate the LPC from the speech signal, and use a Levinson-Durbin recursion or a lattice filter to compute the reflection coefficients or the prediction error filter from the LPC.
- LPC methods can also apply a cepstral analysis or a line spectral frequency (LSF) analysis to the LPC, to obtain a compact and robust representation of the speech spectrum, such as the LPC cepstral coefficients or the LSF coefficients.
- LPC methods are widely used for speech coding, speech synthesis, and speech enhancement, as they capture the spectral envelope and the pitch of speech.



```
## Unit 5 - SPEECH-ANALYSIS

- Speech-analysis is the process of examining the features and characteristics of spoken language, such as phonetics, phonology, prosody, syntax, semantics, pragmatics, and discourse.
- Speech-analysis can be applied for various purposes, such as speech recognition, speech synthesis, speech enhancement, speech compression, speech translation, speech therapy, speech forensics, speech education, and speech research.
- Speech-analysis can be performed at different levels of abstraction, such as acoustic, articulatory, perceptual, linguistic, and cognitive.
- Speech-analysis can be done manually or automatically, using various tools and methods, such as spectrograms, waveforms, pitch contours, formant tracks, articulographs, electroglottographs, electroencephalographs, eye-trackers, microphones, speakers, headphones, computers, software, algorithms, models, and theories.
- Speech-analysis can be influenced by various factors, such as speaker identity, speaker variability, speaker emotion, speaker intention, speaker style, speaker accent, speaker dialect, speaker gender, speaker age, speaker health, speaker background, speaker context, speaker audience, speaker channel, speaker noise, speaker feedback, and speaker interaction.
- Speech-analysis can be evaluated by various criteria, such as accuracy, reliability, validity, efficiency, robustness, naturalness, intelligibility, comprehensibility, acceptability, usability, and usefulness.
- Speech-analysis can be improved by various techniques, such as data collection, data annotation, data preprocessing, data augmentation, data analysis, data visualization, data interpretation, data synthesis, data evaluation, data feedback, data correction, and data optimization.
```



### Features for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, intention, and content.
- Speech analysis is a subfield of natural language processing (NLP), which is the branch of computer science and artificial intelligence that deals with understanding and generating natural language.
- Speech analysis involves various techniques and applications, such as speech recognition, speech synthesis, speech segmentation, speech enhancement, speech coding, speech translation, speech summarization, speech emotion recognition, speaker identification, and speech diarization.
- Speech analysis can be performed at different levels of linguistic representation, such as phonetic, phonological, morphological, syntactic, semantic, pragmatic, and discourse.
- Speech analysis can also be performed at different levels of granularity, such as word, phrase, sentence, paragraph, and document.
- Speech analysis can benefit from various sources of information, such as acoustic, prosodic, lexical, syntactic, semantic, and contextual features.
- Speech analysis can be applied to various domains and tasks, such as human-computer interaction, voice assistants, speech therapy, education, entertainment, security, forensics, health care, and social media.

: https://www.techtarget.com/searchenterpriseai/definition/speech-analysis
: https://www.ibm.com/topics/natural-language-processing
: https://indiaai.gov.in/article/natural-language-processing-nlp-simplified-a-step-by-step-guide
: https://www.science.org/doi/10.1126/science.aaa8685
: https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1
: https://www.frontiersin.org/articles/10.3389/fnagi.2018.00369/full



### Feature Extraction And Pattern Comparison Techniques for Speech Analysis

Feature extraction is the process of transforming the speech signal into a set of features that can be used for speech recognition, speaker identification, or other speech-related tasks. Feature extraction aims to reduce the dimensionality and complexity of the speech signal, while preserving the relevant information for the task at hand.

Pattern comparison is the process of matching the extracted features with a set of reference patterns that represent different speech units, such as words, phonemes, or speakers. Pattern comparison aims to find the best match between the features and the patterns, and to assign a score or a label to the speech signal.

Some of the common feature extraction techniques for speech analysis are:

- **Linear Predictive Coding (LPC)**: LPC is a technique that models the speech signal as a linear combination of past samples, and estimates the coefficients of the linear predictor using an autocorrelation method. LPC can capture the spectral envelope of the speech signal, which reflects the vocal tract shape and the formant frequencies. LPC features are usually represented by the LPC coefficients, the reflection coefficients, or the line spectral frequencies.

- **Mel-Frequency Cepstral Coefficients (MFCC)**: MFCC is a technique that applies a mel-scale filter bank to the speech signal, and computes the discrete cosine transform (DCT) of the log-energy of each filter output. MFCC can capture the spectral shape and the energy distribution of the speech signal, which are influenced by the vocal tract and the excitation source. MFCC features are usually represented by the cepstral coefficients, which are the DCT coefficients .

- **Perceptual Linear Prediction (PLP)**: PLP is a technique that applies a perceptual weighting to the speech signal, and computes the LPC coefficients of the weighted signal. PLP can capture the perceptual aspects of the speech signal, such as the critical bands, the equal-loudness curve, and the intensity-loudness power law. PLP features are usually represented by the PLP coefficients, which are the LPC coefficients of the weighted signal.

Some of the common pattern comparison techniques for speech analysis are:

- **Dynamic Time Warping (DTW)**: DTW is a technique that aligns two sequences of features by finding the optimal warping path that minimizes the distance between them. DTW can handle the temporal variations and distortions of the speech signal, such as different speaking rates, pauses, and hesitations. DTW can be used for isolated word recognition, speaker verification, or speech segmentation .

- **Hidden Markov Models (HMM)**: HMM is a technique that models the speech signal as a stochastic process that transitions between a finite number of hidden states, each of which emits a feature vector according to a probability distribution. HMM can handle the sequential and probabilistic nature of the speech signal, and can capture the temporal and spectral dynamics of the speech units. HMM can be used for continuous speech recognition, speaker identification, or speech synthesis.

- **Support Vector Machines (SVM)**: SVM is a technique that finds the optimal hyperplane that separates two classes of features with the maximum margin. SVM can handle the high-dimensional and nonlinear features of the speech signal, and can achieve high generalization performance with a small number of training samples. SVM can be used for speaker recognition, speech emotion recognition, or speech enhancement.



### Speech Distortion Measures

- Speech distortion measures are methods to quantify the amount and type of distortion that occurs in speech signals due to various factors, such as hearing loss, noise, or processing algorithms.
- Speech distortion measures can be classified into two categories: subjective and objective.
  - Subjective measures are based on human perception and evaluation of speech quality, intelligibility, or naturalness. They require listening tests with human subjects who rate the speech samples on a scale or identify the words or sentences they hear. Subjective measures are reliable and valid, but they are time-consuming, costly, and prone to variability among listeners and test conditions.
  - Objective measures are based on mathematical or statistical calculations that compare the original and distorted speech signals in terms of their spectral, temporal, or perceptual features. They do not require human listeners, but they rely on assumptions and models that may not capture all aspects of speech perception and cognition. Objective measures are fast, cheap, and consistent, but they may not correlate well with subjective measures or reflect the actual impact of distortion on speech communication.
- Some examples of speech distortion measures are:
  - Signal-to-noise ratio (SNR): the ratio of the average power of the speech signal to the average power of the noise signal, expressed in decibels (dB). A higher SNR indicates a lower noise level and a better speech quality. SNR is a simple and widely used measure, but it does not account for the spectral or perceptual characteristics of speech and noise, or the effects of nonlinear distortion or hearing loss.
  - Segmental SNR (SSNR): the average of the SNR values calculated for short segments (e.g., 20 ms) of the speech signal. SSNR is more sensitive to the temporal variations of speech and noise than SNR, but it still does not consider the spectral or perceptual features of speech and noise, or the effects of nonlinear distortion or hearing loss.
  - Perceptual evaluation of speech quality (PESQ): an objective measure that compares the original and distorted speech signals in terms of their perceptual similarity, based on a psychoacoustic model of human hearing. PESQ produces a score between 1 and 5, where 1 means very poor quality and 5 means excellent quality. PESQ is designed to mimic subjective ratings of speech quality, and it accounts for the spectral and temporal characteristics of speech and noise, as well as the effects of nonlinear distortion and hearing loss. However, PESQ is complex and computationally intensive, and it may not reflect the intelligibility or naturalness of speech.
  - Speech intelligibility index (SII): an objective measure that estimates the proportion of speech information that is audible and intelligible to a listener with normal hearing, based on a model of speech audibility and intelligibility. SII produces a score between 0 and 1, where 0 means no intelligibility and 1 means perfect intelligibility. SII accounts for the spectral and temporal characteristics of speech and noise, as well as the effects of hearing loss and masking. However, SII does not consider the effects of nonlinear distortion, cognitive factors, or linguistic context on speech intelligibility.
  - Speech transmission index (STI): an objective measure that evaluates the transmission quality of speech signals over a communication channel, based on a model of speech modulation and detection. STI produces a score between 0 and 1, where 0 means very bad transmission and 1 means excellent transmission. STI accounts for the spectral and temporal characteristics of speech and noise, as well as the effects of nonlinear distortion, reverberation, and echo. However, STI does not consider the effects of hearing loss, cognitive factors, or linguistic context on speech intelligibility.



### Mathematical And Perceptual Speech Analysis

- Mathematical speech analysis is the application of mathematical models and methods to study the structure, function, and processing of human language and speech.
- Perceptual speech analysis is the study of how humans perceive, interpret, and produce speech sounds and meanings, using psychological and physiological principles and measurements.
- Some of the topics and concepts that are relevant for mathematical and perceptual speech analysis are:

  - Phonology: the study of the sound patterns and systems of human languages, and how they are represented and manipulated by speakers and listeners. Phonological analysis involves the use of mathematical tools such as finite state automata, regular expressions, and algebraic structures to model and describe phonological phenomena. 
  - Morphology: the study of the internal structure and formation of words and word-like units in human languages, and how they are related to syntax, semantics, and phonology. Morphological analysis involves the use of mathematical tools such as rewrite rules, grammars, and automata to model and describe morphological phenomena. 
  - Syntax: the study of the rules and principles that govern the formation and structure of sentences and phrases in human languages, and how they are related to semantics, pragmatics, and discourse. Syntactic analysis involves the use of mathematical tools such as formal languages, grammars, and parsers to model and describe syntactic phenomena. 
  - Semantics: the study of the meaning and interpretation of words, sentences, and texts in human languages, and how they are related to syntax, pragmatics, and logic. Semantic analysis involves the use of mathematical tools such as logic, set theory, and algebra to model and describe semantic phenomena. 
  - Pragmatics: the study of the use and context of language and speech in human communication, and how they are related to semantics, syntax, and discourse. Pragmatic analysis involves the use of mathematical tools such as game theory, decision theory, and probability theory to model and describe pragmatic phenomena. 
  - Discourse: the study of the structure and coherence of texts and conversations in human languages, and how they are related to pragmatics, semantics, and syntax. Discourse analysis involves the use of mathematical tools such as graphs, networks, and matrices to model and describe discourse phenomena. 
  - Speech recognition: the process of converting speech signals into text or other symbolic representations, using mathematical and statistical methods such as feature extraction, acoustic modeling, language modeling, and decoding. Speech recognition involves the use of perceptual principles such as the critical-band spectral resolution, the equal-loudness curve, and the intensity-loudness power law to derive an estimate of the auditory spectrum.  
  - Speech synthesis: the process of generating speech signals from text or other symbolic representations, using mathematical and statistical methods such as text analysis, prosody modeling, acoustic modeling, and waveform generation. Speech synthesis involves the use of perceptual principles such as the articulatory and auditory phonetics, the speech production and perception systems, and the speech intelligibility and naturalness criteria to produce realistic and expressive speech. 
  - Speech enhancement: the process of improving the quality and intelligibility of speech signals in noisy or degraded environments, using mathematical and statistical methods such as filtering, noise reduction, echo cancellation, and dereverberation. Speech enhancement involves the use of perceptual principles such as the masking and unmasking effects, the auditory scene analysis, and the signal-to-noise ratio to optimize the speech signal. 
  - Speech coding: the process of compressing and decompressing speech signals for efficient transmission and storage, using mathematical and statistical methods such as quantization, entropy coding, and transform coding. Speech coding involves the use of perceptual principles such as the perceptual weighting, the perceptual distortion, and the perceptual quality to achieve high compression ratios and low bit rates. 
  - Speech emotion recognition: the process of identifying and classifying the emotional state and attitude of speakers from their speech signals, using mathematical and statistical methods such as feature extraction, machine learning, and pattern recognition. Speech emotion recognition involves the use of perceptual principles such as the prosodic, spectral, and temporal cues, the vocal affect display, and the emotion recognition accuracy to infer the speaker's emotion. 
  - Speech education: the process of teaching and learning the skills and knowledge related to speech and language, using mathematical and perceptual methods such



# Log–Spectral Distance

- The log-spectral distance (LSD), also referred to as log-spectral distortion or root mean square log-spectral distance, is a distance measure (expressed in dB) between two spectra .
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as p-norm:

```
D_LS = (1/2π) ∫[10 log10(P(ω)/P^(ω))]^p dω
```

- The log-spectral distance is symmetric, unlike the Itakura–Saito distance .
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum .
- The log-spectral distance can be used to measure the quality of speech synthesis or speech recognition systems, by comparing the spectra of the original and the synthesized or recognized speech signals .
- The log-spectral distance can also be used to measure the similarity of two speech signals, by computing the average log-spectral distance over a set of frames .
- The log-spectral distance is sensitive to the phase difference between the spectra, and may not reflect the perceptual difference between the speech signals .



# Cepstral Distances for Speech Analysis

- Cepstral distance is a measure of the similarity or dissimilarity between two speech frames in terms of their spectral envelopes .
- Cepstral distance is computed as the Euclidean distance between the cepstral coefficients of two frames .
- Cepstral coefficients are obtained by applying the inverse Fourier transform to the logarithm of the spectrum of a speech frame .
- Cepstral distance can be used for various speech processing applications, such as endpoint detection, emotion recognition, channel selection, speaker identification, and voice quality assessment  .
- Cepstral distance can capture the spectral variations caused by different factors, such as vocal tract shape, pitch, intensity, and noise  .
- Cepstral distance can be normalized or weighted to account for the different contributions of different cepstral coefficients .
- Cepstral distance can be combined with other features, such as speech energy, to improve the performance of speech analysis tasks.



### Weighted Cepstral Distances And Filtering for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log spectrum of the signal.
- Cepstral distance can be used for speech recognition, speaker recognition, speech enhancement, and speech synthesis applications.
- A simple cepstral distance measure is the Euclidean distance between the cepstral coefficients of two speech frames, but this may not be optimal for capturing the perceptual differences between speech signals.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to the cepstral coefficients according to their importance or variability.
- One way to obtain the weights is to use the inverse of the variance of the cepstral coefficients, which reflects the degree of variation of each coefficient across different speech frames or speakers   .
- Another way to obtain the weights is to use the logarithm of the index of the cepstral coefficient, which reflects the frequency resolution of the cepstral coefficients .
- A weighted cepstral distance measure can improve the performance of speech recognition or speaker recognition systems by reducing the mismatch between the training and testing conditions or between different speakers.
- Filtering is a process of modifying the speech signal by applying a filter function to its spectrum or cepstrum, which can enhance or suppress certain frequency components or features of the signal.
- Filtering can be used for speech analysis to reduce the noise, improve the signal-to-noise ratio, or extract the vocal tract or excitation information from the speech signal.
- Filtering can be performed in the spectral domain or in the cepstral domain, depending on the type of filter function and the desired effect.
- Some examples of filtering techniques are:

  - Spectral subtraction: a method of noise reduction that subtracts an estimate of the noise spectrum from the noisy speech spectrum, resulting in a cleaner speech spectrum.
  - Cepstral liftering: a method of feature extraction that applies a window function to the cepstrum, resulting in a modified cepstrum that emphasizes or de-emphasizes certain cepstral coefficients.
  - Homomorphic filtering: a method of speech decomposition that applies a high-pass filter to the cepstrum, resulting in a separation of the vocal tract and excitation components of the speech signal.



# Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the similarity or dissimilarity between two short-time spectra of speech signals.
- They are used to compare the spectral features of speech signals for speech recognition, enhancement, coding, and synthesis applications.
- There are different types of likelihood distortions, such as:
  - Log likelihood ratio (LLR): the negative logarithm of the ratio of the probability densities of the two spectra.
  - Likelihood ratio (LR): the ratio of the probability densities of the two spectra.
  - Itakura-Saito (IS): the Kullback-Leibler divergence between the two spectra, which is equivalent to the LLR minus the log of the ratio of the spectral variances.
  - Cepstral (CEP): the Euclidean distance between the cepstral coefficients of the two spectra.
  - Weighted likelihood ratio (WLR): the LLR weighted by a perceptual weighting function that emphasizes the spectral regions that are more important for speech perception.
  - Weighted slope metric (WSM): the Euclidean distance between the slopes of the two spectra weighted by a perceptual weighting function.
- The choice of the likelihood distortion measure depends on the application and the characteristics of the speech signals.
- Some factors that affect the performance of the likelihood distortion measures are:
  - The spectral resolution and the window size of the short-time analysis.
  - The presence of noise and channel distortions in the speech signals.
  - The use of frequency warping and spectral normalization techniques to reduce the effects of vocal tract length and speaker variability.
  - The use of suprasegmental information, such as energy, gain, and loudness, to complement the spectral information.
- According to a comparative study of several distortion measures for speech recognition , some of the findings are:
  - The LLR and WSM distortion measures gave the highest recognition accuracy, while the IS distortion measure gave the lowest score.
  - The addition of suprasegmental energy information helped the recognition performance, while the use of gain and absolute loudness degraded the performance.
  - Bark-scale frequency warping did not perform as well as its unwarped counterpart for the highly bandlimited telephone data base tested.
  - The WLR distortion measure did not perform as well as its unweighted counterpart.



### Spectral Distortion Using A Warped Frequency Scale

- Spectral distortion is the difference between the original and the estimated spectra of a speech signal, usually measured in decibels (dB).
- A warped frequency scale is a transformation of the linear frequency scale that emphasizes certain frequency regions over others, based on some perceptual or physiological criteria.
- Warping the frequency scale can improve the accuracy and efficiency of speech analysis methods, such as linear prediction (LP) or cepstral analysis, by reducing the spectral distortion at low model orders or dimensions.
- Some examples of warped frequency scales are:
  - The Bark scale, which is based on the critical band-rate of the human auditory system, derived from auditory masking experiments. It is related to the loudness sensation of sounds.
  - The Mel scale, which is based on the just noticeable differences in frequency, derived from pitch perception experiments. It is related to the pitch sensation of sounds.
  - The ERB (equivalent rectangular bandwidth) scale, which is based on the bandwidth of the auditory filters, derived from psychoacoustic experiments. It is related to the frequency resolution of sounds.
- To apply a warped frequency scale to speech analysis, one can use a frequency warping function that maps the linear frequency to the warped frequency, such as the all-pole warping function or the bilinear transformation.
- The frequency warping function can be applied to the speech signal before or after the analysis, or to the analysis filter itself, depending on the method and the desired effect.
- The advantages of using a warped frequency scale for speech analysis are:
  - It can better match the spectral characteristics of speech sounds, especially vowels, which have formants that are more evenly spaced on a warped frequency scale than on a linear frequency scale.
  - It can better approximate the perceptual relevance of spectral features, by emphasizing the frequency regions that are more important for speech intelligibility and quality, such as the low and mid frequencies.
  - It can reduce the computational complexity and memory requirements of speech analysis, by allowing lower model orders or dimensions to achieve the same or better spectral accuracy as higher model orders or dimensions on a linear frequency scale.



### LPC for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- LPC stands for Linear Predictive Coding, which is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model .
- LPC analyzes the speech signal by estimating the formants, which are the resonant frequencies of the vocal tract, and removing their effects from the speech signal, resulting in a residual signal that contains the pitch and the glottal excitation.
- The process of removing the formants is called inverse filtering, and the residual signal after the subtraction of the filtered modeled signal is called the residue.
- The linear predictive model assumes that the current sample of the speech signal can be approximated as a linear combination of the previous samples, plus some error term .
- The coefficients of the linear combination are called the linear prediction coefficients, and they can be obtained by minimizing the mean squared error between the original signal and the predicted signal .
- The linear prediction coefficients can also be converted to the reflection coefficients, which are the ratios of the backward and forward traveling waves in a lossless transmission line model of the vocal tract .
- The reflection coefficients have some advantages over the linear prediction coefficients, such as being more stable, having a smaller dynamic range, and being more suitable for quantization .
- LPC can be used for speech coding and speech synthesis, as well as for speech enhancement, speech recognition, and speaker identification .
- In speech coding, LPC can reduce the bit rate of the speech signal by transmitting only the linear prediction coefficients and the residual signal, which can be further compressed by using techniques such as adaptive differential pulse code modulation (ADPCM) .
- In speech synthesis, LPC can generate synthetic speech by using the linear prediction coefficients and the residual signal as inputs to a synthesis filter, which reconstructs the speech signal by adding the formants back to the residual signal  .
- LPC can also be used for speech enhancement, by using the linear prediction coefficients to estimate the noise spectrum and subtracting it from the noisy speech signal, resulting in a cleaner speech signal .
- LPC can also be used for speech recognition, by using the linear prediction coefficients as features to represent the speech signal and compare it with the reference templates or models of different words or phonemes .
- LPC can also be used for speaker identification, by using the linear prediction coefficients as features to represent the speaker's vocal characteristics and compare them with the reference templates or models of different speakers .



### PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction, which is the computation of a set of parameters that represent the characteristics of the speech signal.
- Feature extraction methods aim to reduce the dimensionality of the speech signal and capture the relevant information for the task at hand.
- Some of the most widely used feature extraction methods for speech analysis are Perceptual Linear Prediction (PLP) and Mel Frequency Cepstral Coefficients (MFCC).

#### Perceptual Linear Prediction (PLP)

- PLP is a feature extraction method that mimics the human auditory system and applies psychoacoustic principles to speech analysis.
- PLP consists of the following steps :
  - Pre-emphasis: a high-pass filtering operation that enhances the high-frequency components of the speech signal and reduces the effect of noise.
  - Framing and windowing: dividing the speech signal into short segments (frames) of 20-30 ms and applying a window function (such as Hamming) to each frame to smooth the edges and reduce spectral leakage.
  - Critical band analysis: applying a filter bank that divides the frequency spectrum into bands that correspond to the critical bands of the human ear. The critical bands are non-uniform and have higher resolution at lower frequencies and lower resolution at higher frequencies.
  - Intensity loudness transformation: applying a non-linear transformation that converts the spectral energy in each band into a loudness measure that reflects the human perception of loudness.
  - Equal loudness pre-emphasis: applying a weighting function that compensates for the variation of loudness sensitivity across different frequencies.
  - Autoregressive modeling: applying a linear prediction analysis that estimates the spectral envelope of the speech signal using a low-order autoregressive model. The model coefficients are called the PLP coefficients and are the final features extracted by the PLP method.

#### Mel Frequency Cepstral Coefficients (MFCC)

- MFCC is a feature extraction method that also mimics the human auditory system and applies psychoacoustic principles to speech analysis.
- MFCC consists of the following steps  :
  - Pre-emphasis: same as PLP.
  - Framing and windowing: same as PLP.
  - Mel filter bank analysis: applying a filter bank that divides the frequency spectrum into bands that correspond to the mel scale, which is a perceptual scale of pitches that is linear at low frequencies and logarithmic at high frequencies. The mel scale approximates the frequency resolution of the human ear.
  - Logarithmic compression: applying a logarithmic function that converts the spectral energy in each band into a measure of spectral magnitude that reflects the human perception of sound intensity.
  - Discrete cosine transform (DCT): applying a linear transformation that decorrelates the spectral magnitude coefficients and reduces the dimensionality of the feature vector. The resulting coefficients are called the MFCC coefficients and are the final features extracted by the MFCC method.

#### Comparison of PLP and MFCC

- Both PLP and MFCC are popular feature extraction methods for speech analysis that are based on the human auditory system and psychoacoustic principles.
- Both methods use pre-emphasis, framing and windowing, and a non-uniform filter bank analysis to capture the spectral characteristics of the speech signal.
- The main differences between the methods are:
  - PLP uses a critical band filter bank, while MFCC uses a mel filter bank. The critical band filter bank is more accurate in modeling the human auditory system, while the mel filter bank is more computationally efficient and robust to noise.
  - PLP uses an intensity loudness transformation, an equal loudness pre-emphasis, and an autoregressive modeling to estimate the spectral envelope, while MFCC uses a logarithmic compression and a DCT to decorrelate and reduce the feature vector. The PLP method is more sensitive to the fine details of the spectral envelope, while the MFCC method is more compact and invariant to speaker and channel variations.
- The choice of the feature extraction method depends on the application and the data. Some applications may benefit from the higher resolution and accuracy of PLP, while others may prefer the lower dimensionality and robustness of MFCC. Some data may have more noise or variability that may affect the performance of the feature extraction method. Therefore, it is advisable to experiment with different methods and parameters to find the optimal solution for the task at hand



### Time Alignment And Normalization for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Time alignment is the process of finding the best correspondence between the frames of two speech signals, usually from different speakers or different utterances.
- Time alignment is useful for many applications of speech analysis, such as speech recognition, text-to-speech conversion, voice conversion, speaker verification, and speech synthesis.
- Time alignment can be done by using methods such as dynamic time warping (DTW), hidden Markov models (HMMs), or neural networks.
- Time alignment can be improved by using some modifications to DTW, such as adding constraints, using multiple features, or applying post-processing techniques.
- Normalization is the process of reducing the variability of speech signals due to factors such as speaker characteristics, channel conditions, or background noise.
- Normalization is important for enhancing the performance and robustness of speech analysis systems, especially when dealing with heterogeneous or noisy data.
- Normalization can be done by using methods such as automatic gain control, automatic spectrum normalization, cepstral mean subtraction, vocal tract length normalization, or speaker adaptation.
- Normalization can be applied in different domains, such as amplitude, frequency, or time, depending on the type and source of variability.



# Dynamic Time Warping for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Dynamic Time Warping (DTW) is an algorithm for measuring the similarity between two temporal sequences, such as speech signals, that may vary in speed or length  .
- DTW is based on the idea of finding the optimal alignment between two sequences by minimizing the distance between them .
- DTW can handle non-linear distortions and local variations in the sequences, such as different pronunciations, accents, or speaking rates  .
- DTW works by constructing a matrix that represents the pairwise distances between the elements of the two sequences, and then finding the shortest path through the matrix that satisfies some constraints .
- The constraints are: 
  - The path must start at the top-left corner and end at the bottom-right corner of the matrix .
  - The path must move monotonically, i.e., it can only go right, down, or diagonally .
  - The path must be continuous, i.e., it cannot skip any cells in the matrix .
- The length of the path is the DTW distance between the two sequences, and the path itself is the optimal alignment .
- DTW can be used for various applications in speech analysis, such as isolated word recognition, speaker identification, speech segmentation, speech synthesis, and speech enhancement  .
- DTW can also be extended to handle multi-dimensional sequences, such as spectrograms or feature vectors, by using different distance measures or weighting schemes .
- DTW has some limitations, such as high computational complexity, sensitivity to noise, and lack of a clear theoretical foundation .
- DTW can be improved by using various techniques, such as pruning, indexing, warping constraints, normalization, or machine learning .



### Multiple Time – Alignment Paths for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications of speech analysis, such as speech recognition, speech synthesis, voice conversion, speech enhancement, and speech to lips synchronization  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or temporal variations .
- One common technique for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the cumulative distance between the frames.
- DTW can be implemented using dynamic programming, which computes a cost matrix that stores the distances between all pairs of frames from the two time series, and then traces back the optimal path from the matrix.
- However, DTW has some limitations, such as being sensitive to noise, requiring high computational cost, and producing a single alignment path that may not capture the multiple possible correspondences between the time series .
- To overcome these limitations, some alternative techniques have been proposed, such as:

  - Multiview temporal alignment by dependence maximisation in the latent space (TRANSIENCE), which projects the feature vectors from the time series into a common latent subspace where they are maximally similar, and then finds the optimal alignment path using a graph search algorithm.
  - Adaptive, ordered, graph search technique for dynamic time warping (AOGS-DTW), which uses a heuristic search algorithm that adapts the search order and the search space according to the characteristics of the time series, and allows for multiple alignment paths to be generated.
  - Dynamic temporal alignment of speech to lips (DTA-SL), which uses a deep neural network to learn a mapping between speech and lip features, and then uses a modified DTW algorithm that incorporates a smoothness constraint and a lip closure constraint to find the optimal alignment path.

- These techniques aim to improve the accuracy, efficiency, and flexibility of time alignment for speech analysis, and can be applied to various domains and tasks that involve multimodal or multivariate time series data  .



### SPEECH MODELING

Speech modeling is the process of creating mathematical representations of speech signals and the underlying linguistic structures that produce them. Speech modeling is an essential component of natural language processing (NLP), which is a branch of artificial intelligence that aims to enable computers to understand and generate natural language.

Speech modeling can be divided into two main types: acoustic modeling and linguistic modeling.

- Acoustic modeling is the task of mapping speech signals to phonetic units, such as phones, syllables, or words. Acoustic modeling involves extracting features from the speech signals, such as pitch, energy, spectral shape, etc., and using statistical or neural models to estimate the probabilities of different phonetic units given the features. Acoustic modeling is used for speech recognition, speech synthesis, speaker identification, and other applications that require analyzing the sound of speech.

- Linguistic modeling is the task of representing the linguistic structures and rules that govern natural language, such as syntax, semantics, pragmatics, etc. Linguistic modeling involves using grammars, lexicons, ontologies, and other knowledge sources to capture the meaning and structure of natural language. Linguistic modeling is used for natural language understanding, natural language generation, machine translation, dialogue systems, and other applications that require reasoning and generating natural language.

Speech modeling can also be seen as a hierarchical process, where higher-level linguistic models depend on lower-level acoustic models. For example, to recognize a word, one needs to first recognize the phonetic units that compose it, and then use a lexicon and a language model to determine the most likely word given the phonetic units. Similarly, to generate a word, one needs to first select the word based on the context and the intended meaning, and then use a pronunciation model and a speech synthesis model to produce the corresponding speech signal.

Speech modeling is a challenging and active research area, as natural language is complex, diverse, and dynamic. Speech modeling requires integrating knowledge from various disciplines, such as linguistics, computer science, mathematics, psychology, etc. Speech modeling also requires dealing with various sources of variability and uncertainty, such as noise, accents, dialects, emotions, etc. Speech modeling has many potential applications and benefits for human-computer interaction, education, entertainment, health, security, and more.



# Hidden Markov Models for Speech Analysis

- Hidden Markov Models (HMMs) are statistical models that can capture the temporal and sequential dependencies of speech signals by modeling the hidden states of the speech production process and the observable acoustic features of the speech signal.
- HMMs are composed of a set of states, a set of transition probabilities between states, and a set of emission probabilities for each state.
- HMMs can be trained using a large corpus of speech data and a set of phonetic labels, using algorithms such as the Baum-Welch algorithm or the Viterbi algorithm .
- HMMs can be used for speech recognition by finding the most likely sequence of states and phonetic labels that match a given speech signal, using algorithms such as the Viterbi algorithm or the forward-backward algorithm .
- HMMs can also be used for speech synthesis by generating speech signals from a given sequence of phonetic labels, using algorithms such as the maximum likelihood parameter generation algorithm or the speech parameter generation algorithm.
- HMMs have been successfully applied to various speech analysis tasks, such as speech emotion recognition, speech segmentation, speaker identification, and speech enhancement.
- HMMs have some limitations, such as the assumption of independence between observations, the difficulty of modeling long-term dependencies, and the sensitivity to noise and variability .
- HMMs can be improved or extended by using techniques such as Gaussian mixture models, context-dependent models, deep neural networks, and dynamic Bayesian networks .



### Markov Processes for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- A Markov process is a stochastic process that has the Markov property, which means that the future state of the system depends only on the current state and not on the past history .
- A Markov process can be represented by a state diagram, where each node is a possible state and each edge is a transition probability between states.
- A Markov process can be discrete or continuous, depending on whether the state space and the time parameter are discrete or continuous.
- A Markov process can be used to model various phenomena, such as the time pattern of speech, where the presence or absence of speech can be sampled at a certain rate and described as a first-order Markov process.
- A Markov process can also be used in natural language processing (NLP) and machine learning, for example, to generate sentences, to tag parts of speech, or to recognize named entities .
- A Markov process can be extended to a Markov decision process, where the state transitions depend on the current state and an action vector that is applied to the system. This can be used to compute a policy of actions that will maximize some utility with respect to expected rewards.



### HMMs for Speech Analysis

- Hidden Markov Models (HMMs) are statistical models that can represent the temporal and spectral variations of speech signals by using a finite set of states and transition probabilities between them .
- HMMs can be used for speech recognition, speech synthesis, speech segmentation, speech enhancement, and speaker recognition  .
- HMMs can capture the context-dependent information of speech units, such as phonemes, syllables, or words, by using different HMMs for each unit or by using decision trees to cluster similar units .
- HMMs can also model the prosodic features of speech, such as pitch, duration, and energy, by using multi-stream or multi-dimensional HMMs .
- HMMs can be trained from speech data using maximum likelihood estimation or maximum a posteriori estimation, and the parameters can be adapted or interpolated to match different speakers, styles, or emotions .
- HMMs can generate speech waveforms from the trained models by using either a vocoder-based or a waveform-based approach .
- HMMs have some limitations and challenges, such as the independence assumption, the mismatch between training and testing conditions, the lack of naturalness and expressiveness, and the difficulty of incorporating high-level linguistic knowledge  .



### Evaluation for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis can be divided into two main tasks: speech recognition and speaker recognition.
- Speech recognition is the task of converting speech signals into text or commands, such as transcribing a lecture or controlling a device with voice commands.
- Speaker recognition is the task of identifying or verifying the speaker's identity from speech signals, such as authenticating a user or detecting a fraudster.
- Speech analysis involves various techniques and challenges, such as:
  - Acoustic modeling: the process of representing the speech signal as a sequence of acoustic features, such as spectral, temporal, or prosodic features.
  - Language modeling: the process of estimating the probability of a sequence of words or symbols, such as n-grams, neural networks, or grammars.
  - Decoding: the process of finding the best match between the acoustic features and the language model, such as using dynamic programming, beam search, or hidden Markov models.
  - Evaluation: the process of measuring the performance of a speech analysis system, such as using accuracy, error rate, precision, recall, or F1-score.
  - Adaptation: the process of adjusting the speech analysis system to different speakers, environments, domains, or languages, such as using speaker normalization, noise reduction, domain adaptation, or multilingual models.
  - Enhancement: the process of improving the quality or intelligibility of speech signals, such as using speech synthesis, speech separation, speech enhancement, or speech denoising.



### Optimal State Sequence for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Speech analysis is the process of extracting meaningful information from speech signals, such as words, emotions, speaker identity, etc.
- Speech analysis can be performed using various techniques, such as signal processing, machine learning, natural language processing, etc.
- One of the common techniques for speech analysis is to use hidden Markov models (HMMs), which are probabilistic models that can capture the sequential and temporal nature of speech signals.
- HMMs consist of a set of states, each associated with a probability distribution over the possible observations, and a set of transition probabilities between the states.
- HMMs can be used to model the speech signal as a sequence of observations, each generated by one of the states, and the underlying state sequence as a hidden variable that needs to be inferred.
- The optimal state sequence is the most likely sequence of states that generated the observed speech signal, given the parameters of the HMM.
- The optimal state sequence can be used for various speech-related tasks, such as speech recognition, speaker identification, speech segmentation, etc.
- The optimal state sequence can be computed using the Viterbi algorithm, which is a dynamic programming algorithm that finds the maximum likelihood path through the HMM.
- The Viterbi algorithm works by keeping track of the best path and the best score for each state at each time step, and then backtracking from the final state to the initial state to obtain the optimal state sequence.
- The Viterbi algorithm can be modified to incorporate additional constraints or objectives, such as smoothing the state likelihoods, enforcing the HMM topology, or integrating the grammar rules.



### Viterbi Search for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Viterbi search is a dynamic programming algorithm that finds the most likely sequence of hidden states in a hidden Markov model (HMM) given a sequence of observed events .
- Viterbi search is widely used in speech analysis applications, such as speech recognition, speech synthesis, and speech enhancement  .
- Viterbi search consists of two main steps: forward computation and backtracking .
- Forward computation calculates the probability of the most likely path that ends at each state for each time step, using the transition and emission probabilities of the HMM .
- Backtracking traces back the optimal path from the final state to the initial state, using pointers that store the previous state for each state and time step .
- Viterbi search can be generalized to handle multiple observations, multiple models, or multiple dimensions, by using a multidimensional trellis or lattice.
- Viterbi search can be improved by using pruning techniques, such as beam search, to reduce the search space and computational complexity .
- Viterbi search can be combined with other methods, such as acoustic models, language models, or microphone arrays, to enhance the performance and robustness of speech analysis systems .



### Baum-Welch Parameter Re-Estimation

- The Baum-Welch algorithm is a special case of the expectation-maximization (EM) algorithm used to find the unknown parameters of a hidden Markov model (HMM).
- It makes use of the forward-backward algorithm to compute the statistics for the expectation step.
- The algorithm was named after its inventors Leonard E. Baum and Lloyd R. Welch, who first described it in the late 1960s and early 1970s.
- The algorithm works as follows:

  - Initialize the HMM parameters (initial state probabilities, transition probabilities, and observation probabilities) randomly or based on some prior knowledge.
  - Repeat until convergence or a maximum number of iterations:
    - E-step: For each sequence in the training data, use the forward-backward algorithm to compute the posterior probabilities of the hidden states and the state transitions given the observations and the current parameters.
    - M-step: Update the parameters by maximizing the expected log-likelihood of the data given the posterior probabilities computed in the E-step.
  - Return the final parameters as the estimate of the HMM.

- The algorithm is guaranteed to converge to a local maximum of the log-likelihood function, but not necessarily to the global maximum.
- The algorithm can be used for various applications of HMMs, such as speech recognition, bioinformatics, and natural language processing.



### Implementation Issues

Speech recognition is the process of converting spoken words into written text or commands. It is a challenging task that involves many technical and social issues. Some of the common implementation issues are:

- **Accuracy**: The accuracy of a speech recognition system depends on many factors, such as the quality of the input speech, the background noise, the speaker's accent, the vocabulary size, the grammar complexity, and the domain knowledge. A low accuracy rate can lead to frustration, misunderstanding, and errors. To improve the accuracy, speech recognition systems need to use robust algorithms, large and diverse training data, and domain-specific models.  
- **Cost and duration**: The cost and duration of implementing a speech recognition system can be high, especially for large-scale and customized applications. The cost includes the hardware, software, data, and human resources required to develop, test, and deploy the system. The duration includes the time needed to collect, annotate, and process the data, to train and evaluate the models, and to integrate and maintain the system. To reduce the cost and duration, speech recognition systems can use open-source or cloud-based platforms, such as Google Cloud Speech-to-Text, Azure Speech to Text, Dragon APIs, and IBM Watson. 
- **Privacy and security**: The privacy and security of the speech data and the speech recognition results are important, especially for sensitive and confidential applications, such as healthcare, banking, and legal services. The speech data and the results may contain personal, financial, or medical information that should be protected from unauthorized access, modification, or disclosure. To ensure the privacy and security, speech recognition systems need to comply with the relevant regulations and standards, such as HIPAA, GDPR, and PCI DSS. They also need to use encryption, authentication, and authorization mechanisms to safeguard the data and the results.  
- **Bias and fairness**: The bias and fairness of the speech recognition system refer to the extent to which the system treats different groups of speakers equally and impartially. The bias and fairness can be affected by the data, the algorithms, and the evaluation metrics used by the system. For example, the system may perform worse for speakers with different accents, dialects, genders, ages, or races, due to the lack of representation or diversity in the data or the algorithms. The system may also use inappropriate or inaccurate metrics to measure the performance or the quality of the system, such as word error rate or user satisfaction. To address the bias and fairness, speech recognition systems need to use inclusive and representative data, to audit and monitor the algorithms, and to use multiple and meaningful metrics.

