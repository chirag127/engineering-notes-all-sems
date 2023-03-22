 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Error Detection & Recovery for the notes of the Unit 4 - Symbol Tables

1. Error Detection
- Lexical Errors: Detect errors like invalid tokens, unmatched parentheses, etc. using lexical analysis.
- Syntactic Errors: Detect errors like incorrect syntax using parsing techniques. Parse tree can be used to detect erroneous syntax.
- Semantic Errors: Detect errors like type mismatches, undefined variables, etc. using semantic analysis.

2. Error Recovery
- Panic Mode: When an error is encountered, ignore all input until the parser can resume normal operation. This leads to missed errors and skipped input.
- Phrase level recovery: When an error is found, discard the current phrase/expression and attempt to parse the following input. Some erroneous phrases may get parsed.
- Error productions: Grammar can be modified to include error productions which can be used to parse erroneous input and allow parsing to continue. The parser can then resume normal operation if valid input is found.
- Nacional recovery: The parser keeps track of multiple possible paths and uses heuristic measures to pick an optimal path in case of errors. This allows maximum input to be parsed but can be complex to implement.

The above points cover the key aspects of error detection and recovery using various techniques. The methods aim to detect as many errors as possible and recover from them to continue parsing maximum possible input.