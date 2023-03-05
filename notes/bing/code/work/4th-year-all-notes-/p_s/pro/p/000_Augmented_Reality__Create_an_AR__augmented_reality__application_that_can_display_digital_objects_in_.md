Augmented Reality: Create an AR (augmented reality) application that can display digital objects in the real world and interact with them. Technologies: Unity, ARKit, ARCore, Vuforia, C#.

Sure, I can help you with that. To create an AR app with Unity and Vuforia, you need to follow these steps:

- Download Unity 2017.3.0p2 or later and select “Vuforia Augmented Reality Support” when installing .
- Create a new Unity project and enable Vuforia support in PlayerSettings/XR .
- Replace the default Main Camera with an AR Camera from the Vuforia menu .
- Add a Vuforia license key to the AR Camera's Vuforia configuration. You can get a free or paid license key from the Vuforia developer portal.
- Add an Image Target to your scene from the Vuforia menu . This will be the marker that triggers your AR content.
- Assign an image to your Image Target from a database that you create and upload on the Vuforia developer portal .
- Add your digital objects as children of the Image Target in the scene hierarchy. They will appear when the Image Target is detected by the camera.
- Build and run your app on a compatible device (iOS, Android, Windows) with a camera.

Here is some sample code for adding a simple cube as a digital object:

```csharp
using UnityEngine;
using System.Collections;

public class CubeScript : MonoBehaviour {

    // Use this for initialization
    void Start () {
        // Create a cube object
        GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        // Set its position and scale
        cube.transform.position = new Vector3(0, 0.5f, 0);
        cube.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
        // Set its color to red
        cube.GetComponent<Renderer>().material.color = Color.red;
        // Make it a child of this script's parent (the Image Target)
        cube.transform.parent = transform;
    }
    
    // Update is called once per frame
    void Update () {
    
    }
}
```