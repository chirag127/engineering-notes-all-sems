### Minimum Edit Distance

- Minimum edit distance is a measure of how similar or dissimilar two strings are by counting the minimum number of operations required to transform one string into another .
- The operations are typically insertion, deletion, and substitution of a single character, or transposition of two adjacent characters.
- Minimum edit distance can be used for various natural language processing tasks, such as spelling correction, text classification, information extraction, and machine translation .
- Minimum edit distance can be computed using a dynamic programming algorithm that fills a matrix with the costs of the optimal alignments between the prefixes of the two strings  .
- The algorithm works as follows  :
  - Initialize the first row and column of the matrix with the costs of inserting or deleting the characters of the first string or the second string, respectively.
  - For each cell in the matrix, compute the minimum cost of aligning the prefixes of the two strings up to that cell, by taking the minimum of three possible costs:
    - The cost of the cell above plus the cost of deleting a character from the first string.
    - The cost of the cell to the left plus the cost of inserting a character to the second string.
    - The cost of the cell diagonally above and to the left plus the cost of substituting a character if the characters at the current position are different, or zero if they are the same.
  - The minimum edit distance is the value of the bottom-right cell of the matrix.
  - Optionally, the optimal alignment can be traced back by following the pointers from the bottom-right cell to the top-left cell, indicating which operation was chosen at each step.
- The costs of the operations can be assigned arbitrarily, depending on the application and the language . For example, some common choices are:
  - Assign a cost of 1 for each operation, regardless of the characters involved. This is also known as the Levenshtein distance.
  - Assign a cost of 2 for substitution and 1 for insertion and deletion. This is also known as the restricted Damerau-Levenshtein distance.
  - Assign a cost of 0.5 for transposition and 1 for the other operations. This is also known as the optimal string alignment distance.
  - Assign different costs for different characters, based on their frequency, similarity, or keyboard layout . For example, substituting 'e' with 'i' may have a lower cost than substituting 'e' with 'z' in English.