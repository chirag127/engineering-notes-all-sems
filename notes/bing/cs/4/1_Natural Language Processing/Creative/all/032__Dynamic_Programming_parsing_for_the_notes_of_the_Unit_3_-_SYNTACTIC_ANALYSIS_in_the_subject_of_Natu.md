### Dynamic Programming parsing for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Dynamic programming (DP) is a technique for solving problems that have overlapping subproblems and optimal substructure.
- DP parsing is a method for finding the most probable parse tree for a given sentence and a grammar, based on the principle of DP.
- DP parsing can be applied to different types of grammars, such as context-free grammars (CFGs), probabilistic context-free grammars (PCFGs), or lexicalized PCFGs (LPCFGs).
- DP parsing algorithms typically use a bottom-up or a top-down approach, or a combination of both, to fill a table with the best scores or probabilities for each possible substructure of the sentence.
- DP parsing algorithms can be classified into two categories: chart parsing and matrix parsing.

#### Chart parsing
- Chart parsing is a DP parsing method that uses a data structure called a chart to store and retrieve partial analyses of the sentence.
- A chart is a directed graph that represents the syntactic structure of the sentence, where the nodes are words or nonterminal symbols, and the edges are labeled with rules or constituents.
- Chart parsing algorithms start with an empty chart and add edges to it incrementally, following the rules of the grammar and the input sentence.
- Chart parsing algorithms can use different strategies to decide which edges to add next, such as breadth-first, depth-first, or best-first.
- Chart parsing algorithms can also use different types of charts, such as edge-based, item-based, or dot-based, depending on how they represent the edges and their states.
- Chart parsing algorithms can handle ambiguity and multiple parses by storing all possible edges in the chart, and then extracting the best or all parses from the chart at the end.
- Chart parsing algorithms can be generalized to handle probabilistic grammars by associating probabilities with the edges and using them to compute the best scores or probabilities for each substructure.
- Chart parsing algorithms can also be extended to handle lexicalized grammars by incorporating lexical information into the edges and the chart.

#### Matrix parsing
- Matrix parsing is a DP parsing method that uses a matrix or a table to store and retrieve the best scores or probabilities for each substructure of the sentence.
- A matrix is a two-dimensional array that represents the syntactic structure of the sentence, where the rows and columns are words or positions in the sentence, and the cells are labeled with nonterminal symbols or constituents.
- Matrix parsing algorithms start with an empty matrix and fill it with the best scores or probabilities for each cell, following the rules of the grammar and the input sentence.
- Matrix parsing algorithms typically use a bottom-up approach, where they fill the cells in a diagonal or a triangular order, starting from the smallest substructures to the largest ones.
- Matrix parsing algorithms can handle ambiguity and multiple parses by storing the best or all scores or probabilities for each cell, and then extracting the best or all parses from the matrix at the end.
- Matrix parsing algorithms can be generalized to handle probabilistic grammars by associating probabilities with the rules and using them to compute the best scores or probabilities for each cell.
- Matrix parsing algorithms can also be extended to handle lexicalized grammars by incorporating lexical information into the rules and the matrix.

#### Mnemonics and learning tricks
- A possible mnemonic to remember the difference between chart parsing and matrix parsing is: **CHART** stands for **C**omplex **H**ierarchical **A**nalysis using **R**ules and **T**rees, while **MATRIX** stands for **M**inimal **A**nalysis using **T**ables and **R**ows and **I**ndices and **X**-symbols.
- A possible learning trick to understand the principle of DP is to use the analogy of climbing a mountain: DP parsing is like finding the shortest or easiest path to the summit, by reusing the paths that have already been explored and avoiding the paths that are longer or harder.