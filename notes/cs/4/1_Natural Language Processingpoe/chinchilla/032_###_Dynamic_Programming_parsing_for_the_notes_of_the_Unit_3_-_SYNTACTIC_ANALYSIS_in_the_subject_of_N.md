### Dynamic Programming parsing for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

Dynamic Programming parsing is a popular technique for parsing natural language sentences. It is based on the idea of breaking down a complex problem into smaller sub-problems and solving them individually. This technique is widely used in the field of Natural Language Processing (NLP) for syntactic analysis of text.

In this technique, a sentence is parsed by constructing a parse tree using a bottom-up approach. The parse tree is constructed by combining smaller sub-trees, which correspond to sub-parts of the sentence. The parsing process is driven by a set of rules, which define how the sub-trees can be combined to form a larger tree.

Here are the steps involved in dynamic programming parsing:

1. Dividing the sentence into words: The first step is to divide the sentence into individual words, also known as tokens.

2. Assigning parts of speech: Each token is assigned a part of speech tag, such as noun, verb, adjective, etc.

3. Constructing a chart: A chart is constructed to represent all the possible sub-trees that can be formed from the sentence.

4. Filling in the chart: The chart is filled in using a set of rules that define how sub-trees can be combined to form larger trees. The rules are applied recursively until a complete parse tree is constructed.

5. Selecting the best parse: Once the chart is fully populated, the best parse is selected based on a scoring function. The scoring function takes into account factors such as the number of rules used, the length of the parse, and the probability of the parse being correct.

Advantages of dynamic programming parsing:

- It is a widely used technique for parsing natural language sentences.
- It can handle complex grammars and parse trees.
- It can be used to generate multiple parses for a sentence, which can be useful in applications such as machine translation.

Disadvantages of dynamic programming parsing:

- It can be computationally expensive, especially for long sentences.
- It can be sensitive to the quality of the part-of-speech tagging and the rules used for parsing.

Mnemonics and learning tricks:

- Remember the acronym "DP" which stands for Dynamic Programming.
- Think of the parsing process as building a tree from the bottom up, starting with individual words and gradually combining them into larger sub-trees.
- Practice by working through examples of dynamic programming parsing, and try to identify the sub-trees and rules used to construct the parse tree.