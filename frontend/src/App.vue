<template>
  <div id="app">
    <h1>Todo App</h1>
    <form v-on:submit.prevent="addNewTodo">
      <label for="new-todo">Add a todo</label>
      <input
        v-model="newTodoText"
        id="new-todo"
        placeholder="sanpo"
      >
    </form>
    <ul>
      <TodoListItem
        v-for="todo in todos"
        :key="todo.id"
        v-bind:title="todo.title"
        v-bind:id="todo.id"
        v-bind:onClickRemoveButton="removeTodo(todo.id)"
      />
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Axios, { AxiosResponse } from 'axios';
import TodoListItem from './components/TodoListItem.vue';

const baseURL = process.env.VUE_APP_BASE_API_URL;

type Todo = {
  id: number;
  title: string;
}

@Component({
  components: {
    TodoListItem,
  },
})
export default class App extends Vue {
  todos: Array<Todo> = [];

  newTodoText = '';

  addNewTodo() {
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

  removeTodo(todoID: number) {
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
