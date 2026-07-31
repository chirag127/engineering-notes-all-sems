### Software fault isolation

- Software fault isolation (SFI) is a technique to prevent faulty or malicious software components from compromising the security or reliability of a system.
- SFI establishes a logical protection domain by inserting dynamic checks before memory and control-transfer instructions.
- SFI ensures that each component can only access its own memory region and can only invoke predefined entry points of other components.
- SFI can be implemented using various techniques, such as:
  - Code rewriting: modifying the binary code of a component to insert the checks.
  - Code verification: verifying that the source or binary code of a component conforms to the checks.
  - Hardware support: using hardware features, such as segmentation or virtualization, to enforce the checks.
- SFI can provide several benefits, such as:
  - Isolating faults and errors within a component and preventing them from propagating to other components or the system.
  - Enforcing confidentiality and integrity policies between components and preventing unauthorized information flows or modifications.
  - Reducing the attack surface and mitigating the impact of software vulnerabilities or exploits.
  - Supporting modularity and extensibility of software systems by allowing the integration of untrusted or third-party components.