##### Function Point (FP) Based Measures in software design

Function Point (FP) is a unit of measure for software functionality that is independent of the technology used for implementation. It is based on the user's perspective of the software requirements and the complexity of the software components. FP can be used to estimate the cost, duration, and resources required for a software project.

To calculate FP, the following steps are usually followed:

- Identify the types of functions that the software provides, such as external inputs, external outputs, external inquiries, internal logical files, and external interface files. Each function type has a different weight based on its complexity.
- Count the number of functions of each type and multiply them by their respective weights to obtain the unadjusted function point (UFP) count.
- Apply a complexity adjustment factor (CAF) based on 14 general system characteristics that affect the software functionality, such as data communications, distributed functions, performance, etc. Each characteristic is rated from 0 to 5 based on its degree of influence. The CAF is calculated as 0.65 + (0.01 * sum of ratings).
- Multiply the UFP by the CAF to obtain the adjusted function point (AFP) count.

The following is an example of a pseudo-code for calculating FP based on the above steps:

```python
# Define the weights for each function type
input_weight = {"low": 3, "average": 4, "high": 6}
output_weight = {"low": 4, "average": 5, "high": 7}
inquiry_weight = {"low": 3, "average": 4, "high": 6}
file_weight = {"low": 7, "average": 10, "high": 15}
interface_weight = {"low": 5, "average": 7, "high": 10}

# Define the ratings for each general system characteristic
data_communication = 4 # High degree of influence
distributed_function = 3 # Moderate degree of influence
performance = 5 # Essential degree of influence
# ... and so on for the remaining 11 characteristics

# Count the number of functions of each type and complexity
input_low = 10 # 10 low-complexity external inputs
input_average = 5 # 5 average-complexity external inputs
input_high = 0 # 0 high-complexity external inputs
output_low = 8 # 8 low-complexity external outputs
output_average = 4 # 4 average-complexity external outputs
output_high = 2 # 2 high-complexity external outputs
inquiry_low = 6 # 6 low-complexity external inquiries
inquiry_average = 3 # 3 average-complexity external inquiries
inquiry_high = 0 # 0 high-complexity external inquiries
file_low = 2 # 2 low-complexity internal logical files
file_average = 1 # 1 average-complexity internal logical file
file_high = 0 # 0 high-complexity internal logical file
interface_low = 1 # 1 low-complexity external interface file
interface_average = 0 # 0 average-complexity external interface file
interface_high = 0 # 0 high-complexity external interface file

# Calculate the unadjusted function point (UFP) count
UFP = (input_low * input_weight["low"]) + (input_average * input_weight["average"]) + (input_high * input_weight["high"]) + (output_low * output_weight["low"]) + (output_average * output_weight["average"]) + (output_high * output_weight["high"]) + (inquiry_low * inquiry_weight["low"]) + (inquiry_average * inquiry_weight["average"]) + (inquiry_high * inquiry_weight["high"]) + (file_low * file_weight["low"]) + (file_average * file_weight["average"]) + (file_high * file_weight["high"]) + (interface_low * interface_weight["low"]) + (interface_average * interface_weight["average"]) + (interface_high * interface_weight["high"])

# Calculate the complexity adjustment factor (CAF)
CAF = 0.65 + (0.01 * (data_communication + distributed_function + performance + ...))

# Calculate the adjusted function point (AFP) count
AFP = UFP * CAF
```