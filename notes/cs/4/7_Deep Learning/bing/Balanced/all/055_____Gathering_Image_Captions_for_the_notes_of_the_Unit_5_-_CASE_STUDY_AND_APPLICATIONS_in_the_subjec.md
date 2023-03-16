# Gathering Image Captions

- Image captioning is the task of generating natural language descriptions for images.
- Image captioning has many applications, such as assisting visually impaired people, enhancing web search, creating photo albums, and generating educational content.
- Image captioning can be formulated as a supervised learning problem, where a model is trained on a large dataset of image-caption pairs.
- However, collecting such a dataset is costly and time-consuming, as it requires human annotators to provide captions for each image.
- Therefore, alternative methods of gathering image captions have been proposed, such as using existing web resources, crowdsourcing, or self-training.

## Using existing web resources

- One way of gathering image captions is to leverage existing web resources, such as image search engines, social media platforms, or online photo collections.
- These resources often contain images that are accompanied by textual information, such as titles, tags, comments, or descriptions.
- This textual information can be used as captions for the images, or as a source of inspiration for generating captions.
- For example, the Flickr8k and Flickr30k datasets were created by using Flickr images and their user-provided tags and comments as captions.
- However, using existing web resources has some limitations, such as:
  - The textual information may not be relevant, accurate, or descriptive enough for the images.
  - The textual information may contain noise, such as spelling errors, slang, or abbreviations.
  - The textual information may not cover all the aspects of the images, such as the background, the context, or the emotions.
  - The textual information may not be consistent, as different users may provide different captions for the same image.
  - The textual information may not be diverse, as some images may have many captions, while others may have none.

## Using crowdsourcing

- Another way of gathering image captions is to use crowdsourcing platforms, such as Amazon Mechanical Turk (AMT), where human workers are paid to perform various tasks, such as labeling, transcribing, or captioning images.
- Crowdsourcing can provide high-quality and diverse captions, as human workers can use their creativity, common sense, and domain knowledge to describe images.
- For example, the MS COCO dataset was created by using AMT workers to provide captions for images from various sources, such as Flickr, Instagram, or stock photos.
- However, using crowdsourcing also has some challenges, such as:
  - The cost and time of hiring and managing human workers.
  - The quality and reliability of the workers, as some may provide low-quality, incomplete, or inappropriate captions.
  - The variability and subjectivity of the workers, as different workers may have different perspectives, preferences, and styles of captioning images.
  - The scalability and diversity of the workers, as some workers may dominate the tasks, while others may be underrepresented or excluded.

## Using self-training

- A third way of gathering image captions is to use self-training, where a model is trained on a small dataset of image-caption pairs, and then used to generate captions for new images, which are then added to the dataset, and the process is repeated iteratively.
- Self-training can reduce the dependency on human annotations, as the model can learn from its own generated captions, and improve over time.
- For example, the Self-Critical Sequence Training (SCST) method was proposed to use self-training to improve the performance of image captioning models, by using reinforcement learning to optimize the model's own captions.
- However, using self-training also has some drawbacks, such as:
  - The quality and diversity of the generated captions, as the model may produce inaccurate, repetitive, or generic captions.
  - The feedback and evaluation of the generated captions, as the model may not have a reliable way of measuring its own performance, or correcting its own errors.
  - The stability and convergence of the self-training process, as the model may get stuck in a local optimum, or diverge from the desired goal.