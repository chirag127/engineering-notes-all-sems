 Here is the content in markdown format with formal tone and without emojis:

### 9. Write program to find Simulate First and Follow of any given grammar.

1. Take the grammar in the form of rules. e.g:
E -> TE'
E' -> +TE' | ε
T -> FT'
T' -> *FT' | ε
F -> (E) | id

2. Find the First of each non-terminal.
First(E) = {id, (}
First(E') = {+, ε}
First(T) = {id, (}
First(T') = {*, ε}
First(F) = {id, (}

3. Find the Follow of each non-terminal.
Follow(E) = {$, +, *}
Follow(E') = {$, +, *}
Follow(T) = {$, +, *}
Follow(T') = {$, +, *}
Follow(F) = {$, +, *}

4. Check if all the terminals appearing in the First and Follow sets are present in the input string. If Yes, the input string is accepted by the grammar else it is rejected.

This is a program to simulate the concepts of First and Follow sets to check if a given input string is accepted by the grammar or not. The steps involve finding the First and Follow sets of the grammar and then verifying the input string using these sets.