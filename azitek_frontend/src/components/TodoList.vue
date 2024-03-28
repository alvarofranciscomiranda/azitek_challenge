<!-- TodoList.vue -->
<template>
  <div>
    <h2>TO-DO List</h2>
    <ul class="list-group">
      <li class="list-group-item" v-for="(todo, index) in notFavoriteTodos" :key="index">
        <div>
          <div v-if="!todo.editing" @dblclick="editTodoTitle(todo)" >{{ todo.title }}</div>
          <input v-else type="text" v-model="todo.title" @blur="doneEditTitle(todo)" @keyup.enter="doneEditTitle(todo)" @keyup.esc="cancelEditTitle(todo)" v-focus>
          -
          <div v-if="!todo.editing" @dblclick="editTodoDescription(todo)" >{{ todo.description }}</div>
          <input v-else type="text" v-model="todo.description" @blur="doneEditDescription(todo)" @keyup.enter="doneEditDescription(todo)" @keyup.esc="cancelEditDescription(todo)" v-focus>

          <button class="btn btn-danger btn-sm" @click="deleteTodo(index)">Delete</button>
          <button class="btn btn-warning btn-sm" @click="addToFavorites(todo)">Add to Favorites</button>
        </div>
      </li>
    </ul>

    <h2>Favorites</h2>
    <ul class="list-group">
      <li class="list-group-item" v-for="(todo, index) in favoriteTodos" :key="index">
        <div>
          <strong>{{ todo.title }}</strong> - {{ todo.description }}

          <button class="btn btn-danger btn-sm" @click="deleteTodo(index)">Delete</button>
          <button class="btn btn-warning btn-sm" @click="removeFromFavorites(todo)">Remove from Favorites</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  props: ['todos'],
  computed: {
    ...mapGetters(['favoriteTodos', 'notFavoriteTodos']),
  },
  methods: {
    ...mapActions(['persistState',  'removeFromFavorites']),

    deleteTodo(index) {
      this.$store.commit('deleteTodo', index);
      this.saveTodosToLocalStorage();
    },

    editTodoTitle(todo) {
      this.$store.commit('editTodoTitle', todo);
    },
    editTodoDescription(todo) {
      this.$store.commit('editTodoDescription', todo);
    },

    doneEditTitle(todo) {
      this.$store.commit('doneEditTitle', todo);
    },
    doneEditDescription(todo) {
      this.$store.commit('doneEditDescription', todo);
    },

    cancelEditTitle(todo) {
      this.$store.commit('cancelEditTitle', todo);
    },
    cancelEditDescription(todo) {
      this.$store.commit('cancelEditDescription', todo);
    },

    addToFavorites(todo) {
      this.$store.dispatch('addToFavorites', this.todos.indexOf(todo));
      this.saveTodosToLocalStorage();
    },

    saveTodosToLocalStorage() {
      this.$store.commit('persistState');
    },
  },
  directives: {
    focus: {
      mounted(el, binding) {
        if (binding.value) {
          el.focus();
        }
      },
      updated(el, binding) {
        if (binding.value) {
          el.focus();
        }
      },
    },
  },
};
</script>