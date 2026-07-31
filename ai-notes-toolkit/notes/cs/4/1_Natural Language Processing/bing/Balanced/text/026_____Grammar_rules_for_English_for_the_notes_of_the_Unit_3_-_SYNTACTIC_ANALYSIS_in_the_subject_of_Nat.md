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

![Parse tree](https://i.imgur.com/9Q6yf0g.png)

(S (NP (DT The) (NN dog)) (VP (VBD chased) (NP (DT the) (NN cat))))

- A phrase structure grammar can be ambiguous, meaning that it can generate more than one parse tree or bracketed notation for the same sentence. This can lead to different interpretations of the sentence, which may or may not be intended by the speaker or writer.
- For example, the sentence "I saw the man with the telescope" can be represented by two different parse trees and bracketed notations, depending on whether the phrase "with the telescope" modifies the verb "saw" or the noun "man":

![Parse tree 1](https://i.imgur.com/0Z0x8xN.png)

(S (NP (PRP I)) (VP (VBD saw) (NP (DT the) (NN man) (PP (IN with) (NP (DT the) (NN telescope))))))

![Parse tree 2](https://i.imgur.com/1fZjxLr.png)

(S (NP (PRP I)) (VP (VBD saw) (NP (DT the) (NN man)) (PP (IN with) (NP (DT the) (NN telescope)))))

- To resolve syntactic ambiguity, one can use additional information, such as semantic, pragmatic, or contextual cues, or apply some heuristics or preferences, such as the principle of minimal attachment or the principle of late closure, that favor certain interpretations over others.
- Syntactic analysis is an important task in natural language processing, as it can provide useful information for other tasks, such as semantic analysis, discourse analysis, machine translation, information extraction, question answering, etc.