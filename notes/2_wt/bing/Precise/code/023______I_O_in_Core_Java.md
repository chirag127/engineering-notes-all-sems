#### I/O in Core Java
```java
import java.io.*;

public class IOExample {
    public static void main(String[] args) {
        try {
            // Create a new file
            File file = new File("example.txt");
            file.createNewFile();

            // Write to the file
            FileWriter writer = new FileWriter(file);
            writer.write("Hello, World!");
            writer.close();

            // Read from the file
            FileReader reader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(reader);
            String line = bufferedReader.readLine();
            while (line != null) {
                System.out.println(line);
                line = bufferedReader.readLine();
            }
            bufferedReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```