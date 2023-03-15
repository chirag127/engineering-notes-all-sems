### Implementation of LR Parsing Tables

LR Parsing Tables are a two-dimensional array in which each entry represents an Action or goto entry. A programming language grammar having a large number of productions has a large number of states or items, i.e., I0, I1 … … In. So, due to more states, more Actions & goto entries will be filled.

The LR Parsing algorithm is the same for all the parser, but the parsing table is different for each parser. It consists of the following components: Input Buffer, Stack, Parsing Table, and Output.

The Input Buffer contains the given string, and it ends with a $ symbol. The combination of state symbol and current input symbol is used to refer to the parsing table in order to determine the next action.

There are different types of LR Parsers, such as CLR and SLR. CLR parsing uses the canonical collection of LR (1) items to construct the CLR (1) parsing table. CLR (1) parsing table makes more number of states as compared to the SLR (1) parsing. In the CLR (1), it can locate the reduce node only in the lookahead symbols.