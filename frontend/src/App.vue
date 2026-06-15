<script setup>

async function getTasks(){
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

</script>

<template>
  <h1>TODO List!</h1>
  <button @click="getTasks"> Tasks</button>
</template>

