<!-- App.vue -->
<template>
  <div class="container mt-5">
    <AddTodo />
    <TodoList :todos="todos" :favorites="favorites" />
  </div>
</template>

<script>
import AddTodo from './components/AddTodo.vue';
import TodoList from './components/TodoList.vue';

export default {
  components: {
    AddTodo,
    TodoList,
  },
  computed: {
    todos() {
      return this.$store.state.todos;
    },
    favorites() {
      return this.$store.state.favorites;
    },
  },
};
</script>