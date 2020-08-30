<template>
  <li>{{ id }}:{{ title }}</li>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class TodoListItem extends Vue {
  @Prop() private id!: number;

  @Prop() private title!: string;
}
</script>
