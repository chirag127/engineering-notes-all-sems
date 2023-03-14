### ImageNet

- ImageNet is an image database organized according to the WordNet hierarchy (currently only the nouns), in which each node of the hierarchy is depicted by hundreds and thousands of images. 
- The project has been instrumental in advancing computer vision and deep learning research. The data is available for free to researchers for non-commercial use. 
- ImageNet contains more than 20,000 categories, with a typical category, such as "balloon" or "strawberry", consisting of several hundred images. 
- The database of annotations of third-party image URLs is freely available directly from ImageNet, though the actual images are not owned by ImageNet. 
- ImageNet crowdsources its annotation process. Image-level annotations indicate the presence or absence of an object class in an image, such as "there are tigers in this image" or "there are no tigers in this image". Object-level annotations provide a bounding box around the (visible part of the) indicated object. 
- ImageNet uses a variant of the broad WordNet schema to categorize objects, augmented with 120 categories of dog breeds to showcase fine-grained classification. 
- One downside of WordNet use is the categories may be more "elevated" than would be optimal for ImageNet: "Most people are more interested in Lady Gaga or the iPod Mini than in this rare kind of diplodocus." 
- Since 2010, the ImageNet project runs an annual software contest, the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), where software programs compete to correctly classify and detect objects and scenes. The challenge uses a "trimmed" list of one thousand non-overlapping classes. 
- The ILSVRC has been a major catalyst for the development of deep learning methods for image recognition, such as convolutional neural networks (CNNs). 
- In 2012, a CNN called AlexNet achieved a top-5 error of 15.3% in the ILSVRC, more than 10.8 percentage points lower than that of the runner up. This was made feasible due to the use of graphics processing units (GPUs) during training. 
- In 2015, a very deep CNN with over 100 layers, called ResNet, won the ILSVRC with a top-5 error of 3.6%. 
- ImageNet is useful for many computer vision applications such as object recognition, image classification and object localization. Prior to ImageNet, a researcher wrote one algorithm to identify dogs, another to identify cats, and so on. After training with ImageNet, the same algorithm could be used to identify different objects. 

: ImageNet website, https://www.image-net.org/
: ImageNet - Wikipedia, https://en.wikipedia.org/wiki/ImageNet
: ImageNet - Devopedia, https://devopedia.org/imagenet
: The Economist, "The return of the machinery question", https://www.economist.com/special-report/2016/06/23/the-return-of-the-machinery-question
: Krizhevsky et al., "ImageNet Classification with Deep Convolutional Neural Networks", https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
: He et al., "Deep Residual Learning for Image Recognition", https://arxiv.org/abs/1512.03385