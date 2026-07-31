
### 9. Write program to find Simulate First and Follow of any given grammar

* First and Follow are two important concepts of Compiler Design. 
* First is used to find the First set of a given grammar. It is defined as the set of terminals that can appear in the beginning of any string derived from a given non-terminal. 
* Follow is used to find the Follow set of a given grammar. It is defined as the set of terminals that can appear immediately after a given non-terminal in some sentential form.
* A program can be written to simulate First and Follow of any given grammar. This program will take a grammar as an input and output the First and Follow sets of the given grammar. 
* The algorithm for writing such a program is as follows: 
    1. Start with the given grammar 
    2. Create an empty First and Follow set for each non-terminal in the grammar 
    3. For each production in the grammar, add the First set of the right side of the production to the First set of the left side of the production 
    4. For each production in the grammar, add the Follow set of the left side of the production to the Follow set of the right side of the production 
    5. Repeat steps 3 and 4 until no more changes can be made
    6. Output the First and Follow sets of the given grammar 
* This program can be written in any programming language.