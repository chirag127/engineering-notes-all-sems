#### Multithread programming in Core Java
Multithreading in Java is a process of executing multiple threads simultaneously. A thread is a lightweight sub-process, the smallest unit of processing. Here is an example of how to create a thread in Java:

```java
class MultithreadingDemo extends Thread {
    public void run() {
        try {
            System.out.println("Thread " + Thread.currentThread().getId() + " is running");
        } catch (Exception e) {
            System.out.println("Exception is caught");
        }
    }
}

public class Multithread {
    public static void main(String[] args) {
        int n = 8;
        for (int i = 0; i < n; i++) {
            MultithreadingDemo object = new MultithreadingDemo();
            object.start();
        }
    }
}
```
This code creates a class `MultithreadingDemo` that extends the `Thread` class and overrides its `run` method. The `run` method is where the code for the new thread is defined. In the `main` method, we create 8 instances of the `MultithreadingDemo` class and call their `start` method to start the new threads. When the `start` method is called, the `run` method of the corresponding `MultithreadingDemo` object is executed in a new thread.