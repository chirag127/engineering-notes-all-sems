### Software Re- Engineering (SR) of Software

Software Re- Engineering (SR) of Software is a process of software development which is done to improve the maintainability, efficiency, and effectiveness of a software system . It involves examining and altering the system to reconstitute it in a new form, while preserving its functionality and architecture . It encompasses a combination of sub-processes such as reverse engineering, forward engineering, reconstructing, etc.

Reverse engineering is the process of analyzing the existing system to extract its design and specification. Forward engineering is the process of creating a new system from the extracted design and specification. Reconstructing is the process of modifying the system to improve its quality and performance. 

A possible code for SR of software is:

```python
# Define the existing system
system = SoftwareSystem(name="Old System", functionality="F", architecture="A")

# Perform reverse engineering
design, specification = reverse_engineer(system)

# Perform forward engineering
new_system = forward_engineer(design, specification, name="New System")

# Perform reconstructing
new_system = reconstruct(new_system, quality="Q", performance="P")

# Output the new system
print(new_system)
```