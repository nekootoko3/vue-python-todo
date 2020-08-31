<template>
  <div id="app">
    <h1>Todo App</h1>
    <form v-on:submit.prevent="addNewTodo">
      <label for="new-todo">Add a todo</label>
      <input
        v-model="newTodoText"
        id="new-todo"
        placeholder="e.g. sanpo"
      >
    </form>
    <TodoTable
      v-bind:todos="todos"
      v-bind:removeTodo="removeTodo"
      id="todo-table"
    />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Axios, { AxiosResponse } from 'axios';

import TodoTable from './components/TodoTable.vue';
import Axios from 'axios';

const baseURL = process.env.VUE_APP_BASE_API_URL; //eslint-disable-line

export type Todo = {
  id: number;
  title: string;
}

@Component({
  components: {
    TodoTable,
  },
})
export default class App extends Vue {
  todos: Array<Todo> = [];

  newTodoText = '';

  addNewTodo(): () => void {
    if (this.newTodoText === '') {
      return;
    }

    const postData = { title: this.newTodoText };
    Axios.post(`${baseURL}/api/v1/todos`, postData)
      .then((res: AxiosResponse<Todo>) => {
        const todo = res.data;
        this.todos.unshift({
          id: todo.id,
          title: todo.title,
        });
        this.newTodoText = '';
      });
  }

  removeTodo(todoID: number): (toodID: number) => void {
    return () => {
      Axios.delete(`${baseURL}/api/v1/todos/${todoID}`)
        .then(() => {
          this.todos = this.todos.filter((todo: Todo) => {
            return todo.id !== todoID;
          });
        });
    }
  }

  created() {
    Axios.get(`${baseURL}/api/v1/todos`)
      .then((res: AxiosResponse<Array<Todo>>) => {
        this.todos = res.data.sort((a: Todo, b: Todo) => {
          if (a.id < b.id) {
            return 1;
          }

          return -1;
        });
      });
  }
}
</script>

<style>
#app {
  padding: 20px 30px;
}
#new-todo {
  margin-left: 5px;
}
#todo-table {
  margin-top: 10px;
}
</style>
