Augmented Reality: Create an AR (augmented reality) application that can display digital objects in the real world and interact with them. Technologies: Unity, ARKit, ARCore, Vuforia, C#.

Here is a basic code for an AR application using Unity and ARKit:

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.iOS;

public class ARKitController : MonoBehaviour
{
    private UnityARAnchorManager unityARAnchorManager;

    // Start is called before the first frame update
    void Start()
    {
        unityARAnchorManager = new UnityARAnchorManager();
        UnityARUtility.InitializePlanePrefab(transform);
    }

    // Update is called once per frame
    void Update()
    {
        unityARAnchorManager.Update();
    }

    public void AddAnchor(ARPlaneAnchor arPlaneAnchor)
    {
        unityARAnchorManager.AddAnchor(arPlaneAnchor);
    }

    public void RemoveAnchor(ARPlaneAnchor arPlaneAnchor)
    {
        unityARAnchorManager.RemoveAnchor(arPlaneAnchor);
    }
}
```

This code sets up an ARKitController script that manages the creation and removal of AR anchors in the scene. The `UnityARAnchorManager` class is used to keep track of the AR anchors, and the `UnityARUtility` class is used to initialize the plane prefab that will be used to display the digital objects.

You can add more functionality to this code by adding more scripts to interact with the digital objects and perform actions based on user input. For example, you could add a script that allows the user to select an object and move it around in the real world.
