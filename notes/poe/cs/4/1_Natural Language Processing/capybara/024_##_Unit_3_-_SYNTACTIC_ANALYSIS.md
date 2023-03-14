## Unit 3 - SYNTACTIC ANALYSIS

Syntactic analysis, also known as parsing, is the process of analyzing a sequence of tokens or words to determine its grammatical structure. This unit focuses on the various techniques used for syntactic analysis. 

### Techniques for Syntactic Analysis

1. Top-down parsing: This technique starts with the root node of a tree and works its way down to the leaves. It is also known as a predictive parser, as it predicts which production rule to use next based on the input token.

2. Bottom-up parsing: This technique starts with the leaves of a tree and works its way up to the root node. It is also known as a shift-reduce parser, as it shifts input tokens onto a stack and then reduces them based on the production rules.

3. Recursive descent parsing: This technique uses a set of recursive procedures to parse the input. Each procedure corresponds to a non-terminal symbol in the grammar and calls other procedures to parse the corresponding sub-trees.

4. Earley parsing: This technique uses dynamic programming to parse the input. It uses a chart to keep track of the possible completions of each production rule and combines them to form the final parse tree.

### Mnemonics and Learning Tricks

1. "TOP-down is like a CEO: starts at the top and works down." 

2. "BOTTOM-up is like a worker: starts at the bottom and works up." 

### Advantages and Disadvantages

1. Top-down parsing is easy to implement and can be used for LL(k) grammars. However, it may be inefficient for large grammars or ambiguous languages.

2. Bottom-up parsing can handle a wider range of grammars, including LR(k) grammars. However, it may be difficult to implement and can be slow for complex grammars.

3. Recursive descent parsing is easy to understand and can be used for LL(k) grammars. However, it may suffer from left-recursion and require special handling.

4. Earley parsing can handle any context-free grammar and is efficient for ambiguous languages. However, it may require more memory than other techniques and be slower for LL(k) grammars.

### Applications

Syntactic analysis is used in various fields such as natural language processing, compilers, and programming languages. It is essential for understanding the structure of a language and generating correct output.