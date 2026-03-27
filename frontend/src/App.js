import { useState, useEffect } from "react";

function App() {
  const [task, setTask] = useState("");
  const [tasks, setTasks] = useState([]);

  const API = "https://task-manager-backend-j6me.onrender.com";

  const fetchTasks = async () => {
    const res = await fetch(`${API}/tasks`);
    const data = await res.json();
    setTasks(data.tasks);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const addTask = async () => {
    await fetch(`${API}/tasks?task=${task}`, { method: "POST" });
    setTask("");
    fetchTasks();
  };

  const deleteTask = async (t) => {
    await fetch(`${API}/tasks?task=${t}`, { method: "DELETE" });
    fetchTasks();
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Task Manager</h1>

      <input
        value={task}
        onChange={(e) => setTask(e.target.value)}
        placeholder="Enter task"
      />

      <button onClick={addTask}>Add Task</button>

      <ul>
        {tasks.map((t, i) => (
          <li key={i}>
            {t}
            <button onClick={() => deleteTask(t)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;