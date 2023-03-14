### Syntactic Parsing for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

Syntactic parsing is a process of analyzing the structure of sentences in natural language. It involves identifying the grammatical relationships between words in a sentence and grouping them into phrases or clauses. The goal of syntactic parsing is to create a parse tree that represents the syntactic structure of a sentence.

There are two main approaches to syntactic parsing: 

1. Top-down Parsing: This approach starts with the highest level of the parse tree and recursively breaks it down into smaller sub-trees until individual words are reached. This approach is also known as "recursive descent parsing." 

2. Bottom-up Parsing: This approach starts with the individual words of a sentence and builds up the parse tree by combining them into larger sub-trees. This approach is also known as "shift-reduce parsing."

There are different types of syntactic parsing algorithms that can be used to parse a sentence:

1. Chart Parsing: This algorithm uses dynamic programming to efficiently parse a sentence. It creates a chart of all possible parse trees and selects the most likely parse tree based on a probabilistic model.

2. Earley Parsing: This algorithm uses a chart to keep track of all possible partial parse trees. It uses a set of rules to combine these partial parse trees into complete parse trees.

3. CYK Parsing: This algorithm uses dynamic programming to parse a sentence in Chomsky Normal Form (CNF). It uses a table to store all possible combinations of non-terminals and terminals that can generate a particular substring of the sentence.

There are different types of grammars that can be used for syntactic parsing:

1. Context-Free Grammar (CFG): This is a type of grammar that describes the syntactic structure of a language using a set of production rules. Each production rule defines how a non-terminal symbol can be replaced by a sequence of terminal and/or non-terminal symbols.

2. Dependency Grammar (DG): This is a type of grammar that describes the syntactic structure of a language using directed arcs between words. Each arc represents a grammatical relationship between two words, such as subject or object.

Some commonly used syntactic parsing tools are:

1. Stanford Parser: This is a popular syntactic parsing tool developed by Stanford University. It uses a probabilistic model and supports both CFG and DG parsing.

2. NLTK Parser: This is a syntactic parsing tool developed by the Natural Language Toolkit (NLTK) library in Python. It supports both top-down and bottom-up parsing algorithms and can be used with different types of grammars.

3. CoreNLP Parser: This is a syntactic parsing tool developed by Stanford University as part of the CoreNLP toolkit. It supports both CFG and DG parsing and can output parse trees in different formats.

Learning Trick:
A common mnemonic for remembering the two main syntactic parsing approaches is "TD for top-down" and "BU for bottom-up." Another trick is to remember that "TD" and "top" both start with "t" while "BU" and "bottom" both start with "b."