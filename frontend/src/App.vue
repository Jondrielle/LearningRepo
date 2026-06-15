<script setup>
import {ref,onMounted} from 'vue'

const tasks = ref([])

const name = ref('')
const description = ref('')
const id = ref(0)

async function getTasks(){
  console.log("Getting Tasks from backend")
  try{
    const response = await fetch("http://127.0.0.1:8000/");

    if (!response.ok){
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();

    console.log(result);
  }
  catch(error){
    console.error(error.message);
  }  
}

async function addTask(){
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

onMounted(()=>{
  getTasks()
})
</script>

<template>
  <h1>TODO List!</h1>

  <input v-model="name" placeholder="Task name"/>
  <input v-model="description" placeholder="Task Description"/>

  <button @click="addTask">Add Task</button>
  
  <h3>-------Tasks-------</h3>
  <div v-for="task in tasks" :key="task.id">
    <h4>{{task.name}}</h4>
    <p>{{task.description}}</p>
    <button @click="deleteTask(task.id)">Delete Task</button>
  </div>
</template>

