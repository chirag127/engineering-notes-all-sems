 Here are the notes on decaying window for the Unit 4 - Mining Data Streams in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION:

### Decaying Window

- A decaying window is a type of sliding window where older events/data points are given less weightage as compared to the recent ones.
- This is done to keep the model more focused on the recent trends/patterns in the data rather than the old ones.
- The weightage of the old data points is reduced by applying an exponential decay function.
- The decay function can be tuned based on how fast we want the older data points to lose weightage.
- A faster decay rate will make the model more reactive to recent changes but can also lead to overfitting. A slower decay rate leads to more stable models but can cause delay in detecting newer trends.
- Decaying windows are useful in scenarios like fraud detection, trend analysis, etc. where recent data is more important than old data.

The key points to summarize are:

1. Decaying window is a sliding window where recent data points have higher weightage.
2. Older data points lose weightage exponentially using a decay function.
3. Decay rate tuning impacts model reactivity and stability.
4. Useful in scenarios where recent data is more important (fraud detection, trend analysis, etc.).