# Case studies for the notes of the Unit 4 - Mining Data Streams in the subject of INTRODUCTION TO DATA ANALYTICS AND VISUALIZATION

- Mining data streams is the process of extracting knowledge structures represented in models and patterns from continuous and unbounded streams of information.
- Data streams pose several challenges for data mining, such as high volume, high velocity, concept drift, limited memory, and real-time processing .
- Data stream mining algorithms need to be scalable, adaptive, incremental, and robust to handle these challenges .
- Some of the applications of data stream mining include network monitoring, sensor networks, web mining, social media analysis, fraud detection, and recommender systems  .
- Here are some case studies of data stream mining from different domains:

## Case study 1: Stream Data Mining Classification

- This case study presents a data stream mining classification task using the MOA (Massive Online Analysis) framework.
- The goal is to classify the network traffic data into normal or anomalous based on various features, such as duration, protocol, service, flag, source bytes, destination bytes, etc.
- The data stream is generated from the KDD Cup 1999 dataset, which contains 4.9 million records of network connections.
- The data stream mining classification algorithm used is the Hoeffding Tree, which is a decision tree that grows incrementally and adapts to the changing data distribution .
- The performance of the algorithm is evaluated using various metrics, such as accuracy, kappa, precision, recall, F1-score, and memory consumption.
- The results show that the Hoeffding Tree achieves an accuracy of 99.2% and a kappa of 0.98, which indicate a high agreement between the predicted and actual labels.
- The algorithm also consumes less memory and time than other classification algorithms, such as Naive Bayes and k-Nearest Neighbors.

## Case study 2: Improvised methods for tackling big data stream mining challenges: case study of electricity price prediction

- This case study proposes a holistic data stream mining approach for predicting the electricity price in the Australian National Electricity Market (NEM).
- The approach consists of four components: data preprocessing, feature selection, ensemble learning, and concept drift detection.
- The data preprocessing component applies various techniques, such as normalization, outlier detection, and missing value imputation, to improve the quality of the data stream.
- The feature selection component uses a wrapper method based on genetic algorithms to select the most relevant and informative features for the prediction task.
- The ensemble learning component combines multiple base learners, such as linear regression, support vector regression, and artificial neural networks, to improve the accuracy and diversity of the predictions.
- The concept drift detection component monitors the performance of the ensemble and triggers an update when a significant change in the data distribution is detected.
- The performance of the proposed approach is compared with several baseline methods, such as single learners, bagging, and boosting.
- The results show that the proposed approach achieves the lowest mean absolute percentage error (MAPE) and root mean square error (RMSE) among all the methods.
- The approach also adapts well to the concept drifts and maintains a stable performance over time.

## Case study 3: An update on global mining land use

- This case study presents an update on the global mining land use dataset, which maps the extent and location of active and inactive mining sites worldwide.
- The dataset is based on two sources: the Global Mining Database (GMD) and the Global Surface Mining Landsat (GSML).
- The GMD contains information on 1,073 major mining sites, such as name, location, commodity, status, and area.
- The GSML contains satellite images of 31,396 km2 of mining land use, which are classified into four categories: active mining, inactive mining, waste rock, and tailings.
- The dataset is updated using the latest available data from 2019 to 2020, which covers 1,016 mining sites and 29,988 km2 of mining land use.
- The dataset provides a comprehensive and consistent view