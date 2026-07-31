# The ESCAPE SYMBOL for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data file by removing redundant or irrelevant information, or by using more efficient encoding schemes.
- Coding a sequence is one of the techniques of data compression, which involves assigning a unique code to each symbol in the data, such that the code length reflects the symbol frequency or probability.
- The escape symbol is a special symbol that is used to indicate the occurrence of a new or rare symbol that has not been assigned a code yet, or that has a very low probability of occurrence.
- The escape symbol is usually chosen to be a symbol that does not appear in the original data, or that has a very low frequency in the data.
- The escape symbol is followed by a fixed-length code or a uniform probability code that represents the new or rare symbol, using the symbols that have not occurred or have a low probability of occurrence.
- The escape symbol itself has an artificial count, often a constant throughout the encoding, that determines its code length and probability.
- The use of the escape symbol allows the coding scheme to be adaptive, meaning that it can adjust to the changing statistics of the data, and encode new or rare symbols without having to reassign codes to the existing symbols.
- The use of the escape symbol also allows the coding scheme to be universal, meaning that it can encode any data without knowing the alphabet or the probabilities of the symbols in advance.
- Example: Let T = badada and \u0006 be the escape symbol. Using a simple coding scheme that assigns codes based on the symbol frequency, we can encode T as follows:

| Symbol | Frequency | Code  |
|--------|-----------|-------|
| a      | 3         | 0     |
| b      | 1         | 10    |
| d      | 2         | 11    |
| \u0006 | 1         | 01    |

- The encoded sequence is: 10 0 11 0 01 0 11 0
- The escape symbol is used to indicate the first occurrence of a, which is followed by a uniform probability code 0, using the only symbol that has not occurred yet, a.
- The escape symbol has a frequency of 1, which is the same as b, so it has the same code length as b, 2 bits.