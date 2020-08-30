<template>
  <div id="app">
    <h1>Todo App</h1>
    <form v-on:submit.prevent="addNewTodo">
      <label for="new-todo">Add a todo</label>
      <input
        v-model="newTodoText"
        id="new-todo"
        placeholder="E.g. Feed the cat"
      >
    </form>
    <ul>
      <TodoListItem
        v-for="todo in todos"
        :key="todo.id"
        v-bind:title="todo.title"
        v-bind:id="todo.id"
      />
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import TodoListItem from './components/TodoListItem.vue';

const items = [
  { id: 1, title: 'neko' },
  { id: 2, title: 'inu' },
];

@Component({
  components: {
    TodoListItem,
  },
})
export default class App extends Vue {
  todos: Array<{id: number; title: string}> = items;

  newTodoText = '';

  onClick() {
    this.newTodoText = 'さようなら';
  }

  addNewTodo() {
    this.todos.push({
      id: 1,
      title: this.newTodoText,
    });
    this.newTodoText = '';
  }
}
</script>
