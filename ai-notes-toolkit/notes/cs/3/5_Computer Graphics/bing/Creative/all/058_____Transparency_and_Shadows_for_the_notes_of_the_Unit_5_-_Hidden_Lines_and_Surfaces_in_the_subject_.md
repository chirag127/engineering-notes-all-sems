# Transparency and Shadows

## Transparency
- Transparency is the property of a material that allows light to pass through it partially or fully.
- Transparency can be used to create realistic effects such as glass, water, ice, etc. in computer graphics.
- Transparency can be classified into two types: **binary transparency** and **partial transparency** .
- Binary transparency is when a pixel is either fully transparent or fully opaque, such as in GIF images or masks.
- Partial transparency is when a pixel can have varying degrees of transparency, such as in PNG images or alpha blending.
- Partial transparency can be simulated by mixing the colors of the transparent object and the background object, using a factor called the **alpha value** .
- The alpha value ranges from 0 to 1, where 0 means fully transparent and 1 means fully opaque.
- The formula for alpha blending is:

  C = alpha * C1 + (1 - alpha) * C2

  where C is the resulting color, C1 is the color of the transparent object, C2 is the color of the background object, and alpha is the alpha value.

- Transparency can also be affected by the viewing angle, the thickness of the material, the refraction of light, and the presence of multiple transparent layers .
- Transparency can be implemented in computer graphics using various techniques, such as ray tracing, depth peeling, alpha testing, etc.

## Shadows
- Shadows are the regions where light is blocked by an object, creating a contrast between the illuminated and the dark areas.
- Shadows can enhance the realism, depth, and mood of a scene in computer graphics.
- Shadows can be classified into two types: **hard shadows** and **soft shadows**.
- Hard shadows are when the boundary between the shadow and the light is sharp and well-defined, such as in a sunny day or a point light source.
- Soft shadows are when the boundary between the shadow and the light is fuzzy and blurred, such as in a cloudy day or an area light source.
- Soft shadows are more realistic than hard shadows, but also more computationally expensive to generate.
- Shadows can be implemented in computer graphics using various techniques, such as shadow mapping, shadow volumes, ray tracing, etc.