## Unit 2 - Basic Parsing Techniques

Parsing is the process of analyzing a string of symbols, either in natural language, computer languages or data structures, conforming to the rules of a formal grammar. The term parsing comes from Latin pars (orationis), meaning part (of speech).

There are several basic parsing techniques, including:

1. **Top-down parsing**: This parsing technique starts from the top of the parse tree and works its way down. It begins with the start symbol and applies production rules to generate a string of symbols that matches the input string.

2. **Bottom-up parsing**: This parsing technique starts from the bottom of the parse tree and works its way up. It begins with the input string and applies production rules in reverse to derive the start symbol.

3. **Recursive descent parsing**: This is a top-down parsing technique that uses a set of recursive procedures to process the input. Each procedure corresponds to a non-terminal symbol in the grammar.

4. **Shift-reduce parsing**: This is a bottom-up parsing technique that uses a stack to hold the grammar symbols. The parser shifts input symbols onto the stack and applies production rules to reduce the stack's top symbols to a non-terminal symbol.

5. **Chart parsing**: This is a dynamic programming technique that is used to parse natural language. It builds a chart that records the intermediate results of parsing and reuses them to avoid redundant computations.

These are some of the basic parsing techniques. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the application.