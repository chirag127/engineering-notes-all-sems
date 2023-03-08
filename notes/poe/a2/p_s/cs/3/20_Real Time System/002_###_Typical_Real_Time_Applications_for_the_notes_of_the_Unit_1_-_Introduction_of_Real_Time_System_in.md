 Here is the content in markdown format:

### Typical Real Time Applications

Some typical real time applications are:

1. Process Control Systems: These systems are used to control physical processes such as temperature, pressure, flow etc. in industries. For example, systems that control steam pressure or chemical mixture in a manufacturing plant. Any delay or error in control can lead to system instability or damage to the process. Hence, real time response is critical in such systems.
2. Robotics Systems: Robots are automated machines that perform tasks with time critical response requirements. The motion and action of robots have to be precisely controlled and coordinated in real time based on sensory inputs. Any delays can lead to errors and inefficient functioning.
3. Multimedia Systems: Systems involving playback or streaming of audio and video data require real time response. Data has to be processed and transmitted in sync with its playback time to avoid gaps or lag.
4. Telecommunications: Routing and switching of calls and data in telecom networks have to be done in real time to ensure seamless connectivity. There are time constraints on establishing and terminating calls.
5. Aircraft and Vehicle Control Systems: The control systems in aircraft and vehicles have to respond to events in real time to ensure safety, stability and efficient functioning. For example, the controls governing engine throttle, braking, steering etc. have to react promptly to driver inputs or sensor data.

#### Java interfaces to HDFS

The main Java interfaces to interact with HDFS are:

1. FileSystem - This is the main interface that provides client access to HDFS. It allows operations like opening, closing, reading, writing, seeking, etc. on files.
2. FileContext - This interface provides an alternate way to interact with HDFS and deals with pathnames as URIs. It allows appending to files, creating directories, etc.
3. DistributedFileSystem - This interface extends the FileSystem interface and provides interactions specific to distributed file systems like HDFS. It allows getting file status, listing files, setting replication factors, etc.
4. FsShell - This is a command line shell interface to run commands on HDFS. It can be used to perform several file system operations via scripts.

There are specific implementations of these interfaces for the HDFS file system, namely Hadoop Distributed File System and Raw Local FileSystem. Developers can use these interfaces and implementations to create Java programs and applications that can read and write data on HDFS.