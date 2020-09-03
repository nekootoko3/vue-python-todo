<template>
  <div>
    <TodoTableRow
      v-for="todo in todos"
      :key="todo.id"
      v-bind:title="todo.title"
      v-bind:id="todo.id"
      v-bind:removeTodo="createRemoveTodo(todo.id)"
      v-bind:createUpdateTodo="createUpdateTodo"
      class="todo-row"
    />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { Todo } from "../App.vue";
import TodoTableRow from "./TodoTableRow.vue";

@Component({
  components: {
    TodoTableRow
  }
})
export default class TodoTable extends Vue {
  @Prop() private todos!: Array<Todo>;

  @Prop() private createRemoveTodo!: Function;

  @Prop() private createUpdateTodo!: Function;
}
</script>

<style scoped></style>
