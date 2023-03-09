### 9. Write program to find Simulate First and Follow of any given grammar.

First and Follow sets are important concepts in the field of Compiler Design. They are used to predict the behavior of the parser while parsing a string of symbols. The First set of a non-terminal symbol is the set of all possible symbols that can appear as the first symbol in a string derived from that non-terminal. The Follow set of a non-terminal symbol is the set of all possible symbols that can appear immediately after that non-terminal in any string derived from the start symbol.

A program can be written to find the First and Follow sets of any given grammar. Here are the steps to write the program:

1. Read the input grammar and store it in a data structure. This can be done using a list or dictionary.

2. Identify all the non-terminal symbols in the grammar. This can be done by scanning all the production rules and extracting the non-terminal symbols on the left-hand side.

3. For each non-terminal symbol, compute its First set. This can be done by iterating through all the production rules and checking if the non-terminal symbol is on the left-hand side. If it is, then add the First set of the right-hand side symbols to the First set of the non-terminal symbol.

4. Compute the Follow set for each non-terminal symbol. This can be done by iterating through all the production rules and checking if the non-terminal symbol appears on the right-hand side. If it does, then add the Follow set of the non-terminal symbol to the Follow set of the symbols that appear after it.

5. Print the First and Follow sets for each non-terminal symbol.

Advantages:
- Helps in constructing a predictive parser.
- Helps in detecting left recursion in the grammar.
- Helps in detecting ambiguities in the grammar.

Disadvantages:
- It can be time-consuming for large grammars.
- It may not be accurate for complex grammars.

Example:
Consider the following grammar:

S → ( L ) | a
L → L , S | S

The First and Follow sets for this grammar are:

First(S) = { (, a }
Follow(S) = { ), $ }
First(L) = { (, a }
Follow(L) = { ), $ }

Application:
The First and Follow sets are used in constructing a predictive parser. They are also used in detecting left recursion and ambiguities in the grammar.