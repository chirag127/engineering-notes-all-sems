# making A To-Do List Application using HTML, CSS, and JavaScript

Sure, here's an example of how you could write the code for a to-do list application using HTML, CSS, and JavaScript all in a single file:

```
<!DOCTYPE html>
<html>
  <head>
    <style>
      /* Add your CSS styles here */
      body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
      }
      
      h1 {
        text-align: center;
        margin-top: 50px;
      }
      
      .container {
        max-width: 600px;
        margin: 0 auto;
        background-color: #fff;
        padding: 20px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
      }
      
      .task-input {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        margin-bottom: 20px;
      }
      
      .task-list {
        list-style: none;
        padding: 0;
      }
      
      .task-item {
        display: flex;
        align-items: center;
        padding: 10px;
        border-bottom: 1px solid #ccc;
      }
      
      .task-item input[type="checkbox"] {
        margin-right: 10px;
      }
      
      .task-item p {
        flex-grow: 1;
        margin: 0;
      }
      
      .task-item button {
        background-color: #ff0000;
        color: #fff;
        padding: 5px 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>To-Do List</h1>
      <input type="text" class="task-input" placeholder="Add a task...">
      <ul class="task-list">
        <!-- Add your tasks here -->
      </ul>
    </div>
    
    <script>
      // Add your JavaScript code here
      const taskInput = document.querySelector('.task-input');
      const taskList = document.querySelector('.task-list');
      
      taskInput.addEventListener('keypress', function(e) {
        if (e.keyCode === 13) {
          const taskValue = taskInput.value;
          
          if (!taskValue) return;
          
          const taskItem = document.createElement('li');
          taskItem.classList.add('task-item');
          
          taskItem.innerHTML = `
            <input type="checkbox">
            <p>${taskValue}</p>
            <button>Delete</button>
          `;
          
          taskList.appendChild(taskItem);
          
          taskInput.value = '';
        }
      });
      
      taskList.addEventListener('click', function(e) {
        if (e.target.tagName === 'BUTTON') {
          const taskItem = e.target.parentElement;
          taskList.removeChild(taskItem);
        }
      });
    </script>
  </body>
</html>
```

This code creates a simple to-do list application that allows you to add tasks, mark them as complete, and delete them. The CSS styles the page to make it look professional and visually appealing, while the JavaScript provides the functionality for adding, marking, and deleting tasks.
