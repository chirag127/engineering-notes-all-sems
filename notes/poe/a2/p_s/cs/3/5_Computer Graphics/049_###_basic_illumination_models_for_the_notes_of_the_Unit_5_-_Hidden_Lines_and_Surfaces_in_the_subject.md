 Here is the content in markdown format for the topic ### basic illumination models for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics:

#### Point light source:
- A point light source emits light in all directions equally
- The intensity decreases with increasing distance (following inverse-square law)
- Used to simulate localized light sources like light bulbs
- Requires calculating illumination for many surfaces due to widespread diffusion of light
- Casts soft shadows with fuzzy edges

#### Directional light source:
- Light rays are parallel to each other
- No defined location, light comes from a particular direction
- Intensity does not decrease with distance
- Simulates light from distant sources like sun or moon
- Casts sharp, distinct shadows

#### Spotlight:
-Light is emitted within a cone from the source
- Intensity highest at center (hotspot) and decreases towards edges ( spill )
- Allows highlighting focus areas
- Allows control over spread of light and hardness of shadows

Advantages:
- Adds realism by simulating different types of light sources
- Allows flexibility to create desired effects like highlights and shadows

Disadvantages:
- Computing illumination for every surface can be time-consuming for complex scenes especially with many point light sources
- Does not account for indirect illumination (light reflected off other surfaces) leading to less realistic results

Applications:
- 3D modeling and rendering software
- Video games
- Special effects in movies
- architectural visualization

[Include diagrams and codes if helpful]