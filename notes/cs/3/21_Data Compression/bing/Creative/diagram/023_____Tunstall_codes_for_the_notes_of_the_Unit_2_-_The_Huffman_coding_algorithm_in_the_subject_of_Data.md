### Tunstall codes

- Tunstall codes are a form of entropy coding used for lossless data compression.
- Tunstall codes are variable-to-fixed length codes, which means they map variable-length source words to fixed-length codewords .
- Tunstall codes are based on a source model that assigns probabilities to source words, which are sequences of symbols from a finite alphabet.
- Tunstall codes are constructed by using a prefix tree, where each leaf node corresponds to a codeword and each internal node corresponds to a source word prefix .
- Tunstall codes are optimal for sources that have a geometric distribution of word probabilities, such as run-length encoded data.
- Tunstall codes have some advantages over other entropy coding methods, such as:
  - They are easy to implement and decode.
  - They have a bounded compression ratio, which means they never expand the data by more than a fixed factor.
  - They are suitable for streaming data, since they do not require a priori knowledge of the source statistics or a header to store them.
- Tunstall codes have some disadvantages, such as:
  - They are not adaptive, which means they cannot adjust to changes in the source statistics.
  - They are not universal, which means they cannot achieve the entropy of any source.
  - They require a large codebook size, which limits their practical applicability.