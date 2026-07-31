## Unit 2 - Basic Parsing Techniques

Parsing is the process of analyzing a string of symbols, either in natural language, computer languages or data structures, conforming to the rules of a formal grammar. The term parsing comes from Latin pars (orationis), meaning part (of speech).

There are several basic parsing techniques, including:

1. **Top-down parsing**: This parsing technique starts from the top of the parse tree and works its way down. It begins with the start symbol and applies production rules to generate a string of symbols. If the generated string matches the input string, the parse is successful.

2. **Bottom-up parsing**: This parsing technique starts from the bottom of the parse tree and works its way up. It begins with the input string and applies production rules in reverse to reduce the string to the start symbol. If the reduction is successful, the parse is successful.

3. **Recursive descent parsing**: This is a top-down parsing technique that uses a set of recursive procedures to process the input. Each procedure corresponds to a non-terminal symbol in the grammar.

4. **Shift-reduce parsing**: This is a bottom-up parsing technique that uses a stack to hold the grammar symbols. The parser shifts input symbols onto the stack and applies production rules to reduce the top of the stack to a non-terminal symbol.

5. **Predictive parsing**: This is a top-down parsing technique that uses a parsing table to determine which production rule to apply based on the current input symbol and the top of the stack.

These are some of the basic parsing techniques. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the application.