# Verification of Truth Table of Various Logic Gates

## Introduction

A logic gate is a device that performs a Boolean logic operation on one or more binary inputs and outputs a single binary output. There are different types of logic gates, such as AND, OR, NOT, NAND, NOR, and XOR, each with its own truth table that shows the output for every possible combination of inputs. A truth table is a table that lists all the possible input values and the corresponding output values for a logic gate or a logic circuit.

## Objective

The objective of this experiment is to verify the truth tables of various logic gates using integrated circuits (ICs). Integrated circuits are electronic devices that contain many logic gates and other components on a single chip. By using ICs, we can simplify the wiring and testing of logic circuits.

## Components Required

The components required for this experiment are:

- Breadboard
- Power supply (5V)
- Logic probe
- ICs: 7408 (AND gate), 7432 (OR gate), 7404 (NOT gate), 7400 (NAND gate), 7402 (NOR gate), 7486 (XOR gate)
- Connecting wires

## Procedure

The procedure for this experiment is as follows:

1. Connect the power supply to the breadboard and turn it on.
2. Connect the pin 14 of each IC to the positive terminal of the power supply and the pin 7 of each IC to the ground terminal of the power supply. These pins are used to power the ICs.
3. Connect the logic probe to the power supply and the ground terminals. The logic probe is a device that can detect and display the logic level (high or low) of a signal.
4. To verify the truth table of a logic gate, connect the inputs of the gate to the switches on the breadboard and the output of the gate to the logic probe. The switches can be used to change the input values from high (1) to low (0) and vice versa.
5. For each possible combination of inputs, note down the output value displayed by the logic probe and compare it with the expected output value from the truth table of the gate. If the output values match, the truth table is verified.
6. Repeat steps 4 and 5 for each logic gate using the appropriate IC and pin numbers. The pin numbers for each gate are given below:

| Gate | IC | Pin numbers |
|------|----|--------------|
| AND  | 7408 | Input 1: 1, Input 2: 2, Output: 3 |
|      |      | Input 1: 4, Input 2: 5, Output: 6 |
|      |      | Input 1: 9, Input 2: 10, Output: 8 |
|      |      | Input 1: 12, Input 2: 13, Output: 11 |
| OR   | 7432 | Input 1: 1, Input 2: 2, Output: 3 |
|      |      | Input 1: 4, Input 2: 5, Output: 6 |
|      |      | Input 1: 9, Input 2: 10, Output: 8 |
|      |      | Input 1: 12, Input 2: 13, Output: 11 |
| NOT  | 7404 | Input: 1, Output: 2 |
|      |      | Input: 3, Output: 4 |
|      |      | Input: 5, Output: 6 |
|      |      | Input: 9, Output: 8 |
|      |      | Input: 11, Output: 10 |
|      |      | Input: 13, Output: 12 |
| NAND | 7400 | Input 1: 1, Input 2: 2, Output: 3 |
|      |      | Input 1: 4, Input 2: 5, Output: 6 |
|      |      | Input 1: 9, Input 2: 10, Output: 8 |
|      |      | Input 1: 12, Input 2: 13, Output: 11 |
| NOR  | 7402 | Input 1: 1, Input 2: 2, Output: 3 |
|      |      | Input 1: 4, Input 2: 5, Output: