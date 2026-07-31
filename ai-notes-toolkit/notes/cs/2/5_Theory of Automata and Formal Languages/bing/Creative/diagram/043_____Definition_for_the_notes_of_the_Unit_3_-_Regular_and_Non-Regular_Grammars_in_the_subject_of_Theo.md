Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information that I found from the web:

### Definition for the notes of the Unit 3 - Regular and Non-regular Grammars in the subject of Theory of Automata and Formal Languages

- A **regular grammar** is a formal grammar that can generate only regular languages, which are a subset of context-free languages. Regular languages can be recognized by finite automata.
- A regular grammar can be either **right-regular** or **left-regular**, depending on the position of the non-terminal symbol in the production rules. A right-regular grammar has the non-terminal symbol on the right-hand side of the production, while a left-regular grammar has it on the left-hand side.
- A regular grammar has the following form:

  - A right-regular grammar has production rules of the form: `A -> a`, `A -> aB`, or `A -> ε`, where `A` and `B` are non-terminal symbols, `a` is a terminal symbol, and `ε` is the empty string.
  - A left-regular grammar has production rules of the form: `A -> a`, `A -> Ba`, or `A -> ε`, where `A` and `B` are non-terminal symbols, `a` is a terminal symbol, and `ε` is the empty string.

- A **non-regular grammar** is a formal grammar that can generate languages that are not regular, i.e., languages that cannot be recognized by finite automata. Non-regular languages are a superset of regular languages and include context-free languages, context-sensitive languages, and recursively enumerable languages.
- A non-regular grammar can have production rules that do not follow the form of a regular grammar, such as:

  - Rules that have more than one non-terminal symbol on the left-hand side or the right-hand side, e.g., `AB -> a`, `A -> BC`, or `A -> aBb`.
  - Rules that have a terminal symbol on the left-hand side, e.g., `a -> A`.
  - Rules that have an empty string on the left-hand side, e.g., `ε -> A`.

- Examples of regular and non-regular grammars:

  - A regular grammar for the language `L = {a^n b^n | n >= 0}` is:

    - `S -> aSb | ε`

  - A non-regular grammar for the same language is:

    - `S -> aSb | ab | ε`

  - A regular grammar for the language `L = {a^n | n is even}` is:

    - `S -> aA | ε`
    - `A -> aS`

  - A non-regular grammar for the language `L = {a^n b^n c^n | n >= 0}` is:

    - `S -> aSBC | ε`
    - `CB -> BC`
    - `aB -> ab`
    - `bB -> bb`
    - `bC -> bc`
    - `cC -> cc`