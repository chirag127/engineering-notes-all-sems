### Architectural Models

1. **Lambda Architecture:** This architecture is designed to handle massive quantities of data by taking advantage of both batch and stream processing methods. It divides the processing into three layers: batch, serving, and speed.
2. **Kappa Architecture:** This architecture is a simplification of the Lambda architecture, where the batch processing layer is removed and all data is treated as a stream. It is designed to handle real-time data processing and analysis.
3. **Zeta Architecture:** This architecture is a generalization of the Lambda and Kappa architectures, where the processing is divided into microservices that can be deployed and scaled independently. It is designed to handle both batch and stream processing, as well as other types of data processing.

These are some of the common architectural models used in the design of data platforms for stream processing and analytics. Each model has its own strengths and weaknesses, and the choice of architecture depends on the specific requirements of the system being designed.