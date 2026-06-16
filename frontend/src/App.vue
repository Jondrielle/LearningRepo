<script setup>
import {ref,onMounted} from 'vue'

const tasks = ref([])

const name = ref('')
const description = ref('')
const id = ref(0)
const complete = ref('False')

async function getTasks(){
  console.log("Getting Tasks from backend")
  try{
    const response = await fetch("http://127.0.0.1:8000/");

    if (!response.ok){
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();

    console.log(result);

    tasks.value = result
  }
  catch(error){
    console.error(error.message);
  }  
}

async function addTask(){
  if (!name.value.trim()) return

  try{
    const response = await fetch("http://127.0.0.1:8000/tasks",{
      method:"POST",
      headers:{
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name:name.value,
        description:description.value
      })
    })

    if (!response.ok){
      throw new Error(`Status: ${response.status}`)
    }

    const newTask = await response.json()

    tasks.value.push(newTask)

    name.value = ""
    description.value = ""

  }catch(error){
    console.error(error.message)
  } 
}

async function deleteTask(id){
  try{
    const response = await fetch(`http://127.0.0.1:8000/tasks/${id}`,{
      method: "DELETE"
    })

    if(!response.ok){
      throw new Error(`Status:${response.status}`)
    }

    tasks.value = tasks.value.filter(
      task => task.id !== id
    )

    console.log("Task was deleted")
  }catch(error){
    console.error(error.message)
  }
}

async function updateTask(id, isComplete){
  try{
    const response = await fetch(`http://127.0.0.1:8000/tasks/${id}`,{
      method:"PATCH",
      headers:{
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        is_complete: isComplete
      })
    })
    complete.value = isComplete
    const updatedTask = await response.json()

    const index = tasks.value.findIndex(task => task.id === id)

    if (index !== -1){
      tasks.value[index] = updatedTask
    }

    console.log(updatedTask)
  }
  catch(error){
    console.error(error.message)
  }  
}

onMounted(()=>{
  getTasks()
})
</script>

<template>
  <h1>TODO List</h1>

  <input v-model="name" placeholder="Task name" class="input"/>
  <input v-model="description" placeholder="Task Description" class="input"/>

  <button @click="addTask">Add Task</button>
  
  <h3>-------Tasks-------</h3>
  <div class="taskCard">
    <div v-for="task in tasks" :key="task.id" class="task">
      <div class="contents">
        <h4>{{task.name}}</h4>
        <p>{{task.description}}</p>

        <div>Completed?</div>
        <button @click="updateTask(task.id,!task.is_complete)" class="button">Is complete: {{task.is_complete}}</button>
        <button @click="deleteTask(task.id)"class="button">Delete Task</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .input {
  margin-right: 8px;
  border: 1px solid gray;
  border-radius: 3px;
}

.button {
  margin-right: 6px;
}

.taskCard {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 30px;
  gap: 10px;
}

.task {
  width: 300px;
  border: 1px solid gray;
  border-radius: 8px;
}

.contents {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 10px;
}
</style>
