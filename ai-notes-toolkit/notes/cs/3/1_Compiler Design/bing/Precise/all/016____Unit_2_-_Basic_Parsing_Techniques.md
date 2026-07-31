## Unit 2 - Basic Parsing Techniques

Parsing is the process of analyzing a string of symbols, either in natural language, computer languages or data structures, conforming to the rules of a formal grammar. The term parsing comes from Latin pars (orationis), meaning part (of speech).

There are several basic parsing techniques, including:

1. **Top-down parsing**: This parsing technique starts from the root of the parse tree and works its way down to the leaves. It attempts to match the input string with the leftmost derivation of the grammar.

2. **Bottom-up parsing**: This parsing technique starts from the leaves of the parse tree and works its way up to the root. It attempts to construct the rightmost derivation of the input string in reverse.

3. **Recursive descent parsing**: This is a top-down parsing technique that uses a set of recursive procedures to process the input. Each procedure usually corresponds to one of the non-terminals in the grammar.

4. **Shift-reduce parsing**: This is a bottom-up parsing technique that uses a stack to hold the grammar symbols. The parser shifts input symbols onto the stack until it recognizes a handle, which is a sequence of symbols on top of the stack that can be reduced to a non-terminal.

5. **Chart parsing**: This is a general parsing technique that can be used for both top-down and bottom-up parsing. It uses a data structure called a chart to keep track of all possible parses of the input.

These are some of the basic parsing techniques. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the application.