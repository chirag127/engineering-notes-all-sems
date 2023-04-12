

## Course Outcome (CO) Bloom’s Knowledge Level (KL)

Course outcomes (COs) are statements that describe the knowledge, skills, and abilities that students should possess upon completion of a course. These outcomes are aligned with the course objectives and are used to assess the effectiveness of the course in achieving its goals.

Bloom’s taxonomy is a framework for categorizing educational goals and objectives into different levels of complexity and specificity. The taxonomy consists of six levels of cognitive learning, ranging from lower-order thinking skills (LOTS) to higher-order thinking skills (HOTS). These levels are:

1. **Remembering**: The ability to recall or retrieve previously learned information.
2. **Understanding**: The ability to comprehend the meaning of the material.
3. **Applying**: The ability to use learned material in new and concrete situations.
4. **Analyzing**: The ability to break down material into its component parts so that its organizational structure may be understood.
5. **Evaluating**: The ability to make judgments about the value of ideas or materials.
6. **Creating**: The ability to put parts together to form a new whole.

Each course outcome can be mapped to a specific level of Bloom’s taxonomy, indicating the level of cognitive learning that is expected of students in achieving that outcome. This mapping can help instructors design assessments and activities that are aligned with the desired level of cognitive learning for each outcome.



### At the end of the course, the student will be able to:
1. Demonstrate a comprehensive understanding of the course material.
2. Apply the concepts and theories learned in the course to real-world situations.
3. Analyze and evaluate information critically and effectively.
4. Communicate ideas and arguments clearly and effectively in both written and oral forms.
5. Work collaboratively with others to achieve common goals.
6. Demonstrate ethical and professional behavior in academic and professional settings.
7. Engage in lifelong learning and professional development.



#### CO 1 Identify patterns, tokens & regular expressions for lexical analysis. K2, K4

Lexical analysis is the process of converting a sequence of characters into a sequence of tokens. It is the first phase of the compilation process. The main objective of lexical analysis is to identify the tokens, patterns, and regular expressions in the given input.

1. **Patterns**: A pattern is a set of rules that define the structure of a token. It is used to identify the tokens in the input. For example, a pattern for an identifier can be a letter followed by zero or more letters or digits.

2. **Tokens**: A token is a sequence of characters that represents a single unit of information. It is the smallest unit of information that can be processed by the compiler. Tokens can be keywords, identifiers, constants, operators, and punctuations.

3. **Regular expressions**: A regular expression is a pattern that describes a set of strings. It is used to specify the patterns for the tokens. Regular expressions are used to define the rules for identifying the tokens in the input.

In summary, lexical analysis involves identifying the patterns, tokens, and regular expressions in the given input. These concepts are essential for the process of converting a sequence of characters into a sequence of tokens.



#### CO 2 Design Lexical analyser for given language using C and LEX /YACC tools K3, K5

- A lexical analyzer is a program that takes a stream of characters as input and produces a stream of tokens as output.
- C is a general-purpose programming language that can be used to implement a lexical analyzer.
- LEX is a tool that generates lexical analyzers. It takes a specification of the tokens to be recognized, in the form of regular expressions, and generates C code that implements the lexical analyzer.
- YACC (Yet Another Compiler-Compiler) is a tool that generates parsers. It takes a specification of the grammar of the language to be parsed, in the form of production rules, and generates C code that implements the parser.
- To design a lexical analyzer for a given language using C and LEX/YACC tools, one would need to:
    1. Define the tokens to be recognized by the lexical analyzer, using regular expressions.
    2. Write the LEX specification, which includes the regular expressions and associated C code to be executed when a token is recognized.
    3. Use the LEX tool to generate C code for the lexical analyzer.
    4. Write the YACC specification, which includes the production rules for the grammar of the language to be parsed.
    5. Use the YACC tool to generate C code for the parser.
    6. Write additional C code, if necessary, to implement the lexical analyzer and parser.
    7. Compile and link the generated C code with the additional C code to produce the final lexical analyzer and parser program.



#### CO 3 Design and analyze top down and bottom up parsers. K4, K5

Top-down parsers and bottom-up parsers are two types of parsers used in the process of translating source code into an executable program.

1. **Top-down parsers** start by constructing the most general structure of the program and then gradually refine it by adding more specific details. This approach is also known as recursive descent parsing. Top-down parsers use a set of production rules to generate a parse tree, starting from the start symbol and working downwards.

2. **Bottom-up parsers**, on the other hand, start by identifying the most specific elements of the program and then gradually combine them to form more general structures. This approach is also known as shift-reduce parsing. Bottom-up parsers use a set of reduction rules to generate a parse tree, starting from the leaves and working upwards.

Both top-down and bottom-up parsers have their advantages and disadvantages. Top-down parsers are generally easier to implement and understand, but they may not be able to handle certain types of grammars, such as left-recursive grammars. Bottom-up parsers, on the other hand, can handle a wider range of grammars, but they can be more difficult to implement and understand.

When designing and analyzing top-down and bottom-up parsers, it is important to consider factors such as the type of grammar being used, the efficiency of the parsing algorithm, and the ease of implementation and maintenance. Ultimately, the choice between a top-down and a bottom-up parser will depend on the specific requirements of the program being developed.



#### CO 4 Generate the intermediate code K4, K5

Intermediate code generation is the process of converting a source code into an intermediate representation that is independent of the target machine. This intermediate representation is then used by the code generator to produce the final machine code. The intermediate code is usually in the form of a low-level or machine-like language, such as three-address code or quadruples.

K4 and K5 are two types of intermediate code that can be generated. K4 is a type of three-address code, while K5 is a type of quadruple code.

Three-address code is a type of intermediate code where each instruction has at most three operands. The operands can be variables, constants, or temporary variables. The instructions in three-address code are usually in the form of `x = y op z`, where `x`, `y`, and `z` are the operands and `op` is the operator.

Quadruple code is a type of intermediate code where each instruction is represented as a quadruple, consisting of an operator, two operands, and a result. The operands and result can be variables, constants, or temporary variables. The instructions in quadruple code are usually in the form of `(op, y, z, x)`, where `op` is the operator, `y` and `z` are the operands, and `x` is the result.

In summary, CO 4 is the process of generating the intermediate code K4 or K5, which are two types of intermediate code that can be used by the code generator to produce the final machine code. K4 is a type of three-address code, while K5 is a type of quadruple code. Both types of intermediate code are low-level or machine-like languages that are independent of the target machine.



#### CO 5 Generate machine code from the intermediate code forms K3, K4

- Intermediate code forms K3 and K4 are used to generate machine code.
- Machine code is the lowest-level representation of a program, consisting of binary instructions that can be executed directly by the computer's hardware.
- Intermediate code forms K3 and K4 are higher-level representations of a program, designed to be more human-readable and easier to manipulate than machine code.
- The process of generating machine code from intermediate code forms K3 and K4 involves translating the higher-level instructions into equivalent sequences of machine code instructions.
- This translation is typically performed by a compiler or assembler, which takes the intermediate code as input and produces machine code as output.
- The resulting machine code can then be loaded into memory and executed by the computer's hardware.
- The use of intermediate code forms K3 and K4 allows for greater portability of programs, as the same intermediate code can be translated into machine code for different hardware platforms.
- It also allows for easier optimization of the generated machine code, as the higher-level intermediate code can be more easily analyzed and manipulated by the compiler or assembler.



## DETAILED SYLLABUS

A detailed syllabus is a comprehensive outline of the topics, assignments, and assessments that will be covered in a course. It is typically provided by the instructor at the beginning of the course and serves as a guide for students to understand the expectations and requirements of the course.

Some key components of a detailed syllabus may include:

1. Course description: A brief overview of the course, including its objectives and goals.
2. Course schedule: A list of topics and assignments, along with their due dates, that will be covered throughout the course.
3. Grading policy: An explanation of how grades will be calculated, including the weight of each assignment and assessment.
4. Attendance policy: The instructor's expectations for attendance and participation in the course.
5. Course materials: A list of required and recommended textbooks, articles, and other resources for the course.
6. Contact information: The instructor's contact information, including office hours and preferred methods of communication.
7. Academic integrity policy: A statement on the importance of academic integrity and the consequences of academic dishonesty.

A detailed syllabus is an important tool for students to succeed in a course. It provides a clear roadmap of what is expected and allows students to plan their time and efforts accordingly. It is important for students to review the syllabus carefully and ask the instructor for clarification if anything is unclear.



### Design and Implementation of a Lexical Analyzer for a Given Language Using C

A lexical analyzer, also known as a lexer or scanner, is a program that takes a stream of characters as input and produces a stream of tokens as output. The tokens represent the smallest meaningful units of the input, such as keywords, identifiers, and operators.

Here are the steps to design and implement a lexical analyzer for a given language using C:

1. **Define the tokens**: The first step is to define the tokens that the lexical analyzer will recognize. These tokens will depend on the language being analyzed. For example, if the language is C, the tokens might include keywords such as `if`, `while`, and `return`, as well as identifiers, operators, and punctuation.

2. **Write regular expressions for the tokens**: Once the tokens have been defined, the next step is to write regular expressions for each token. A regular expression is a pattern that describes a set of strings. For example, the regular expression for an identifier in C might be `[a-zA-Z_][a-zA-Z0-9_]*`, which matches a string that starts with a letter or underscore, followed by zero or more letters, digits, or underscores.

3. **Implement the lexical analyzer**: The lexical analyzer can be implemented using a finite automaton, which is a machine that reads the input one character at a time and transitions between states based on the current character and the current state. The states represent the progress that the lexical analyzer has made in recognizing a token. When the lexical analyzer reaches an accepting state, it has recognized a complete token and can output it.

4. **Ignore redundant characters**: The lexical analyzer should be designed to ignore redundant characters, such as whitespace and comments. This can be done by adding states to the finite automaton that represent the lexical analyzer being in the middle of a comment or a sequence of whitespace characters.

In summary, to design and implement a lexical analyzer for a given language using C, one needs to define the tokens, write regular expressions for the tokens, implement the lexical analyzer using a finite automaton, and design the lexical analyzer to ignore redundant characters. This process can be applied to any language, and the resulting lexical analyzer can be used as the first stage of a compiler or interpreter for that language.



### Spaces, Tabs and New Lines

- **Spaces** are characters used to separate words or other elements in text. They are represented by the ASCII code 32 or the Unicode code point U+0020.
- **Tabs** are characters used to align text in columns. They are represented by the ASCII code 9 or the Unicode code point U+0009. The width of a tab character is usually equivalent to 8 spaces, but this can vary depending on the software being used.
- **New lines** are characters used to indicate the end of a line of text and the beginning of a new one. They are represented by the ASCII code 10 or the Unicode code point U+000A. In some systems, a new line is represented by a combination of a carriage return (ASCII code 13 or Unicode code point U+000D) and a line feed (ASCII code 10 or Unicode code point U+000A).

These characters are used to format text and improve its readability. They are often used in programming languages to improve the readability of code. It is important to use them consistently to ensure that text is properly formatted and easy to read.



### 2. Implementation of Lexical Analyzer using Lex Tool

Lex is a tool used to generate lexical analyzers, which are programs that can recognize lexical patterns in text. Lex reads an input stream specifying the lexical analyzer and outputs source code implementing the lexer in the C programming language.

Here are the steps to implement a lexical analyzer using Lex tool:

1. Write a Lex specification file that defines the rules for token recognition. This file typically has a `.l` extension.
2. Run the Lex tool on the specification file to generate a C source file. The generated file is commonly named `lex.yy.c`.
3. Compile the generated C source file using a C compiler to create an executable program.
4. Run the executable program to perform lexical analysis on the input text.

The Lex specification file consists of three sections separated by `%%`:

1. Definitions section: This section contains definitions of regular expressions and macros that can be used in the rules section.
2. Rules section: This section contains the rules for token recognition. Each rule consists of a regular expression followed by an action to be performed when the regular expression is matched.
3. User code section: This section contains C code that is copied verbatim to the generated C source file. It can contain auxiliary functions and declarations needed by the actions in the rules section.

Lex uses regular expressions to specify the patterns to be matched. When the generated lexical analyzer is run, it reads the input text and tries to match the regular expressions in the order they are specified in the rules section. When a match is found, the corresponding action is executed. The action can return a token to the parser or perform other tasks such as updating a symbol table or counting the number of lines in the input text.

In summary, Lex is a powerful tool for generating lexical analyzers. It allows the programmer to specify the rules for token recognition using regular expressions and actions written in C. The generated lexical analyzer can be used as a component in a compiler or interpreter for a programming language, or as a standalone program for text processing tasks.



### 3. Generate YACC specification for a few syntactic categories.

YACC (Yet Another Compiler-Compiler) is a tool that generates a parser for a given grammar. The parser takes as input a stream of tokens and produces a parse tree based on the grammar rules specified in the YACC specification.

Here are the steps to generate a YACC specification for a few syntactic categories:

1. Define the tokens: The first step in writing a YACC specification is to define the tokens that will be used in the grammar. This is done using the `%token` directive. For example, to define tokens for identifiers, numbers, and basic arithmetic operators, the following lines could be added to the YACC specification:

```
%token IDENTIFIER NUMBER PLUS MINUS TIMES DIVIDE
```

2. Write the grammar rules: The next step is to write the grammar rules for the syntactic categories. Each rule is written in the form: `result: expression1 | expression2 | ... | expressionN ;` where `result` is the non-terminal symbol that the rule defines, and `expression1`, `expression2`, ..., `expressionN` are the possible expressions that can derive the `result`. For example, to define a rule for an arithmetic expression, the following rule could be added to the YACC specification:

```
expr: expr PLUS term
    | expr MINUS term
    | term
    ;
```

3. Add actions: YACC allows actions to be associated with each rule. These actions are written in C code and are executed when the rule is applied during parsing. Actions can be used to build the parse tree, perform semantic analysis, or generate code. For example, to build a parse tree for an arithmetic expression, the following actions could be added to the rule for `expr`:

```
expr: expr PLUS term { $$ = make_node('+', $1, $3); }
    | expr MINUS term { $$ = make_node('-', $1, $3); }
    | term { $$ = $1; }
    ;
```

4. Write the remaining code: In addition to the grammar rules and actions, the YACC specification may also include other code, such as declarations, auxiliary functions, and the main function. This code is written in C and is placed in the appropriate sections of the YACC specification.

Once the YACC specification is complete, it can be processed by the YACC tool to generate a parser for the specified grammar. This parser can then be used to parse input and produce a parse tree based on the grammar rules and actions specified in the YACC specification.



### a) Program to recognize a valid arithmetic expression that uses operator +, – , * and /.

A valid arithmetic expression is a string of characters that represents a mathematical calculation. It can contain numbers, operators, and parentheses. The operators that can be used in this expression are +, -, *, and /. To recognize a valid arithmetic expression, the following rules must be followed:

1. The expression must start and end with a number or a closing parenthesis.
2. The operators +, -, *, and / must be surrounded by numbers or parentheses.
3. Parentheses must be used in pairs, with an opening parenthesis followed by a closing parenthesis.
4. The expression must not contain any other characters except for numbers, operators, and parentheses.

Here is an example of a program in Python that can recognize a valid arithmetic expression:

```python
import re

def is_valid_expression(expression):
    # Check if the expression starts and ends with a number or a closing parenthesis
    if not re.match(r'^[\d\)]', expression) or not re.match(r'[\d\)]$', expression):
        return False

    # Check if the operators are surrounded by numbers or parentheses
    if re.search(r'[\+\-\*\/]{2,}', expression) or re.search(r'[\+\-\*\/][^\d\(\)]', expression) or re.search(r'[^\d\(\)][\+\-\*\/]', expression):
        return False

    # Check if the parentheses are used in pairs
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    if stack:
        return False

    # Check if the expression contains any other characters
    if re.search(r'[^\d\+\-\*\/\(\)]', expression):
        return False

    return True
```

This program uses regular expressions to check if the expression follows the rules mentioned above. The function `is_valid_expression` takes an expression as an input and returns `True` if the expression is valid and `False` otherwise. The program can be modified to recognize expressions with other operators or to perform other tasks.



### b) Program to recognize a valid variable which starts with a letter followed by any number of letters or digits.

A valid variable name in most programming languages must start with a letter or an underscore, followed by any number of letters, digits, or underscores. Here is an example of a program that checks if a given string is a valid variable name:

```python
import re

def is_valid_variable_name(name):
    # Regular expression to match a valid variable name
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    # Use the search method to check if the name matches the pattern
    if re.search(pattern, name):
        return True
    else:
        return False
```

This program uses a regular expression to define the pattern of a valid variable name. The `^` symbol at the beginning of the pattern indicates that the match must start at the beginning of the string. The `[a-zA-Z_]` part of the pattern matches a single character that is either a letter or an underscore. The `[a-zA-Z0-9_]*` part of the pattern matches zero or more characters that are either letters, digits, or underscores. The `$` symbol at the end of the pattern indicates that the match must end at the end of the string.

The `is_valid_variable_name` function takes a string as an input and returns `True` if the string is a valid variable name, and `False` otherwise. The function uses the `search` method from the `re` module to check if the input string matches the pattern of a valid variable name.

Here are some examples of how the `is_valid_variable_name` function can be used:

```python
print(is_valid_variable_name('myVariable')) # True
print(is_valid_variable_name('_private_var')) # True
print(is_valid_variable_name('2nd_var')) # False
print(is_valid_variable_name('var-with-hyphen')) # False
```

In these examples, the `is_valid_variable_name` function correctly identifies that `myVariable` and `_private_var` are valid variable names, while `2nd_var` and `var-with-hyphen` are not. This is because `2nd_var` starts with a digit, and `var-with-hyphen` contains a hyphen, which is not a valid character in a variable name.



### c) Implementation of Calculator using LEX and YACC

LEX and YACC are tools used for generating lexical analyzers and parsers, respectively. They can be used to implement a calculator by following these steps:

1. Define the grammar for the calculator: The first step in implementing a calculator using LEX and YACC is to define the grammar for the calculator. This includes defining the rules for expressions, operators, and operands.

2. Write the LEX file: The LEX file contains the rules for tokenizing the input. This includes defining the regular expressions for recognizing numbers, operators, and other tokens.

3. Write the YACC file: The YACC file contains the rules for parsing the input. This includes defining the grammar rules and the actions to be taken when a rule is matched.

4. Compile the LEX and YACC files: The LEX and YACC files are compiled to generate the lexical analyzer and parser, respectively.

5. Write the main program: The main program uses the lexical analyzer and parser to evaluate expressions entered by the user.

6. Test the calculator: The final step is to test the calculator to ensure that it is working correctly.

In summary, the implementation of a calculator using LEX and YACC involves defining the grammar, writing the LEX and YACC files, compiling them, writing the main program, and testing the calculator. These steps can be followed to create a functional calculator using these tools.



### d) Convert the BNF rules into YACC form and write code to generate abstract syntax tree

1. BNF (Backus-Naur Form) is a notation used to formally describe the grammar of a language. YACC (Yet Another Compiler-Compiler) is a tool that generates a parser for a given grammar, specified in BNF-like notation.

2. To convert BNF rules into YACC form, the first step is to identify the non-terminals and terminals in the BNF rules. Non-terminals are the left-hand side of the rules, while terminals are the symbols that appear on the right-hand side.

3. In YACC, non-terminals are represented by C-like identifiers, while terminals are represented by token names, usually written in all-caps.

4. The next step is to translate the BNF rules into YACC rules. In YACC, a rule is written as a C-like production, with the non-terminal on the left-hand side, followed by a colon, and the right-hand side consisting of a sequence of non-terminals and terminals.

5. To generate an abstract syntax tree (AST) using YACC, additional code needs to be written in the actions associated with each rule. This code constructs the nodes of the AST and links them together to form the tree structure.

6. The code to generate the AST can be written in any programming language supported by YACC, such as C or C++. The code typically involves creating data structures to represent the nodes of the AST, and using these data structures to build the tree as the input is parsed.

7. Once the YACC rules and the code to generate the AST have been written, the YACC tool can be used to generate the parser. This parser can then be used to parse input according to the specified grammar and generate the corresponding AST.



### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

The ε-closure of a state `q` in an NFA with ε transition is the set of all states that can be reached from `q` by following only ε-transitions. The ε-closure of a set of states `Q` is the union of the ε-closures of all the states in `Q`.

Here is an algorithm to find the ε-closure of all states of a given NFA with ε transition:

1. Initialize an empty stack `S` and an empty set `ε-closure(q)` for each state `q` in the NFA.
2. For each state `q` in the NFA, push `q` onto the stack `S` and add `q` to `ε-closure(q)`.
3. While the stack `S` is not empty:
    1. Pop the top state `q` from the stack `S`.
    2. For each state `p` that can be reached from `q` by following only ε-transitions:
        1. If `p` is not in `ε-closure(q)`, add `p` to `ε-closure(q)` and push `p` onto the stack `S`.
4. The set `ε-closure(q)` now contains the ε-closure of state `q` for all states `q` in the NFA.

This algorithm can be implemented in a programming language of your choice. The time complexity of this algorithm is `O(n^2)` where `n` is the number of states in the NFA. The space complexity is `O(n)`.



### 5. Write program to convert NFA with ε transition to NFA without ε transition.

An NFA with ε transitions (also called ε-NFA) is a type of NFA where transitions can occur without any input symbol, via the use of ε transitions. To convert an ε-NFA to an NFA without ε transitions, we can follow these steps:

1. **Identify ε-closure of states**: For each state in the ε-NFA, identify the set of states that can be reached from it via zero or more ε transitions. This set of states is called the ε-closure of the state.

2. **Create new transition function**: For each state and input symbol in the ε-NFA, find the set of states that can be reached from the ε-closure of the state via the input symbol. This set of states will be the value of the transition function for the corresponding state and input symbol in the new NFA.

3. **Update initial and final states**: The initial state of the new NFA will be the ε-closure of the initial state of the ε-NFA. The set of final states of the new NFA will be the set of states in the ε-NFA whose ε-closure contains at least one final state of the ε-NFA.

Here is an example of a program in Python that converts an ε-NFA to an NFA without ε transitions:

```python
def e_closure(state, transition_function):
    stack = [state]
    closure = set(stack)
    while stack:
        current_state = stack.pop()
        next_states = transition_function.get((current_state, ''), set())
        for next_state in next_states:
            if next_state not in closure:
                stack.append(next_state)
                closure.add(next_state)
    return closure

def convert_nfa_with_epsilon_to_nfa_without_epsilon(nfa_with_epsilon):
    states, input_symbols, transition_function, initial_state, final_states = nfa_with_epsilon
    new_transition_function = {}
    for state in states:
        closure = e_closure(state, transition_function)
        for symbol in input_symbols:
            next_states = set()
            for closure_state in closure:
                next_states |= transition_function.get((closure_state, symbol), set())
            new_transition_function[(state, symbol)] = next_states
    new_initial_state = e_closure(initial_state, transition_function)
    new_final_states = set()
    for state in states:
        closure = e_closure(state, transition_function)
        if any(final_state in closure for final_state in final_states):
            new_final_states.add(state)
    return (states, input_symbols, new_transition_function, new_initial_state, new_final_states)
```

This program takes as input an ε-NFA represented as a tuple of its states, input symbols, transition function, initial state, and final states. The transition function is represented as a dictionary where the keys are tuples of a state and an input symbol (or the empty string for ε transitions), and the values are sets of next states. The program returns a new NFA without ε transitions, represented in the same format.

The `e_closure` function takes as input a state and the transition function of the ε-NFA, and returns the ε-closure of the state. The `convert_nfa_with_epsilon_to_nfa_without_epsilon` function uses this function to compute the new transition function, initial state, and final states of the new NFA, following the steps described above.



### 6. Write program to convert NFA to DFA

An NFA (Nondeterministic Finite Automaton) is a finite state machine where, for some cases, when a single input is given to the current state, the machine goes to multiple states. It is not necessary for the machine to go to different states every time the same input is given to the same state.

A DFA (Deterministic Finite Automaton) is a finite state machine where, for each input symbol, there is one and only one transition from the current state to a next state.

Here are the steps to convert an NFA to a DFA:

1. Create a start state for the DFA by taking the epsilon closure of the start state of the NFA.
2. For each state in the DFA, find the set of NFA states reachable by each possible input symbol. Take the epsilon closure of this set to get the next state in the DFA.
3. Repeat step 2 until no new states are added to the DFA.
4. For each state in the DFA, if any of the NFA states it represents is an accepting state, make the DFA state an accepting state as well.

Here is an example of a program that converts an NFA to a DFA in Python:

```python
def convert_nfa_to_dfa(nfa):
    dfa = {}
    nfa_states = list(nfa.keys())
    dfa_states = []
    dfa_start_state = nfa['start_state']
    dfa_states.append(dfa_start_state)
    dfa['start_state'] = dfa_start_state
    dfa['final_states'] = []
    for state in dfa_states:
        dfa[state] = {}
        for symbol in nfa['symbols']:
            next_state = set()
            for nfa_state in state:
                if symbol in nfa[nfa_state]:
                    next_state = next_state.union(set(nfa[nfa_state][symbol]))
            next_state = tuple(sorted(list(next_state)))
            dfa[state][symbol] = next_state
            if next_state not in dfa_states:
                dfa_states.append(next_state)
    for state in dfa_states:
        for nfa_state in state:
            if nfa_state in nfa['final_states']:
                dfa['final_states'].append(state)
                break
    return dfa
```

This program takes as input an NFA represented as a dictionary, where the keys are the states of the NFA, and the values are dictionaries representing the transitions from that state. The start state is represented by the key 'start_state', and the final states are represented by the key 'final_states'. The symbols are represented by the key 'symbols'. The output is a DFA represented in the same format.



### 7. Write program to minimize any given DFA.

A DFA (Deterministic Finite Automaton) is a finite state machine that accepts or rejects a given string of symbols. The process of minimizing a DFA involves reducing the number of states in the DFA while preserving its language.

Here is an algorithm to minimize any given DFA:

1. **Create an equivalent complete DFA**: Add a new non-final state to the DFA and make all the missing transitions from all the states go to this new state.

2. **Create a table for all pairs of states**: Create a table for all pairs of states (Q, R) not including pairs of the form (Q, Q).

3. **Mark all pairs of states where one is final and the other is not**: Mark all pairs of states (Q, R) where one state is final and the other is not.

4. **Apply the table-filling algorithm**: For all unmarked pairs of states (Q, R), mark (Q, R) if there exists a symbol `a` such that the pair of states (delta(Q, a), delta(R, a)) is marked. Repeat this step until no new pairs are marked.

5. **Combine all unmarked pairs of states**: Combine all unmarked pairs of states into a single state.

6. **Create a new minimized DFA**: Create a new minimized DFA with the combined states and the same set of final states and transitions as the original DFA.

This is a general algorithm to minimize any given DFA. The resulting minimized DFA will have the minimum number of states possible while still accepting the same language as the original DFA.



### 8. Develop an operator precedence parser for a given language.

An operator precedence parser is a type of parser for computer languages that is used to determine the order in which operations are performed. It is based on the concept of operator precedence, which is the order in which operators are evaluated in an expression.

Here are the steps to develop an operator precedence parser for a given language:

1. **Define the grammar**: The first step in developing an operator precedence parser is to define the grammar of the language. This includes specifying the set of terminal and non-terminal symbols, as well as the production rules that define how the symbols can be combined to form valid expressions.

2. **Determine the precedence and associativity of operators**: The next step is to determine the precedence and associativity of the operators in the language. Precedence refers to the order in which operators are evaluated, while associativity determines the order in which operators of the same precedence are evaluated.

3. **Construct the parsing table**: Once the precedence and associativity of the operators have been determined, the next step is to construct the parsing table. This table is used to determine the next action to be taken by the parser based on the current state and the next input symbol.

4. **Implement the parser**: The final step is to implement the parser using the parsing table. The parser reads the input string from left to right and uses the parsing table to determine the next action to be taken. The parser can either shift the next input symbol onto the stack, reduce a set of symbols on the stack to a non-terminal symbol, or accept the input string as a valid expression.

By following these steps, one can develop an operator precedence parser for a given language. It is important to note that the specific details of the implementation may vary depending on the language and the requirements of the parser.



### 9. Write program to find Simulate First and Follow of any given grammar.

First and Follow are two important concepts in the construction of predictive parsers for context-free grammars. These concepts are used to determine the possible set of terminals that can appear at the beginning of a string derived from a non-terminal, and the possible set of terminals that can appear immediately after a non-terminal in a sentential form.

Here is an example of how to write a program to find the First and Follow of a given grammar:

1. Define the grammar in a suitable data structure, such as a dictionary where the keys are the non-terminals and the values are lists of productions.
2. Write a function to find the First of a given symbol. This function should take the grammar and the symbol as input and return a set of terminals that can appear at the beginning of a string derived from the symbol.
3. Write a function to find the Follow of a given non-terminal. This function should take the grammar and the non-terminal as input and return a set of terminals that can appear immediately after the non-terminal in a sentential form.
4. Use the above functions to find the First and Follow of all non-terminals in the grammar.
5. Display the results in a suitable format.

This is a general outline of how to write a program to find the First and Follow of a given grammar. The specific details and implementation may vary depending on the programming language and the requirements of the task. It is important to thoroughly understand the concepts of First and Follow and how they are used in the construction of predictive parsers before attempting to write such a program.



### 10. Construct a recursive descent parser for an expression.

A recursive descent parser is a type of parser that uses a set of recursive procedures to process an input expression. Each procedure corresponds to a non-terminal symbol in the grammar of the language being parsed. Here are the steps to construct a recursive descent parser for an expression:

1. **Define the grammar**: The first step in constructing a recursive descent parser is to define the grammar of the language being parsed. This grammar should be in Backus-Naur Form (BNF) or a similar notation.

2. **Create parsing procedures**: For each non-terminal symbol in the grammar, create a parsing procedure. These procedures should be named after the non-terminal symbols they correspond to.

3. **Implement the parsing procedures**: Each parsing procedure should implement the production rules for the corresponding non-terminal symbol. This can be done using a combination of conditional statements and calls to other parsing procedures.

4. **Handle errors**: The parser should be able to detect and handle errors in the input expression. This can be done by adding error-handling code to the parsing procedures.

5. **Test the parser**: Once the parser has been implemented, it should be tested with a variety of input expressions to ensure that it is working correctly.

In summary, constructing a recursive descent parser for an expression involves defining the grammar, creating parsing procedures for each non-terminal symbol, implementing the parsing procedures, handling errors, and testing the parser.



### 11. Construct a Shift Reduce Parser for a given language

A shift-reduce parser is a type of bottom-up parser for context-free grammars. It works by shifting input symbols onto a stack and reducing them to grammar rules when possible. Here are the steps to construct a shift-reduce parser for a given language:

1. **Define the grammar**: The first step is to define the context-free grammar for the language. This includes specifying the terminals, non-terminals, and production rules.

2. **Construct the parsing table**: The next step is to construct the parsing table, which is a two-dimensional table that specifies the actions to be taken for each combination of the current state and the next input symbol. The parsing table is constructed using the LR(0) or SLR(1) algorithm.

3. **Implement the parser**: The final step is to implement the shift-reduce parser using the parsing table. The parser maintains a stack of symbols and states. It reads the input symbols one by one and performs actions based on the current state and the next input symbol. The actions can be to shift the input symbol onto the stack, reduce a sequence of symbols on the stack to a non-terminal using a production rule, or accept the input if it is valid.

In summary, to construct a shift-reduce parser for a given language, one needs to define the context-free grammar, construct the parsing table, and implement the parser using the parsing table. The parser works by shifting input symbols onto a stack and reducing them to grammar rules when possible.



### 12. Write a program to perform loop unrolling

Loop unrolling is a technique used to optimize the execution time of a program by reducing the number of iterations of a loop. This is achieved by replicating the body of the loop multiple times and adjusting the loop control variable accordingly.

Here is an example of loop unrolling in C:

```c
#include <stdio.h>

int main() {
    int i;
    for (i = 0; i < 100; i += 5) {
        printf("%d\n", i);
        printf("%d\n", i + 1);
        printf("%d\n", i + 2);
        printf("%d\n", i + 3);
        printf("%d\n", i + 4);
    }
    return 0;
}
```

In this example, the loop is unrolled by a factor of 5. This means that the body of the loop is replicated 5 times and the loop control variable is incremented by 5 in each iteration. This reduces the number of iterations of the loop from 100 to 20, resulting in faster execution of the program.

- Loop unrolling can improve the performance of a program by reducing the overhead associated with loop control instructions.
- However, it can also increase the size of the code, which may have a negative impact on performance if the code size exceeds the size of the instruction cache.
- Loop unrolling is most effective when the number of iterations of the loop is known at compile time and is a multiple of the unrolling factor.
- It is important to carefully choose the unrolling factor to balance the trade-off between code size and performance.



### 13. Write a program to perform constant propagation

Constant propagation is a compiler optimization technique that aims to reduce the number of computations performed at runtime by replacing variables with their constant values whenever possible.

Here are the steps to write a program to perform constant propagation:

1. Identify the variables that are assigned constant values in the program.
2. Traverse the program's control flow graph to determine the points where the variables' values are used.
3. Replace the variables with their constant values at the points where their values are used.
4. Repeat the process until no more replacements can be made.

Here is an example of a program that performs constant propagation:

```python
def constant_propagation(code):
    # Step 1: Identify the variables that are assigned constant values
    constants = {}
    for line in code:
        if '=' in line:
            left, right = line.split('=')
            left = left.strip()
            right = right.strip()
            if right.isnumeric():
                constants[left] = right

    # Step 2: Traverse the program's control flow graph
    new_code = []
    for line in code:
        new_line = line
        for var, value in constants.items():
            # Step 3: Replace the variables with their constant values
            new_line = new_line.replace(var, value)
        new_code.append(new_line)

    # Step 4: Repeat the process
    if new_code == code:
        return new_code
    else:
        return constant_propagation(new_code)

# Example
code = [
    'x = 5',
    'y = 3',
    'z = x + y',
    'print(z)'
]

new_code = constant_propagation(code)
print(new_code)
```

This program takes a list of code lines as input and returns a new list of code lines where the variables have been replaced with their constant values whenever possible. In the example, the variable `z` is replaced with the constant value `8`, which is the result of adding the constant values of `x` and `y`.



### 14. Implement Intermediate code generation for simple expressions

Intermediate code generation is a phase in the compilation process where the source code is transformed into an intermediate representation that is lower level and easier for the compiler to translate into machine code. This intermediate representation is often platform-independent, allowing the same code to be compiled for multiple target architectures.

Here are the steps to implement intermediate code generation for simple expressions:

1. **Lexical analysis**: The first step is to perform lexical analysis on the source code to identify the tokens that make up the expression. This involves breaking the expression into its constituent parts, such as operators, operands, and parentheses.

2. **Syntax analysis**: The next step is to perform syntax analysis to determine the structure of the expression. This involves checking that the expression is well-formed and conforms to the rules of the programming language.

3. **Semantic analysis**: After the structure of the expression has been determined, semantic analysis is performed to ensure that the expression is meaningful. This involves checking that the operands and operators are of the correct type and that the expression can be evaluated.

4. **Intermediate code generation**: Once the expression has been analyzed, it can be translated into an intermediate representation. This involves generating a sequence of instructions that can be executed by the target machine to evaluate the expression.

5. **Optimization**: After the intermediate code has been generated, it can be optimized to improve its performance. This involves applying techniques such as constant folding, dead code elimination, and loop unrolling to reduce the number of instructions that need to be executed.

By following these steps, it is possible to implement intermediate code generation for simple expressions, allowing the compiler to translate the source code into machine code that can be executed by the target machine.



### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language

The back end of a compiler is responsible for generating the target code from the intermediate representation, in this case, the three address code. The target code for this specific implementation is the 8086 assembly language.

Here are the steps to implement the back end of the compiler:

1. **Instruction selection**: Map the three address code instructions to the corresponding 8086 assembly language instructions. This can be done using a table-driven approach or a tree-rewriting approach.

2. **Register allocation**: Assign registers to the variables used in the three address code. This can be done using graph coloring or linear scan algorithms.

3. **Code generation**: Generate the final 8086 assembly language code by replacing the variables in the instructions with the assigned registers.

It is important to note that the 8086 assembly language has its own set of instructions and addressing modes, which must be taken into account when implementing the back end of the compiler. Additionally, optimization techniques can be applied to improve the efficiency of the generated code.



### Instructions that can be assembled and run using an 8086 assembler

The 8086 microprocessor is a 16-bit CPU that can execute a variety of instructions. Some of the instructions that can be assembled and run using an 8086 assembler are:

1. **Data transfer instructions**: These instructions are used to move data between registers, memory, and I/O ports. Some examples of data transfer instructions are `MOV`, `XCHG`, `PUSH`, and `POP`.
2. **Arithmetic instructions**: These instructions perform arithmetic operations such as addition, subtraction, multiplication, and division. Some examples of arithmetic instructions are `ADD`, `SUB`, `MUL`, and `DIV`.
3. **Logical instructions**: These instructions perform logical operations such as AND, OR, XOR, and NOT. Some examples of logical instructions are `AND`, `OR`, `XOR`, and `NOT`.
4. **Control transfer instructions**: These instructions are used to change the flow of the program. Some examples of control transfer instructions are `JMP`, `CALL`, `RET`, and `LOOP`.
5. **String instructions**: These instructions are used to perform operations on strings of characters. Some examples of string instructions are `MOVSB`, `MOVSW`, `CMPSB`, and `CMPSW`.
6. **Processor control instructions**: These instructions are used to control the operation of the processor. Some examples of processor control instructions are `HLT`, `WAIT`, `LOCK`, and `ESC`.

These are some of the instructions that can be assembled and run using an 8086 assembler. The target assembly instructions can be simple move, arithmetic, logical, control transfer, string, or processor control instructions.



### Add, Sub, Jump etc.

- **Add** is an arithmetic operation that combines two or more numbers to produce a sum.
- **Sub** is an arithmetic operation that finds the difference between two numbers by subtracting one from the other.
- **Jump** is a control flow instruction in computer programming that causes the program to jump to a different location in the code. This can be used for loops, conditional statements, and other control structures.
- These operations are fundamental in computer programming and are used to perform a wide range of tasks.
- Understanding these operations and how to use them effectively is essential for writing efficient and effective code.



### Note: The Instructor may add/delete/modify/tune experiments, wherever he/she feels in a justified manner

- This statement indicates that the instructor has the authority to make changes to the experiments.
- The instructor may add new experiments or delete existing ones.
- The instructor may also modify or tune the experiments to better suit the needs of the course or the students.
- These changes should be made in a justified manner, meaning that the instructor should have a valid reason for making the changes.
- This statement serves as a reminder to students that the experiments are subject to change and that they should be prepared for any modifications that may occur.



### Open Source Tools for Conducting Lab

It is suggested that open source tools should be preferred to conduct the lab. Some of the reasons for this are:

1. **Cost-effective**: Open source tools are usually free or available at a low cost, making them a cost-effective option for conducting lab experiments.

2. **Customizable**: Open source tools can be easily customized to meet the specific needs of the lab.

3. **Community support**: Open source tools often have a large and active community of users and developers who can provide support and assistance.

4. **Transparency**: The source code of open source tools is openly available, allowing for greater transparency and the ability to verify the tool's functionality.

Some open source tools that can be used to conduct the lab include C, C++, Lex, and Flex. These tools are widely used and have a strong community of users and developers. They are also well-documented and have a wealth of resources available to help users learn how to use them effectively.



### YACC tools (Unix/Linux utilities)

YACC (Yet Another Compiler Compiler) is a Unix/Linux utility that generates a parser for a given grammar. It is commonly used to write compilers and interpreters for programming languages.

Some key points about YACC tools are:

1. YACC is a tool that generates code for a parser based on a given grammar.
2. The generated parser can be used to parse input according to the specified grammar.
3. YACC is commonly used to write compilers and interpreters for programming languages.
4. YACC is available on Unix and Linux systems.
5. YACC is often used in conjunction with the lexical analyzer generator, LEX.




### Curriculum & Evaluation Scheme CS & CSE (V & VI semester) 19

The curriculum and evaluation scheme for Computer Science (CS) and Computer Science and Engineering (CSE) for the fifth and sixth semesters is designed to provide students with a comprehensive understanding of the core concepts and practical skills required in the field.

1. The curriculum includes courses on advanced topics such as data structures and algorithms, computer networks, database systems, and software engineering.
2. Students are also required to complete a project, which provides an opportunity to apply the knowledge and skills acquired in the classroom to a real-world problem.
3. The evaluation scheme includes a combination of written exams, practical exams, and continuous assessment through assignments and quizzes.
4. The weightage of each component of the evaluation may vary from course to course, but the overall aim is to ensure that students have a thorough understanding of the subject matter and are able to apply their knowledge in practical situations.


