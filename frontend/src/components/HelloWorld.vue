<template>


      <div id="projectsList" v-if="projects.length > 0">
        <div v-for="project in projects" :key="project.ProjectTitle">
           <h3 id="projectItem">{{ project.ProjectTitle }}</h3>
          
        </div>
      </div>
  
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data() {
    return {
      selectedProject: null,
      projects: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8001/api/all_projects")
      .then((response) => {
        this.projects = response.data;
        console.log(this.projects);
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
