### Call-back mechanism

- A call-back mechanism is a way of implementing event-driven programming in object-oriented languages.
- It allows an application to handle subscribed events, arising at runtime, through a listener interface .
- The listener interface defines one or more abstract methods that correspond to the events of interest.
- The subscribers (or clients) of the events will need to provide a concrete implementation of the interface methods, and register themselves with the event source (or server).
- The event source will keep a list of registered listeners, and invoke their methods when the events occur.
- The call-back mechanism decouples the event source from the event handlers, and allows for dynamic and flexible behavior .
- A call-back mechanism can be implemented using function pointers, closures, delegates, or objects, depending on the language features .

#### Example

- Suppose we want to design a system that allows users to download files from a server, and notifies them of the progress and completion of the download.
- We can use a call-back mechanism to implement this system, as follows:

```java
// Define a listener interface that declares the call-back methods
public interface DownloadListener {
  // This method is called when the download starts
  void onDownloadStarted(String fileName, long fileSize);
  // This method is called when the download progresses
  void onDownloadProgress(String fileName, long downloadedBytes, long remainingBytes);
  // This method is called when the download finishes
  void onDownloadFinished(String fileName, boolean success);
}

// Define a download manager class that acts as the event source
public class DownloadManager {
  // A list of registered listeners
  private List<DownloadListener> listeners;
  // A constructor that initializes the list
  public DownloadManager() {
    listeners = new ArrayList<>();
  }
  // A method that allows listeners to register themselves
  public void addDownloadListener(DownloadListener listener) {
    listeners.add(listener);
  }
  // A method that allows listeners to unregister themselves
  public void removeDownloadListener(DownloadListener listener) {
    listeners.remove(listener);
  }
  // A method that performs the download and notifies the listeners
  public void downloadFile(String url) {
    // Create a file object from the url
    File file = new File(url);
    // Get the file name and size
    String fileName = file.getName();
    long fileSize = file.length();
    // Notify the listeners that the download has started
    for (DownloadListener listener : listeners) {
      listener.onDownloadStarted(fileName, fileSize);
    }
    // Create a buffer for reading the file
    byte[] buffer = new byte[1024];
    // Create a variable for tracking the downloaded bytes
    long downloadedBytes = 0;
    // Create a variable for tracking the remaining bytes
    long remainingBytes = fileSize;
    // Create a variable for tracking the success of the download
    boolean success = true;
    try {
      // Create an input stream for reading the file
      InputStream in = new FileInputStream(file);
      // Create an output stream for writing the file to a local directory
      OutputStream out = new FileOutputStream("downloads/" + fileName);
      // Read the file in chunks and write them to the output stream
      int bytesRead;
      while ((bytesRead = in.read(buffer)) != -1) {
        out.write(buffer, 0, bytesRead);
        // Update the downloaded and remaining bytes
        downloadedBytes += bytesRead;
        remainingBytes -= bytesRead;
        // Notify the listeners that the download has progressed
        for (DownloadListener listener : listeners) {
          listener.onDownloadProgress(fileName, downloadedBytes, remainingBytes);
        }
      }
      // Close the streams
      in.close();
      out.close();
    } catch (IOException e) {
      // Handle the exception and set the success flag to false
      e.printStackTrace();
      success = false;
    }
    // Notify the listeners that the download has finished
    for (DownloadListener listener : listeners) {
      listener.onDownloadFinished(fileName, success);
    }
  }
}

// Define a user class that implements the listener interface and acts as the event handler
public class User implements DownloadListener {
  // A name field for the user
  private String name;
  // A constructor that sets the name
  public User(String name) {
    this.name = name;
  }
  // An override of the onDownloadStarted method
  @Override
  public void onDownloadStarted(String fileName, long fileSize) {
    // Print a message to the