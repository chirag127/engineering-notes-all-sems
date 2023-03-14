Steganography is the art and science of embedding secret messages in a cover message in such a way that no one, apart from the sender and intended recipient, suspects the existence of the message. 

The following diagram illustrates the basic architecture of a steganographic system:

```
+----------------+     +----------------+     +----------------+
| Cover message  |     | Secret message |     | Stego key      |
+----------------+     +----------------+     +----------------+
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
                              |
                              v
                    +---------------------+
                    | Steganographic     |
                    | encoder            |
                    +---------------------+
                              |
                              v
                      +---------------+
                      | Stego message |
                      +---------------+
                              |
                              v
                    +---------------------+
                    | Steganographic     |
                    | decoder            |
                    +---------------------+
                              |
                              v
        +----------------+     +----------------+     +----------------+
        | Cover message  |     | Secret message |     | Stego key      |
        +----------------+     +----------------+     +----------------+
```

The cover message is the original message that is used to hide the secret message. The secret message is the data that needs to be concealed from others. The stego key is an optional parameter that can be used to enhance the security of the system. The steganographic encoder is a function that takes the cover message, the secret message, and the stego key as inputs and produces the stego message as output. The stego message is the modified message that contains the secret message embedded in it. The steganographic decoder is a function that takes the stego message and the stego key as inputs and extracts the secret message and the cover message as outputs.

There are different types of steganography depending on the nature of the cover message and the secret message. Some of the common types are:

- Text steganography: The cover message and the secret message are both text. The secret message can be hidden by using various techniques such as changing the font size, color, or spacing of the characters, inserting invisible characters, or using acrostics or null ciphers.
- Image steganography: The cover message is an image and the secret message can be text, image, audio, or video. The secret message can be hidden by using various techniques such as modifying the least significant bits of the pixels, using color palettes, or applying transformations or filters.
- Audio steganography: The cover message is an audio file and the secret message can be text, image, audio, or video. The secret message can be hidden by using various techniques such as modifying the amplitude, frequency, or phase of the sound waves, using echo hiding, or applying compression or encryption.
- Video steganography: The cover message is a video file and the secret message can be text, image, audio, or video. The secret message can be hidden by using various techniques such as modifying the frames, pixels, or motion vectors of the video, using scene transitions, or applying watermarking or encryption.
- Network steganography: The cover message is a network protocol or a network packet and the secret message can be text, image, audio, or video. The secret message can be hidden by using various techniques such as modifying the header fields, payload, or timing of the packets, using covert channels, or applying encryption or tunneling.

Steganography is different from cryptography, which is the practice of protecting the contents of a message by making it unreadable to anyone except the intended recipient. Cryptography does not hide the existence of the message, whereas steganography does. Cryptography can be combined with steganography to achieve a higher level of security and privacy. 

: Steganography Tutorial – A Complete Guide For Beginners. https://www.edureka.co/blog/steganography-tutorial