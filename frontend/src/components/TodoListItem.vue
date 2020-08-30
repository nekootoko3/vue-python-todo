<template>
  <li>{{ title }}</li>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class TodoListItem extends Vue {
  @Prop() private title!: string;
}
</script>
