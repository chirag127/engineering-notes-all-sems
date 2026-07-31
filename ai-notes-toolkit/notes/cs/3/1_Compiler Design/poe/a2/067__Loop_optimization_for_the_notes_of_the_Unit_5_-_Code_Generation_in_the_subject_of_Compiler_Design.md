 Here is the content in markdown format without any emojis or external links as per your instructions:

### Loop optimization for the notes of the Unit 5 - Code Generation in the subject of Compiler Design.

1. Loop invariant code motion:
- If a statement is loop invariant (does not change in the loop iterations), it can be moved out of the loop.
- This improves cache locality and reduces the work done in each iteration.

2. Loop unrolling:
- The loop body is duplicated a fixed number of times.
- This reduces the overhead of loop control and Fetch-Execute cycles.
- However, this increases the code size and can exceed cache capacity.

3. Loop interchange:
- The order of nested loops is interchanged.
- This can improve cache locality if the arrays have a different access pattern with the new loop order.

4. Loop fusion:
- Two adjacent loops are combined into a single loop.
- This avoids duplicate initialization and finalization of the loop and may expose more loop-level parallelism.

5. Loop distribution:
- A loop is split into multiple loops that can be executed in parallel.
- This exploits parallelism but can increase the overhead.

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.