### Iterated Messages

- Iterated messages are a way of representing repeated or conditional messages in a sequence diagram.
- Iterated messages are shown by placing an asterisk (*) in front of the message name, followed by an optional iteration expression in square brackets.
- The iteration expression specifies the condition or the number of times the message is sent or received.
- For example, `*m[i]` means that message `m` is sent or received for each value of `i` in some range.
- Iterated messages can be used to model loops, collections, recursion, or any other situation where a message is repeated or conditional.
- Iterated messages can simplify the sequence diagram by reducing the number of lifelines and messages.
- Iterated messages can also show the order or the concurrency of the repeated messages, by using different notations such as nested, parallel, or interleaved.
- For example, `*m[i] || *n[j]` means that messages `m` and `n` are sent or received in parallel for each value of `i` and `j` in some ranges.
- Iterated messages are useful for modeling the dynamic behavior of complex or repetitive scenarios in object-oriented systems.