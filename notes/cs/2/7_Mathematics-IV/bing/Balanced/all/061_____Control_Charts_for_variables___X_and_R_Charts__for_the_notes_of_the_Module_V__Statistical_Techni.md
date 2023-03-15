# Control Charts for Variables (X and R Charts)

- Control charts are graphical tools that help monitor the quality and stability of a process over time by plotting sample data and control limits.
- Variables are measurable characteristics of a process, such as length, weight, temperature, etc.
- X and R charts are a pair of control charts that are used with variables data that have a subgroup size of two or more.
- X chart plots the sample means (X) of the subgroups and monitors the changes in the process mean.
- R chart plots the sample ranges (R) of the subgroups and monitors the changes in the process variation.
- The control limits for the X chart are calculated as:

  - Upper control limit (UCL) = X + A2 * R
  - Lower control limit (LCL) = X - A2 * R
  - Center line (CL) = X

  where X is the grand mean of all subgroup means, R is the average of all subgroup ranges, and A2 is a constant that depends on the subgroup size.

- The control limits for the R chart are calculated as:

  - Upper control limit (UCL) = D4 * R
  - Lower control limit (LCL) = D3 * R
  - Center line (CL) = R

  where R is the average of all subgroup ranges, and D3 and D4 are constants that depend on the subgroup size.

- The constants A2, D3 and D4 can be found in standard tables or calculated from the formulae:

  - A2 = 3 / sqrt(n)
  - D3 = 3 * (1 - 1 / sqrt(n))
  - D4 = 3 * (1 + 1 / sqrt(n))

  where n is the subgroup size.

- To construct the X and R charts, the following steps are followed:

  1. Collect and organize the data into subgroups of equal size.
  2. Calculate the subgroup means and ranges.
  3. Calculate the grand mean of all subgroup means and the average of all subgroup ranges.
  4. Calculate the control limits for the X and R charts using the formulas above.
  5. Plot the subgroup means and ranges on the X and R charts, along with the control limits and the center lines.
  6. Analyze the charts for any patterns or points that indicate an out-of-control process.

- An example of X and R charts is shown below:

  | Subgroup | X | R |
  | -------- | - | - |
  | 1        | 5 | 2 |
  | 2        | 6 | 3 |
  | 3        | 7 | 4 |
  | 4        | 8 | 5 |
  | 5        | 9 | 6 |

  - The subgroup size is n = 2.
  - The grand mean of all subgroup means is X = (5 + 6 + 7 + 8 + 9) / 5 = 7.
  - The average of all subgroup ranges is R = (2 + 3 + 4 + 5 + 6) / 5 = 4.
  - The constants are A2 = 3 / sqrt(2) = 2.121, D3 = 3 * (1 - 1 / sqrt(2)) = 0.879, D4 = 3 * (1 + 1 / sqrt(2)) = 5.364.
  - The control limits for the X chart are:

    - UCL = 7 + 2.121 * 4 = 15.484
    - LCL = 7 - 2.121 * 4 = -1.484
    - CL = 7

  - The control limits for the R chart are:

    - UCL = 5.364 * 4 = 21.456
    - LCL = 0.879 * 4 = 3.516
    - CL = 4

  - The X and R charts are shown below:

    ```markdown
    X chart:

    16 |              *
    15 |              *
    14 |              *
    13 |              *
    12 |              *
    11 |              *
    10 |              *
     9 |              *
     8 |