<template>
  <tr>
    <td class="todo-title">{{ title }}</td>
    <td class="todo-remove-btn">
      <button @click="showModal = true" class="todo-update-btn">
        Edit
      </button>
      <button @click="removeTodo" class="todo-remove-btn">
        Remove
      </button>
    </td>

    <EditTodoModal
      v-if="showModal"
      @close="showModal = false"
      v-bind:id="id"
      v-bind:currentTitle="title"
      v-bind:createUpdateTodo="createUpdateTodo"
    />
  </tr>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

import EditTodoModal from './EditTodoModal.vue'

@Component({
  components: {
    EditTodoModal,
  }
})
export default class TodoTableRow extends Vue {
  @Prop() private id!: number;

  @Prop() private title!: string;

  @Prop() private removeTodo!: Function;

  @Prop() private createUpdateTodo!: Function;

  showModal = false;
}
</script>

<style scoped>
.todo-update-btn {
  margin: 4px;
}
.todo-remove-btn {
  margin: 4px;
}
</style>
