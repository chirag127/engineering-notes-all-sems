# 2. Implementation of Lexical Analyzer using Lex Tool

- Lex is a tool that generates lexical analyzers, also known as scanners or tokenizers, from a set of rules that specify the tokens to be recognized in the input stream.
- Lexical analyzers are programs that read an input stream of characters and produce an output stream of tokens, which are the basic units of meaning in a programming language or a text file.
- Lexical analyzers are often used as the first phase of a compiler or an interpreter, to divide the source code into tokens that can be processed by the subsequent phases, such as the parser or the semantic analyzer.
- Lex is based on the concept of regular expressions, which are a concise and powerful way of describing patterns of characters. A regular expression can be used to define a token, such as a keyword, an identifier, a number, a string literal, or a comment.
- Lex uses a special notation to write the rules for the lexical analyzer. A rule consists of two parts: a pattern and an action. The pattern is a regular expression that matches a sequence of characters in the input stream. The action is a fragment of C code that is executed when the pattern is matched. The action usually returns a token code or a value to the calling program, or performs some other operation, such as printing an error message or updating a counter.
- Lex rules have the following general form:

    `pattern   action`

- The pattern and the action are separated by whitespace (spaces or tabs). The action is enclosed in curly braces `{ }`. The action can span multiple lines, but the pattern must be on a single line. A semicolon `;` can be used to terminate the action, but it is optional.
- Lex rules are written in a file with the extension `.l` or `.lex`. The file can also contain some optional sections, such as definitions, declarations, start conditions, and user subroutines. These sections are delimited by special symbols: `%{` and `%}` for the definitions section, `%%` for the rules section, and `%{` and `%}` for the user subroutines section. The declarations section can contain any C code that is copied verbatim to the generated C file. The definitions section can contain macros or definitions of regular expressions that can be used in the rules. The start conditions section can define different states or modes for the lexical analyzer, which can be switched by using the `BEGIN` macro in the actions. The user subroutines section can contain any C functions that are used by the actions or the calling program.
- The following is an example of a Lex file that implements a simple lexical analyzer for a subset of the C language:

    ```
    %{ /* definitions section */
    #include <stdio.h>
    #include <stdlib.h>
    #define MAXID 32 /* maximum length of an identifier */
    enum tokentype { /* token codes */
        T_EOF, T_INT, T_FLOAT, T_CHAR, T_IF, T_ELSE, T_WHILE, T_FOR, T_RETURN, T_ID, T_NUM, T_STR, T_LPAR, T_RPAR, T_LBRA, T_RBRA, T_LBRC, T_RBRC, T_COMMA, T_SEMI, T_PLUS, T_MINUS, T_MUL, T_DIV, T_MOD, T_ASSIGN, T_EQ, T_NE, T_LT, T_LE, T_GT, T_GE, T_AND, T_OR, T_NOT
    };
    char lexeme[MAXID+1]; /* buffer to store the current lexeme */
    int lineno = 1; /* line number counter */
    %}

    /* regular expression definitions */
    letter [A-Za-z_]
    digit [0-9]
    id {letter}({letter}|{digit})*
    num {digit}+(\.{digit}+)?(E[+-]?{digit}+)?
    str \"(\\.|[^\\"])*\"
    ws [ \t\n]+

    %%

    /* rules section */
    {ws} { /* ignore whitespace and newline */ 
        if (*yytext == '\n') lineno++; /* increment line number */
    }
    "int" { return T_INT; }
    "float" { return T_FLOAT; }
    "char" { return T_CHAR; }
    "if" { return T_IF; }
    "else" { return T_ELSE; }
    "while" { return T_WHILE; }
    "for" { return T_FOR; }
    "return" { return T_RETURN; }
    {id} { /* identifier */
        strncpy(lexeme, yytext, MAXID); /* copy the lexeme to the buffer