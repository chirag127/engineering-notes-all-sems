 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Code optimization for the notes of the Unit 5 - Code Generation in the subject of Compiler Design.

1. Constant folding: Replace constants with their values.
For example: Replace c = a + 10; with c = a + 5; if a equals 5.

2. Common subexpression elimination: Identify common subexpressions and evaluate them only once.
For example: Replace x = a + b; y = a + b; with t = a + b; x = t; y = t;.

3. Local code motion: Move computations out of loops if their operands do not change within the loop.
For example: Replace for (i=0; i<n; i++) x = a + b; with x = a + b; for (i=0; i<n; i++).

4. Global code motion: Move computations out of loops if their operands do not change anywhere within the enclosing block.
For example: Same as local code motion but applies to a wider scope.

5. Induction variable elimination: Replace the use of variables that change in increments related to the loop increment with the loop variable.
For example: Replace i = 0; while (i < n) { t = a[i]; i = i + 1; } with t = a[i]; while (i < n) i = i + 1;.

6. Loop inversion: Change the order of operations to perform loop-invariant computations outside the loop.
For example: Replace for (i=0; i<n; i++) s = s + a[i]; with s = n * a[0]; for (i=1; i<n; i++) s = s - a[i];.

7. Strength reduction: Replace costly operations by less costly ones.
For example: Replace multiplication by shifting/masking where appropriate. Replace divisions by multiplications (after scaling).