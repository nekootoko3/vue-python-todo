<template>
  <li>
    {{ id }}:{{ title }}
    <button @click="onClickRemoveButton">Remove</button>
  </li>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class TodoListItem extends Vue {
  @Prop() private id!: number;

  @Prop() private title!: string;

  @Prop() private onClickRemoveButton!: Function;
}
</script>
