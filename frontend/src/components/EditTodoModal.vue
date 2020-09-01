<template>
  <transition name="modal" appear>
    <div class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-window">
        <form
          v-on:submit.prevent="onSubmit"
        >
          <label for="edit-todo">Edit todo</label>
            <input
              v-model="todoTitle"
              id="edit-todo"
            >
        </form>
      </div>
    </div>
  </transition>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component({})
export default class EditTodoModal extends Vue {
  @Prop() private id!: number;

  @Prop() private currentTitle!: string;

  @Prop() private createUpdateTodo!: Function;

  todoTitle = this.currentTitle;

  onSubmit(): () => void {
    this.$emit('close');
    this.createUpdateTodo(this.id, this.todoTitle)();
    return;
  }
}
</script>

<style scoped>
.modal-overlay {
  position: absolute;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}
.modal-window {
  position: absolute;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  top: 100px;
  left: 150px;
  width: 300px;
  height: 100px;
  background-color: white;
  border: 1px solid black;
}
#edit-todo {
  margin-left: 5px;
}
</style>
