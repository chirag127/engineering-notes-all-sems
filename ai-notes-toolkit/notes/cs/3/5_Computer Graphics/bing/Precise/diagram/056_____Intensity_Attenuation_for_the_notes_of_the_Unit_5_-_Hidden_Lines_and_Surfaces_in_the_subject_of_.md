### Intensity Attenuation for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- In computer graphics, attenuation is the reduction or loss of intensity of any kind of flux through a medium .
- Attenuation is the gradual decrease in energy as the X-radiation passes through absorbing material .
- The intensity field stores the RGB components of the surface color at that point and the percent of pixel coverage .
- If depth < 0, it indicates multiple-surface contributions to the pixel intensity. The intensity field then stores a pointer to a linked list of surface data .
- A fast and straightforward method for rendering an object with polygon surfaces is constant intensity shading, also called Flat Shading .
- In this method, a single intensity is calculated for each polygon. All points over the surface of the polygon are then displayed with the same intensity value .
- The surface attenuation model simulates scattering effects .
- Intensity attenuation is the light falling off the further away one gets from the source .
- This distinguishes overlapping surfaces having the same reflection parameters .
- Radiant energy disperses as 1/d2 .
