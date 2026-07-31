# Real Time System

A real time system is an information processing system that can respond to events within predictable and specific time constraints . The system must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization).

Some examples of real time systems are:

- Flight control systems: These systems control the flight parameters of an aircraft, such as altitude, speed, direction, etc. They must react to sensor inputs and user commands within milliseconds to ensure the safety and stability of the flight .
- Process control systems: These systems are used in industrial applications where production is continuous and requires precise monitoring and regulation of physical variables, such as temperature, pressure, flow, etc. They must adjust the output of the system according to the input and feedback signals within seconds or less .
- Machine vision: These systems are used to help machines rapidly interpret data so they can see their surroundings and perform tasks, such as object recognition, face detection, quality inspection, etc. They must process the images and videos captured by cameras and sensors within milliseconds or less .
- Robotics: These systems are used to control the movements and actions of robots, such as industrial robots, autonomous vehicles, surgical robots, etc. They must coordinate the sensors, actuators, and controllers of the robots within milliseconds or less to achieve the desired goals and avoid collisions and errors  .
- Medical imaging: These systems are used to capture, process, and display images of the human body for diagnosis and treatment, such as X-ray, MRI, ultrasound, etc. They must process the signals from the imaging devices and display the results within seconds or less to provide accurate and timely information to the medical staff.

Real time systems can be classified into two types based on the timing constraints:

- Hard real time systems: These systems have absolute deadlines, and if those allotted time spans are missed, a system failure will occur. For example, a flight control system must respond to a sudden change in the air pressure within a certain time limit, otherwise the aircraft may crash  .
- Soft real time systems: These systems have relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail. For example, a video streaming system must deliver the frames within a certain time limit, otherwise the video quality will decrease but not stop  .

Real time systems face many challenges and requirements, such as:

- Concurrency: Real time systems must handle multiple tasks and events simultaneously and coordinate them efficiently and correctly .
- Schedulability: Real time systems must ensure that all the tasks and events can meet their deadlines and priorities, and allocate the available resources accordingly .
- Reliability: Real time systems must ensure that the system can function correctly and consistently under normal and abnormal conditions, and recover from faults and errors .
- Safety: Real time systems must ensure that the system can avoid or minimize the harm to the environment and the users in case of failures or errors .
- Security: Real time systems must ensure that the system can protect the data and the functionality from unauthorized access and malicious attacks .

Real time systems are key pieces of technology, and as such, they are used in a variety of industries with applications spanning from process automation systems to warehousing to production assembly lines, agriculture, and healthcare .