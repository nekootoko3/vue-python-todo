<template>
  <div>
    <TodoTableRow
      v-for="todo in todos"
      :key="todo.id"
      v-bind:title="todo.title"
      v-bind:id="todo.id"
      v-bind:onClickRemoveButton="removeTodo(todo.id)"
      class="todo-row"
    />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import { Todo } from '../App.vue'
import TodoTableRow from "./TodoTableRow.vue"

@Component({
  components: {
    TodoTableRow,
  },
})
export default class TodoTable extends Vue {
  @Prop() private todos!: Array<Todo>;

  @Prop() private removeTodo!: Function;
}
</script>

<style scoped>
</style>
