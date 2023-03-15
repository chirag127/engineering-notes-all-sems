## Implementing 3-8 line DECODER for the notes of the Computer Organization Lab in the subject of Computer Organization

- A 3-8 line decoder is a digital circuit that converts a 3-bit binary input into an 8-bit output, where only one of the output lines is active (high) at a time.
- A 3-8 line decoder can be used for various applications, such as selecting one of eight devices, decoding memory addresses, or demultiplexing data signals.
- A 3-8 line decoder can be implemented using AND and NAND gates, as shown in the following block diagram  :

```markdown
    A0 A1 A2
     |  |  |
     |  |  |   _______
     |  |  |__|       |
     |  |_____|       |
     |_______ |       |
             ||       |
             ||_______|  Y0
             ||       |
             ||       |
             ||_______|  Y1
             ||       |
             ||       |
             ||_______|  Y2
             ||       |
             ||       |
             ||_______|  Y3
             ||       |
             ||       |
             ||_______|  Y4
             ||       |
             ||       |
             ||_______|  Y5
             ||       |
             ||       |
             ||_______|  Y6
             ||       |
             ||       |
             ||_______|  Y7
             ||_______|
                E
```

- The decoder has three inputs (A0, A1, A2) that represent the binary code to be decoded, and eight outputs (Y0 to Y7) that correspond to the eight possible combinations of the inputs.
- The decoder also has an enable input (E) that controls whether the decoder is active or not. When E is low, the decoder is disabled and all the outputs are low. When E is high, the decoder is enabled and one of the outputs is high, depending on the input code.
- The truth table for the 3-8 line decoder is as follows  :

```markdown
| E | A2 | A1 | A0 | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 |
|---|----|----|----|----|----|----|----|----|----|----|----|
| 0 | X  | X  | X  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 1 | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 1 | 0  | 0  | 1  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
| 1 | 0  | 1  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
| 1 | 0  | 1  | 1  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 1 | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 1 | 1  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 1 | 1  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  |
| 1 | 1  | 1  | 1  | 0  | 0  | 0  | 0  |