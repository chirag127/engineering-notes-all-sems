
### The LZ77 Approach 

* The LZ77 algorithm is a data compression technique developed by Abraham Lempel and Jacob Ziv in 1977.
* It is a dictionary-based compression technique which uses a sliding window to store a previously seen sequence of characters and then matches the current sequence of characters with the stored sequence. 
* The algorithm works by searching for matches between the current sequence of characters and the stored sequence. 
* When a match is found, the algorithm stores the index of the match and the length of the match.
* This index and length are then encoded and sent to the receiver. 
* At the receiver side, the index and length are decoded and the original sequence of characters is reconstructed. 
* The LZ77 algorithm is used in many applications such as compression of text, images, audio, video, etc.