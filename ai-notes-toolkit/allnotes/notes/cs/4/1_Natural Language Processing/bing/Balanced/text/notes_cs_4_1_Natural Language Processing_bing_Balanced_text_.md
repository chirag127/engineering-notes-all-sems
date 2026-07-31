

## Unit 1 - INTRODUCTION

- This unit provides an overview of the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI can be classified into different types based on the goals, methods, and applications of the systems. Some of the common types are:
  - Weak AI or Narrow AI: Systems that are designed to perform a specific task or domain, such as face recognition, chess playing, or speech recognition. They do not have general intelligence or understanding of other domains.
  - Strong AI or Artificial General Intelligence (AGI): Systems that can perform any intellectual task that a human can, across different domains and contexts. They have general intelligence and can reason, learn, and adapt to new situations. This type of AI is still a hypothetical goal and has not been achieved yet.
  - Artificial Superintelligence (ASI): Systems that can surpass human intelligence and capabilities in all domains and contexts. They can create and discover new knowledge and goals that humans cannot. This type of AI is also a hypothetical goal and has not been achieved yet.
- AI can also be classified into different types based on the degree of human involvement and control over the systems. Some of the common types are:
  - Reactive AI: Systems that do not have any memory or learning capabilities. They react to the current inputs and stimuli without considering the past or future consequences. For example, a chess program that only evaluates the current board position and makes the best move.
  - Limited Memory AI: Systems that can store and use some information from the past to improve their performance. They can learn from their experiences and adapt to changing situations. For example, a self-driving car that can remember the traffic rules and road conditions.
  - Theory of Mind AI: Systems that can understand and model the mental states, emotions, beliefs, and intentions of other agents, both human and artificial. They can interact and communicate with others in a natural and empathetic way. For example, a social robot that can recognize and respond to human emotions and expressions.
  - Self-Aware AI: Systems that can have a sense of self and consciousness. They can reflect on their own actions, goals, and abilities, and modify them accordingly. They can also understand and respect the values and ethics of other agents. For example, an AI agent that can explain its own reasoning and decisions to humans.



### Origins and challenges of NLP

- Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics that deals with the interactions between computers and human languages.
- The origins of NLP can be traced back to the early attempts to automate the translation of natural languages, such as the Georgetown experiment in 1954, which translated 60 sentences from Russian to English.
- The initial approach to NLP was based on complex, hand-written rules that tried to capture the structure and meaning of natural languages. However, this approach faced many limitations, such as the ambiguity, variability, and richness of natural languages.
- In the late 1980s, a paradigm shift occurred in NLP, with the introduction of statistical and machine learning methods that used large corpora of text data to learn patterns and probabilities of natural languages. This approach enabled more robust and scalable NLP systems that could handle noisy and incomplete data.
- In the 2010s, another breakthrough in NLP was achieved with the development of deep learning techniques, such as neural networks and transformers, that could learn complex and high-dimensional representations of natural languages from massive amounts of data. This approach enabled more powerful and versatile NLP systems that could perform tasks such as machine translation, text summarization, sentiment analysis, question answering, and natural language generation.
- Despite the remarkable advances in NLP, there are still many challenges and open problems that need to be addressed, such as:
  - The diversity and dynamism of natural languages, which require NLP systems to adapt to different domains, genres, styles, dialects, and contexts.
  - The sparsity and imbalance of natural language data, which require NLP systems to deal with rare words, unseen events, and long-tail phenomena.
  - The ambiguity and complexity of natural language semantics, which require NLP systems to understand the meaning, intention, and sentiment of natural language utterances, as well as the common sense and world knowledge that humans rely on.
  - The evaluation and explainability of NLP systems, which require NLP systems to provide reliable and interpretable results, as well as to justify and correct their errors.
  - The ethical and social implications of NLP systems, which require NLP systems to respect the privacy, security, fairness, and diversity of natural language users and data.



### Language Modeling

- Language modeling is the task of estimating the probability of a given sequence of words or tokens in a natural language.  
- Language models are useful for various natural language processing applications, such as speech recognition, machine translation, text summarization, text generation, etc. 
- Language models can be classified into two main types: **n-gram models** and **neural models**. 
- N-gram models are based on counting the frequency of n consecutive words in a large corpus of text and using the Markov assumption to estimate the probability of the next word given the previous n-1 words. 
- Neural models are based on using deep neural networks, such as recurrent neural networks (RNNs), long short-term memory (LSTM), gated recurrent units (GRU), transformers, etc., to learn the probability distribution of words or tokens in a language. 
- Neural models can capture more complex and long-range dependencies between words than n-gram models, but they also require more computational resources and data to train. 
- Some of the challenges and open problems in language modeling are: dealing with out-of-vocabulary words, handling rare words, modeling multilingual and cross-lingual data, generating coherent and diverse texts, evaluating the quality and usefulness of language models, etc.  

: https://www.techtarget.com/searchenterpriseai/definition/language-modeling
: https://en.wikipedia.org/wiki/Language_model
: https://builtin.com/data-science/beginners-guide-language-models



### Grammar-based LM for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A language model (LM) is a system that assigns probabilities to sequences of words or symbols in a natural language.
- A grammar-based language model (GLM) is a type of LM that uses a formal grammar to generate and constrain the possible word sequences.
- A grammar is a set of rules that specify the syntax and structure of a language, such as word order, agreement, and morphology.
- A grammar-based language model can be seen as a generative model that defines a probability distribution over sentences or utterances in a language.
- A grammar-based language model can be based on different types of grammars, such as regular, context-free, or context-sensitive grammars.
- A grammar-based language model can capture long-range dependencies and complex syntactic phenomena that are hard to model with statistical methods, such as n-grams.
- A grammar-based language model can also incorporate semantic and pragmatic information, such as word meanings, discourse relations, and speech acts.
- A grammar-based language model can be used for various natural language processing tasks, such as speech recognition, machine translation, natural language generation, and parsing.
- A grammar-based language model can be combined with a statistical language model to improve the performance and robustness of the system.
- A grammar-based language model can be learned from data using various methods, such as rule induction, probabilistic parsing, or neural networks.



### Statistical Language Model for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A statistical language model (SLM) is a mathematical tool that assigns probabilities to sequences of words or symbols in a natural language, such as English, Chinese, or Hindi.
- SLMs are used to generate or analyze natural language texts for various applications, such as speech recognition, machine translation, natural language generation, information retrieval, and text summarization.
- SLMs are based on the assumption that the probability of a word or symbol depends on its previous words or symbols, or its context. This is known as the Markov property.
- SLMs can be classified into two main types: n-gram models and neural network models.
- N-gram models are the simplest and most widely used SLMs. They estimate the probability of a word or symbol based on its previous n-1 words or symbols, where n is a fixed number. For example, a bigram model (n=2) estimates the probability of a word based on its previous word, and a trigram model (n=3) estimates the probability of a word based on its previous two words.
- Neural network models are more complex and powerful SLMs. They use artificial neural networks to learn the probability distribution of words or symbols in a natural language. They can capture long-range dependencies and semantic similarities between words or symbols. For example, a recurrent neural network (RNN) model can process variable-length sequences of words or symbols, and a transformer model can encode the context and attention of words or symbols.
- SLMs are trained on large corpora of natural language texts, such as books, news articles, or social media posts. The quality of SLMs depends on the size and diversity of the training data, as well as the choice of the model architecture and parameters.
- SLMs are evaluated by various metrics, such as perplexity, accuracy, and BLEU score. Perplexity measures how well a SLM predicts the next word or symbol in a sequence. Accuracy measures how often a SLM predicts the correct word or symbol. BLEU score measures how similar the output of a SLM is to a human reference.



### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE are useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE can be applied in many programming languages like Java, JS, php, C++, etc.
- RE are based on regular sets, which are sets of strings that can be defined by a finite number of rules.
- Examples of regular sets are:

| Regular Expressions | Regular Set |
| ------------------- | ----------- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s |

- RE can be composed of simple symbols, such as letters, digits, or punctuation marks, and operators, such as +, *, ?, |, etc.
- Examples of RE operators are:

| Operator | Meaning |
| -------- | ------- |
| + | One or more occurrences of the preceding expression |
| * | Zero or more occurrences of the preceding expression |
| ? | Zero or one occurrence of the preceding expression |
| | | Alternation (either the expression before or after the operator) |
| () | Grouping (the expression inside the parentheses is treated as a unit) |
| [] | Character class (any one of the characters inside the brackets) |
| [^] | Negated character class (any one of the characters not inside the brackets) |
| . | Any single character (except newline) |
| ^ | Beginning of the string |
| $ | End of the string |
| \ | Escape character (used to indicate that the next character is not to be interpreted literally) |

- RE can be used to perform various tasks on natural language texts, such as:

  - Tokenization: splitting a text into smaller units, such as words, sentences, or phrases.
  - Stemming: reducing a word to its base or root form, such as removing suffixes or prefixes.
  - Lemmatization: finding the canonical or dictionary form of a word, such as finding the verb form of an inflected word.
  - Normalization: transforming a text into a standard or consistent form, such as converting case, spelling, or punctuation.
  - Filtering: removing unwanted or irrelevant parts of a text, such as stopwords, noise, or duplicates.
  - Extraction: identifying and extracting specific information from a text, such as names, dates, numbers, or keywords.
  - Validation: checking if a text conforms to a certain format or pattern, such as email addresses, phone numbers, or URLs.
  - Replacement: substituting parts of a text with other strings, such as correcting errors, anonymizing data, or generating variations.

- RE are powerful and flexible tools for natural language processing, but they also have some limitations, such as:

  - RE are not able to capture the meaning or semantics of natural language, only its surface form.
  - RE are not able to handle complex linguistic phenomena, such as ambiguity, context, or pragmatics.
  - RE are not able to deal with irregular or exceptional cases, such as idioms, slang, or neologisms.
  - RE are not able to learn from data or generalize to new cases, unlike machine learning or deep learning methods.



### Finite-State Automata for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Finite-state automata (FSA) are abstract machines that can recognize and generate patterns of symbols, such as strings of characters or words.
- FSA have a finite number of states, and can change from one state to another according to some rules, depending on the input symbol.
- FSA can be deterministic (DFA) or non-deterministic (NFA). DFA have exactly one transition for each input symbol and state, while NFA can have zero, one, or more transitions for each input symbol and state.
- FSA can be used to model various aspects of natural language processing (NLP), such as morphology, syntax, semantics, and phonology.
- FSA can also be extended to finite-state transducers (FST), which can produce an output symbol for each input symbol, or vice versa. FST can be used to perform tasks such as morphological analysis, text normalization, spelling correction, and machine translation.
- FSA and FST have several advantages in NLP, such as efficiency, simplicity, modularity, and transparency. They can also be combined with other methods, such as probabilistic models, to improve their performance and accuracy.



### English Morphology

- Morphology is the **study of the internal structure of words** and how they are formed from smaller units called **morphemes**  .
- Morphemes are the **smallest meaningful units** in a language, such as roots, prefixes, and suffixes.
- For example, the word "unhappy" consists of two morphemes: the prefix "un-" and the root "happy". The prefix "un-" changes the meaning of the root "happy" to its opposite.
- Morphology can be divided into two main branches: **inflectional morphology** and **derivational morphology**.
- Inflectional morphology deals with the **changes in the form of words** that indicate grammatical information, such as number, person, tense, case, etc.
- For example, the word "books" has an inflectional suffix "-s" that indicates plural number.
- Derivational morphology deals with the **creation of new words** from existing words by adding affixes or changing the word class, such as noun, verb, adjective, etc.
- For example, the word "happiness" is derived from the word "happy" by adding the suffix "-ness" that changes the word class from adjective to noun.
- Morphology is an important aspect of natural language processing, as it helps to **analyze, generate, and understand words** in a language.
- Morphology can also help to **identify the meaning, origin, and history** of words, as well as their **relations and variations** with other words in the same language or different languages.



### Transducers for lexicon and rules for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A transducer is a device or a model that converts one form of data into another. For example, a microphone is a transducer that converts sound waves into electrical signals.
- In natural language processing (NLP), a transducer can be used to map between different levels of linguistic representation, such as surface forms, lexical forms, syntactic structures, semantic representations, etc.
- A lexical transducer is a special type of finite-state transducer that maps inflected surface forms to lexical forms, and vice versa . For example, a lexical transducer can map the word "dogs" to its lexical form "dog+N+PL", indicating that it is a noun in plural form.
- A lexical transducer can be constructed using finite-state methods, such as regular expressions, rewrite rules, and composition operations. For example, a lexical transducer can be composed of a lexicon, which is a finite-state acceptor that recognizes valid words and assigns them lexical features, and a morphotactics, which is a finite-state transducer that specifies the valid combinations of morphemes and their surface forms.
- A lexical transducer can be used for various NLP tasks, such as morphological analysis, morphological generation, spelling correction, text normalization, etc . For example, a lexical transducer can be used to analyze the word "dogs" and generate its possible lexical forms, or to generate the possible surface forms for a given lexical form.
- A lexical transducer can also be combined with other finite-state transducers, such as context dependency transducers, language models, parsers, etc., to form more complex NLP pipelines . For example, a virtual keyboard pipeline can consist of a context dependency transducer, a lexicon transducer, and an n-gram language model, which can be composed together to decode the user input.



### Tokenization for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Tokenization is the process of breaking down a piece of text into small units called tokens   .
- A token may be a word, part of a word or just characters like punctuation.
- Tokenization is used in natural language processing to split paragraphs and sentences into smaller units that can be more easily assigned meaning.
- Tokenization is a crucial step in many NLP tasks, such as part-of-speech tagging, text classification, sentiment analysis, topic modeling, and machine translation .
- One of the main advantages of tokenization is that it can help to improve the accuracy of these tasks by providing more context for each word.
- Tokenization is also the first step in any NLP pipeline. It has an important effect on the rest of the pipeline.
- A tokenizer breaks unstructured data and natural language text into chunks of information that can be considered as discrete elements.
- The token occurrences in a document can be used directly as a vector representing that document.
- Tokenization is not a simple process, because every language has its own grammatical constructs, which are often difficult to write down as rules.
- Tokenization also depends on the level of analysis required for the task. For example, some tasks may require splitting words into subwords or characters, while others may require grouping words into phrases or sentences.
- Tokenization can be done using different methods, such as rule-based, dictionary-based, statistical, or machine learning-based.
- Tokenization can also face various challenges, such as dealing with abbreviations, contractions, hyphenated words, compound words, slang, emoticons, and foreign words .
- Tokenization is an essential and fundamental step in natural language processing, and it can have a significant impact on the performance and quality of the subsequent tasks .



### Detecting and Correcting Spelling Errors

- Spelling errors are a common source of noise and ambiguity in natural language processing (NLP) tasks, such as information retrieval, machine translation, text summarization, etc.
- Spelling errors can be classified into two types: non-word errors and real-word errors  .
  - Non-word errors are errors that result in a word that does not exist in the language, such as *teh* for *the*, *recieve* for *receive*, etc.
  - Real-word errors are errors that result in a word that exists in the language, but is not the intended one, such as *their* for *there*, *form* for *from*, etc.
- Detecting and correcting non-word errors can be done by using a dictionary or a lexicon to check if a word exists or not, and then applying some rules or algorithms to generate and rank possible corrections  .
  - Some common algorithms for generating corrections are:
    - Edit distance: the number of insertions, deletions, substitutions, or transpositions of characters needed to transform one word into another, such as *Damerau-Levenshtein distance*, *Jaro-Winkler distance*, etc.
    - N-gram similarity: the number of common n-grams (substrings of length n) between two words, such as *Jaccard similarity*, *Dice coefficient*, etc.
    - Phonetic similarity: the similarity of the sounds of two words, such as *Soundex*, *Metaphone*, etc.
  - Some common methods for ranking corrections are:
    - Frequency-based: the probability of a word occurring in a large corpus of text, such as *Zipf's law*, *Google n-gram*, etc.
    - Context-based: the probability of a word occurring given its surrounding words, such as *Markov models*, *Hidden Markov models*, *N-gram language models*, etc.
- Detecting and correcting real-word errors can be done by using a combination of linguistic and statistical methods to analyze the syntactic and semantic compatibility of a word with its context  .
  - Some common methods for detecting real-word errors are:
    - Part-of-speech tagging: the process of assigning a grammatical category to each word in a sentence, such as *noun*, *verb*, *adjective*, etc.
    - Parsing: the process of analyzing the syntactic structure of a sentence, such as *constituency parsing*, *dependency parsing*, etc.
    - Semantic analysis: the process of determining the meaning of a word or a phrase in a sentence, such as *word sense disambiguation*, *semantic role labeling*, etc.
  - Some common methods for correcting real-word errors are:
    - Rule-based: the use of predefined rules or patterns to identify and replace errors, such as *spelling rules*, *grammar rules*, etc.
    - Machine learning-based: the use of supervised or unsupervised learning algorithms to learn from data and generate corrections, such as *decision trees*, *neural networks*, *transformers*, etc.



### Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are by counting the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, or transposition of two adjacent characters.
- Each operation has a cost, which can be uniform or weighted depending on the application.
- The minimum edit distance between two strings is the sum of the costs of the operations that transform one string into another.
- For example, the minimum edit distance between "intention" and "execution" is 5, with the following operations and costs:

| Operation | Cost | Result |
|-----------|------|--------|
| Substitute "e" for "i" | 1 | "entention" |
| Substitute "x" for "n" | 1 | "extention" |
| Insert "c" after "x" | 1 | "execution" |
| Delete "n" | 1 | "executio" |
| Insert "n" at the end | 1 | "execution" |

- The minimum edit distance can be computed using a dynamic programming algorithm that fills a matrix with the optimal costs for all possible substrings.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of inserting or deleting the characters of the strings.
  - For each cell in the matrix, compute the cost of the three possible operations: insertion, deletion, and substitution (or transposition if allowed), and choose the minimum one.
  - The cost of insertion or deletion is the cost of the operation plus the cost of the previous cell in the same row or column.
  - The cost of substitution is the cost of the operation plus the cost of the previous cell in the diagonal, unless the characters are the same, in which case the cost is zero.
  - The cost of transposition is the cost of the operation plus the cost of the cell two positions back in the diagonal, if the characters are swapped.
  - The minimum edit distance is the value of the last cell in the matrix.

- The minimum edit distance can be used for various applications in natural language processing, such as spelling correction, speech recognition, machine translation, and text similarity.



## Unit 2 - WORD LEVEL ANALYSIS

- Word level analysis is the process of identifying and describing the structure and meaning of words in a text.
- Word level analysis involves the following subtasks:
  - Morphological analysis: identifying the smallest meaningful units (morphemes) that make up a word and how they are combined.
  - Lexical analysis: identifying the part of speech (noun, verb, adjective, etc.) and the lexical category (common, proper, abstract, etc.) of a word.
  - Semantic analysis: identifying the meaning and the sense of a word in a given context, as well as its synonyms, antonyms, hyponyms, hypernyms, etc.
  - Pragmatic analysis: identifying the use and the function of a word in a speech act, as well as its connotation, implication, presupposition, etc.
- Word level analysis can be applied to different types of texts, such as written, spoken, or multimodal texts, and to different genres, such as narrative, descriptive, persuasive, or informative texts.
- Word level analysis can help to improve one's reading comprehension, writing skills, vocabulary, and critical thinking. It can also help to appreciate the stylistic and rhetorical effects of word choice and word formation in a text.



### Unsmoothed N-grams

- An n-gram is a sequence of n words or tokens in a text. For example, "natural language processing" is a trigram (n = 3).
- N-grams are used to model the probability of a word given its previous words or context. For example, P(processing | natural language) is the probability of the word "processing" given the previous words "natural language".
- An unsmoothed n-gram model estimates the probability of a word by counting the frequency of the n-gram in the text and dividing it by the frequency of the (n-1)-gram. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C is the count function.
- Unsmoothed n-gram models have some advantages and disadvantages:
  - Advantages:
    - They are simple and easy to implement.
    - They can capture local dependencies and patterns in the text.
    - They can be used for various tasks in natural language processing, such as text generation, speech recognition, language identification, etc.
  - Disadvantages:
    - They suffer from data sparsity, which means that many n-grams may not occur in the text or have zero counts, leading to zero probabilities and unreliable estimates.
    - They have a high dimensionality, which means that the number of possible n-grams grows exponentially with n and the vocabulary size, making them computationally expensive and memory intensive.
    - They make a strong independence assumption, which means that they only consider the previous n-1 words as the context and ignore the rest of the history, which may not be realistic or sufficient for some tasks.



### Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams are useful for various natural language processing tasks, such as language modeling, text generation, machine translation, speech recognition, spelling correction, etc.
- However, n-grams also have some limitations and challenges that need to be evaluated and addressed, such as:

  - Data sparsity: N-grams with higher n values are more specific and less frequent in the training data, which leads to zero or low probabilities for unseen n-grams in the test data. This can affect the performance and generalization of n-gram models.
  - Smoothing techniques: To deal with data sparsity, smoothing techniques are applied to assign some non-zero probabilities to unseen n-grams by redistributing the probabilities of seen n-grams. There are various smoothing techniques, such as add-one smoothing, Good-Turing smoothing, Kneser-Ney smoothing, etc. Each technique has its own advantages and disadvantages, and the choice of the best technique depends on the data and the task.
  - Perplexity: Perplexity is a common metric to evaluate the quality of n-gram models. It measures how well the model predicts the test data, or how surprised the model is by the test data. Lower perplexity means higher probability and better prediction. Perplexity is calculated as the inverse of the geometric mean of the probabilities of the test words given their previous words. However, perplexity is not a perfect metric, as it does not capture the semantic or syntactic aspects of the text, and it can be influenced by the size and domain of the test data.
  - Out-of-vocabulary words: Out-of-vocabulary words are words that appear in the test data but not in the training data. They can cause problems for n-gram models, as they have zero probability and can affect the perplexity score. One way to deal with out-of-vocabulary words is to replace them with a special token, such as `<UNK>`, and estimate its probability based on the frequency of unknown words in the training data. Another way is to use subword units, such as characters or morphemes, to model the words, which can increase the vocabulary coverage and reduce the data sparsity.



### Smoothing

- Smoothing is the process of flattening a probability distribution implied by a language model so that all reasonable word sequences can occur with some probability .
- Smoothing often involves broadening the distribution by redistributing weight from high probability regions to zero probability regions .
- Smoothing is very important in natural language processing, as some words may have zero or close to zero probabilities such as the out-of-vocabulary words (words that do not exist in the vocabulary), but the same rare words may not have the same values in test data.
- Smoothing techniques in NLP are used to address scenarios related to determining probability / likelihood estimate of a sequence of words (say, a sentence) occurring together when one or more words individually (unigram) or N-grams such as bigram or trigram in the given set have never occurred in the past.
- Smoothing can help performance whenever data sparsity is an issue, and data sparsity is almost always an issue in statistical modeling.
- Smoothing can also allow expanding the model, such as by moving to a higher n-gram model, to improve the accuracy of the language model.
- Some common smoothing techniques are:
  - Additive smoothing: adding a small constant to all counts
  - Backoff smoothing: using lower order n-grams when higher order n-grams have zero counts
  - Interpolation smoothing: combining different order n-grams with different weights
  - Kneser-Ney smoothing: using a modified count that discounts the probability of seen n-grams and assigns some probability mass to unseen n-grams



### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models, which are used to estimate the probability of a word given its previous words in a sequence.
- Smoothing is needed to deal with the problem of data sparseness, which occurs when some n-grams are not observed in the training data, resulting in zero probabilities.
- Backoff is a method that uses lower-order n-grams when higher-order n-grams have insufficient evidence. For example, if a trigram probability is zero, then a bigram or a unigram probability is used instead.
- Interpolation is a method that combines n-grams of different orders with some weights, which are usually learned from a held-out corpus. For example, a trigram probability can be interpolated with a bigram and a unigram probability as follows:

  p(w<sub>n</sub>|w<sub>n-2</sub>,w<sub>n-1</sub>) = λ<sub>1</sub>p(w<sub>n</sub>|w<sub>n-2</sub>,w<sub>n-1</sub>) + λ<sub>2</sub>p(w<sub>n</sub>|w<sub>n-1</sub>) + λ<sub>3</sub>p(w<sub>n</sub>)

  where λ<sub>1</sub> + λ<sub>2</sub> + λ<sub>3</sub> = 1

- In general, interpolation works better than backoff, as it can capture more information from different n-gram orders. However, interpolation requires more parameters to be estimated, which can be computationally expensive.
- There are various techniques to improve interpolation and backoff, such as deleted interpolation, absolute discounting, and Kneser-Ney smoothing. These techniques aim to optimize the weights or the probabilities of n-grams based on some criteria, such as minimizing perplexity or maximizing likelihood.



### Word Classes

- Word classes, also known as parts of speech, are categories of words that share common grammatical properties and functions in a sentence.
- Word classes are useful for natural language processing (NLP) tasks such as parsing, tagging, and generating sentences.
- There are different ways to classify words into word classes, depending on the language and the level of granularity. Some common word classes are:

  - Nouns: words that denote entities, such as people, places, things, or concepts. Examples: `book`, `Sydney`, `love`.
  - Verbs: words that denote actions, states, or events. Examples: `read`, `is`, `happened`.
  - Adjectives: words that modify nouns, expressing qualities, quantities, or degrees. Examples: `red`, `big`, `happy`.
  - Adverbs: words that modify verbs, adjectives, or other adverbs, expressing manner, time, place, degree, or frequency. Examples: `quickly`, `yesterday`, `here`, `very`, `often`.
  - Pronouns: words that substitute for nouns or noun phrases, referring to entities that are already known or can be inferred from the context. Examples: `he`, `it`, `they`.
  - Prepositions: words that introduce phrases that express the relation of a noun or pronoun to another word in the sentence. Examples: `in`, `on`, `with`, `from`.
  - Conjunctions: words that connect words, phrases, or clauses, expressing logical relations such as coordination, subordination, or contrast. Examples: `and`, `but`, `because`, `although`.
  - Determiners: words that precede nouns, specifying their reference, quantity, or possession. Examples: `the`, `a`, `some`, `my`.
  - Interjections: words that express emotions, attitudes, or reactions, usually followed by an exclamation mark. Examples: `wow`, `ouch`, `oops`.

- Some words can belong to more than one word class, depending on their usage and meaning in a sentence. For example, `book` can be a noun or a verb, `well` can be an adverb or an adjective, and `like` can be a verb, a preposition, or a conjunction.



### Part-of-Speech Tagging

- Part-of-speech (POS) tagging is the process of assigning a grammatical category to each word in a sentence or text, such as noun, verb, adjective, adverb, etc.   
- POS tagging is an important task in natural language processing (NLP), as it can help to analyze the structure and meaning of a sentence, and to perform other tasks such as parsing, named entity recognition, sentiment analysis, machine translation, etc.   
- POS tagging can be done manually by human annotators, or automatically by computer programs. Manual POS tagging is more accurate but time-consuming and costly, while automatic POS tagging is faster and cheaper but prone to errors.  
- There are different methods and techniques for automatic POS tagging, such as rule-based, statistical, and neural network-based approaches. Rule-based methods rely on predefined rules and dictionaries to assign tags, while statistical methods use probabilistic models and machine learning algorithms to learn from annotated data and predict tags. Neural network-based methods use deep learning architectures such as recurrent neural networks (RNNs) and transformers to encode the contextual information and generate tags.   
- The performance of automatic POS tagging depends on various factors, such as the language, the domain, the size and quality of the training data, the complexity and accuracy of the model, and the evaluation metrics. Common evaluation metrics for POS tagging include accuracy, precision, recall, and F1-score.   
- POS tagging is a challenging and active research area in NLP, as different languages and domains have different grammatical rules and conventions, and new words and expressions are constantly emerging. Some of the current research topics and challenges in POS tagging include cross-lingual and multilingual POS tagging, domain adaptation and transfer learning, low-resource and zero-shot POS tagging, and fine-grained and morphological POS tagging.



### Rule-based word level analysis

- Word level analysis is the process of identifying and labeling the words and their parts of speech in a natural language text.
- Rule-based word level analysis is a method that uses predefined rules and patterns to perform word level analysis, such as tokenization, part-of-speech tagging, stemming, lemmatization, etc.
- Rule-based word level analysis can be implemented using regular expressions, finite state automata, context-free grammars, or other formalisms that can capture the structure and syntax of natural language.
- Rule-based word level analysis has some advantages and disadvantages compared to machine learning-based word level analysis.
  - Advantages:
    - It does not require large amounts of annotated data for training.
    - It can be more transparent and interpretable than machine learning models.
    - It can handle domain-specific or rare words better than machine learning models.
  - Disadvantages:
    - It can be more labor-intensive and time-consuming to develop and maintain.
    - It can be less robust and adaptable to new or unseen data than machine learning models.
    - It can have lower accuracy and coverage than machine learning models.



### Stochastic Word Level Analysis

- Word level analysis is the process of identifying and categorizing the words in a natural language text according to their morphology, syntax, and semantics.
- Stochastic word level analysis is the use of probabilistic models and methods to perform word level analysis, such as part-of-speech tagging, word segmentation, and spelling correction.
- Some of the advantages of stochastic word level analysis are:
  - It can handle ambiguity and uncertainty in natural language texts, such as homonyms, synonyms, and unknown words.
  - It can learn from data and adapt to new domains and languages, without requiring extensive manual rules and dictionaries.
  - It can leverage large-scale corpora and computational resources to achieve high accuracy and efficiency.
- Some of the challenges of stochastic word level analysis are:
  - It requires annotated data for training and evaluation, which can be costly and time-consuming to obtain.
  - It may not capture the linguistic and contextual nuances of natural language, such as pragmatics, discourse, and style.
  - It may be sensitive to noise and errors in the input data, such as typos, slang, and dialects.
- Some of the common techniques and models for stochastic word level analysis are:
  - Hidden Markov Models (HMMs), which are generative models that use a sequence of hidden states and observable symbols to represent the word level analysis task, such as part-of-speech tagging.
  - Conditional Random Fields (CRFs), which are discriminative models that use a sequence of features and labels to represent the word level analysis task, such as word segmentation.
  - Neural Networks (NNs), which are non-linear models that use layers of neurons and activation functions to represent the word level analysis task, such as spelling correction.
  - Reinforcement Learning (RL), which is a learning paradigm that uses rewards and actions to represent the word level analysis task, such as word-level sentiment analysis.



### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill  .
- It is an instance of transformation-based learning (TBL), which is a general framework for learning from examples by applying transformation rules  .
- Transformation rules are of the form: change the tag of a word from X to Y if condition Z is met .
- The algorithm starts with an initial state, where all words are assigned a default tag (usually the most frequent tag in the training data) .
- Then, it iteratively applies the best transformation rule that reduces the most errors on the training data, until no more improvement can be made .
- The best transformation rule is selected by using an error-driven learning method, which compares the current state with the correct state (the gold standard) and tries to correct the most frequent error .
- The final state is the output of the algorithm, which contains the learned transformation rules and the tagged text .
- Transformation-based tagging has some advantages over other methods, such as:
  - It allows us to have linguistic knowledge in a readable form, as the transformation rules are easy to interpret and explain .
  - It can handle unknown words and sparse data, as it does not rely on probabilities or statistics .
  - It can be applied at a higher level of textual interpretation, such as chunking or named entity recognition, by using different types of tags and conditions .
- Transformation-based tagging also has some limitations, such as:
  - It can be slow and inefficient, as it requires multiple passes over the training data and the application of many rules .
  - It can be sensitive to the order of the rules and the initial state, as different choices can lead to different results .
  - It can be prone to overfitting, as it may learn rules that are specific to the training data and do not generalize well to new data .



### Issues in PoS tagging

- Part-of-speech (PoS) tagging is the task of assigning a word category (such as noun, verb, adjective, etc.) to each word in a text based on its definition and context.
- PoS tagging is useful for many natural language processing (NLP) applications, such as syntactic parsing, semantic analysis, information extraction, machine translation, etc.
- PoS tagging is not a trivial task, as it faces several challenges and difficulties, such as:
  - **Ambiguity**: Many words can have multiple PoS depending on the context. For example, the word "book" can be a noun or a verb, as in "I read a book" or "Book the flight". A PoS tagger has to resolve this ambiguity accurately based on the surrounding words and their PoS.
  - **Unknown words**: A PoS tagger may encounter words that are not in its vocabulary, such as new words, proper names, foreign words, etc. A PoS tagger has to assign a PoS to these words based on some heuristics, such as word morphology, word position, etc.
  - **Variation**: Different languages, dialects, genres, domains, etc. may have different PoS systems and conventions. A PoS tagger has to adapt to these variations and use the appropriate PoS tags for different texts. For example, some languages may have more or fewer PoS categories than others, or some genres may use more or fewer PoS tags than others.
  - **Noise**: A PoS tagger may have to deal with noisy texts, such as speech transcripts, social media posts, etc. that may contain spelling errors, grammatical errors, slang, abbreviations, etc. A PoS tagger has to cope with these errors and assign PoS tags as accurately as possible.



### Hidden Markov and Maximum Entropy models

- Hidden Markov models (HMMs) are a probabilistic framework for modeling sequential data, such as words in a sentence or speech signals. They assume that the data is generated by an underlying stochastic process that has a finite number of hidden states, and that the observed data depends only on the current state.
- Maximum entropy models (MaxEnt) are a general method for estimating probability distributions from data, based on the principle of choosing the distribution that maximizes the entropy (or uncertainty) subject to the constraints imposed by the data. They can incorporate various types of features and prior knowledge into the model.
- Maximum entropy Markov models (MEMMs) are a combination of HMMs and MaxEnt models, where the hidden states are predicted by a MaxEnt classifier that uses features of the previous and current observations. They can overcome some of the limitations of HMMs, such as the independence assumption and the lack of contextual information .
- Some applications of HMMs and MEMMs in natural language processing are:
  - Part-of-speech tagging: assigning a grammatical category to each word in a sentence, such as noun, verb, adjective, etc. HMMs and MEMMs can model the sequential nature of the words and their dependencies on the surrounding context  .
  - Text segmentation: dividing a text into meaningful units, such as sentences, paragraphs, topics, etc. HMMs and MEMMs can capture the transitions and boundaries between different segments .
  - Information extraction: extracting structured information from unstructured text, such as names, dates, locations, etc. HMMs and MEMMs can identify the relevant entities and their relationships in the text .



## Unit 3 - SYNTACTIC ANALYSIS

- Syntactic analysis is the process of analyzing the structure and grammar of a natural language sentence or program code.
- Syntactic analysis can be performed by using formal methods such as grammars, parsers, and automata, or by using statistical methods such as machine learning and natural language processing.
- Syntactic analysis can be used for various applications, such as:
  - Checking the validity and correctness of a sentence or code.
  - Extracting the meaning and information from a sentence or code.
  - Translating a sentence or code from one language to another.
  - Generating a sentence or code from a given input or context.
- Syntactic analysis can be divided into two main phases: lexical analysis and parsing.
  - Lexical analysis is the process of breaking a sentence or code into smaller units called tokens, such as words, symbols, numbers, etc.
  - Parsing is the process of building a hierarchical structure called a parse tree or syntax tree that represents the syntactic relations among the tokens.
- Syntactic analysis can be further classified into two types: top-down and bottom-up.
  - Top-down syntactic analysis is the process of starting from the root or the highest level of the parse tree and expanding it by applying the rules of the grammar until the tokens are matched.
  - Bottom-up syntactic analysis is the process of starting from the tokens or the lowest level of the parse tree and combining them by applying the rules of the grammar until the root is reached.



### Context Free Grammars

- A **context-free grammar (CFG)** is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a **left-hand side**, which identifies a syntactic category, and a **right-hand side**, which defines its alternative component parts, reading from left to right.
- For example, the rule `S -> NP VP` means that a sentence (S) can be composed of a noun phrase (NP) followed by a verb phrase (VP).
- A CFG can be used to model the constituent structure of natural language, which is the hierarchical organization of words into phrases and sentences.
- A CFG can also be used to define the high level structure of a programming language, such as the syntax of statements, expressions, and declarations.
- A CFG can be formally defined as a 4-tuple: `G = (N, Σ, R, S)`, where
  - `N` is a finite set of **non-terminal symbols**, which are the syntactic categories that can be expanded by the rules.
  - `Σ` is a finite set of **terminal symbols**, which are the basic units of the language, such as words or tokens.
  - `R` is a finite set of **production rules**, which are of the form `A -> α`, where `A` is a non-terminal symbol and `α` is a string of symbols from `(N ∪ Σ)*`, the Kleene closure of the union of `N` and `Σ`.
  - `S` is a distinguished non-terminal symbol, called the **start symbol**, which represents the whole language.
- A CFG can generate a language, which is the set of all strings that can be derived from the start symbol by applying the rules repeatedly.
- A CFG can also parse a string, which is the process of finding a derivation or a parse tree for the string, if it belongs to the language.
- A CFG is called **context-free** because the production rules can be applied regardless of the surrounding symbols, unlike in a context-sensitive grammar, where the rules depend on the context.
- Natural languages are not strictly context-free, as they have some phenomena that require context-sensitive rules, such as agreement, anaphora, and long-distance dependencies.
- However, CFGs are often used as a simple and convenient approximation of natural languages, as they can capture many of their syntactic patterns and regularities.
- CFGs are also useful for natural language processing (NLP) tasks, such as parsing, generation, translation, and summarization.



### Grammar rules for English for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Syntactic analysis is the process of analyzing the structure and meaning of sentences in a natural language, such as English.
- A grammar is a set of rules that defines the syntax and semantics of a language, i.e., how words can be combined into phrases and sentences, and what they mean.
- A grammar can be divided into two components: a lexicon and a set of rules.
- A lexicon is a list of words and their properties, such as part of speech, number, gender, tense, etc.
- A rule is a statement that specifies how words and phrases can be combined, and what constraints apply to them.
- There are different types of grammars, such as phrase structure grammars, dependency grammars, and lexical-functional grammars, that use different formalisms and representations to capture the syntactic structure and meaning of sentences.
- A common formalism for phrase structure grammars is the context-free grammar (CFG), which consists of a set of production rules of the form A -> B C, where A, B, and C are symbols that represent either words or phrases.
- A phrase structure grammar can be represented by a parse tree, which is a hierarchical diagram that shows how a sentence is derived from the grammar rules and the lexicon.
- A parse tree has a root node that represents the whole sentence, and branches that represent the subparts of the sentence. The leaves of the tree are the words of the sentence, and the internal nodes are the phrases and their labels.
- A phrase structure grammar can also be represented by a bracketed notation, which uses parentheses to indicate the boundaries and labels of the phrases in a sentence.
- For example, the sentence "The dog chased the cat" can be represented by the following parse tree and bracketed notation:

Parse tree

(S (NP (DT The) (NN dog)) (VP (VBD chased) (NP (DT the) (NN cat))))

- A phrase structure grammar can be ambiguous, meaning that it can generate more than one parse tree or bracketed notation for the same sentence. This can lead to different interpretations of the sentence, which may or may not be intended by the speaker or writer.
- For example, the sentence "I saw the man with the telescope" can be represented by two different parse trees and bracketed notations, depending on whether the phrase "with the telescope" modifies the verb "saw" or the noun "man":

Parse tree 1

(S (NP (PRP I)) (VP (VBD saw) (NP (DT the) (NN man) (PP (IN with) (NP (DT the) (NN telescope))))))

Parse tree 2

(S (NP (PRP I)) (VP (VBD saw) (NP (DT the) (NN man)) (PP (IN with) (NP (DT the) (NN telescope)))))

- To resolve syntactic ambiguity, one can use additional information, such as semantic, pragmatic, or contextual cues, or apply some heuristics or preferences, such as the principle of minimal attachment or the principle of late closure, that favor certain interpretations over others.
- Syntactic analysis is an important task in natural language processing, as it can provide useful information for other tasks, such as semantic analysis, discourse analysis, machine translation, information extraction, question answering, etc.



### Treebanks

- A treebank is a corpus of natural language sentences annotated with syntactic structure, such as phrase structure trees or dependency graphs .
- Treebanks can be used to study linguistic phenomena, such as word order, grammatical categories, and syntactic relations.
- Treebanks can also be used to engineer natural language processing systems, such as part-of-speech taggers, parsers, semantic analyzers, and machine translation systems .
- Treebanks are usually created by human annotators, who follow a set of guidelines and use annotation tools to assign syntactic labels to sentences.
- Treebanks can vary in size, language, genre, annotation scheme, and level of detail.
- Some examples of treebanks are the Penn Treebank for English, the Prague Dependency Treebank for Czech, the Universal Dependencies Treebank for multiple languages, and the PropBank for semantic roles.



### Normal Forms for Grammar

- A normal form for grammar is a standard way of writing the rules of a context-free grammar (CFG) that satisfies certain properties and simplifies the process of parsing and analyzing natural language sentences.
- There are different types of normal forms for grammar, such as Chomsky normal form (CNF), Greibach normal form (GNF), and Kuroda normal form (KNF).
- Each normal form has its own advantages and disadvantages, depending on the application and the complexity of the grammar.
- In this section, we will focus on Chomsky normal form, which is widely used in natural language processing (NLP) for parsing and analyzing natural language sentences.

#### Chomsky Normal Form

- A CFG is in Chomsky normal form if every rule is of the form:
  - A -> BC, where A, B, and C are non-terminal symbols
  - A -> a, where A is a non-terminal symbol and a is a terminal symbol
  - S -> ε, where S is the start symbol and ε is the empty string
- The advantages of CNF are:
  - It reduces the number of possible rules and derivations for a given sentence, making parsing more efficient and tractable.
  - It allows the use of efficient algorithms, such as the CYK algorithm, to determine whether a sentence belongs to a language generated by a CFG in CNF.
  - It preserves the language generated by the original CFG, i.e., any CFG can be converted to an equivalent CFG in CNF without changing the set of sentences it generates.
- The disadvantages of CNF are:
  - It may increase the number of non-terminal symbols and rules in the grammar, making it less readable and intuitive.
  - It may lose some information about the original structure and hierarchy of the grammar, making it harder to interpret and manipulate.
- The steps to convert a CFG to CNF are:
  - Eliminate the start symbol from the right-hand side of any rule, by introducing a new start symbol S' and adding the rule S' -> S.
  - Eliminate the rules with ε on the right-hand side, except for S -> ε, by replacing each occurrence of a nullable non-terminal symbol with an alternative derivation that does not include it.
  - Eliminate the rules with a single non-terminal symbol on the right-hand side, by replacing each occurrence of a unit production with an equivalent derivation that does not include it.
  - Eliminate the rules with more than two non-terminal symbols on the right-hand side, by introducing new non-terminal symbols and breaking down the long production into shorter ones.
  - Eliminate the rules with a mix of terminal and non-terminal symbols on the right-hand side, by introducing new non-terminal symbols and replacing each terminal symbol with a production that generates it.



### Dependency Grammar

- Dependency grammar is a descriptive and theoretical tradition in linguistics that can be traced back to antiquity.
- It has long been influential in the European linguistics tradition and has more recently become a mainstream approach to representing syntactic and semantic structure in natural language processing.
- Dependency grammar states that words of a sentence are dependent upon other words of the sentence .
- Dependency grammar is based on the concept that there is a direct link between every linguistic unit of a sentence.
- The links between words are called dependencies, and they are represented by directed edges in a dependency tree.
- The word that depends on another word is called the dependent, and the word that the dependent depends on is called the head.
- The head of a sentence is usually the main verb, and the dependents are the words that modify or complement the verb.
- The dependencies can be labeled with the type of syntactic or semantic relation that holds between the head and the dependent, such as subject, object, modifier, etc.
- Dependency grammar can capture the hierarchical and linear structure of a sentence, as well as the functional and thematic roles of the words .
- Dependency grammar can also account for the word order variations and the syntactic phenomena that are common in natural languages, such as coordination, ellipsis, anaphora, etc .
- Dependency grammar is often contrasted with phrase structure grammar, which is another approach to representing syntactic structure in natural language processing .
- Phrase structure grammar states that words of a sentence are grouped into phrases or constituents, and the phrases are recursively combined to form larger phrases or sentences .
- Phrase structure grammar is based on the concept that there is a hierarchical structure of phrases that can be represented by a tree diagram .
- The phrases are labeled with the category of the words that they contain, such as noun phrase, verb phrase, etc .
- Phrase structure grammar can capture the constituent structure and the category information of a sentence, but it may not reflect the semantic relations and the word order variations that are present in natural languages .
- Dependency grammar and phrase structure grammar are not mutually exclusive, and they can be combined or converted to each other in some cases .
- Dependency grammar and phrase structure grammar have different advantages and disadvantages, and they can be used for different purposes and applications in natural language processing .



### Syntactic Parsing

- Syntactic parsing is the process of analyzing the strings of symbols in natural language conforming to the rules of formal grammar.
- Syntactic parsing assigns a semantic structure to text, such as a constituent or dependency tree, that represents the syntactic relations between words and phrases .
- Syntactic parsing is one of the important tasks in natural language processing, and has been a subject of research since the mid-20th century with the advent of computers.
- Syntactic parsing is useful for downstream tasks such as semantic parsing, relation extraction, and machine translation .
- Syntactic parsing can be performed using different theories of grammar, such as context-free grammar, dependency grammar, lexical-functional grammar, etc.
- Syntactic parsing can be performed using different methods, such as rule-based, statistical, neural, or unsupervised .
- Syntactic parsing can be evaluated using different metrics, such as precision, recall, F1-score, or tree edit distance .
- Syntactic parsing can be challenging due to the ambiguity, complexity, and variability of natural language .



### Ambiguity

- Ambiguity is the property of a sentence or phrase that can have more than one meaning or interpretation.
- Ambiguity can arise at different levels of language processing, such as lexical, syntactic, semantic, pragmatic, or discourse.
- Ambiguity can cause problems for natural language processing systems, as they may not be able to resolve the intended meaning of the input or output.
- Ambiguity can also be a source of creativity and humor in natural language, as it allows for multiple interpretations and associations.

#### Lexical ambiguity

- Lexical ambiguity occurs when a word or phrase has more than one sense or meaning in a given context.
- For example, the word "bank" can mean a financial institution, a river shore, or a verb meaning to tilt or turn.
- Lexical ambiguity can be resolved by using context clues, word sense disambiguation techniques, or external knowledge sources.

#### Syntactic ambiguity

- Syntactic ambiguity occurs when a sentence or phrase has more than one possible syntactic structure or parse tree.
- For example, the sentence "I saw the man with the telescope" can have two different parse trees, depending on whether "with the telescope" modifies "saw" or "man".
- Syntactic ambiguity can be resolved by using syntactic rules, grammatical constraints, or probabilistic models.

#### Semantic ambiguity

- Semantic ambiguity occurs when a sentence or phrase has more than one possible meaning or interpretation at the level of meaning representation or logic.
- For example, the sentence "He visited his uncle's house" can have two different meanings, depending on whether "his" refers to the subject or the uncle.
- Semantic ambiguity can be resolved by using semantic rules, world knowledge, or common sense reasoning.

#### Pragmatic ambiguity

- Pragmatic ambiguity occurs when a sentence or phrase has more than one possible meaning or interpretation at the level of speech acts or communicative intentions.
- For example, the sentence "Can you pass the salt?" can be interpreted as a question, a request, or a command, depending on the tone, context, and relationship of the speaker and the hearer.
- Pragmatic ambiguity can be resolved by using pragmatic rules, discourse cues, or conversational implicatures.

#### Discourse ambiguity

- Discourse ambiguity occurs when a sentence or phrase has more than one possible meaning or interpretation at the level of discourse structure or coherence.
- For example, the sentence "She left him because he was unhappy" can have two different meanings, depending on whether "she" or "he" is the main topic of the discourse.
- Discourse ambiguity can be resolved by using discourse rules, anaphora resolution, or rhetorical relations.



### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- The idea is to store the results of subproblems (i.e., smaller constituents) in a table or chart and reuse them to find larger constituents, avoiding redundant computations.
- The most common dynamic programming parsing algorithm is the Cocke-Kasami-Younger (CKY) algorithm, which is a bottom-up, chart-based parser that works as follows:
  - Initialize an n x n chart, where n is the number of words in the sentence, and each cell (i,j) corresponds to the span from word i to word j (inclusive).
  - For each word i, fill the cell (i,i) with the non-terminal symbols that can generate that word according to the grammar rules.
  - For each span length l from 2 to n, and for each start position i from 1 to n-l+1, fill the cell (i,i+l-1) with the non-terminal symbols that can generate the span from word i to word i+l-1 by combining two smaller spans according to the grammar rules. For example, if A -> BC is a grammar rule, and B is in cell (i,k) and C is in cell (k+1,j), then add A to cell (i,j).
  - The chart is filled in a diagonal fashion, starting from the main diagonal and moving upwards and to the right.
  - The final parse tree can be obtained by tracing back the non-terminal symbols from the top-right cell (1,n), which corresponds to the whole sentence. If the start symbol of the grammar is in that cell, then the sentence is accepted by the grammar; otherwise, it is rejected.
- The complexity of the CKY algorithm is O(n^3|G|), where n is the length of the sentence and |G| is the size of the grammar. This is because there are O(n^2) cells to fill, each cell takes O(n) time to check all possible splits, and each split takes O(|G|) time to check all possible rules.
- Dynamic programming parsing can handle ambiguity and produce multiple parse trees for a sentence, but it cannot handle context-sensitive or ungrammatical sentences. It also requires the grammar to be in CNF, which may not be natural or intuitive for some languages.



### Shallow parsing

- Shallow parsing (also called chunking or light parsing) is an analysis of a sentence which first identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and then links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.).
- Shallow parsing is different from deep parsing, which aims to produce a complete and detailed parse tree that represents the syntactic structure of a sentence according to a formal grammar.
- Shallow parsing is useful for many natural language processing applications that do not require full syntactic analysis, such as information extraction, named entity recognition, sentiment analysis, question answering, etc.
- Shallow parsing can be seen as a set of cascaded classification problems with separate classifiers for tagging, chunk boundary detection, chunk labeling, relation finding, etc.
- Shallow parsing can also be used to assign semantic roles to words or phrases in a sentence, such as that of an agent, goal, or result. This is also called semantic role labeling or slot-filling.
- Shallow parsing can be performed using various methods, such as rule-based systems, statistical models, machine learning algorithms, etc. Some popular tools for shallow parsing are NLTK, spaCy, Stanford CoreNLP, etc.



### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns a probability to each of its production rules.
- The probability of a rule is the conditional probability of expanding the left-hand side nonterminal into the right-hand side symbols, given the left-hand side nonterminal.
- The probability of a parse tree is the product of the probabilities of the rules used to generate it.
- The probability of a sentence is the sum of the probabilities of all possible parse trees for that sentence.
- PCFGs can be used to model natural languages and perform syntactic analysis, such as parsing and disambiguation.
- PCFGs can be learned from a corpus of annotated sentences, such as the Penn Treebank, by counting the occurrences of each rule and normalizing by the occurrences of each nonterminal.
- PCFGs can be parsed using algorithms such as the CKY algorithm, which is a bottom-up dynamic programming algorithm that fills a chart with the most probable parses for each span of the sentence.
- PCFGs have some limitations, such as the independence assumption, which ignores the dependencies between different parts of the sentence, and the sparsity problem, which results from the lack of data for some rare rules or words.
- PCFGs can be improved by adding more features, such as lexicalization, subcategorization, and annotation, which can capture more syntactic and semantic information and reduce ambiguity.



### Probabilistic CYK

- The probabilistic CYK algorithm is an extension of the CYK algorithm for parsing sentences with probabilistic context-free grammars (PCFGs).
- PCFGs are context-free grammars that assign probabilities to each production rule, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm finds the most likely parse tree for a given sentence according to the production probabilities, using dynamic programming to avoid redundant computations.
- The algorithm works as follows:

  - Initialize a table T of size n x n, where n is the length of the input sentence. Each cell T[i,j] will store a set of nonterminals that can generate the substring from i to j, along with their probabilities.
  - For each word in the sentence, fill the diagonal cells of the table with the nonterminals that can directly produce the word, and their probabilities. For example, if the word is "dog" and the grammar has the rule N -> dog [0.5], then T[i,i] = {N: 0.5}.
  - For each substring of length 2 or more, fill the upper triangular cells of the table by considering every possible split point k between i and j, and every possible pair of nonterminals A and B that can generate T[i,k] and T[k+1,j], respectively. For each such pair, check if there is a rule C -> A B [p] in the grammar, and if so, add C to T[i,j] with the probability p * T[i,k].A * T[k+1,j].B. For example, if T[i,k] = {N: 0.5, V: 0.2} and T[k+1,j] = {N: 0.3, D: 0.1}, and the grammar has the rule S -> N V [0.4], then T[i,j] = {S: 0.04}.
  - The most likely parse tree for the sentence is the one that has the highest probability among the nonterminals in T[0,n-1]. This can be found by backtracking from the table, starting from the nonterminal with the highest probability in T[0,n-1], and recursively choosing the most probable split point and nonterminals at each step. For example, if T[0,n-1] = {S: 0.04, NP: 0.02}, then the most likely parse tree is the one that starts with S and has the highest probability among the possible splits and nonterminals for S.



### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule, such that the sum of the probabilities of all rules with the same left-hand side is 1.
- PCFGs can be used to model the likelihood of different syntactic structures for a given sentence, and to select the most probable parse tree among the possible ones.
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the non-terminal symbols, such that each non-terminal is associated with a head word that determines its subcategorization and selectional preferences.
- L-PCFGs can capture more fine-grained syntactic distinctions and dependencies than PCFGs, and can improve the accuracy of parsing.
- Neural bi-lexicalized PCFGs (NBL-PCFGs) are a recent approach that uses neural networks to learn the parameters of L-PCFGs from data, and to encode the bi-directional context of each word in the sentence.
- NBL-PCFGs can achieve state-of-the-art results on unsupervised grammar induction, and can handle long-distance dependencies and rare words better than previous methods.



### Feature structures for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Natural Language Processing (NLP) is a branch of artificial intelligence that attempts to bridge the gap between what a machine recognizes as input and the human language.
- NLP combines artificial intelligence, computational linguistics and machine learning to enable computers and humans to communicate seamlessly.
- NLP can be divided into three main tasks: speech recognition, natural language understanding and natural language generation.
- Speech recognition is the translation of spoken language into text.
- Natural language understanding (NLU) is the computer's ability to understand what we say.
- Natural language generation (NLG) is the generation of natural language by a computer.
- Syntactic analysis is a subtask of NLU that deals with the structure and rules of language.
- Syntactic analysis involves parsing sentences into their constituent parts and assigning grammatical roles and relations to them.
- Syntactic analysis can be done using different types of grammars, such as context-free grammars, dependency grammars and feature-based grammars.
- Feature-based grammars are a type of grammars that use features to describe the properties and constraints of linguistic units, such as words, phrases and sentences.
- Features are attributes that have values, such as number, gender, case, tense, mood, etc.
- Feature structures are representations of features and their values, usually in the form of attribute-value matrices (AVMs).
- Feature structures can be used to encode various kinds of linguistic information, such as morphology, syntax, semantics and pragmatics.
- Feature structures can also be used to model agreement, subcategorization, selectional restrictions, anaphora resolution and other phenomena that require complex interactions between linguistic units.
- Feature structures can be manipulated using the operation of unification, which allows us to combine the information contained in two different feature structures.
- Unification is the process of finding a feature structure that is compatible with both input feature structures, or failing if there is no such feature structure.
- Unification can be used to check the well-formedness of sentences, to resolve ambiguities, to infer missing information and to generate output sentences.
- Feature-based grammars can be implemented using various formalisms, such as Head-Driven Phrase Structure Grammar (HPSG), Lexical Functional Grammar (LFG) and Tree Adjoining Grammar (TAG).
- Feature-based grammars can be processed using various tools, such as the Natural Language Toolkit (NLTK), which provides a module for building and manipulating feature structures in Python.



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
- For example, the unification of the feature structures `[A: 1 B: 2]` and `[A: 1 C: 3]` is `[A: 1 B: 2 C: 3]`.
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- Unification can also be used to check the compatibility of two feature structures. If the unification of two feature structures is undefined, it means that they are incompatible or contradictory.
- For example, the unification of the feature structures `[A: 1 B: 2]` and `[A: 2 C: 3]` is undefined, because they have different values for the attribute `A`.
- Unification is widely used in natural language processing (NLP) for various tasks, such as parsing, generation, grammar formalisms, and semantic interpretation.
- Unification can be implemented using different methods, such as binding lists, feature matrices, feature trees, or feature graphs.
- Unification can also be extended to E-unification, which allows the use of equations or constraints on the values of the attributes .
- E-unification of feature structures can be useful for handling linguistic phenomena such as agreement, anaphora, ellipsis, and lexical rules.



## Unit 4 - SEMANTICS AND PRAGMATICS

- Semantics is the study of meaning in language, especially the relationship between words and sentences and the situations they refer to.
- Pragmatics is the study of how language is used in context, especially the relationship between speakers and hearers and the assumptions they make about each other.
- Some of the main topics in semantics and pragmatics are:
  - Reference and sense: how words and phrases relate to the entities and concepts they denote or imply.
  - Truth conditions: how the meaning of a sentence depends on the facts of the world and the possible situations it describes.
  - Entailment and presupposition: how the meaning of a sentence affects or depends on the meaning of other sentences or the background knowledge of the speakers and hearers.
  - Implicature and inference: how speakers and hearers use language to convey or derive additional meanings beyond the literal or explicit ones.
  - Speech acts and illocutionary force: how speakers and hearers use language to perform actions and express intentions, such as asking, promising, commanding, etc.
  - Politeness and face: how speakers and hearers use language to show respect, deference, solidarity, or distance, and to maintain their self-image and social relationships.
  - Discourse and conversation: how speakers and hearers use language to structure and manage their interactions, such as taking turns, signaling topics, making repairs, etc.



### Requirements for representation for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- The representation of meaning in natural language processing (NLP) requires a formal system that can capture the semantic and pragmatic aspects of natural language utterances.
- Semantic representation deals with the literal meaning of words, phrases, and sentences, and how they are combined to form complex meanings. Pragmatic representation deals with the use of context, world knowledge, and speaker intentions to infer the intended meaning of utterances.
- Some of the requirements for representation are:

  - The representation should be able to handle ambiguity, which is a common feature of natural language. Ambiguity can arise at different levels of linguistic analysis, such as lexical, syntactic, semantic, and pragmatic. For example, the word "bank" can have different meanings depending on the context and the domain of discourse.
  - The representation should be able to handle variability, which is another common feature of natural language. Variability refers to the fact that natural language expressions can have different forms and structures, but convey the same meaning. For example, the sentences "She gave him a book" and "He received a book from her" have the same meaning, but different syntactic structures.
  - The representation should be able to handle inference, which is a crucial aspect of natural language understanding. Inference refers to the process of deriving new information from existing information, using logical rules and world knowledge. For example, from the sentence "She is a doctor", one can infer that she has a medical degree, she works in a hospital, she can treat patients, etc.
  - The representation should be able to handle pragmatics, which is the study of meaning in context. Pragmatics involves the use of real-world knowledge and speaker intentions to interpret natural language utterances. For example, the sentence "How are you?" can have different meanings depending on the situation and the relationship between the speaker and the hearer.

- Some of the common representation schemes used in NLP are:

  - Semantic networks, which are graphs that represent concepts and their relations using nodes and links. For example, a semantic network for the word "bank" can have nodes for different senses of the word, such as financial institution, river bank, blood bank, etc., and links for their relations, such as is-a, part-of, has-a, etc.
  - Frames, which are data structures that represent concepts and their attributes using slots and fillers. For example, a frame for the concept of a book can have slots for its title, author, genre, publisher, etc., and fillers for their values, such as "Harry Potter", "J.K. Rowling", "fantasy", "Bloomsbury", etc.
  - Conceptual dependency, which is a representation scheme that uses a set of primitive concepts and relations to capture the meaning of natural language sentences. For example, the sentence "She gave him a book" can be represented as PTRANS (ACTOR: SHE, OBJECT: BOOK, TO: HIM), where PTRANS is a primitive relation that stands for physical transfer.
  - Scripts, which are data structures that represent stereotypical sequences of events and actions that occur in a given situation. For example, a script for the situation of going to a restaurant can have slots for the roles of the participants, such as customer, waiter, chef, etc., and the actions they perform, such as ordering, serving, eating, paying, etc.



### First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL consists of symbols for constants, variables, predicates, functions, logical connectives, and quantifiers.
- Constants represent specific objects or individuals, such as John, Mary, 2, or red.
- Variables range over a domain of possible objects or individuals, such as x, y, or z.
- Predicates represent properties or relations of objects or individuals, such as Animal(x), Larger(x, y), or Loves(x, y).
- Functions represent mappings from objects or individuals to other objects or individuals, such as Father(x), SquareRoot(x), or Add(x, y).
- Logical connectives represent the truth-functional operations of negation, conjunction, disjunction, implication, and equivalence, such as ¬, ∧, ∨, →, and ↔.
- Quantifiers represent the scope of variables over a domain of possible objects or individuals, such as ∀ (universal quantifier) and ∃ (existential quantifier).

- FOL formulas are constructed from symbols using the following rules:
  - A constant or a variable is a term.
  - If f is an n-ary function symbol and t1, ..., tn are terms, then f(t1, ..., tn) is a term.
  - If P is an n-ary predicate symbol and t1, ..., tn are terms, then P(t1, ..., tn) is an atomic formula.
  - If φ and ψ are formulas, then ¬φ, (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), and (φ ↔ ψ) are formulas.
  - If φ is a formula and x is a variable, then ∀xφ and ∃xφ are formulas.

- FOL formulas can be interpreted in a model, which consists of a domain of objects or individuals and an interpretation function that assigns a denotation to each symbol.
- The denotation of a constant is an object or individual in the domain.
- The denotation of a variable is determined by an assignment function that maps variables to objects or individuals in the domain.
- The denotation of a predicate is a set of n-tuples of objects or individuals in the domain that satisfy the predicate.
- The denotation of a function is a mapping from n-tuples of objects or individuals in the domain to other objects or individuals in the domain.
- The denotation of a logical connective is determined by the truth tables of the corresponding operations.
- The denotation of a quantifier is determined by the range of the variable over the domain.

- FOL formulas can be evaluated for truth or falsity in a model, given an assignment function for the variables.
- The truth or falsity of a formula depends on the denotations of the symbols and the logical rules of inference.
- FOL formulas can be logically equivalent, meaning that they have the same truth value in every model and assignment.
- FOL formulas can be logically entailed, meaning that the truth of one formula follows from the truth of another formula in every model and assignment.
- FOL formulas can be logically consistent, meaning that there is at least one model and assignment where they are both true.

- FOL is widely used in natural language processing (NLP) for representing and reasoning about the meaning of natural language sentences and texts.
- FOL can capture many aspects of natural language semantics, such as quantification, negation, implication, and equivalence.
- FOL can also support various NLP tasks, such as semantic parsing, question answering, information extraction, and natural language inference.



### Description Logics for Natural Language Processing

- Description logics (DLs) are a family of logic-based knowledge representation languages that allow for the formalization of concepts, roles, and individuals in a domain of interest .
- DLs can be used for various applications, such as ontology engineering, semantic web, and natural language processing (NLP) .
- In NLP, DLs can be used to represent the meaning of natural language expressions, such as sentences, phrases, or words, in a precise and unambiguous way .
- DLs can also be used to perform reasoning tasks on natural language expressions, such as entailment, consistency, subsumption, and satisfiability .
- DLs are based on the notions of concepts, roles, and individuals, which correspond to the linguistic notions of nouns, verbs, and proper names, respectively .
- Concepts are unary predicates that denote sets of individuals, such as `Human`, `Dog`, or `Red` .
- Roles are binary predicates that denote relations between individuals, such as `hasPet`, `loves`, or `isColorOf` .
- Individuals are constants that denote specific objects in the domain, such as `Alice`, `Fido`, or `the sky` .
- DLs allow for the construction of complex concepts and roles from atomic ones, using logical operators, such as conjunction, disjunction, negation, quantification, and modalities .
- For example, the concept `Dog and (hasPet some Cat)` denotes the set of dogs that have at least one cat as a pet .
- The role `loves o loves^-` denotes the relation of mutual love between individuals, where `o` is the composition operator and `^-` is the inverse operator .
- DLs also allow for the definition of axioms, which are statements that constrain the interpretation of concepts and roles .
- For example, the axiom `Human subClassOf Animal` states that every human is an animal .
- The axiom `hasPet domain Human` states that only humans can have pets .
- DLs have different expressive power and computational complexity, depending on the operators and axioms that they allow .
- For example, the DL `ALC` allows for conjunction, disjunction, negation, universal and existential quantification, and subsumption axioms, and has a decidable and polynomial-time satisfiability problem .
- The DL `S5` extends `ALC` with modal operators, and has a decidable and exponential-time satisfiability problem .
- The DL `SHOIN` extends `ALC` with transitive roles, inverse roles, role hierarchies, nominals, and number restrictions, and is the basis of the web ontology language `OWL-DL` .
- DLs can be used to model natural language semantics in various ways, such as:
  - Using concepts and roles to represent the meaning of words and phrases, and using axioms to capture their lexical and ontological relations .
  - Using individuals and roles to represent the meaning of sentences and discourse, and using axioms to capture their syntactic and pragmatic relations .
  - Using modal operators to represent the meaning of modal verbs and adverbs, and using axioms to capture their logical and epistemic relations .
  - Using number restrictions to represent the meaning of quantifiers and numerals, and using axioms to capture their semantic and pragmatic relations .
- DLs can also be used to perform various reasoning tasks on natural language expressions, such as:
  - Checking the consistency of a set of sentences or a discourse, by checking the satisfiability of the corresponding DL concepts or individuals .
  - Checking the entailment of a sentence or a discourse by another, by checking the subsumption of the corresponding DL



### Syntax-Driven Semantic Analysis

- Syntax-driven semantic analysis is a method of assigning meaning representations to natural language sentences based solely on static knowledge from the lexicon and the grammar .
- The meaning representations are usually logical forms that can be used for further reasoning or inference .
- Syntax-driven semantic analysis can be implemented by augmenting a context-free grammar with semantic rules that specify how to compose the meanings of the constituents of a sentence .
- The semantic rules can be based on lambda calculus, a formal system for expressing functions and applying them to arguments .
- Syntax-driven semantic analysis can be applied to various natural language processing tasks, such as constructing use case diagrams from requirements, analyzing privacy policies, or disambiguating requirements for ontology construction.
- Syntax-driven semantic analysis can provide a representation that is both context independent and inference free, but it may also face challenges such as ambiguity, vagueness, or incompleteness of natural language.



### Semantic attachments for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Semantic analysis is the process of understanding the meaning of natural language texts  .
- Semantic analysis involves identifying and representing the semantic relations between words, phrases, sentences, and documents   .
- Semantic analysis can help natural language processing applications such as chatbots, search engines, text summarization, sentiment analysis, etc. to extract valuable data from unstructured information and provide relevant and accurate responses  .
- Semantic analysis can be performed at different levels of granularity, such as lexical, syntactic, and pragmatic  .
- Lexical semantics deals with the meaning of individual words and their relations, such as synonyms, antonyms, hyponyms, hypernyms, etc .
- Syntactic semantics deals with the meaning of phrases and sentences based on their structure and grammar, such as subject, predicate, modifiers, etc .
- Pragmatic semantics deals with the meaning of texts in relation to the context, such as speaker, listener, intention, situation, etc .
- Semantic analysis can be performed using different methods and techniques, such as rule-based, statistical, neural, or hybrid approaches  .
- Rule-based semantic analysis uses predefined rules and dictionaries to assign meaning to texts based on their syntax and logic .
- Statistical semantic analysis uses probabilistic models and machine learning algorithms to assign meaning to texts based on their frequency and distribution in large corpora .
- Neural semantic analysis uses deep learning models and neural networks to assign meaning to texts based on their vector representations and embeddings .
- Hybrid semantic analysis uses a combination of rule-based, statistical, and neural methods to leverage the strengths and overcome the limitations of each approach .
- Semantic attachments are a way of representing the meaning of natural language expressions using formal languages, such as logic, algebra, or programming languages .
- Semantic attachments can be used to link natural language expressions to their corresponding representations in a knowledge base, a database, or a software system .
- Semantic attachments can be used to perform various tasks, such as query answering, inference, reasoning, translation, generation, etc .
- Semantic attachments can be defined using different methods, such as manual annotation, automatic extraction, or learning from data .
- Semantic attachments can be evaluated using different criteria, such as accuracy, completeness, consistency, and efficiency .



### Word Senses

- A word sense is the meaning of a word in a given context or usage.
- Words can have multiple senses, depending on how they are used in different situations or domains.
- For example, the word "bank" can have different senses, such as a financial institution, a river shore, or a verb meaning to tilt or turn.
- Word senses are often represented by sense definitions or glosses in dictionaries or lexical resources.
- Word senses can also be associated with sense identifiers or labels, such as WordNet synsets, BabelNet IDs, or Wikipedia titles.
- Word senses are important for natural language processing (NLP) tasks, such as word sense disambiguation (WSD), semantic similarity, sentiment analysis, information extraction, and machine translation.
- Word sense disambiguation (WSD) is the task of assigning the correct sense to a word in a given context, by using linguistic or external knowledge sources.
- WSD can help to resolve lexical ambiguity, which is one of the main challenges in NLP.
- WSD can also improve the performance and accuracy of downstream NLP applications that rely on semantic information.
- WSD methods can be classified into two main categories: knowledge-based and data-driven.
- Knowledge-based methods use lexical resources, such as dictionaries, thesauri, or ontologies, to compare the word sense definitions or relations with the context words or features.
- Data-driven methods use machine learning techniques, such as supervised, unsupervised, or semi-supervised learning, to train models or classifiers on annotated or unannotated corpora, and use them to predict the word sense labels or embeddings.
- WSD evaluation can be done by using intrinsic or extrinsic measures.
- Intrinsic measures compare the WSD output with a gold standard or reference annotation, and compute metrics such as accuracy, precision, recall, or F1-score.
- Extrinsic measures assess the impact of WSD on a downstream NLP task, such as information retrieval, text summarization, or machine translation, and compute metrics such as BLEU, ROUGE, or NDCG.



### Relations between Senses

- In natural language processing (NLP), word sense disambiguation (WSD) is the task of determining the meaning of a word in a given context, based on its possible senses .
- WSD is important for NLP applications such as machine translation, information retrieval, text summarization, question answering, and sentiment analysis, as the same word can have different meanings and implications in different situations .
- For example, the word "bank" can mean a financial institution, a river shore, or a verb meaning to tilt or incline. Depending on the context, the word "bank" can have different translations, synonyms, antonyms, and associations.
- WSD can be performed using various methods, such as rule-based, knowledge-based, supervised, semi-supervised, or unsupervised approaches. Each method has its own advantages and disadvantages, such as accuracy, scalability, coverage, and availability of resources.
- WSD is closely related to other linguistic phenomena in semantics and pragmatics, such as lexical ambiguity, polysemy, homonymy, synonymy, antonymy, hyponymy, hypernymy, meronymy, holonymy, metonymy, and metaphor .
- Lexical ambiguity is the property of a word or phrase that can have more than one meaning or interpretation . Lexical ambiguity can be classified into syntactic ambiguity and semantic ambiguity .
- Syntactic ambiguity is when a word or phrase can have more than one syntactic role or function in a sentence, such as subject, object, modifier, etc . For example, the sentence "I saw the man with the telescope" can mean either that I used a telescope to see the man, or that the man had a telescope with him .
- Semantic ambiguity is when a word or phrase can have more than one meaning or sense in a given context, such as the word "bank" mentioned above . Semantic ambiguity can be further divided into polysemy, homonymy, synonymy, and antonymy .
- Polysemy is when a word has multiple related meanings or senses that share a common origin or concept . For example, the word "eye" can mean the organ of vision, the center of a storm, or a spy .
- Homonymy is when a word has multiple unrelated meanings or senses that do not share a common origin or concept . For example, the word "bat" can mean a flying mammal, a wooden club, or a verb meaning to strike .
- Synonymy is when two or more words have the same or similar meaning or sense in a given context . For example, the words "big" and "large" are synonyms .
- Antonymy is when two or more words have the opposite or contrasting meaning or sense in a given context . For example, the words "hot" and "cold" are antonyms .
- Hyponymy is when a word is a specific instance or subtype of a more general word . For example, the word "rose" is a hyponym of the word "flower" .
- Hypernymy is when a word is a more general or superordinate word that includes more specific words as its instances or subtypes . For example, the word "flower" is a hypernym of the word "rose" .
- Meronymy is when a word is a part or component of a larger whole . For example, the word "petal" is a meronym of the word "flower" .
- Holonymy is when a word is a larger whole that includes smaller parts or components . For example, the word "flower" is a hol



### Thematic Roles

- Thematic roles are the semantic roles that arguments of a verb play in a sentence. They describe the relationship between the verb and its arguments, such as who did what to whom, how, when, where, why, etc.
- Thematic roles are important for natural language processing because they help to identify the meaning and structure of a sentence, and to resolve ambiguities and anaphora.
- Thematic roles are also called theta roles, case roles, or semantic roles. Different theories and frameworks may use different names and definitions for thematic roles, but some of the most common ones are:

  - **Agent**: The entity that intentionally performs the action of the verb. For example, in "John opened the door", John is the agent.
  - **Patient**: The entity that undergoes the action of the verb or is affected by it. For example, in "John opened the door", the door is the patient.
  - **Experiencer**: The entity that perceives or feels something expressed by the verb. For example, in "John saw the movie", John is the experiencer.
  - **Theme**: The entity that is involved in or moved by the action of the verb. For example, in "John gave Mary a book", the book is the theme.
  - **Instrument**: The entity that is used to perform the action of the verb. For example, in "John cut the cake with a knife", the knife is the instrument.
  - **Beneficiary**: The entity that benefits from or is intended to benefit from the action of the verb. For example, in "John baked a cake for Mary", Mary is the beneficiary.
  - **Source**: The entity from which something originates or moves away. For example, in "John came from Paris", Paris is the source.
  - **Goal**: The entity to which something moves or is directed. For example, in "John went to London", London is the goal.
  - **Location**: The entity where something is or takes place. For example, in "John lives in New York", New York is the location.
  - **Manner**: The entity that describes how something is done or happens. For example, in "John ran quickly", quickly is the manner.
  - **Cause**: The entity that causes or triggers the action of the verb. For example, in "John sneezed because of the dust", the dust is the cause.
  - **Purpose**: The entity that expresses the reason or intention for the action of the verb. For example, in "John studied hard to pass the exam", to pass the exam is the purpose.

- Thematic roles can be assigned by different methods, such as syntactic rules, semantic frames, or machine learning algorithms. The task of identifying and labeling thematic roles in a sentence is called semantic role labeling.



### Selectional restrictions

Selectional restrictions are semantic constraints that limit the possible combinations of words in a sentence. They account for the implausibility or ungrammaticality of sentences such as:

- Colorless green ideas slept furiously.
- The chair ate the sandwich.
- She kicked the truth.

Selectional restrictions are based on the semantic features or types of words, such as animacy, concreteness, countability, etc. For example, the verb eat requires an animate subject and a concrete object, while the verb kick requires a physical subject and object.

Selectional restrictions can be used in natural language processing for various purposes, such as:

- Disambiguation: resolving the meaning of words that have multiple senses, based on the semantic compatibility with other words in the sentence. For example, the word bank can mean a financial institution or a river shore, but the sentence He robbed the bank implies the former sense, while the sentence He walked along the bank implies the latter sense.
- Pronoun resolution: identifying the referent of a pronoun, based on the semantic agreement with the antecedent. For example, the pronoun he in the sentence He loves his dog can refer to any male person, but the pronoun it in the sentence He loves it can only refer to a non-human entity, such as a dog, a car, or a book.
- Lexical insertion: choosing the appropriate word to fill a slot in a sentence, based on the semantic fit with the surrounding words. For example, the word book in the sentence She read a book is a suitable choice, but the word idea in the sentence She read an idea is not.

Selectional restrictions can be represented in different ways, such as:

- Feature structures: a set of attribute-value pairs that specify the semantic properties of a word. For example, the word dog can have the feature structure [+animate, +concrete, +count, +mammal], while the word idea can have the feature structure [-animate, -concrete, +count, -mammal].
- Types and categories: a system of hierarchical classes that define the semantic domain of a word. For example, the word dog can belong to the type animal, which is a subtype of the type entity, while the word idea can belong to the type proposition, which is a subtype of the type abstract.
- Distributional semantics: a vector space model that represents the meaning of a word as a point in a high-dimensional space, based on the co-occurrence patterns with other words in a large corpus. For example, the word dog can have a vector that is close to the vectors of other animals, but far from the vectors of abstract concepts.

Selectional restrictions can be violated for various reasons, such as:

- Metaphor: a figure of speech that uses a word or phrase in a non-literal sense, based on some similarity or analogy with another domain. For example, the sentence She kicked the truth is a metaphor that compares the act of revealing the truth to the act of kicking something.
- Humor: a form of expression that intends to amuse or provoke laughter, often by creating incongruity or absurdity. For example, the sentence The chair ate the sandwich is a joke that violates the expectation of the verb eat and the noun chair.
- Creativity: a process of generating novel and useful ideas, often by combining existing concepts in new ways. For example, the sentence Colorless green ideas slept furiously is a creative sentence that was coined by Noam Chomsky to illustrate the distinction between syntax and semantics.



### Word Sense Disambiguation

- Word sense disambiguation (WSD) is the problem of determining which "sense" (meaning) of a word is activated by the use of the word in a particular context, a process which appears to be largely unconscious in people.
- WSD is a subfield of natural language processing (NLP) that deals with identifying the intended meaning of a word in a given context. It is the process of selecting the correct sense of a word from a set of possible senses, based on the context in which the word appears.
- WSD is an important research problem in NLP because lexical ambiguity, syntactic or semantic, is one of the very first problems that any NLP system faces. Lexical ambiguity occurs when a word has more than one possible meaning, and the correct meaning depends on the context.
- For example, the word "bank" can have different meanings, such as a financial institution, a river shore, or a verb meaning to tilt or turn. To understand the meaning of a sentence containing the word "bank", we need to disambiguate the word based on the surrounding words and the overall topic of the text.
- WSD can be useful for many NLP applications, such as machine translation, information retrieval, text summarization, sentiment analysis, question answering, and more. By resolving the ambiguity of words, these applications can improve their performance and accuracy.
- WSD can be performed using different methods, such as rule-based, knowledge-based, supervised, semi-supervised, or unsupervised. Each method has its own advantages and disadvantages, depending on the availability of resources, the quality of data, the complexity of the task, and the evaluation criteria.
- WSD also faces some challenges, such as the lack of standard sense inventories, the difficulty of defining word senses, the sparsity of annotated data, the domain and genre specificity of word senses, and the evaluation of WSD systems.
- WSD is an active and evolving research area in NLP, with many open problems and opportunities for future work. Some of the current research directions include cross-lingual and multilingual WSD, contextualized word embeddings, neural network models, and explainable WSD.



### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the common supervised WSD algorithms are:
  - Naive Bayes: This is a probabilistic classifier that assumes that the features are conditionally independent given the sense. It estimates the probability of a sense given the features using the Bayes' rule and chooses the sense with the highest probability.
  - Decision Trees: This is a non-parametric classifier that builds a tree-like structure of rules based on the features. Each node in the tree represents a feature and each branch represents a possible value of the feature. The leaves of the tree are the senses. The classifier follows the path from the root to the leaf that matches the features of the input and assigns the corresponding sense.
  - Support Vector Machines (SVM): This is a linear classifier that tries to find a hyperplane that separates the features of different senses with the maximum margin. The classifier assigns the sense that corresponds to the side of the hyperplane where the input features lie.
  - Neural Networks: This is a non-linear classifier that consists of multiple layers of artificial neurons that can learn complex patterns from the features. The classifier uses a feed-forward network with an input layer, one or more hidden layers, and an output layer. The input layer receives the features, the hidden layers perform non-linear transformations, and the output layer produces the sense probabilities.
- Supervised WSD methods have the advantage of being able to learn from large amounts of data and achieve high accuracy on the same domain and genre as the training data. However, they also have some limitations, such as:
  - Data sparsity: The sense-annotated corpora are often limited in size, coverage, and diversity, which makes it difficult to train robust models that can generalize to unseen words, senses, and contexts .
  - Sense granularity: The sense inventory used for annotation may not match the level of detail required for the application. For example, WordNet senses are often too fine-grained and may not capture the relevant distinctions for a given task .
  - Domain adaptation: The performance of supervised WSD models may degrade when applied to a different domain or genre than the training data, due to the differences in vocabulary, style, and sense distribution .



### Dictionary & Thesaurus for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- A **dictionary** is a collection of words and their meanings, pronunciations, usage examples, and other information. A dictionary can be used to look up the meaning of a word, to check its spelling, or to find synonyms or antonyms.
- A **thesaurus** is a specialized dictionary that stores synonyms and antonyms of selected words in a language. A thesaurus can be used to find alternative words with similar or opposite meanings, to enrich the vocabulary, or to avoid repetition.
- In natural language processing (NLP), a dictionary and a thesaurus can be useful resources for various tasks, such as:
  - **Word sense disambiguation**: the process of identifying the correct meaning of a word in a given context, based on its definition, usage, and relation to other words.
  - **Text summarization**: the process of creating a concise and informative summary of a longer text, based on its main ideas, keywords, and salient points.
  - **Text generation**: the process of producing natural language text from a given input, such as a prompt, a query, or a data source, based on the rules, patterns, and style of the language.
  - **Text analysis**: the process of extracting information, insights, and knowledge from natural language text, such as sentiment, topics, entities, relations, and opinions.
- Some of the challenges and limitations of using a dictionary and a thesaurus in NLP are:
  - **Ambiguity**: words can have multiple meanings, senses, or usages, depending on the context, domain, or genre. A dictionary or a thesaurus may not be able to capture all the nuances and variations of a word, or to resolve the ambiguity automatically .
  - **Coverage**: words can be dynamic, evolving, or emerging, especially in informal or creative language. A dictionary or a thesaurus may not be able to include all the new words, slang, or neologisms, or to update their meanings and usage frequently.
  - **Granularity**: words can have different levels of specificity, generality, or abstraction, depending on the purpose, audience, or tone. A dictionary or a thesaurus may not be able to provide the optimal level of granularity for a given task, or to account for the preferences and expectations of the users.



### Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods can be applied to various natural language processing (NLP) tasks, such as part-of-speech tagging, named entity recognition, relation extraction, sentiment analysis, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., words, phrases, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., manually annotated examples, rules, patterns, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using similarity measures, classifiers, parsers, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more things can be found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Self-training: The model uses its own predictions on the unlabeled data to augment the labeled data and retrain itself.
  - Co-training: Two or more models use different views or features of the data to make predictions and exchange their confident predictions to augment the labeled data for each other.
- Bootstrapping methods can benefit from the following advantages :
  - They can reduce the cost and effort of manual annotation.
  - They can exploit the large amount of unlabeled data available for NLP tasks.
  - They can improve the performance and generalization of the model or the task.
- Bootstrapping methods can also face the following challenges :
  - They can suffer from semantic drift, which is the deviation of the learned things from the original seeds due to noise or ambiguity in the data.
  - They can be sensitive to the choice and quality of the seeds, which can affect the coverage and accuracy of the learned things.
  - They can be affected by the distribution and diversity of the unlabeled data, which can influence the reliability and confidence of the predictions.



### Word Similarity using Thesaurus and Distributional methods

- Word similarity is a measure of how closely related two words are in terms of their meaning, usage, or association.
- Word similarity can be computed using different methods, such as thesaurus-based methods and distributional methods.
- Thesaurus-based methods rely on manually curated lexical resources, such as WordNet, that group words into synonym sets (synsets) and define semantic relations (such as hypernymy, hyponymy, meronymy, etc.) between them.
- Distributional methods rely on statistical analysis of large corpora, such as the Google N-gram corpus, that capture the co-occurrence patterns of words in different contexts.
- Thesaurus-based methods have the advantage of being more precise and interpretable, but they have the disadvantage of being incomplete, inconsistent, and domain-specific.
- Distributional methods have the advantage of being more comprehensive and robust, but they have the disadvantage of being noisy, ambiguous, and context-dependent.
- Word similarity can be used for various natural language processing tasks, such as word sense disambiguation, information retrieval, text summarization, sentiment analysis, etc.



## Unit 5 - BASIC CONCEPTS of Speech Processing

Speech processing is the study of how humans produce, perceive, and understand speech, as well as how speech can be processed by machines. Speech processing has many applications, such as speech recognition, speech synthesis, speech enhancement, speech coding, speech translation, and speech emotion analysis.

Some of the basic concepts of speech processing are:

- Speech production: This is the process by which thoughts are translated into speech. This includes the selection of words, the organization of relevant grammatical forms, and then the articulation of the resulting sounds by the motor system using the vocal apparatus. Speech production involves three major levels of processing: conceptualization, formulation, and articulation. Some of the ideas that explain how speech production works are:
  - Speech is planned in advance.
  - The lexicon is organized both semantically and phonologically. That is by meaning, and by the sound of the words.
  - Morphologically complex words are assembled.
  - Affixes and functors behave differently from context words in slips of the tongue.
  - Speech errors reflect rule knowledge.
- Speech perception: This is the process by which the acoustic signals of speech are decoded and interpreted by the listener. Speech perception involves the interaction of auditory, cognitive, and linguistic processes, as well as the use of contextual cues and prior knowledge. Some of the factors that affect speech perception are:
  - The variability of speech sounds across different speakers, dialects, and accents.
  - The coarticulation of speech sounds, which means that the production of one sound influences the production of the next sound.
  - The segmentation of speech into meaningful units, such as words and phrases.
  - The integration of speech with other modalities, such as visual and gestural information.
- Speech analysis: This is the process by which the acoustic properties of speech are measured and represented by mathematical models. Speech analysis can be done in different domains, such as time, frequency, or cepstrum. Some of the techniques used for speech analysis are:
  - Waveform analysis, which examines the shape and amplitude of the speech signal over time.
  - Spectral analysis, which examines the frequency components and energy distribution of the speech signal.
  - Cepstral analysis, which examines the periodicity and envelope of the speech signal.
  - Linear predictive coding (LPC), which estimates the vocal tract parameters and the excitation source of the speech signal.
- Speech synthesis: This is the process by which speech is generated artificially from text or other sources of information. Speech synthesis can be done in different ways, such as concatenative synthesis, parametric synthesis, or neural synthesis. Some of the challenges of speech synthesis are:
  - Generating natural and expressive speech that matches the intended meaning, style, and emotion of the text.
  - Handling out-of-vocabulary words, abbreviations, acronyms, and foreign words.
  - Adapting to different speakers, languages, and domains.
- Speech recognition: This is the process by which speech is converted into text or other forms of representation. Speech recognition can be done in different modes, such as isolated word recognition, continuous speech recognition, or speaker-dependent recognition. Some of the challenges of speech recognition are:
  - Dealing with noise, reverberation, and distortion in the speech signal.
  - Handling different accents, dialects, and speaking styles.
  - Coping with homophones, synonyms, and ambiguous words.
  - Incorporating grammatical and semantic knowledge.



### Speech Fundamentals

- Speech is the natural mode of communication for humans, and it involves the production and perception of sounds that convey meaning.
- Speech processing is the field of study that deals with the analysis, synthesis, recognition, and understanding of speech signals by machines.
- Speech processing is a subfield of natural language processing (NLP), which is the branch of artificial intelligence that aims to enable computers to understand and generate natural language texts and spoken words.
- Speech processing has many applications, such as speech recognition, speech synthesis, speech translation, speech enhancement, speech coding, speech emotion recognition, speaker identification, and speech summarization.
- Speech processing involves several challenges, such as the variability and ambiguity of speech signals, the complexity and diversity of natural languages, the noise and distortion in speech recordings, and the limitations of computational resources and algorithms.
- Speech processing relies on various techniques and models from different disciplines, such as linguistics, mathematics, statistics, signal processing, machine learning, and deep learning.
- Speech processing can be divided into several subtasks, such as:

  - Speech analysis: the process of extracting features and information from speech signals, such as pitch, intensity, duration, formants, spectral envelope, etc.
  - Speech synthesis: the process of generating speech signals from text or other representations, such as phonetic symbols, prosodic features, etc.
  - Speech recognition: the process of converting speech signals into text or other representations, such as phonetic symbols, word sequences, etc.
  - Speech understanding: the process of deriving the meaning and intent of speech signals, such as the topic, sentiment, emotion, dialogue act, etc.
  - Speech translation: the process of converting speech signals from one language to another, either directly or through an intermediate text representation.
  - Speech enhancement: the process of improving the quality and intelligibility of speech signals, such as reducing noise, reverberation, echo, etc.
  - Speech coding: the process of compressing and decompressing speech signals, such as reducing the bit rate, bandwidth, or storage requirements, etc.
  - Speech emotion recognition: the process of identifying and classifying the emotional state of the speaker or the listener from speech signals, such as happiness, sadness, anger, etc.
  - Speaker identification: the process of recognizing the identity of the speaker from speech signals, such as the name, gender, age, accent, etc.
  - Speech summarization: the process of extracting the main points and information from speech signals, such as the key words, phrases, sentences, etc.



### Articulatory Phonetics

- Articulatory phonetics is the branch of phonetics that studies how speech sounds are produced by the human vocal tract .
- Speech sounds are produced by the movements and/or positions of the vocal organs, such as the tongue, lips, teeth, palate, velum, glottis, etc. These are called the articulators .
- Articulatory phonetics is concerned with the transformation of aerodynamic energy (airflow through the vocal tract) into acoustic energy (sound waves) by the action of the articulators.
- Articulatory phonetics can be divided into two main subfields: segmental phonetics and suprasegmental phonetics.
  - Segmental phonetics deals with the production and classification of speech sounds (phonemes) that can be distinguished by their articulatory features, such as place of articulation, manner of articulation, and voicing.
  - Suprasegmental phonetics deals with the production and perception of speech features that go beyond the individual sounds, such as stress, intonation, tone, and length.
- Articulatory phonetics is an important part of speech processing, as it provides the basis for speech synthesis, speech recognition, speech analysis, and speech modification .
- Articulatory phonetics is also related to other fields of linguistics, such as phonology, morphology, syntax, and pragmatics, as well as to other disciplines, such as psychology, sociology, anthropology, and medicine .



### Production And Classification Of Speech Sounds

- Speech sounds are the basic units of human communication that convey meaning and intention.
- Speech sounds are produced by the coordinated movement of various organs of speech, such as the lungs, larynx, velum, tongue, lips, etc.
- Speech sounds are classified into two main categories: vowels and consonants.
  - Vowels are speech sounds that are produced without any significant obstruction or narrowing of the air stream in the vocal tract. Vowels are usually voiced, meaning that the vocal folds vibrate during their production. Vowels are characterized by their height, backness, roundness, and length.
  - Consonants are speech sounds that are produced with some degree of constriction or closure of the air stream in the vocal tract. Consonants can be voiced or voiceless, depending on whether the vocal folds vibrate or not. Consonants are characterized by their place, manner, and voicing of articulation.
- Speech sounds can also be classified into phonemes and allophones.
  - Phonemes are the smallest distinctive units of sound in a language that can change the meaning of a word. For example, the phonemes /p/ and /b/ can distinguish the words "pat" and "bat" in English.
  - Allophones are the different variants of a phoneme that do not change the meaning of a word. For example, the phoneme /p/ can have two allophones in English: aspirated [pʰ] and unaspirated [p]. The aspirated [pʰ] occurs at the beginning of a word or a stressed syllable, while the unaspirated [p] occurs elsewhere. The words "pin" and "spin" have different allophones of /p/, but they are not different words.



### Acoustic Phonetics

- Acoustic phonetics is the study of the acoustic characteristics of speech, including an analysis and description of speech in terms of its physical properties, such as frequency, intensity, and duration .
- Acoustic phonetics is an instrumental science that depends on ways to store, replicate, visualize, and analyze the speech signal. Acoustic phonetics is also a cumulative science in which older research continues to be influential.
- Acoustic phonetics investigates time domain features such as the mean squared amplitude of a waveform, its duration, its fundamental frequency, or frequency domain features such as the frequency spectrum, or even combined spectrotemporal features and the relationship of these properties to other branches of phonetics (e.g. articulatory or auditory phonetics), and to abstract linguistic concepts such as phonemes, phrases, or utterances.
- Acoustic phonetics uses various tools and techniques to measure and represent the speech signal, such as oscilloscopes, sound spectrographs, spectrograms, pitch trackers, formant trackers, etc.
- Acoustic phonetics can be applied to various areas of linguistics, such as phonology, morphology, syntax, semantics, pragmatics, sociolinguistics, psycholinguistics, etc., as well as to speech technology, such as speech recognition, speech synthesis, speech enhancement, speech coding, etc.



### Acoustics of Speech Production

- Acoustics of speech production is the study of how speech sounds are generated and modified by the human vocal tract and the physical properties of the resulting sound waves .
- Speech production involves a complex interaction of three main components: the sound source, the vocal tract filter, and the radiation at the lips .
- The sound source is the part of the speech production system that provides the acoustic energy for speech. It can be either voiced or voiceless, depending on whether the vocal folds vibrate or not .
- The vocal tract filter is the part of the speech production system that shapes the sound source by changing the configuration of the oral and nasal cavities. It can be modeled as a series of tubes with varying cross-sectional areas and lengths, which affect the resonance frequencies and the spectral envelope of the sound source  .
- The radiation at the lips is the part of the speech production system that transmits the sound from the vocal tract to the air. It can be modeled as a high-pass filter that attenuates the low-frequency components of the sound source and amplifies the high-frequency components .
- The acoustic theory of speech production is a mathematical model that describes how the sound source, the vocal tract filter, and the radiation at the lips combine to produce the acoustic speech signal. It is based on the source-filter theory, which assumes that the sound source and the vocal tract filter are independent of each other and that the radiation at the lips is a linear function of the sound source  .
- The acoustic theory of speech production can be used to analyze and synthesize speech sounds, to measure and model the vocal tract shape and size, and to understand the acoustic cues for speech perception and recognition   .



### Review Of Digital Signal Processing Concepts for Speech Processing

- Speech processing is the study of how speech signals are acquired, manipulated, stored, transferred and output.
- Speech signals are usually processed in a digital representation, so speech processing can be regarded as a special case of digital signal processing (DSP), applied to speech signals.
- DSP is concerned with both a discrete signal representation, and with the theory, design and implementation of numerical procedures for processing discrete representation.
- Some basic concepts and algorithms of DSP that are relevant for speech processing are:

  - Sampling and quantization: the process of converting a continuous-time signal into a discrete-time signal by taking samples at regular intervals and assigning them numerical values.
  - Fourier transform: a mathematical tool that decomposes a signal into its frequency components, revealing the spectral characteristics of the signal.
  - Z-transform: a generalization of the Fourier transform that allows the analysis of discrete-time signals and systems in the complex domain.
  - Linear systems: systems that satisfy the properties of superposition and homogeneity, and can be characterized by their impulse response or transfer function.
  - Convolution: a mathematical operation that describes the output of a linear system in terms of the input and the impulse response.
  - Correlation: a measure of similarity between two signals, often used for signal detection, estimation and enhancement.
  - Filter design: the process of designing a system that passes or attenuates certain frequency components of a signal, according to a desired specification.
  - Discrete Fourier transform (DFT) and fast Fourier transform (FFT): algorithms that compute the Fourier transform of a finite-length discrete-time signal, with applications in spectral analysis, filtering and compression.
  - Windowing: a technique that applies a weighting function to a signal segment to reduce spectral leakage and improve frequency resolution in the DFT.
  - Short-time Fourier transform (STFT) and spectrogram: methods that perform the DFT on overlapping segments of a signal, resulting in a time-frequency representation of the signal.
  - Linear prediction: a method that models a signal as a linear combination of its past samples, and estimates the model parameters using the autocorrelation or the least-squares method.
  - Cepstrum and mel-frequency cepstrum (MFC): features that are derived from the logarithm of the spectrum or the filter-bank output of a signal, and are widely used for speech recognition and synthesis.
  - Homomorphic filtering: a technique that separates the excitation and the vocal tract components of a speech signal using the cepstrum, and allows the manipulation of each component independently.
  - LPC vocoder: a speech coding system that uses linear prediction to represent the vocal tract filter, and a source model to represent the excitation signal.
  - LPC analysis and synthesis: methods that use the LPC vocoder to analyze and synthesize speech signals, with applications in speech compression, modification and enhancement.

- These concepts and algorithms provide the foundation for understanding and implementing various speech processing applications, such as voice communication, speech synthesis and speech recognition .



### Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique for analyzing the frequency content of a signal over time.
- It involves dividing the signal into overlapping segments, applying a window function to each segment, and computing the discrete Fourier transform (DFT) of the windowed segments.
- The result is a matrix of complex numbers that represent the magnitude and phase of the signal at each time and frequency bin.
- The STFT is useful for speech and audio processing because it can capture the non-stationary and time-varying nature of these signals.
- The STFT can be used for various applications, such as spectral analysis, filtering, enhancement, compression, recognition, synthesis, and modification of speech and audio signals.
- The STFT has some limitations, such as the trade-off between time and frequency resolution, the leakage effect, and the phase distortion. These can be addressed by using different window functions, zero-padding, and phase reconstruction methods.



### Filter Bank and LPC Methods

- Filter bank and LPC methods are two common techniques for feature extraction in speech processing.
- Feature extraction is the process of transforming the speech signal into a compact and meaningful representation that can be used for speech recognition, synthesis, coding, or analysis.
- Filter bank methods divide the speech signal into frequency bands and compute the energy or power spectrum of each band. The most popular filter bank method is the mel-frequency cepstral coefficients (MFCC), which use a nonlinear frequency scale (mel) to mimic the human perception of sound and apply a discrete cosine transform (DCT) to reduce the correlation between the coefficients .
- LPC methods model the speech signal as the output of a linear filter driven by an excitation source. The filter coefficients are estimated by minimizing the prediction error between the actual and the modeled speech samples. The filter coefficients represent the formants or resonances of the vocal tract, while the excitation source represents the glottal pulse or the noise generated by the airflow .
- Filter bank and LPC methods have different advantages and disadvantages. Filter bank methods are more robust to noise and channel distortion, but require more computation and storage. LPC methods are more efficient and compact, but more sensitive to noise and pitch variation.



## Unit 6 - SPEECH-ANALYSIS

- Speech-analysis is the process of examining spoken language to identify its features, such as words, sounds, intonation, rhythm, and meaning.
- Speech-analysis can be used for various purposes, such as:
  - Transcribing speech into text or other formats.
  - Recognizing speakers or languages from speech samples.
  - Synthesizing speech from text or other inputs.
  - Analyzing the emotions, attitudes, or intentions of speakers.
  - Evaluating the quality, clarity, or effectiveness of speech.
  - Enhancing or modifying speech signals for better communication or entertainment.
- Speech-analysis involves different levels of representation and processing, such as:
  - Acoustic level: the physical properties of speech sounds, such as frequency, amplitude, duration, and spectrum.
  - Phonetic level: the basic units of speech sounds, such as vowels, consonants, and tones.
  - Phonological level: the patterns and rules of speech sounds, such as stress, syllables, and rhyme.
  - Morphological level: the smallest units of meaning in speech, such as roots, prefixes, and suffixes.
  - Lexical level: the words and their meanings in speech, such as nouns, verbs, and adjectives.
  - Syntactic level: the structure and order of words in speech, such as phrases, clauses, and sentences.
  - Semantic level: the meaning and logic of speech, such as concepts, relations, and propositions.
  - Pragmatic level: the use and function of speech in context, such as speech acts, discourse, and conversation.
- Speech-analysis requires various methods and techniques, such as:
  - Signal processing: the manipulation and transformation of speech signals, such as filtering, sampling, and encoding.
  - Feature extraction: the identification and measurement of speech features, such as pitch, energy, and formants.
  - Pattern recognition: the classification and matching of speech patterns, such as speech recognition, speaker recognition, and language identification.
  - Natural language processing: the understanding and generation of natural language, such as speech synthesis, speech translation, and speech summarization.
  - Machine learning: the learning and adaptation of speech models, such as neural networks, hidden Markov models, and deep learning.
  - Evaluation: the assessment and comparison of speech systems, such as accuracy, speed, and usability.



### Features for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis can be divided into two main tasks: speech recognition and speaker recognition.
- Speech recognition is the task of converting speech signals into text or commands, such as transcribing a lecture or controlling a device with voice commands.
- Speaker recognition is the task of identifying or verifying the speaker's identity or characteristics, such as detecting a fraudster or a celebrity.
- Speech analysis involves various steps, such as preprocessing, feature extraction, modeling, and decoding.
- Preprocessing is the step of enhancing the speech signal and removing noise or other irrelevant sounds, such as background music or laughter.
- Feature extraction is the step of transforming the speech signal into a sequence of feature vectors, such as Mel-frequency cepstral coefficients (MFCCs) or linear predictive coding (LPC) coefficients, that capture the acoustic characteristics of the speech.
- Modeling is the step of learning a statistical model that represents the speech signal or the speaker, such as a hidden Markov model (HMM) or a Gaussian mixture model (GMM).
- Decoding is the step of finding the most likely text or speaker given the feature vectors and the model, such as using the Viterbi algorithm or the Bayes rule.
- Speech analysis can be applied to various domains and applications, such as speech synthesis, speech translation, speech enhancement, speech emotion recognition, speech diarization, etc.



### Feature Extraction And Pattern Comparison Techniques for Speech Analysis

- Feature extraction is the process of transforming the speech waveform into a set of parameters that can be used for further processing and analysis.
- Feature extraction aims to reduce the dimensionality, noise, and variability of the speech signal, and to capture the relevant information for the task at hand, such as speech recognition, speaker identification, or emotion detection.
- Feature extraction techniques can be classified into two categories: temporal and spectral.
  - Temporal techniques use the speech waveform itself as the input, and extract features based on the amplitude, energy, zero-crossing rate, or autocorrelation of the signal.
  - Spectral techniques use the frequency domain representation of the speech signal, such as the Fourier transform, the cepstrum, or the filter bank, and extract features based on the magnitude, phase, or shape of the spectrum.
- Some commonly used feature extraction techniques are:
  - Linear Predictive Coding (LPC): LPC models the speech signal as a linear combination of past samples, and estimates the coefficients of the linear predictor using the autocorrelation method or the Levinson-Durbin algorithm. LPC features are the predictor coefficients, the residual error, and the gain.
  - Mel-Frequency Cepstral Coefficients (MFCC): MFCC applies a mel-scale filter bank to the power spectrum of the speech signal, and computes the discrete cosine transform (DCT) of the log filter bank energies. MFCC features are the DCT coefficients, which represent the envelope of the spectrum. MFCC can also be augmented with the first and second derivatives, called delta and delta-delta features, to capture the dynamic information of the speech signal.
  - Perceptual Linear Prediction (PLP): PLP is similar to LPC, but incorporates some aspects of human auditory perception, such as the critical band analysis, the equal-loudness curve, and the intensity-loudness power law. PLP features are the coefficients of an all-pole model of the auditory spectrum.
  - Linear Prediction Cepstral Coefficients (LPCC): LPCC is derived from LPC, by applying a recursion formula to the LPC coefficients and taking the DCT. LPCC features are the DCT coefficients, which are more robust and compact than LPC coefficients.
  - RASTA-PLP: RASTA-PLP is a combination of PLP and a technique called RASTA (Relative Spectral Transform - Perceptual Linear Prediction), which applies a band-pass filter to the log filter bank energies to remove the effects of noise and channel distortion. RASTA-PLP features are more robust to environmental variations than PLP features.

- Pattern comparison is the process of matching the extracted features of an unknown speech signal to the features of a known speech signal, such as a reference template, a word model, or a speaker model.
- Pattern comparison aims to find the best match between the unknown and the known features, and to measure the similarity or distance between them.
- Pattern comparison techniques can be classified into three categories: template-based, model-based, and hybrid.
  - Template-based techniques use a stored representation of the known speech signal, such as a time-aligned sequence of feature vectors, and compare it to the unknown speech signal using a distance metric, such as the Euclidean distance, the Mahalanobis distance, or the dynamic time warping (DTW) distance. Template-based techniques are simple and intuitive, but require a large storage space and a high computational cost.
  - Model-based techniques use a statistical model of the known speech signal, such as a Gaussian mixture model (GMM), a hidden Markov model (HMM), or a neural network, and compare it to the unknown speech signal using a likelihood function, such as the Bayesian likelihood, the maximum likelihood, or the maximum a posteriori. Model-based techniques are more flexible and efficient, but require a training phase and a large amount of data.
  - Hybrid techniques use a combination of template-based and model-based techniques, such as using a template to initialize a model, or using a model to generate a template. Hybrid techniques aim to exploit the advantages of both approaches, and to overcome their limitations.



### Speech Distortion Measures

- Speech distortion measures are quantitative methods to evaluate the quality of speech signals that have been altered by some processing or transmission system.
- Speech distortion measures can be classified into two categories: subjective and objective.
- Subjective measures are based on human perception and evaluation of speech quality, such as mean opinion score (MOS) or diagnostic rhyme test (DRT).
- Objective measures are based on mathematical or statistical comparisons of speech signals, such as signal-to-noise ratio (SNR), spectral distortion, or perceptual evaluation of speech quality (PESQ).
- Speech distortion measures can be used for various applications, such as hearing aids, speech coding, speech enhancement, speech recognition, or speech synthesis.
- Speech distortion measures can be influenced by various factors, such as speech content, speaker characteristics, background noise, channel conditions, or listener preferences.
- Speech distortion measures can have different advantages and limitations, depending on the purpose and context of the evaluation. For example, subjective measures are more reliable and valid, but also more time-consuming and expensive, than objective measures. Objective measures are more convenient and consistent, but also more sensitive to signal characteristics and less correlated with human perception, than subjective measures.



### Mathematical And Perceptual Speech Analysis

- Mathematical speech analysis is the application of mathematical models and methods to study the structure, function, and processing of human language and speech.
- Perceptual speech analysis is the study of how humans perceive, interpret, and produce speech sounds and meanings, using psychological and physiological principles and measurements.
- Some of the topics and techniques involved in mathematical and perceptual speech analysis are:

  - Phonology: the study of the sound patterns and systems of languages, and how they are represented and manipulated by speakers and listeners. Phonological analysis can use mathematical tools such as finite state automata, regular expressions, and algebraic structures to model and describe phonological phenomena.
  - Morphology: the study of the internal structure and formation of words, and how they are related to each other and to the syntax and semantics of sentences. Morphological analysis can use mathematical tools such as formal grammars, rewrite rules, and tree structures to model and describe morphological phenomena.
  - Syntax: the study of the rules and principles that govern the formation and structure of sentences, and how they are parsed and generated by speakers and listeners. Syntactic analysis can use mathematical tools such as context-free grammars, Chomsky hierarchy, and parsing algorithms to model and describe syntactic phenomena.
  - Semantics: the study of the meaning and interpretation of words, phrases, and sentences, and how they are related to the context and the world. Semantic analysis can use mathematical tools such as logic, set theory, and lambda calculus to model and describe semantic phenomena.
  - Speech recognition: the process of converting speech signals into text or other symbolic representations, using acoustic, linguistic, and statistical models and methods. Speech recognition can use mathematical tools such as hidden Markov models, neural networks, and dynamic programming to model and describe speech signals and their probabilities.
  - Speech synthesis: the process of generating speech signals from text or other symbolic representations, using acoustic, linguistic, and prosodic models and methods. Speech synthesis can use mathematical tools such as waveform concatenation, formant synthesis, and text-to-speech systems to model and describe speech signals and their characteristics.
  - Speech perception: the process of interpreting and understanding speech signals, using auditory, cognitive, and social models and methods. Speech perception can use perceptual tools such as critical-band spectral resolution, equal-loudness curve, and intensity-loudness power law to model and describe the auditory spectrum and its effects on speech perception.
  - Speech production: the process of planning and executing speech utterances, using motor, articulatory, and phonetic models and methods. Speech production can use perceptual tools such as acoustic-articulatory mapping, coarticulation, and feedback mechanisms to model and describe the speech organs and their movements.
  - Speech communication: the process of exchanging and conveying information, ideas, and emotions through speech, using pragmatic, sociolinguistic, and discourse models and methods. Speech communication can use perceptual tools such as speech acts, conversational implicatures, and gestures to model and describe the speech context and its effects on speech communication.



### Log–Spectral Distance

- Log–Spectral Distance (LSD) is a measure of similarity or dissimilarity between two spectra, usually expressed in decibels (dB).
- It is calculated as the root mean square (RMS) of the difference between the logarithms of the power spectra of the two signals.
- Mathematically, the LSD between spectra P(ω) and P̂(ω) is defined as:

  D<sub>LS</sub> = (1/2π) ∫<sub>−π</sub><sup>π</sup> [10 log<sub>10</sub> P(ω)/P̂(ω)]<sup>2</sup> dω

- LSD is symmetric, meaning that D<sub>LS</sub>(P, P̂) = D<sub>LS</sub>(P̂, P).
- LSD is often used in speech coding to evaluate the quality of the reconstructed speech signal after compression or quantization.
- LSD can also be used to compare different spectral representations of speech, such as linear predictive coding (LPC), mel-frequency cepstral coefficients (MFCC), or perceptual linear prediction (PLP).
- LSD is related to other spectral distance measures, such as the Itakura–Saito distance, the cepstral distance, and the spectral distortion. However, LSD has some advantages over these measures, such as being more robust to noise and more consistent with human perception.



### Cepstral Distances for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of the similarity or dissimilarity between two speech frames based on their cepstral coefficients.
- Cepstral coefficients are obtained by applying the inverse Fourier transform to the logarithm of the spectrum of a speech signal . They represent the envelope of the spectrum and capture the spectral characteristics of the speech signal.
- Cepstral distance can be used for various applications in speech analysis, such as endpoint detection, emotion recognition, speaker recognition, and voice quality assessment  .
- One of the most common ways to compute cepstral distance is to use the Euclidean distance between mel frequency cepstral coefficients (MFCC), which are cepstral coefficients derived from a filter bank that mimics the human auditory system.
- Cepstral distance can be combined with other features, such as speech energy, to improve the performance of speech analysis tasks.
- Cepstral distance can also be normalized or weighted to account for the perceptual significance of different cepstral coefficients.



### Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log spectrum of the signal.
- Cepstral distance can be used for speech recognition, speaker recognition, and speech enhancement applications.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to the cepstral coefficients according to their importance or variability.
- One common way to assign weights is to use the inverse variance of the cepstral coefficients, which reflects the degree of discrimination between different speech classes .
- Another way to assign weights is to use the logarithm of the index of the cepstral coefficients, which reflects the degree of correlation between adjacent coefficients.
- Weighted cepstral distance measures can improve the performance of speech recognition systems by reducing the effects of noise, channel distortion, and speaker variability  .
- Filtering is a process of modifying or enhancing a speech signal by applying a filter, which is a function that operates on the signal and produces a new signal as output.
- Filtering can be used for speech analysis to remove noise, enhance features, or extract information from the signal.
- Some common types of filters used for speech analysis are:
  - Low-pass filters: filters that attenuate the high-frequency components of the signal and preserve the low-frequency components.
  - High-pass filters: filters that attenuate the low-frequency components of the signal and preserve the high-frequency components.
  - Band-pass filters: filters that attenuate the components of the signal outside a specified frequency band and preserve the components within the band.
  - Band-stop filters: filters that attenuate the components of the signal within a specified frequency band and preserve the components outside the band.
  - Linear filters: filters that have a linear relationship between the input and output signals, such as the finite impulse response (FIR) and infinite impulse response (IIR) filters.
  - Nonlinear filters: filters that have a nonlinear relationship between the input and output signals, such as the median filter and the Wiener filter.
- Filtering can affect the cepstral distance measure by changing the spectral characteristics of the speech signal, which in turn affect the cepstral coefficients.
- Therefore, filtering should be carefully designed and applied to avoid introducing unwanted distortions or losing important information in the speech signal  .



### Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the similarity or dissimilarity between two short-time spectra of speech signals.
- They are used to compare the spectral features of speech signals for speech recognition, enhancement, coding, and synthesis applications.
- There are different types of likelihood distortions, such as:
  - Log likelihood ratio (LLR): the negative logarithm of the ratio of the probability densities of two spectra.
  - Likelihood ratio (LR): the ratio of the probability densities of two spectra.
  - Itakura-Saito (IS): the negative logarithm of the LR minus the LR plus one.
  - Cepstral (CEP): the squared Euclidean distance between the cepstral coefficients of two spectra.
  - Weighted likelihood ratio (WLR): the LLR weighted by a perceptual weighting function that emphasizes the spectral regions with higher auditory sensitivity.
  - Weighted slope metric (WSM): the squared Euclidean distance between the slopes of the log spectra weighted by a perceptual weighting function.
- The choice of the likelihood distortion measure depends on the application and the characteristics of the speech signals.
- Some factors that affect the performance of the likelihood distortion measures are:
  - The spectral resolution and frequency warping of the spectra.
  - The inclusion or exclusion of the energy, gain, and loudness information of the spectra.
  - The perceptual relevance and robustness of the distortion measure to noise and channel variations.
- Some studies have compared the performance of different likelihood distortion measures for speech recognition using dynamic time warping (DTW) algorithms.
- Some of the findings are:
  - The LLR and WSM distortion measures gave the highest recognition accuracy, while the IS distortion measure gave the lowest score .
  - The addition of suprasegmental energy information helped the recognition performance, while the use of gain and absolute loudness degraded the performance .
  - Bark-scale frequency warping did not perform as well as its unwarped counterpart for highly bandlimited telephone data .
  - The WLR distortion measure did not perform as well as its unweighted counterpart .



### Spectral Distortion Using A Warped Frequency Scale

- Spectral distortion is a measure of how much the spectral shape of a signal is changed by a transformation, such as linear prediction, filtering, or compression.
- A warped frequency scale is a nonlinear mapping of the frequency axis that emphasizes certain frequency regions over others, based on some perceptual or physiological criteria.
- Warped frequency scales are often used in speech analysis and synthesis to improve the accuracy and intelligibility of spectral representations, especially at low resolutions or model orders.
- Some examples of warped frequency scales are:
  - The Bark scale, which is based on the critical band rate of the human auditory system, derived from auditory masking experiments.
  - The Mel scale, which is based on the just noticeable differences in frequency of the human ear, derived from pitch perception experiments.
  - The ERB scale, which is based on the equivalent rectangular bandwidth of the auditory filters, derived from psychoacoustic measurements.
- To use a warped frequency scale in speech analysis, the frequency axis of the signal is transformed by a warping function before applying a spectral estimation method, such as linear prediction, Fourier transform, or cepstral analysis.
- The warping function can be defined by a parameter that controls the degree of warping, such as the all-pass coefficient in the bilinear transform, or the warping constant in the Laguerre transform .
- The warping function can also be adapted to the characteristics of the speech signal, such as the fundamental frequency, the formant frequencies, or the spectral tilt .
- The advantages of using a warped frequency scale in speech analysis are:
  - It can reduce the spectral distortion caused by harmonic peaks, noise, or quantization errors, by smoothing the spectral envelope and allocating more resolution to the important frequency regions.
  - It can improve the perceptual quality and intelligibility of speech synthesis, by matching the spectral resolution to the human auditory system and preserving the salient spectral features.
  - It can enhance the performance of speech recognition, by reducing the mismatch between the training and testing conditions and capturing the speaker-specific information.



### LPC for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- LPC stands for Linear Predictive Coding, which is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model .
- LPC analyzes the speech signal by estimating the formants, which are the resonant frequencies of the vocal tract, and removing their effects from the speech signal, leaving behind the residual signal, which contains the pitch and the noise components.
- LPC is based on the assumption that the speech signal is produced by a linear system, which can be modeled by an all-pole filter with a finite number of coefficients. The coefficients are determined by minimizing the mean squared error between the original signal and the predicted signal .
- LPC is the most widely used method in speech coding and speech synthesis, as it can achieve high compression ratios and natural sounding speech quality.
- LPC can be divided into two steps: analysis and synthesis. In the analysis step, the speech signal is divided into frames of fixed length, and the LPC coefficients and the residual signal are computed for each frame. In the synthesis step, the LPC coefficients and the residual signal are used to reconstruct the speech signal by passing the residual signal through the inverse filter defined by the LPC coefficients.



### PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting features from speech signals that can be used for various applications, such as speech recognition, speaker identification, emotion detection, etc.
- Speech features are usually derived from the spectral, temporal, or cepstral properties of speech signals, which reflect the characteristics of the vocal tract, the glottal source, and the prosody of speech.
- Two common methods of speech feature extraction are Perceptual Linear Prediction (PLP) and Mel Frequency Cepstral Coefficients (MFCC).
- PLP is a technique that mimics the human auditory system by applying a psychoacoustic model to the speech spectrum. It consists of the following steps :
  - Pre-emphasis: a high-pass filtering operation that enhances the high-frequency components of speech and reduces the effect of noise.
  - Windowing: a process of dividing the speech signal into short frames (typically 20-30 ms) and applying a window function (such as Hamming or Hanning) to each frame to reduce the discontinuities at the edges.
  - Fourier transform: a mathematical operation that converts each frame of speech from the time domain to the frequency domain, resulting in a power spectrum.
  - Critical band analysis: a process of applying a set of triangular filters that are spaced according to the Bark scale, which is a perceptual scale of frequency based on the human hearing sensitivity. This reduces the spectral resolution and emphasizes the perceptually important frequency bands.
  - Equal-loudness pre-emphasis: a process of applying a weighting function to the critical band spectrum that compensates for the human ear's non-uniform sensitivity to different frequencies.
  - Intensity-loudness power law: a process of applying a non-linear transformation to the equal-loudness spectrum that simulates the human perception of loudness, which is proportional to the logarithm of the intensity.
  - Autoregressive modeling: a process of fitting a linear predictive model to the intensity-loudness spectrum, resulting in a set of coefficients that represent the spectral envelope of speech.
  - Cepstral coefficients: a process of applying a discrete cosine transform to the autoregressive coefficients, resulting in a set of coefficients that are decorrelated and have a lower dimensionality. The lower-order coefficients are usually retained as the PLP features.
- MFCC is a technique that also mimics the human auditory system by applying a mel-scale filter bank to the speech spectrum. It consists of the following steps  :
  - Pre-emphasis: same as PLP.
  - Windowing: same as PLP.
  - Fourier transform: same as PLP.
  - Mel-scale filter bank: a process of applying a set of triangular filters that are spaced according to the mel scale, which is another perceptual scale of frequency that is based on the human pitch perception. This also reduces the spectral resolution and emphasizes the perceptually important frequency bands.
  - Logarithmic compression: a process of applying a logarithmic function to the mel-scale spectrum, which simulates the human perception of loudness.
  - Cepstral coefficients: same as PLP, except that the discrete cosine transform is applied to the logarithmic mel-scale spectrum, resulting in a set of coefficients that are decorrelated and have a lower dimensionality. The lower-order coefficients are usually retained as the MFCC features.
- Both PLP and MFCC are widely used in speech analysis, as they capture the salient features of speech that are robust to noise and speaker variability. However, they also have some differences and limitations  :
  - PLP is more closely related to the human auditory system, as it incorporates more psychoacoustic principles, such as the equal-loudness pre-emphasis and the intensity-loudness power law. MFCC is more closely related to the human vocal tract, as it reflects the shape of the resonances that are produced by the articulators.
  - PLP is more suitable for low-bitrate speech coding, as it preserves the perceptual quality of speech better than MFCC. MFCC is more suitable for speech recognition, as it provides a better representation of the phonetic content of speech than PLP.
  - PLP and MFCC are both sensitive to the choice of parameters, such as the frame size, the window type, the number of filters, the order of the autoregressive model, and the number of coefficients. These parameters need to be tuned according to



### Time Alignment And Normalization for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Time alignment is the process of finding the optimal correspondence between the frames of two speech signals that are related by some transformation, such as speaker variation, speaking rate variation, or voice conversion   .
- Time alignment is useful for applications such as speech recognition, text-to-speech synthesis, speaker recognition, and voice conversion, where the goal is to compare, match, or transform speech signals from different sources or conditions  .
- Time alignment can be achieved by using methods such as dynamic time warping (DTW), hidden Markov models (HMMs), or neural networks, which measure the dissimilarity between speech events and minimize the timing differences between corresponding speech events   .
- Time alignment can be improved by using techniques such as refinement, normalization, and frame comparison, which reduce the alignment error and increase the sound correspondence between the speech signals.
- Normalization is the process of adjusting the speech signals to reduce the effects of speaker variation, such as pitch, intensity, duration, and spectral characteristics, which can affect the perception and recognition of speech.
- Normalization is important for speech perception and processing, as it allows listeners and systems to recognize words and phonemes spoken by different speakers despite the acoustic variation.
- Normalization can be achieved by using methods such as vocal tract length normalization (VTLN), cepstral mean subtraction (CMS), z-score normalization, or speaker adaptation, which modify the speech signals to make them more comparable or compatible across speakers.



### Dynamic Time Warping

- Dynamic Time Warping (DTW) is an algorithm for measuring the similarity between two temporal sequences, such as speech signals, that may vary in speed or length  .
- DTW is based on the idea of finding the optimal alignment between two sequences by minimizing the distance between them .
- DTW can handle non-linear distortions and local variations in the sequences, such as different pronunciations or accents in speech  .
- DTW works by constructing a matrix that represents the pairwise distances between the elements of the two sequences, and then finding the shortest path through the matrix that satisfies some constraints .
- The constraints are: 
  - The path must start at the top-left corner and end at the bottom-right corner of the matrix .
  - The path must move monotonically, i.e., it can only move right, down, or diagonally .
  - The path must be continuous, i.e., it cannot skip any elements of the matrix .
- The length of the path is the DTW distance between the two sequences, and the path itself is the optimal alignment .
- DTW can be used for various applications, such as speech recognition, speaker identification, gesture recognition, data mining, financial markets, etc   .
- DTW has some limitations, such as high computational complexity, sensitivity to noise, and lack of theoretical guarantees .
- DTW can be improved by using various techniques, such as pruning, indexing, lower bounding, warping constraints, normalization, etc .



### Multiple Time – Alignment Paths for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data  .
- Time alignment is useful for many applications of speech analysis, such as speech recognition, speech synthesis, voice conversion, speech enhancement, and speech-to-lips synchronization  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or noise levels  .
- One of the most popular methods for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the total distance between the matched frames.
- DTW can be implemented using a dynamic programming algorithm that fills a matrix of distances between the frames of the two time series and then traces back the minimum-cost path from the end to the beginning of the matrix.
- However, DTW has some limitations, such as being sensitive to noise, requiring a global alignment, and having a high computational complexity  .
- To overcome these limitations, various extensions and modifications of DTW have been proposed, such as subsequence DTW, multi-level DTW, segmental DTW, and multiview temporal alignment  .
- These methods aim to find multiple time-alignment paths that can capture the local or global variations, the hierarchical or sequential structure, the segmental or continuous nature, or the cross-modal or multimodal relationships of the time series  .
- Multiple time-alignment paths can provide more flexibility, robustness, and accuracy for speech analysis tasks, as well as more information about the temporal dynamics and correlations of the time series  .
- Some examples of applications that can benefit from multiple time-alignment paths are:

  - Non-parallel articulatory-to-acoustic conversion, which aims to generate speech from biosignal data, such as electromyography or electroglottography, without requiring parallel data for training.
  - Time and phase alignment, which is important for sound system optimization, especially when using multiple loudspeakers or microphones with different frequency responses and delays.
  - Improvement of time alignment of the speech signals to enhance the quality of voice conversion, which is the process of modifying the voice characteristics of a source speaker to match those of a target speaker.
  - Adaptive, ordered, graph search technique for dynamic time warping for speech recognition, which is a method to speed up the DTW algorithm by using a graph representation of the time series and pruning the search space based on the order and similarity of the frames.
  - Dynamic temporal alignment of speech to lips, which is a technique to synchronize the lip movements of a speaker with the corresponding speech signal, which can be useful for video conferencing, lip reading, or dubbing.



## Unit 7 - SPEECH MODELING

- Speech modeling is the process of using speech and language to help a child or a learner develop their communication skills   .
- Speech modeling can be used for different purposes, such as:
  - Teaching new words, phrases, or sentence structures
  - Expanding vocabulary and grammar
  - Correcting speech errors or pronunciation
  - Enhancing fluency and confidence
  - Learning a foreign language or a different accent
- Speech modeling can be done in different ways, such as:
  - Imitating the target speech or language
  - Repeating the target speech or language with emphasis or correction
  - Expanding or extending the target speech or language with more information or details
  - Recasting the target speech or language in a different form or context
  - Prompting the target speech or language with cues or questions
- Speech modeling can be effective when it follows these principles   :
  - Be natural and conversational
  - Be positive and encouraging
  - Be consistent and frequent
  - Be appropriate and relevant
  - Be responsive and interactive



### Hidden Markov Models

- A hidden Markov model (HMM) is a probabilistic model that can be used to represent sequential data, such as speech signals, text, or DNA sequences.
- An HMM consists of two components: a set of hidden states and a set of observable symbols.
- The hidden states are not directly observable, but they generate the observable symbols according to some probability distribution.
- The transitions between the hidden states are also governed by some probability distribution, which is called the transition matrix.
- An HMM can be represented by a directed graph, where the nodes are the hidden states and the edges are the transitions, labeled by the transition probabilities.
- The observable symbols are associated with each hidden state by an emission matrix, which specifies the probability of emitting a symbol given a state.
- An HMM can be specified by three parameters: the initial state distribution, the transition matrix, and the emission matrix.
- An HMM can be used for various tasks, such as speech recognition, speech synthesis, natural language processing, and bioinformatics.
- Some of the common problems that can be solved using HMMs are:
  - Evaluation: Given an HMM and a sequence of observable symbols, what is the probability of the sequence being generated by the model?
  - Decoding: Given an HMM and a sequence of observable symbols, what is the most likely sequence of hidden states that generated the symbols?



### Markov Processes

- A Markov process is a random process indexed by time, and with the property that the future is independent of the past, given the present .
- A Markov process can be discrete or continuous in time, and finite or infinite in state space.
- A Markov process can be characterized by a state transition matrix or a state transition function, which specify the probabilities of moving from one state to another in a given time interval .
- Examples of discrete-time Markov processes are Markov chains, which are widely used in natural language processing to model sequences of words, characters, or symbols.
- Examples of continuous-time Markov processes are diffusion processes and processes with independent increments, such as Poisson and Wiener processes, which are widely used in physics, biology, and finance .
- Markov processes are useful for modeling stochastic systems that exhibit memoryless behavior, such as weather, traffic, population dynamics, and speech recognition .



### HMMs for speech modeling

- Hidden Markov Models (HMMs) are a statistical model that consists of two components: a set of hidden states, and a set of observations .
- Each hidden state has a probability distribution over the possible observations, and each observation is assumed to be generated by one of the hidden states .
- The hidden states are not directly observable, but they can be inferred from the observations using the Bayes' rule .
- The transitions between the hidden states are governed by a stochastic process, which can be represented by a transition matrix .
- HMMs can be trained from data using efficient algorithms, such as the Expectation-Maximization (EM) algorithm or the Baum-Welch algorithm .
- HMMs are a natural choice for speech recognition, because they can model the temporal dynamics and variability of speech, and because they can be trained from data using efficient algorithms  .
- Speech recognition is the task of converting a speech signal into a textual representation, such as a word or a sentence .
- Speech signals can be represented by a sequence of spectral vectors, which capture the frequency components of the sound waves .
- Each spectral vector can be considered as an observation, and each hidden state can correspond to a phonetic unit, such as a phone, a syllable, or a word .
- HMMs can be used to model the probability of a sequence of spectral vectors given a sequence of hidden states, and vice versa .
- HMMs can also be combined with language models, which capture the syntactic and semantic constraints of natural language, to improve the accuracy of speech recognition .

#### Advantages of HMMs for speech recognition

- HMMs can capture the probabilistic dependencies between the observed features and the underlying states of a system, and allow for efficient inference and learning algorithms  .
- HMMs can handle the variability and uncertainty of speech signals, such as noise, accents, dialects, and emotions  .
- HMMs can model the temporal structure and dynamics of speech, such as the duration, the pauses, and the transitions between phonetic units  .
- HMMs can be trained from data using unsupervised or supervised methods, and can be adapted to new speakers or domains  .
- HMMs can be combined with other models, such as language models, acoustic models, or neural networks, to improve the performance of speech recognition  .

#### Disadvantages of HMMs for speech recognition

- HMMs make some simplifying assumptions, such as the independence of observations given the hidden states, and the stationarity of the transition matrix, which may not hold in reality  .
- HMMs require a large amount of data and computational resources to train and test, and may suffer from overfitting or underfitting problems  .
- HMMs may not capture the complex and nonlinear relationships between the speech features and the hidden states, or the long-term dependencies between the hidden states  .
- HMMs may not be able to handle the diversity and ambiguity of natural language, such as homophones, synonyms, or idioms  .
- HMMs may not be able to model the high-level semantic and pragmatic aspects of speech, such as the intention, the context, or the emotion of the speaker  .



### Evaluation for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Speech modeling is the process of representing speech signals in a mathematical or statistical way, such as using acoustic features, phonetic units, or word sequences.
- Speech modeling can be used for various applications, such as speech recognition, speech synthesis, speech enhancement, speech compression, speech analysis, and speech translation.
- Speech modeling can be divided into two main categories: parametric and non-parametric models.
- Parametric models assume that speech signals follow a certain distribution or structure, and use a finite set of parameters to describe them. Examples of parametric models are linear predictive coding (LPC), hidden Markov models (HMMs), and deep neural networks (DNNs).
- Non-parametric models do not make any assumptions about the underlying distribution or structure of speech signals, and use a large amount of data to capture the variability and complexity of speech. Examples of non-parametric models are Gaussian mixture models (GMMs), support vector machines (SVMs), and k-nearest neighbors (k-NN).
- Speech modeling can be evaluated based on different criteria, such as accuracy, robustness, efficiency, and interpretability.
- Accuracy measures how well the model can reproduce or recognize the speech signals, and can be quantified by metrics such as mean squared error (MSE), word error rate (WER), or perceptual evaluation of speech quality (PESQ).
- Robustness measures how well the model can handle noisy, distorted, or mismatched speech signals, and can be quantified by metrics such as signal-to-noise ratio (SNR), cepstral distance (CD), or word recognition rate (WRR).
- Efficiency measures how fast and how much computational resources the model requires to process the speech signals, and can be quantified by metrics such as runtime, memory usage, or model size.
- Interpretability measures how easy it is to understand the model and its parameters, and can be quantified by metrics such as entropy, mutual information, or feature importance.



### Optimal State Sequence for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Speech modeling is the process of representing speech signals as sequences of discrete symbols, such as words, phonemes, or acoustic features.
- Speech modeling is essential for speech recognition, speech synthesis, speech enhancement, and speech analysis.
- One of the most popular and widely used speech modeling techniques is the hidden Markov model (HMM), which is a probabilistic model that assumes that the speech signal is generated by a stochastic process that transitions among a finite set of hidden states, each emitting an observable output according to a probability distribution.
- The optimal state sequence is the most likely sequence of hidden states that generated a given speech signal, according to the HMM parameters and the observation probabilities.
- The optimal state sequence can be used for various purposes, such as:
  - Aligning the speech signal with the corresponding transcription, which is useful for speech recognition and speech synthesis training.
  - Segmenting the speech signal into smaller units, such as words, syllables, or phonemes, which is useful for speech analysis and speech synthesis.
  - Extracting acoustic features from the speech signal, such as pitch, energy, or spectral coefficients, which is useful for speech enhancement and speech synthesis.
  - Modifying the speech signal, such as changing the speed, pitch, or emotion, which is useful for speech synthesis and speech transformation.
- The optimal state sequence can be computed by various algorithms, such as:
  - The Viterbi algorithm, which is a dynamic programming algorithm that finds the optimal state sequence by maximizing the joint probability of the state sequence and the observation sequence, using the HMM parameters and the observation probabilities .
  - The forward-backward algorithm, which is a dynamic programming algorithm that finds the optimal state sequence by maximizing the posterior probability of the state sequence given the observation sequence, using the HMM parameters and the observation probabilities.
  - The expectation-maximization (EM) algorithm, which is an iterative algorithm that finds the optimal state sequence by alternating between estimating the HMM parameters using the current state sequence and estimating the state sequence using the current HMM parameters and the observation probabilities.
  - The variational inference algorithm, which is an approximate algorithm that finds the optimal state sequence by minimizing the Kullback-Leibler divergence between the posterior distribution of the state sequence given the observation sequence and a tractable variational distribution, using the HMM parameters and the observation probabilities.
  - The latent trajectory hidden Markov model (LTHMM) algorithm, which is a novel algorithm that finds the optimal state sequence by modeling the observation sequence as a continuous function of a latent trajectory variable that evolves according to a stochastic differential equation, using the HMM parameters and the observation probabilities.
- The optimal state sequence can be influenced by various factors, such as:
  - The number and type of hidden states, which determine the granularity and complexity of the speech modeling.
  - The transition probabilities, which determine the likelihood of switching between different hidden states.
  - The observation probabilities, which determine the likelihood of emitting different outputs from each hidden state.
  - The initial and final state probabilities, which determine the likelihood of starting and ending the speech signal with each hidden state.
  - The noise and distortion in the speech signal, which affect the accuracy and reliability of the observation probabilities.
  - The prosody and emotion in the speech signal, which affect the variability and expressiveness of the speech modeling.



### Viterbi Search for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Viterbi search is a dynamic programming algorithm that finds the most likely sequence of hidden states in a hidden Markov model (HMM) that generates a given sequence of observations.
- Viterbi search is widely used in speech recognition to find the most likely sequence of phonemes or words that corresponds to a given speech signal.
- Viterbi search consists of the following steps:
  - Initialize a state list with one cell for each state in the HMM and assign the initial probabilities to the starting states.
  - For each observation in the sequence, compute the transition probabilities from the previous states to the current states and multiply them by the emission probabilities of the observation given the current states. This gives the joint probabilities of the observation and the current states.
  - For each current state, select the previous state that has the highest joint probability and store it as the back pointer. Also, store the maximum joint probability as the new state probability.
  - Repeat steps 2 and 3 until all observations are processed.
  - Trace back the pointers from the final state with the highest probability to the initial state and obtain the most likely sequence of hidden states.
- Viterbi search can be extended to handle multiple sources of observations, such as speech signals from different directions or microphones, by using a 3-dimensional trellis space composed of source directions, input frames, and HMM states.
- Viterbi search can also be applied to other natural language processing tasks, such as part-of-speech tagging, where the hidden states are the tags and the observations are the words.



### Baum-Welch Parameter Re-Estimation

- Baum-Welch is an algorithm that uses the Expectation-Maximization (EM) method to find the maximum likelihood estimate of the parameters of a Hidden Markov Model (HMM) given a set of observed feature vectors.
- The algorithm iteratively updates the parameters of the HMM until convergence or a predefined number of iterations is reached.
- The algorithm consists of two main steps: the forward-backward procedure and the re-estimation formulas.
- The forward-backward procedure computes the posterior probabilities of the hidden states given the observations using dynamic programming. These probabilities are denoted by $\alpha_t(i)$ and $\beta_t(i)$, where $t$ is the time index and $i$ is the state index.
- The re-estimation formulas update the parameters of the HMM using the posterior probabilities computed by the forward-backward procedure. The parameters include the initial state probabilities $\pi_i$, the state transition probabilities $a_{ij}$, and the emission probabilities $b_i(o_t)$, where $o_t$ is the observation at time $t$.
- The re-estimation formulas are derived by applying the principle of maximum likelihood, which maximizes the log-likelihood function of the HMM given the observations. The log-likelihood function is given by
$$
\log P(O|\lambda) = \sum_{t=1}^T \log \sum_{i=1}^N \alpha_t(i) \beta_t(i),
$$
where $O = (o_1, o_2, \dots, o_T)$ is the observation sequence, $\lambda = (\pi, A, B)$ is the parameter set of the HMM, $N$ is the number of states, and $T$ is the length of the observation sequence.
- The re-estimation formulas for the parameters are given by
$$
\hat{\pi}_i = \frac{\alpha_1(i) \beta_1(i)}{\sum_{j=1}^N \alpha_1(j) \beta_1(j)},
$$
$$
\hat{a}_{ij} = \frac{\sum_{t=1}^{T-1} \alpha_t(i) a_{ij} b_j(o_{t+1}) \beta_{t+1}(j)}{\sum_{t=1}^{T-1} \alpha_t(i) \beta_t(i)},
$$
$$
\hat{b}_i(o_t) = \frac{\sum_{t=1}^T \alpha_t(i) \beta_t(i) \delta(o_t, v_k)}{\sum_{t=1}^T \alpha_t(i) \beta_t(i)},
$$
where $v_k$ is the $k$-th symbol in the observation alphabet, and $\delta(o_t, v_k)$ is the Kronecker delta function, which is 1 if $o_t = v_k$ and 0 otherwise.
- The algorithm starts with an initial guess of the parameters and repeats the following steps until convergence or a predefined number of iterations is reached:
  - Step 1: Apply the forward-backward procedure to compute the posterior probabilities $\alpha_t(i)$ and $\beta_t(i)$ for each state $i$ and time $t$.
  - Step 2: Apply the re-estimation formulas to update the parameters $\pi_i$, $a_{ij}$, and $b_i(o_t)$ for each state $i$ and observation $o_t$.
  - Step 3: Compute the log-likelihood function of the HMM given the observations using the updated parameters and check if it has increased or reached a predefined threshold.
- The algorithm is guaranteed to converge to a local maximum of the log-likelihood function, but not necessarily to the global maximum. Therefore, the initial guess of the parameters may affect the final result.



### Implementation Issues for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Speech modeling is the process of representing speech signals in a mathematical or statistical way, such as using hidden Markov models, neural networks, or deep learning methods.
- Speech modeling is essential for speech recognition, speech synthesis, speech enhancement, speech coding, and speech analysis applications.
- Speech modeling faces several implementation issues that affect its performance, accuracy, and usability. Some of these issues are:

  - Data quality and quantity: Speech modeling requires large amounts of high-quality speech data to train and test the models. However, speech data can be noisy, distorted, corrupted, or incomplete due to various factors, such as background noise, channel distortion, speaker variability, dialects, accents, emotions, etc. These factors can degrade the quality of the speech data and make it difficult to model the speech signals accurately and robustly. Moreover, speech data can be scarce or unavailable for some languages, domains, or tasks, which limits the generalization and scalability of the speech models .
  - Data privacy and security: Speech data contains sensitive and personal information about the speakers, such as their identity, location, health, preferences, etc. Therefore, speech data must be collected, stored, and processed in a secure and ethical way, respecting the privacy and consent of the speakers. However, speech data can be vulnerable to various threats, such as unauthorized access, leakage, theft, manipulation, or misuse. These threats can compromise the confidentiality, integrity, and availability of the speech data and the speech models, and cause harm to the speakers or the users of the speech applications .
  - Data diversity and complexity: Speech data is highly diverse and complex, as it reflects the natural and rich variations of human speech and language. Speech data can vary in terms of the acoustic, linguistic, and paralinguistic features of the speech signals, such as the pitch, intensity, duration, phonemes, words, sentences, prosody, intonation, stress, emotion, etc. These features can depend on various factors, such as the speaker, the context, the domain, the task, the channel, etc. Therefore, speech data can be challenging to model and process, as it requires sophisticated and flexible methods that can capture and handle the diversity and complexity of the speech data .
  - Data interpretation and understanding: Speech data is not only a signal, but also a means of communication and expression. Speech data conveys meaning, intention, and information that can be relevant and useful for the speakers and the listeners. Therefore, speech data must be interpreted and understood in a correct and appropriate way, taking into account the semantic, pragmatic, and social aspects of the speech and language. However, speech data can be ambiguous, vague, incomplete, or inconsistent, which can make it difficult to interpret and understand the speech data accurately and reliably. Moreover, speech data can be influenced by the culture, background, and perspective of the speakers and the listeners, which can affect the interpretation and understanding of the speech data .

