 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Programming problems based on the properties of CFGs for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

1. Write a CFG to generate all strings over {a,b} with equal number of a's and b's.
- Example: aabba, baaba etc.
- Solution:
S → AB
A → aA
A → ε
B → bB
B → ε

2. Write a CFG to generate all strings with equal number of a's and b's such that no 'aa' or 'bb' substrings are present.
- Example: abab, baba etc.
- Solution:
S → AB
A → Ac
A → ε
B → Bb
B → ε
c → a
b → b

3. Write a CFG to generate all palindromes over {a,b}.
- Example: aaba, abba, bbba etc.
- Solution:
S → A
A → aAa | bBb

[Additional points and examples can be added.]

The content is written in points in a formal tone as instructed without any emojis or external links. Let me know if you would like me to modify or expand the content.