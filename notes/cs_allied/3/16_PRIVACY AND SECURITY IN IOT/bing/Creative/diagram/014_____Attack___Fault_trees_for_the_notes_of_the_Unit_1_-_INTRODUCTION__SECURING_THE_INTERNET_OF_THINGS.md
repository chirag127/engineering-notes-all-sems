### Attack & Fault Trees

- Attack and fault trees are graphical methods to model and analyze the reliability and security of systems, especially in the context of IoT.
- A fault tree represents the logical combinations of events that can cause a system failure, using AND, OR, and other gates. A fault tree can be used to calculate the probability of failure, identify the critical components, and perform reliability analysis.
- A fault tree example for a car brake failure is shown below:

```
    Car brake failure
    /             \
  AND             AND
 /  \            /  \
Brake fluid   Brake pads
pressure      wear out
low           too much
```

- An attack tree represents the logical combinations of actions that an attacker can perform to achieve a malicious goal, using AND, OR, and other gates. An attack tree can be used to evaluate the security level of a system, identify the attack scenarios, and perform risk assessment.
- An attack tree example for stealing data from a smart home is shown below:

```
    Steal data from smart home
    /             \
  OR             OR
 /  \            /  \
Hack Wi-Fi   Break into   Bribe owner
network      house        to reveal data
```

- Attack and fault trees can be combined to model the interaction of malicious deliberate acts with random failures, and to consider both attacks and countermeasures. This is called an attack-fault tree or an attack-defense tree.
- An attack-fault tree example for a cyber-physical system is shown below:

```
    System failure
    /             \
  OR             OR
 /  \            /  \
Fault tree   Attack tree
for system   for system
failure      compromise
```

- Attack and fault trees can help to improve the security and reliability of IoT systems by providing a systematic and formal way to identify and analyze the potential threats and vulnerabilities, and to design and evaluate the mitigation strategies.