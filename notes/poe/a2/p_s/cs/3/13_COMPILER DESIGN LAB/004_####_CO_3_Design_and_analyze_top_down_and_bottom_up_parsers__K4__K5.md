 Here is the content in markdown format:

#### CO 3 Design and analyze top down and bottom up parsers. K4, K5.

Top down and bottom up parsers are two approaches to parsing input data/tokens.

- **Top down parsing**: In top down parsing, the parsing is done from top to bottom. The parsing starts from the root of the syntax tree and goes downwards. The input is matched against the patterns in the grammar rules from top to bottom. If the match is successful, the corresponding syntax tree is constructed. If the match fails, backtracking is done to try other alternatives. Some advantages of top down parsing are:
- It is intuitive and mimics how a human would parse the input.
- It can parse the input even with insufficient tokens as it uses backtracking.
- Some disadvantages are:
- Backtracking can be complex to implement.
- It may take exponential time in worst cases due to backtracking.

- **Bottom up parsing**: In bottom up parsing, the parsing is done from bottom to top. The parsing starts by matching individual tokens and combining them into larger and larger chunks. The syntax tree is constructed from leaves to the root. Some advantages of bottom up parsing are:
- It is more efficient as it avoids backtracking.
- The parsers are relatively simple to build.
- Some disadvantages are:
- It requires the entire input to start parsing.
- The parsing logic is not very intuitive.

Bottom up parsers are mainly of two types: Shift reduce parsers and LR parsers. Ascii diagrams, examples and applications of top down and bottom up parsers can also be included to aid learning. The choice between top down and bottom up parsing depends on the grammar and the application. Both approaches have their pros and cons and are used accordingly.