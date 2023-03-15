### 9. Write program to find Simulate First and Follow of any given grammar.

First and Follow are two important concepts in the construction of predictive parsers for context-free grammars. These concepts are used to determine the possible set of terminals that can appear at the beginning of a string derived from a non-terminal, and the possible set of terminals that can appear immediately after a non-terminal in a sentential form.

Here is an example of how to write a program to find the First and Follow of a given grammar:

1. Define the grammar in a suitable data structure, such as a dictionary where the keys are the non-terminals and the values are lists of productions.
2. Write a function to find the First of a given symbol. This function should take the grammar and the symbol as input and return a set of terminals that can appear at the beginning of a string derived from the symbol.
3. Write a function to find the Follow of a given non-terminal. This function should take the grammar and the non-terminal as input and return a set of terminals that can appear immediately after the non-terminal in a sentential form.
4. Use the above functions to find the First and Follow of all non-terminals in the grammar.
5. Display the results in a suitable format.

This is a general outline of how to write a program to find the First and Follow of a given grammar. The specific details and implementation may vary depending on the programming language and the requirements of the task. It is important to thoroughly understand the concepts of First and Follow and how they are used in the construction of predictive parsers before attempting to write such a program.