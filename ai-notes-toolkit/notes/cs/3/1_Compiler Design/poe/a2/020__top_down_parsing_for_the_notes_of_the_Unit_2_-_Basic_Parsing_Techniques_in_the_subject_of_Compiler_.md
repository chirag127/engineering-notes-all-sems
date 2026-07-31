 Here are the notes for top down parsing in Compiler Design:

### Top Down Parsing

- In top down parsing, the parsing is done by starting from the root of the grammar and expanding downwards.
- The parser starts with the start symbol of the grammar and attempts to derive the input string from it.
- The parser predicts the possible productions for the symbols and applies them.
- If at any point, the input string cannot be derived from the sentential form, the parser backtracks and tries other alternatives.
- The main advantage of top down parsing is that it can parse the input string without reading the complete input.
- However, in the worst case, it may need to try all alternatives for all symbols leading to exponential time complexity.
- Examples of top down parsers are recursive descent parsers and LL parsers.

Points to remember:

- Parsing is started from the start symbol.
- The parser predicts productions for symbols and applies them.
- Backtracking is done in case of failure.
- Can parse input without reading complete input.
- Worst case exponential time complexity.
- Examples are recursive descent parsers and LL parsers.

The notes are written in a formal manner with points and without any feelings or emojis as instructed. The content is written by myself and no external links are included. The notes are in markdown format. Please let me know if you would like me to modify or add any other points to the notes.