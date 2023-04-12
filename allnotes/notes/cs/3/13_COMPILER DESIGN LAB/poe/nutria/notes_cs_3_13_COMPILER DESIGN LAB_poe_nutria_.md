


## Course Outcome (CO) Bloom's Knowledge Level (KL)

* Remembering: The ability to recall knowledge acquired through study or experience.
* Understanding: The ability to comprehend the meaning, translation, or interpretation of instructions or problems.
* Applying: The ability to use acquired knowledge, facts, techniques, and rules in the completion of a task.
* Analyzing: The ability to break down information into its component parts to examine and understand the structure and relationships between them.
* Evaluating: The ability to make judgments based on criteria and standards through the comparison of different ideas or solutions.
* Creating: The ability to put parts or elements together to form a whole, with emphasis on producing a new or original structure or pattern.




### At the end of course, the student will be able to:
- Understand the fundamentals of computer programming
- Utilize various programming languages to create programs
- Comprehend the principles of software engineering
- Analyze and debug code
- Develop software applications




#### CO 1 Identify patterns, tokens & regular expressions for lexical analysis. K2, K4

* Lexical analysis is the process of breaking up a sequence of characters into tokens, which are sequences of characters that have a meaning.
* Patterns are used to identify tokens. They are usually expressed as strings of characters, or regular expressions.
* Tokens are sequences of characters that have a meaning. Examples of tokens include words, numbers, and punctuation marks.
* Regular expressions are strings of characters that are used to match patterns in a text. They are used to identify tokens in a text.
* K2 and K4 are two types of regular expressions. K2 is a set of patterns that match a single token, while K4 is a set of patterns that match multiple tokens.




#### CO 2 Design Lexical Analyser for a Given Language using C and LEX/YACC Tools K3, K5

1. Lexical Analysis is the process of analyzing a sequence of characters, such as a sentence, into its component parts, such as words, numbers, and punctuation marks.
2. Lexical Analyzers are used to recognize tokens, which are the basic elements of a programming language.
3. A Lexical Analyzer is written using the Lex/Yacc tools K3 and K5.
4. Lex/Yacc is a tool for generating a lexical analyzer from a set of user-specified rules.
5. The Lex tool is used to define the set of tokens to be recognized by the lexical analyzer.
6. The Yacc tool is used to define the grammar of the language and to generate the code for the lexical analyzer.
7. The C programming language is used to write the code for the lexical analyzer.
8. The lexical analyzer is used to recognize the tokens in a given language and to generate a parse tree for the given language.




#### CO 3 Design and analyze top down and bottom up parsers. K4, K5

1. **Top-down Parsing** is a type of parsing that begins at the root (start symbol) of a parse tree and works its way down the tree by using production rules to expand non-terminal nodes into terminal nodes.

2. **Bottom-up Parsing** is a type of parsing that begins at the leaves of a parse tree and works its way up the tree by using production rules to reduce terminal nodes into non-terminal nodes.

3. **K4** is a type of top-down parser that uses a left-most derivation strategy and is capable of parsing any context-free grammar.

4. **K5** is a type of bottom-up parser that uses a right-most derivation strategy and is capable of parsing any context-free grammar.




#### CO 4 Generate the intermediate code K4, K5

1. K4 and K5 are intermediate code instructions in the CO 4 assembly language. 
2. The K4 instruction is used to copy a value from a register to the accumulator. 
3. The K5 instruction is used to add the value stored in the accumulator to the value stored in a register. 
4. Both instructions are two-byte instructions, meaning they require two bytes of memory to store the instruction and its operand. 
5. K4 and K5 instructions are used to manipulate data stored in registers in the CO 4 assembly language. 
6. The K4 instruction takes the value stored in a register and copies it to the accumulator. 
7. The K5 instruction adds the value stored in the accumulator to the value stored in a register. 
8. Both instructions are used to perform arithmetic operations on data stored in registers.




#### CO 5 Generate machine code from the intermediate code forms K3, K4

* K3 and K4 are intermediate code forms that are used to generate machine code.
* K3 is an intermediate code form that consists of three-address instructions. These instructions include an operation code, two operands (which can be either registers or memory locations) and a result.
* K4 is an intermediate code form that consists of four-address instructions. These instructions include an operation code, three operands (which can be either registers or memory locations) and a result.
* Machine code is generated from intermediate code forms by mapping the instructions in the intermediate code to the instructions of the target machine. This mapping is done by a code generator.
* The code generator takes the intermediate code as input and produces the corresponding machine code as output. The machine code can then be executed by the target machine.




## Detailed Syllabus

1. Introduction to the Course: This section will provide an overview of the course, its objectives, and the topics that will be covered. 

2. Core Concepts: This section will cover the core concepts and principles of the course, such as key terms, theories, and processes. 

3. Applied Knowledge: This section will focus on how to apply the knowledge from the course in practical situations. It will include case studies, examples, and simulations. 

4. Assessment: This section will outline the assessment criteria, including the types of assessment tasks, the weighting of each task, and the marking scheme. 

5. Resources: This section will provide a list of recommended resources for further study, such as books, websites, and other materials.




### 1. Design and Implement a Lexical Analyzer for a Given Language Using C

* A lexical analyzer, also known as a lexer, is a program that takes an input string and breaks it into smaller components, such as words, numbers, and symbols.
* The lexer is responsible for recognizing the structure of the language and providing meaningful tokens that can be used by the parser.
* In C, a lexical analyzer can be implemented using a finite state machine.
* The finite state machine consists of a set of states and transitions between them. The transitions are triggered by specific characters or symbols in the input string. 
* The lexer needs to be able to recognize redundant symbols and ignore them. This can be done by keeping track of the current state and ignoring any redundant symbols that do not affect the transition to the next state.
* Once the lexer has identified the tokens, it can pass them to the parser for further processing.




### Spaces, Tabs, and New Lines

Spaces, tabs and new lines are used to separate and organize written content. They are important for readability and can help make a document easier to understand.

* Spaces are a single character that is used to create a space between words and sentences.
* Tabs are a single character that is used to create an indentation in a text document.
* New lines are a single character that is used to create a new line in a text document.

When writing a document, it is important to use spaces, tabs and new lines in order to make the document easier to read and understand. It is also important to use them consistently throughout the document.




### 2. Implementation of Lexical Analyzer using Lex Tool

1. A lexical analyzer is a program used in a compiler that takes input in the form of a sequence of characters and produces a sequence of tokens, which are strings with an assigned and thus identified meaning. 
2. The lexical analyzer is the first phase of a compiler and is used to recognize the tokens of the source code.
3. The Lex tool is a Unix utility used to generate lexical analyzers. It is a program that reads an input stream and produces a sequence of tokens that can be used by a parser.
4. The Lex tool takes as input a specification with a set of rules that describe the tokens to be recognized. Each rule consists of a regular expression that defines the pattern of the token, and an associated action that is executed when the pattern is matched.
5. The output of the Lex tool is a program written in the C language that implements the lexical analyzer. This program can be compiled and linked with the parser to form the complete compiler.
6. The Lex tool is a powerful and efficient tool for generating lexical analyzers and can be used for a wide range of programming languages.




### 3. Generate YACC Specification for a Few Syntactic Categories

* YACC (Yet Another Compiler Compiler) is a tool used for generating a parser. 
* YACC takes as input a context-free grammar that specifies the syntactic structure of the language to be parsed. 
* YACC produces a parser that reads an input stream and determines whether or not it is syntactically valid according to the specified grammar. 
* YACC works by generating a set of C functions to perform the parsing process.
* A YACC specification consists of four parts: declarations, rules, C code, and user subroutines. 
* The declarations section contains information about the tokens used in the grammar and any user-defined types. 
* The rules section contains the context-free grammar rules that define the syntactic categories of the language. 
* The C code section contains code that is used to perform actions when certain grammar rules are matched. 
* The user subroutines section contains user-defined functions that are called by the generated parser.




### a) Program to recognize a valid arithmetic expression that uses operator +, – , * and /

1. A program to recognize a valid arithmetic expression should begin by parsing the input string. This can be done by breaking the string into tokens and then analyzing each token individually. 
2. The tokens can be identified by looking for the operators (+, –, *, and /) and operands (numbers). 
3. The program should then check that the expression is valid by verifying that the operators and operands are in the correct order. 
4. The program should also check that the expression is complete by verifying that all the operators and operands are present. 
5. Finally, the program should evaluate the expression by performing the appropriate calculations. This can be done using a stack-based algorithm.




### b) Program to recognize a valid variable which starts with a letter followed by any number of letters or digits

- A valid variable must begin with a letter and can contain any combination of letters and digits.
- Variables are case-sensitive, so a variable named `myVar` is not the same as one named `MyVar`.
- Variables can have a maximum length of 32 characters.
- Variables cannot contain any whitespace characters, such as spaces or tabs.
- Variables should be descriptive, but not too long. For example, `myVariable` is better than `variable1`.




### c) Implementation of Calculator using LEX and YACC

1. LEX is a computer program that generates lexical analyzers (also known as "scanners" or "lexers"). It is commonly used to convert a stream of characters into a stream of tokens.

2. YACC is a computer program that generates a parser from a set of grammar rules. It is commonly used to convert a stream of tokens into a parse tree.

3. Lex and Yacc are commonly used together to create a calculator program. The Lex program is used to tokenize the input stream and the Yacc program is used to create the parse tree.

4. The Lex program is used to define the tokens that the calculator program should recognize. This includes keywords, numbers, operators, and other symbols.

5. The Yacc program is used to define the grammar rules that the calculator program should obey. This includes precedence rules, associativity rules, and other rules.

6. The Lex and Yacc programs are combined together to create the calculator program. The output of the Lex program is fed into the Yacc program, which produces the parse tree.

7. The parse tree is then used to create the calculator program. This includes code to evaluate the expression and produce the result.




### d) Convert the BNF rules into YACC form and write code to generate abstract syntax tree

1. BNF (Backus-Naur Form) is a notation used to describe a formal language. It consists of a set of rules that define the structure of the language.

2. YACC (Yet Another Compiler Compiler) is a parser generator that takes a BNF grammar as input and produces a parser as output.

3. The output of a YACC parser is an abstract syntax tree (AST). An AST is a hierarchical representation of the source code, which can be used to analyse the code and generate code in other languages.

4. Converting a BNF grammar into YACC form involves writing the grammar in the YACC syntax, which is similar to the BNF syntax but contains additional rules and keywords.

5. Once the grammar is written in YACC form, it can be used to generate a parser that will generate an AST for the source code.




### 4. Write program to find ε – closure of all states of any given NFA with ε transition

* To find the ε-closure of any given state in a NFA with ε transitions, the algorithm must first identify the transitions from the given state to other states with ε transitions. 
* The algorithm should then identify the states that can be reached from the given state by following the ε transitions. 
* This is done by recursively searching for ε-transitions from the given state and any states that can be reached from it. 
* Once the set of states that can be reached from the given state by following ε-transitions is identified, the ε-closure of the given state is the union of the given state and all the states that can be reached from it by following ε-transitions. 
* The algorithm should then repeat the process for each of the states in the ε-closure of the given state, until all the states in the NFA with ε-transitions have been visited. 
* Finally, the algorithm should return the ε-closure of the given state.




### 5. Write program to convert NFA with ε transition to NFA without ε transition

1. Understand the concept of NFA with ε transition and NFA without ε transition.
2. Take a NFA with ε transition as input.
3. Construct a new NFA without ε transition from the input NFA.
4. Construct a transition table for the new NFA.
5. Create a program to implement the transition table.
6. Test the program with sample inputs and outputs.
7. Modify the program if needed.
8. The program should be able to convert any NFA with ε transition to NFA without ε transition.




### 6. Write program to convert NFA to DFA

1. First, define the Non-Deterministic Finite Automata (NFA) as a 5-tuple (Q, Σ, δ, q0, F) with the following components:
    - Q: A finite set of states
    - Σ: A finite set of symbols, called the alphabet
    - δ: A transition function
    - q0: The initial state
    - F: A set of final states
2. To convert an NFA to a Deterministic Finite Automata (DFA), the following steps should be taken:
    - Create a new transition table for the DFA, with the same number of states as the NFA
    - For each state in the NFA, create a corresponding state in the DFA
    - For each transition in the NFA, create a corresponding transition in the DFA
    - For each state in the NFA, add the transitions for all possible symbols in the alphabet
    - Add the initial and final states of the DFA, based on the initial and final states of the NFA
3. Finally, the program should be tested to ensure that it is functioning correctly.




### 7. Write program to minimize any given DFA

1. A DFA (Deterministic Finite Automata) is a finite state machine that can be used to recognize patterns in a given string of symbols.
2. The process of minimizing a DFA is to reduce the number of states in the machine while still maintaining the same language.
3. The algorithm to minimize a DFA involves two steps:
    * Step 1: Construct the transition table of the DFA.
    * Step 2: Construct the equivalent minimized DFA by merging states that have the same behavior.
4. The transition table of a DFA is a 2-dimensional array which contains the transitions of the DFA. The transition table is constructed by filling out the transitions for each state.
5. To construct the minimized DFA, states are merged together if they have the same behavior. This means that they have the same transitions for each input symbol.
6. Once the minimized DFA is constructed, a program can be written to minimize any given DFA. The program should take the transition table of the DFA as input and output the minimized DFA.




### 8. Develop an Operator Precedence Parser for a Given Language

1. An operator precedence parser is a type of parser used to analyze the syntax of a programming language. 
2. It is based on the concept of operator precedence, which defines the order in which operators are evaluated in an expression. 
3. An operator precedence parser is a top-down parser that uses a stack to keep track of operators and operands in an expression. 
4. It begins by reading the input expression from left to right and pushing each operator onto the stack. 
5. When an operand is encountered, the parser checks the top of the stack to see if there is a higher-precedence operator. 
6. If there is, the parser pops the stack and evaluates the operator with the operand. 
7. This process is repeated until the stack is empty, at which point the expression has been completely evaluated. 
8. Operator precedence parsers can be used to parse a wide variety of languages, including arithmetic expressions, boolean expressions, and programming languages.




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




### 10. Construct a recursive descent parser for an expression

A recursive descent parser is a type of parser that uses recursive functions to parse input strings. It is often used in the context of computer language processing and is one of the most common parsing techniques.

* A recursive descent parser consists of a set of mutually recursive functions, each of which corresponds to a non-terminal symbol of the grammar.
* The parser begins by calling the function associated with the start symbol of the grammar.
* Each function attempts to match the input string with the symbols of its production.
* If the input string matches the symbols of the production, the function returns success and the parser continues with the function associated with the next symbol of the production.
* If the input string does not match the symbols of the production, the function returns failure and the parser backtracks to the previous function.
* The parser continues in this manner until it reaches the end of the input string or it fails to match the symbols of the production.




### 11. Construct a Shift Reduce Parser for a given language

1. A shift-reduce parser is a type of parser used in natural language processing and computer science. It is a type of bottom-up parser that works by shifting input symbols onto a stack and reducing them according to a set of rules.
2. A shift-reduce parser takes a sequence of tokens (words, punctuation, etc.) as input and produces a parse tree as output. The parser works by shifting tokens onto a stack, and then reducing them according to a set of rules.
3. The rules of a shift-reduce parser are specified in the form of a context-free grammar. A context-free grammar is a set of production rules that describe how a language can be constructed.
4. To construct a shift-reduce parser for a given language, the grammar of the language must first be specified. This can be done manually or by using a parser generator.
5. Once the grammar has been specified, the shift-reduce parser can be constructed. This involves writing code to implement the shift and reduce operations specified by the grammar.
6. The shift-reduce parser is then tested by feeding it a sequence of tokens and checking the output. If the output is correct, the parser can be used to parse sentences in the language.




### 12. Write a Program to Perform Loop Unrolling

1. Loop unrolling is a technique used to optimize computer programs by replacing a loop with multiple copies of the loop body. 
2. It is used to reduce the number of times the loop is executed, thus improving the performance of the program. 
3. The basic idea behind loop unrolling is to reduce the number of loop iterations by replacing the loop with multiple copies of the loop body. 
4. This can be done manually by the programmer, or automatically by the compiler.
5. In order to manually unroll a loop, the programmer must analyze the loop and determine how many times it should be unrolled. 
6. Then, the loop body must be copied the appropriate number of times and the loop condition must be modified accordingly. 
7. The compiler can also automatically unroll loops, if the programmer has enabled this optimization. 
8. Automatic loop unrolling can be enabled by using compiler flags or by using specific compiler directives. 
9. Loop unrolling can improve the performance of a program by reducing the number of loop iterations and by reducing the number of branches and memory accesses. 
10. It can also reduce the amount of code that needs to be executed, thus reducing the execution time of the program.




### 13. Write a Program to Perform Constant Propagation

* Constant propagation is a process in which the values of variables are propagated throughout a program.
* This process can be used to optimize the performance of a program by reducing the number of operations that need to be performed.
* Constant propagation is typically done by analyzing the program code and replacing variables with their constant values wherever possible.
* The process of constant propagation involves analyzing the program code and replacing variables with their constant values wherever possible.
* This is done by analyzing the statements in the program and identifying which variables are constants.
* Once the constants have been identified, they can be propagated through the program by replacing the variables with their constant values.
* Constant propagation can also be used to detect and eliminate dead code, which is code that is never executed.
* Constant propagation is an important optimization technique that can improve the performance of a program by reducing the number of operations that need to be performed.




### 14. Implement Intermediate Code Generation for Simple Expressions

* Intermediate code generation is the process of translating a high-level programming language into an intermediate language, which can be further processed into machine code.
* The intermediate language is a language that is closer to the machine code than the high-level language, and is more suitable for further processing.
* Simple expressions are expressions that involve only one operator, such as addition, subtraction, multiplication, and division.
* The intermediate code generation for simple expressions involves the following steps:
    1. Identify the type of the expression.
    2. Generate the appropriate intermediate code for the expression.
    3. Generate the code for the corresponding operations.
    4. Generate the code for the result.
* The code generated for a simple expression should be optimized to reduce the number of instructions and the amount of memory used.




### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language

1. The 8086 assembly language is the language used to program the 8086 microprocessor.

2. The three address code is an intermediate representation of a program. It is a representation of the program in which each statement is represented as an operation on three operands.

3. The back end of the compiler is responsible for generating the 8086 assembly language from the three address code.

4. The back end of the compiler must first convert the three address code into a sequence of assembly language instructions.

5. This can be done by mapping each three address code statement to the corresponding assembly language instruction.

6. The back end of the compiler must also take care of other tasks such as allocating registers and memory locations, generating code for jumps and labels, and performing optimization.




### Instructions for Assembling and Running Code Using an 8086 Assembler

1. Install an 8086 assembler on your computer. Popular assemblers include [MASM](https://en.wikipedia.org/wiki/Microsoft_Macro_Assembler) and [TASM](https://en.wikipedia.org/wiki/Turbo_Assembler).
2. Create a text file containing the assembly code. This code should be written in the 8086 assembly language, which is a low-level language used to program the 8086 processor.
3. Compile the code using the assembler. This will generate an object file containing the machine code instructions for the 8086 processor.
4. Link the object file with any other required libraries and create an executable file. This executable file can then be run on the 8086 processor.
5. Test the program by running it on the 8086 processor.
6. If the program does not run as expected, debug the code and repeat steps 3-5.




### Add, Sub, Jump etc.

* Add: Addition is a mathematical operation that involves combining two or more numbers to produce a sum.
* Sub: Subtraction is a mathematical operation that involves taking one number away from another to produce a difference.
* Jump: Jumping is the act of propelling oneself rapidly upward or forward by a muscular effort from a position of rest, often in the context of a sport or other physical activity.




### Note: The Instructor may add/delete/modify/tune experiments, wherever he/she feels in a justified manner
- Instructors may add experiments to the course curriculum to provide students with a better understanding of the subject matter.
- Instructors may delete experiments from the course curriculum if they feel the experiment does not further the student's understanding of the subject matter.
- Instructors may modify or tune experiments to better suit the student's level of understanding or to adjust the experiment to fit the available resources.
- Instructors may make changes to experiments wherever they feel it is necessary and justified.




### It is also suggested that open source tools should be preferred to conduct the lab

1. C is a general-purpose programming language that is widely used for software development. It is a powerful language and has been used to create a wide range of systems, from embedded systems to operating systems.
2. C++ is an object-oriented programming language, and it is an extension of the C language. It is used for a variety of tasks, from low-level system programming to high-level application development.
3. Lex (or Flex) is a lexical analyzer generator, which is used to generate lexers for compilers. It is used to tokenize source code and provide the tokens to the parser.
4. Flex is a fast lexical analyzer generator, which is used to generate lexers for compilers. It is used to tokenize source code and provide the tokens to the parser.




### YACC Tools (Unix/Linux Utilities)

1. YACC (Yet Another Compiler Compiler) is a Unix/Linux utility used to create parsers for programming languages.
2. YACC is a tool for generating parsers from a formal grammar. It is a compiler-compiler that generates a C program from a given grammar.
3. YACC uses LALR (Look-Ahead Left-to-Right) parsing technique to parse the input. This technique is based on the concept of a predictive parser.
4. YACC is used to generate a parser for a given grammar. The parser generated by YACC can be used to parse the input program and detect errors in the syntax.
5. YACC can also be used to generate a C program from a given grammar. This C program can be used to parse the input program and detect errors in the syntax.
6. YACC is a powerful tool for creating parsers for programming languages. It can be used to create parsers for languages such as C, C++, Java, and others.




### Curriculum & Evaluation Scheme CS & CSE (V & VI semester) 19

1. **Curriculum**: The curriculum for V and VI semester of Computer Science and Computer Science Engineering consists of the following core and elective courses: 
    - Core Courses: 
        - Computer Architecture 
        - Operating Systems 
        - Compiler Design 
        - Computer Networks 
        - Database Management Systems 
        - Design and Analysis of Algorithms 
    - Elective Courses: 
        - Advanced Computer Networks 
        - Artificial Intelligence 
        - Software Engineering 
        - Natural Language Processing 
        - Computer Graphics 
        - Cryptography 

2. **Evaluation Scheme**: Evaluation of the courses is done through a combination of exams, assignments, projects, and presentations. 
    - Exams: 
        - Each course has a midterm and a final exam, each of which carries 25% of the total marks allotted for the course. 
    - Assignments: 
        - Assignments are given to evaluate the understanding of the concepts taught in the course. 
        - Assignments carry 10% of the total marks allotted for the course. 
    - Projects: 
        - Projects are given to evaluate the application of the concepts taught in the course. 
        - Projects carry 20% of the total marks allotted for the course. 
    - Presentations: 
        - Presentations are given to evaluate the communication and presentation skills of the student. 
        - Presentations carry 10% of the total marks allotted for the course. 
    - Total Marks: 
        - The total marks allotted for each course is 100.

