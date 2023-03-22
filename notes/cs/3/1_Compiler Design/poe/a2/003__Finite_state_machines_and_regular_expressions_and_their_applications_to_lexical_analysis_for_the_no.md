 Here are the notes in markdown format on the given topic:

### Finite state machines and regular expressions and their applications to lexical analysis

1. Finite state machines:
 - Finite state machines (FSMs) are abstract machines that can be in only one of a finite number of states at a time.
 - The FSM changes state based on inputs and the current state.
 - The behavior of a FSM is determined by its transition function, which takes the current state and input and returns a new state.
 - FSMs are widely used to model the behavior of systems, devices, algorithms, etc. with inputs and outputs and finite possible states.

2. Regular expressions:
 - Regular expressions are patterns used to match strings. They are written in a notation that expresses common patterns concisely.
 - Regular expressions can be converted into FSMs and vice-versa. This allows FSMs and regular expressions to be used interchangeably in many applications.
 - The applications of regular expressions include lexical analysis, parsing, pattern matching, etc. A FSM that recognizes patterns described by a regular expression is called a deterministic finite automaton (DFA).

3. Lexical analysis:
 - Lexical analysis is the first phase of a compiler which breaks up the input into tokens. Tokens are basic elements that make up a programming language.
 - Lexers use FSMs or regular expressions to recognize patterns in the input that correspond to tokens. The input string is broken into tokens as the lexer matches patterns and consumes characters from the input.
 - The list of tokens produced by the lexer is used as input to the parser in a compiler. The lexer identifies the types of tokens (identifiers, keywords, literals, operators, etc.) and the parser uses this to structure the input and create a syntax tree.

4. Applications:
 - FSMs and regular expressions have a wide range of applications in computer science and engineering including:
   - Lexical analysis as discussed above
   - Pattern matching
   - Syntax analysis
   - Protocol analysis
   - Image processing
   - Speech recognition
   - Manufacturing
   - etc.
 - The simplicity and mathematical basis of FSMs and regular expressions allow them to be widely applied to model systems with complex but finite behavior. They provide a powerful yet understandable means to formalize patterns and processes.