# Uniquely Decodable Codes

- A code is a mapping from a set of symbols (source alphabet) to a set of binary strings (code words).
- A code is uniquely decodable if there is only one way to decode any sequence of code words back to the original symbols.
- A code is non-singular if no two different symbols have the same code word.
- A code is instantaneous if the end of any code word is recognizable without examining subsequent code symbols.
- A code is prefix-free if no code word is a prefix of another code word. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average code word length for a given source alphabet and probability distribution.

## Examples

- Consider the code M1 = {a -> 0, b -> 10, c -> 110, d -> 111}. This code is prefix-free, instantaneous, uniquely decodable, and optimal for a source alphabet of four symbols with probabilities 0.5, 0.25, 0.125, and 0.125 respectively.
- Consider the code M2 = {a -> 0, b -> 01, c -> 011}. This code is non-singular, but not uniquely decodable, because the sequence 0110 could be decoded as either ab or ca. This code is also not instantaneous, because the end of the code word for b is not recognizable without examining the next symbol.
- Consider the code M3 = {a -> 0, b -> 1, c -> 00}. This code is non-singular and uniquely decodable, but not instantaneous, because the end of the code word for a is not recognizable without examining the next symbol. This code is also not prefix-free, because the code word for a is a prefix of the code word for c.