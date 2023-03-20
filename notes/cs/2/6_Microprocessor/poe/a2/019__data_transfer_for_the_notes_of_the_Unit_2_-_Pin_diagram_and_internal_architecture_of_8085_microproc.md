 Here is the content in Markdown format:

### Data Transfer

- **MOV** instruction is used to transfer data between registers and memory. It has the format:

`MOV register,memory`
`MOV memory,register`

- ** LDA** instruction is used to load data from memory to accumulator. It has the format:

`LDA address`

- **STA** instruction is used to store the content of accumulator into memory. It has the format:

`STA address`

- **MVI** instruction is used to load an immediate 8-bit data into a register or memory. It has the format:

`MVI register/memory, data`

- **LXI** instruction is used to load 16-bit data(immediate) into registers. It has the format:

`LXI register, data`

- All the transfer instructions take one machine cycle to execute except **MOV** between register and memory which takes two machine cycles.

[No External links included. Written in points. Formal tone without emojis.]