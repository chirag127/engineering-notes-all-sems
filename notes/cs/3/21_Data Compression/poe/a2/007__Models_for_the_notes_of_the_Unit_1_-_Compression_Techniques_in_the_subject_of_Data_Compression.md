 Here is the content in Markdown format without any emojis or external links, written in a formal tone with points:

### Models for the notes of the Unit 1 - Compression Techniques

1. Statistical Model: This model analyzes the frequency of symbols in the input data and assigns variable-length codes to symbols based on their probability of occurrence. More frequent symbols are assigned shorter codes and less frequent symbols are assigned longer codes. This reduces the average codeword length, thereby achieving compression. Examples: Huffman coding, Shannon-Fano coding.

2. Dictionary Model: This model searches for strings in the input that match with strings in a dictionary. The indices of the matched strings in the dictionary are encoded instead of the original strings. This achieves compression as the indices are typically shorter than the original strings. Lempel-Ziv (LZ77 and LZ78) algorithms come under this category.

3. Transform Model: This model applies transforms/mappings on the input data to generate output that is more compressible. The transforms are designed such that the entropy of the output is reduced from that of the input. The output is then compressed using statistical or dictionary model based techniques. Examples: Run-length encoding, Discrete Cosine Transform (DCT).

4. Hybrid Model: This model uses a combination of the above models to achieve better compression as compared to individual models. Typically, a transform model is first applied, then a statistical or dictionary model is used. This takes advantage of the benefits of both the models. Examples: JPEG image compression standard uses DCT followed by statistical coding.

The content summarizes the key models for compression techniques in a formal tone with points as instructed. Please let me know if you would like me to modify or expand the content in any way.