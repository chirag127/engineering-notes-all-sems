## Unit 2 - Basic Parsing Techniques

Parsing is the process of analyzing the structure and meaning of a sentence or a program based on a given grammar. Parsing techniques are methods for implementing parsers.

Some basic parsing techniques are:

- Top-down parsing: This technique starts from the start symbol of the grammar and tries to derive the input string by applying the production rules. It predicts the structure of the input before reading it. Examples of top-down parsing are recursive descent parsing and LL parsing.
- Bottom-up parsing: This technique starts from the input string and tries to reduce it to the start symbol of the grammar by applying the production rules in reverse. It builds the structure of the input after reading it. Examples of bottom-up parsing are shift-reduce parsing and LR parsing.
- Chart parsing: This technique uses a data structure called a chart to store partial results of the parsing process. It avoids repeating the same work by reusing the results stored in the chart. Examples of chart parsing are Earley parsing and CYK parsing.