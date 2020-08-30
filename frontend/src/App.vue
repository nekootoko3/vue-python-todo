<template>
  <div id="app">
    <h1>Todo App</h1>
    <ul>
      <TodoListItem
        v-for="todoItem in todoItems"
        :key="todoItem.id"
        v-bind:title="todoItem.title"
      />
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import TodoListItem from './components/TodoListItem.vue';

@Component({
  components: {
    TodoListItem,
  },
})
export default class App extends Vue {
  todoItems: Array<{id: number; title: string}> = [
    { id: 1, title: 'neko' },
    { id: 2, title: 'inu' },
  ];
}
</script>
