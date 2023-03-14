### Using Libraries in Arduino

Libraries are a collection of code that makes it easy for you to connect to a sensor, display, module, etc. For example, the LiquidCrystal library makes it easy to talk to character LCD displays. There are thousands of libraries available for download directly through the Arduino IDE, and you can find all of them listed at the Arduino Library Reference.

To use a library in a sketch, select it from Sketch > Import Library. A number of libraries come installed with the IDE, but you can also download or create your own. Here are some instructions for setting up a library on the offline IDE:

- Open the IDE and click "Sketch" on the menu tab and then Include Library > Manage Libraries.
- Search for the library that you need, click on it, then select the version of the library you want to install.
- Finally, click on install and wait for the IDE to install the new library. Once it has finished, an Installed tag should appear next to the library name. You can close the library manager.
- Now the new library will be available in the Sketch > Include Library menu.

If you want to add your own library to Library Manager, follow these instructions.

The process of setting up libraries on the online IDE (Arduino Web Editor) is quite similar to the offline one:

- Login to the Arduino Web Editor.
- Open the "Libraries" tab from the left menu, and search for libraries. The list displays read-only libraries, authored and maintained by the Arduino team and its partners.
- When you find the library, you can add it to your sketch by selecting the "Include" button. You can also see the related examples, and select a specific version, if available.
- If you can't find a specific library on the list, you can search every existing library through the library manager. From there you also have the option to add them to your favorites list by clicking on the star next to the library you want. Once you star a library, you can view it under the "favorites" tab and use its examples (if available).

Libraries provide extra functionality for use in sketches, e.g. working with hardware or manipulating data. The Arduino environment can be extended through the use of libraries, just like most programming platforms   .