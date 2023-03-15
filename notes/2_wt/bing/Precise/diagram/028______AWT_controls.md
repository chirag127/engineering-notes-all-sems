#### AWT controls
Here is an ASCII diagram of the AWT controls hierarchy:

```
                    Component
                        |
                -----------------
                |               |
            Container        Button
                |
        -----------------
        |               |
    Window           Panel
        |
    Frame
```

The `Component` class is the root of the AWT controls hierarchy. It is the superclass of all AWT components, including containers and controls. The `Container` class is a subclass of `Component` and is the superclass of all container components, such as `Window` and `Panel`. The `Button` class is also a subclass of `Component` and represents a push button control. The `Window` class is a subclass of `Container` and represents a top-level window. The `Frame` class is a subclass of `Window` and represents a window with a title bar and border. The `Panel` class is a subclass of `Container` and represents a container that can hold other components.
