 Here is the content in markdown format for the topic ### Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing:

### Weighted Cepstral Distances And Filtering

Cepstral distance is a measure of similarity between two speech signals based on the cepstral coefficients. It calculates the Euclidean distance between cepstral coefficients of two speech frames.

Weighted Cepstral Distance (WCD) is a modified cepstral distance that weighs lower quefrency cepstral coefficients more than higher quefrency coefficients. This is because lower quefrency coefficients contain more salient information about the speech signal. WCD is calculated as:

WCD = ∑ w[k] × (c1[k] - c2[k])2

where w[k] is the weight for the k-th coefficient and c1[k], c2[k] are k-th cepstral coefficients of signals 1 and 2 respectively.

Filtering cepstral coefficients can enhance the performance of WCD. A low pass filter is applied to cepstral coefficients to remove high frequency noise. Filtered WCD (FWCD) is more robust to noise and gives better results than simple WCD.

Advantages:
- Considers perceptual importance of different frequency bands
- Robust to noise
- Easy and fast to compute

Disadvantages:
- Fixed weighting may not be optimal for all speech signals
- May not detect partial similarities between speech signals

Applications:
- Speaker verification
- Speech recognition
- Plagiarism detection

Mnemonics:
- WCD weighs lower quefrencies more (important speech information)
- Filtering removes high frequency noise (increases robustness)

Learning tricks:
- Understand how cepstral coefficients capture speech dynamics
- Try implementing WCD and FWCD on sample speech data and observe the results
- Play around with weight values and filter parameters to understand their effect