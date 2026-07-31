 Here is the content in Markdown format without any emojis or external links, written in a formal tone with points:

### Segmentation by morphological watersheds

1. Watershed segmentation is a morphological segmentation technique. It treats the image as a topological relief where the pixels act as catchment basins.
2. The algorithm floods the relief from the minimum (seed points) positions, and a dam is built wherever two flooding basins meet, eventually segmenting the image.
3. The key steps are:
- Computing the distance transform of the image
- Finding regional minima (seeds) of the distance transform
- Performing the watershed transform on the distance transform using the seeds

4. The distance transform denotes the minimum distance of a pixel from the nearest seed. The flooding starts from the seeds and terminates at the dams formed by the adjacent catchment basins.
5. The advantages of watershed segmentation are:
- It can separate overlapping and touching objects.
- It does not require prior information about the number of segments.
- It has a strong underlying theory based on mathematical morphology.

6. The disadvantages are:
- It is sensitive to noise as minor gradients can also lead to oversegmentation.
- It can produce irregular-shaped segments.
- It is computationally expensive for large images.

7. To handle the oversegmentation problem, markers can be used to guide the flooding process. The image gradients can also be regularized by filtering before applying the watershed transform.