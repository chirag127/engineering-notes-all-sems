### 2. Engineering Physics-Theory and Practical- Katiyar & Pandey (Wiley India)

- This book is a textbook for Engineering Physics-I and Engineering Physics-II courses of Uttar Pradesh Technical University (UPTU), Lucknow. It also covers the practical syllabus of these courses.
- The book is divided into two parts: Part A covers the theory and Part B covers the practical. Each part has 10 chapters, covering topics such as crystal structure, interference, diffraction, polarization, lasers, fiber optics, quantum mechanics, nuclear physics, semiconductors, and superconductivity.
- The book aims to provide a clear and concise explanation of the concepts and principles of physics, with an emphasis on applications in engineering and technology. It also includes numerous solved examples, exercises, and multiple choice questions to help students test their understanding and prepare for exams.
- The book also provides some mnemonics and learning tricks for some topics, such as:

  - To remember the Bravais lattices, use the acronym **COPIT** (Cubic, Orthorhombic, Primitive, I-centered, Tetragonal).
  - To remember the conditions for constructive and destructive interference, use the phrase **Even path difference, even order, bright fringe** and **Odd path difference, odd order, dark fringe**.
  - To remember the types of polarization, use the acronym **BREW** (Brewster angle, Reflection, Elliptical, Wave plate).
  - To remember the types of lasers, use the acronym **GASH** (Gas, Atomic, Solid, He-Ne).
  - To remember the types of optical fibers, use the acronym **SMMS** (Single mode, Multi mode, Step index, Graded index).
  - To remember the postulates of quantum mechanics, use the phrase **Wave function, observable, probability, Schrodinger equation**.
  - To remember the types of nuclear reactions, use the acronym **FANS** (Fission, Alpha decay, Neutron capture, Spontaneous fission).
  - To remember the types of semiconductors, use the acronym **IGE** (Intrinsic, Germanium, Extrinsic).
  - To remember the types of superconductors, use the acronym **HTC** (High temperature, Type I, Type II).

- The book also provides some detailed diagrams, tables, codes, advantages, disadvantages, examples, and applications for some topics, such as:

  - The diagram of the unit cell of a simple cubic lattice:

```
    +---+---+
   /   /   /|
  +---+---+ +
 /   /   /|/|
+---+---+ + +
|   |   |/|/|
+---+---+ + +
|   |   |/|/
+---+---+ +
|   |   |/
+---+---+
```

  - The table of the properties of some common lasers:

| Laser | Medium | Wavelength | Output power | Application |
|-------|--------|------------|--------------|-------------|
| He-Ne | Gas    | 632.8 nm   | 10 mW        | Holography, metrology, barcode scanners |
| Ruby  | Solid  | 694.3 nm   | 10 J         | Pulsed laser, laser welding, tattoo removal |
| Nd:YAG| Solid  | 1064 nm    | 10 kW        | Continuous laser, laser cutting, laser drilling |
| CO2   | Gas    | 10.6 um    | 100 kW       | Industrial laser, laser surgery, laser engraving |

  - The code for the simulation of the double slit experiment in Python:

```python
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
wavelength = 500e-9 # wavelength of light in meters
slit_width = 20e-6 # width of each slit in meters
slit_distance = 100e-6 # distance between the slits in meters
screen_distance = 1 # distance from the slits to the screen in meters
screen_width = 0.1 # width of the screen in meters
screen_resolution = 1000 # number of pixels on the screen

# Define functions
def slit_pattern(x, d, a):
  # Returns the intensity of the single slit diffraction pattern at position x
  # x: position on the screen in meters
  # d: distance from the slit to the screen in meters