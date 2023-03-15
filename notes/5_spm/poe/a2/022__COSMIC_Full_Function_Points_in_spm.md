 Here is the content in markdown format with points, without emotions or friendliness, being formal, without emojis or external links:

### COSMIC Full Function Points in spm

1. Calculate Unadjusted Function Point (UFP):
- Count Inputs: Count each distinguishable input including those from interfaces to external systems.
- Count Outputs: Count each distinguishable output including those to interfaces to external systems.
- Count Queries: Count each distinct logical internal logical file or data base accessed for information.
- Count External Interfaces: Count each external input, output, query, or interface.

2. Determine Value Adjustment Factor (VAF):
- Consider 14 General System Characteristics and assign value to each from 0-5.
- Calculate VAF = Total of individual values/14.

3. Calculate Adjusted Function Point (AFP):
AFP = UFP x VAF

4. Calculate FP Count for Enhancement/Modification:
AFP of Enhancement or Modification / AFP of Base

The COSMIC Full Function Point method in Software Performance and Metrics (spm) helps obtain a quantitative measure of the functionality of software. The steps involve counting various components like inputs, outputs, queries, external interfaces, determining value adjustment factor and calculating adjusted function points. The adjusted function points can be used to measure enhancement or modification of software.