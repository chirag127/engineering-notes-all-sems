## Design, and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An asynchronous counter is a sequential circuit that uses flip-flops as memory elements and changes its output state in response to the clock pulses applied to one or more of its flip-flops.
- A 4-bit asynchronous counter can count from 0 to 15 in binary, and has four flip-flops connected in a cascade manner, where the output of one flip-flop drives the clock input of the next flip-flop.
- To design a 4-bit asynchronous counter using J-K flip-flops, the following steps are required:
  - Determine the characteristic equation of the J-K flip-flop, which is Q(next) = JQ + K'Q.
  - Determine the excitation table of the J-K flip-flop, which shows the values of J and K inputs required to produce the desired next state for each present state.
  - Determine the state transition table of the 4-bit counter, which shows the present state and the next state for each flip-flop in binary.
  - Determine the logic expressions for J and K inputs of each flip-flop by using the excitation table and the state transition table.
  - Draw the circuit diagram of the 4-bit counter by using the logic expressions and the J-K flip-flops.
- To verify the 4-bit asynchronous counter, the following steps are required:
  - Apply a clock pulse to the clock input of the first flip-flop and observe the output waveforms of each flip-flop on an oscilloscope or a logic analyzer.
  - Check if the output waveforms match the expected binary counting sequence from 0 to 15 and repeat for each clock pulse.
  - Check if the counter recycles back to 0 after reaching 15 and verify the modulus of the counter, which is 16.