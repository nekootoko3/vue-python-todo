<template>
  <div id="app">
    <h1>Todo App</h1>
    <form v-on:submit.prevent="addNewTodo">
      <label for="new-todo">Add a todo</label>
      <input v-model="newTodoText" id="new-todo" placeholder="e.g. sanpo" />
    </form>
    <TodoTable
      v-bind:todos="todos"
      v-bind:createRemoveTodo="createRemoveTodo"
      v-bind:createUpdateTodo="createUpdateTodo"
      id="todo-table"
    />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios, { AxiosResponse, AxiosError } from "axios";

import TodoTable from "./components/TodoTable.vue";

const baseURL = process.env.VUE_APP_BASE_API_URL;

export type Todo = {
  id: number;
  title: string;
};

@Component({
  components: {
    TodoTable
  }
})
export default class App extends Vue {
  todos: Array<Todo> = [];

  newTodoText = "";

  addNewTodo(): () => void {
    if (this.newTodoText) {
      return;
    }

    const postData = { title: this.newTodoText };
    axios
      .post(`${baseURL}/api/v1/todos`, postData)
      .then((res: AxiosResponse<Todo>) => {
        const todo = res.data;
        this.todos.unshift({
          id: todo.id,
          title: todo.title
        });
        this.newTodoText = "";
      })
      .catch(() => {
        alert("Somthing wrong. Please try later");
        // TODO: Notify error
      });
  }

  createUpdateTodo(todoID: number, title: string): () => void {
    return () => {
      const data = { title: title };
      axios
        .put(`${baseURL}/api/v1/todos/${todoID}`, data)
        .then(() => {
          this.todos = this.todos.map((todo: Todo) => {
            if (todo.id === todoID) {
              todo.title = title;
            }
            return todo;
          });
        })
        .catch((err: AxiosError) => {
          const res = err.response;

          if (!!res && res.status === 404) {
            alert("already deleted");
            this.todos = this.todos.filter((todo: Todo) => {
              return todo.id !== todoID;
            });
          } else {
            alert("Somthing wrong. Please try later");
            // TODO: Notify error
          }
        });
    };
  }

  createRemoveTodo(todoID: number): (toodID: number) => void {
    return () => {
      axios
        .delete(`${baseURL}/api/v1/todos/${todoID}`)
        .then(() => {
          this.todos = this.todos.filter((todo: Todo) => {
            return todo.id !== todoID;
          });
        })
        .catch((err: AxiosError) => {
          const res = err.response;

          if (!res && res.status === 404) {
            alert("already deleted");
            this.todos = this.todos.filter((todo: Todo) => {
              return todo.id !== todoID;
            });
          } else {
            alert("Somthing wrong. Please try later");
            // TODO: Notify somewhere
          }
        });
    };
  }

  created() {
    axios
      .get(`${baseURL}/api/v1/todos`)
      .then((res: AxiosResponse<Array<Todo>>) => {
        this.todos = res.data.sort((a: Todo, b: Todo) => {
          if (a.id < b.id) {
            return 1;
          }

          return -1;
        });
      })
      .catch(() => {
        alert("Somthing wrong. Please try later");
        // TODO: Notify somewhere
      });
  }
}
</script>

<style>
#app {
  position: relative;
  padding: 20px 30px;
  width: 100%;
  height: 100%;
}
#new-todo {
  margin-left: 5px;
}
#todo-table {
  margin-top: 10px;
}
</style>
