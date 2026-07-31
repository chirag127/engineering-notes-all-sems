#### Transmission media in Computer Networks

Transmission media refers to the physical pathways that carry data signals between devices in a computer network. There are two main types of transmission media: guided and unguided. Guided media, also known as wired or bounded media, includes copper cables and fiber optic cables. Unguided media, also known as wireless or unbounded media, includes radio waves, microwaves, and infrared waves.

Here is an example of code that can be used to represent the different types of transmission media in a computer network:

```python
class TransmissionMedia:
    def __init__(self, media_type, guided):
        self.media_type = media_type
        self.guided = guided

    def __str__(self):
        return f'{self.media_type} is {"guided" if self.guided else "unguided"} media.'

copper_cable = TransmissionMedia('Copper cable', True)
fiber_optic_cable = TransmissionMedia('Fiber optic cable', True)
radio_wave = TransmissionMedia('Radio wave', False)
microwave = TransmissionMedia('Microwave', False)
infrared_wave = TransmissionMedia('Infrared wave', False)

print(copper_cable)
print(fiber_optic_cable)
print(radio_wave)
print(microwave)
print(infrared_wave)
```

This code defines a `TransmissionMedia` class that takes in two arguments: `media_type` and `guided`. The `media_type` argument represents the type of transmission media, while the `guided` argument is a boolean value that indicates whether the media is guided or unguided. The `__str__` method is used to define how the object should be represented as a string. In this case, it returns a string that indicates the media type and whether it is guided or unguided.

The code then creates five instances of the `TransmissionMedia` class, representing copper cable, fiber optic cable, radio wave, microwave, and infrared wave. These objects are then printed to the console, showing their media type and whether they are guided or unguided.
