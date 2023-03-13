Resource Allocation Models (RAIM) in software project management are methods or frameworks for estimating the time, effort, and resources required to complete a software project of a given size and complexity. One of the most widely used RAIM is the Putnam model, which uses the Norden/Rayleigh curve to describe the relationship between software size, effort, schedule, and defect rate. The following diagram illustrates the basic architecture of the Putnam model using ASCII characters:

```
    /\
   /  \    Effort
  /    \   (person-months)
 /      \  _________
/        \/         \  Schedule
|                   |  (months)
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|___________________|
0                   Software Size
                    (thousands of lines of code)
```

The diagram shows that the effort required to complete a software project increases exponentially with the software size, while the schedule increases logarithmically. The peak of the curve represents the optimal point of resource allocation, where the effort and schedule are balanced and the defect rate is minimized. The Putnam model uses a formula to calculate the effort and schedule based on the software size and a productivity factor that reflects the quality of the development team and the environment. The formula is:

Effort = A * Size^B

Schedule = C * Effort^(1/3) * Size^(1/9)

where A, B, and C are constants that depend on the productivity factor. The Putnam model can be used to estimate the resource allocation for a software project at an early stage, as well as to monitor and control the project progress and quality during the development process. However, the model also has some limitations, such as assuming a fixed software size and ignoring the effects of changing requirements, technology, and team dynamics. Therefore, the Putnam model should be used with caution and adjusted according to the specific characteristics and context of each software project.