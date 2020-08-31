<template>
  <tr>
    <td class="todo-title">{{ title }}</td>
    <td class="todo-remove-btn">
      <button @click="onClickRemoveButton"  class="todo-remove">
        Remove
      </button>
    </td>
  </tr>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class TodoTableRow extends Vue {
  @Prop() private id!: number;

  @Prop() private title!: string;

  @Prop() private onClickRemoveButton!: Function;
}
</script>

<style scoped>
.todo-remove-btn {
  padding: 5px;
}
</style>
