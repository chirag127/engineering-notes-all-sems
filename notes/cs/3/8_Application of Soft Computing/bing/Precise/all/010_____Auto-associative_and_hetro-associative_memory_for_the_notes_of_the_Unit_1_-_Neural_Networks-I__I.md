# Auto-associative and Hetero-associative Memory

Auto-associative and hetero-associative memory are two types of associative memory used in neural networks.

## Auto-associative Memory

Auto-associative memory, also known as auto-association, is a type of memory that allows the retrieval of a piece of data from the memory by presenting a partial or noisy version of that data as input. The network then retrieves the original, complete version of the data from its memory.

- Auto-associative memory is used in neural networks to perform pattern completion.
- The network is trained on a set of patterns, and once trained, it can retrieve the complete pattern when presented with a partial or noisy version of that pattern.
- This type of memory is useful in applications such as image or speech recognition, where the input data may be noisy or incomplete.

## Hetero-associative Memory

Hetero-associative memory, also known as hetero-association, is a type of memory that allows the retrieval of a piece of data from the memory by presenting a related piece of data as input. The network then retrieves the associated data from its memory.

- Hetero-associative memory is used in neural networks to perform pattern association.
- The network is trained on a set of input-output pairs, and once trained, it can retrieve the associated output when presented with the input.
- This type of memory is useful in applications such as language translation, where the input is a sentence in one language and the output is the translation of that sentence in another language.

In summary, auto-associative memory is used for pattern completion, while hetero-associative memory is used for pattern association. Both types of memory are useful in different applications and can be implemented using neural networks.