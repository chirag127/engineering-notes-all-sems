# make a python script which use open ai gpt davinci to make notes

import os

import openai
from prompt_toolkit import prompt

openai.api_key = os.environ.get("OPENAI_API_KEY", "")

topics = """Introduction to Compiler: Phases and passes, Bootstrapping, Finite state machines and regular
expressions and their applications to lexical analysis, Optimization of DFA-Based Pattern Matchers
implementation of lexical analyzers, lexical-analyzer generator, LEX compiler, Formal grammars
and their application to syntax analysis, BNF notation, ambiguity, YACC. The syntactic
specification of programming languages: Context free grammars, derivation and parse trees,
capabilities of CFG.
Basic Parsing Techniques: Parsers, Shift reduce parsing, operator precedence parsing, top down
parsing, predictive parsers Automatic Construction of efficient Parsers: LR parsers, the canonical
Collection of LR(0) items, constructing SLR parsing tables, constructing Canonical LR parsing
tables, Constructing LALR parsing tables, using ambiguous grammars, an automatic parser
generator, implementation of LR parsing tables.
Syntax-directed Translation: Syntax-directed Translation schemes, Implementation of Syntax-directed Translators, Intermediate code, postfix notation, Parse trees & syntax trees, three address
code, quadruple & triples, translation of assignment statements, Boolean expressions, statements
that alter the flow of control, postfix translation, translation with a top down parser. More about
translation: Array references in arithmetic expressions, procedures call, declarations and case
statements.
Symbol Tables: Data structure for symbols tables, representing scope information. Run-Time
Administration: Implementation of simple stack allocation scheme, storage allocation in block
structured language. Error Detection & Recovery: Lexical Phase errors, syntactic phase errors
semantic errors.
Code Generation: Design Issues, the Target Language. Addresses in the Target Code, Basic
Blocks and Flow Graphs, Optimization of Basic Blocks, Code Generator. Code optimization:
Machine-Independent Optimizations, Loop optimization, DAG representation of basic blocks,
value numbers and algebraic laws, Global Data-Flow analysis.
"""


# split the topics into a list of topics to be used in the prompt by comma seperating them
topics = topics.split(",")

for topic in topics:
    # strip the topic of any whitespace at the beginning or end of the string
    topic = topic.strip()
    prompt = f"what is the complete detailed and indepth description about {topic} in compiler design.\n"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(response)
    print(response.choices[0].text)

    with open("cd/1.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\n\n{topic}\n{response.choices[0].text}")
