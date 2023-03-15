# Transparency and Shadows

## Transparency
- Transparency is the property of a material that allows light to pass through it partially or fully.
- Transparency can be used to create realistic effects such as glass, water, ice, etc. in computer graphics.
- Transparency can be classified into two types: **binary transparency** and **partial transparency** .
- Binary transparency is when a pixel is either fully transparent or fully opaque. This can be achieved by using an alpha channel that stores a binary value for each pixel.
- Partial transparency is when a pixel can have varying degrees of transparency, from fully transparent to fully opaque. This can be achieved by using an alpha channel that stores a fractional value for each pixel, or by blending the colors of the pixel and the background according to a transparency function .
- Partial transparency can also be called **translucency** .
- Transparency can be implemented in different ways, such as alpha blending, alpha testing, alpha compositing, etc.

## Shadows
- Shadows are the regions where light is blocked by an object or a surface.
- Shadows can enhance the realism and depth of a scene rendered with computer graphics.
- Shadows can be classified into two types: **hard shadows** and **soft shadows**.
- Hard shadows are when the boundary between the shadow and the illuminated region is sharp and well-defined. This can be achieved by using a single point light source or a directional light source.
- Soft shadows are when the boundary between the shadow and the illuminated region is fuzzy and gradual. This can be achieved by using an area light source or multiple light sources.
- Shadows can be implemented in different ways, such as shadow mapping, shadow volumes, ray tracing, etc.