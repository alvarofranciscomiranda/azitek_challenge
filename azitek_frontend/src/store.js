// store.js
import { createStore } from 'vuex';
import { ref, computed, watchEffect } from 'vue'

const STORAGE_KEY = 'vue-todo';

const filters = {
  notFavorite: (todos) => todos.filter((todo) => !todo.favorite),
  favorite: (todos) => todos.filter((todo) => todo.favorite),
};
export default createStore({
  state: {
    todos: JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]').map(todo => ({
      ...todo,
      editing: false,
      beforeEditCache: ''
    })),
  },
  mutations: {
    addTodo(state, todo) {
      todo.beforeEditCache = '';
      todo.editing = "false"
      state.todos.push(todo);
    },
    deleteTodo(state, index) {
      state.todos.splice(index, 1);
    },

    editTodoTitle(state, todo) {
      this.beforeEditCache = todo.title
      todo.editing = true
    },
    editTodoDescription(state, todo) {
      this.beforeEditCache = todo.description
      todo.editing = true
    },

    doneEditTitle(state, todo) {
      if (todo.title.trim() == '') {
        todo.title = this.beforeEditCache
      }
      todo.editing = false
    },
    doneEditDescription(state, todo) {
      if (todo.description.trim() == '') {
        todo.description = this.beforeEditCache
      }
      todo.editing = false
    },

    cancelEditTitle(state, todo) {
      todo.title = this.beforeEditCache
      todo.editing = false
    },
    cancelEditDescription(state, todo) {
      todo.description = this.beforeEditCache
      todo.editing = false
    },

    toggleFavorite(state, index) {
      state.todos[index].favorite = !state.todos[index].favorite;
    },

    deleteFavorite(state, todo) {
      const index = state.todos.findIndex(t => t === todo);
      if (index !== -1) {
        state.todos.splice(index, 1);
        state.favorite = false; // Set favorite flag to false
        this.commit('persistState');
      }
    },

    importCatFacts(state, catFacts) {
      if (Array.isArray(catFacts)) {
        catFacts.forEach(fact => {
          state.todos.push({ title: 'Cat Fact', description: fact.text });
        });
      } else if (catFacts && catFacts.text) {
        // Handle case when a single cat fact is returned
        state.todos.push({ title: 'Cat Fact', description: catFacts.text });
      } else {
        console.error('Invalid catFacts format:', catFacts);
      }
    },

    persistState(state) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.todos));
    },
  },
  actions: {
    async importCatFacts({ commit }, numberOfFacts) {
      const response = await fetch(`https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=${numberOfFacts}`);
      const data = await response.json();
      commit('importCatFacts', data);
      commit('persistState'); // Call persistState mutation after importing cat facts
    },

    addToFavorites({ commit, state }, index) {
      commit('toggleFavorite', index);
      commit('persistState');
    },
    removeFromFavorites({ commit, state }, todo) {
      const index = state.todos.findIndex(t => t === todo);
      if (index !== -1) {
        commit('toggleFavorite', index);
        commit('persistState');
      }
    },
    deleteFavorite({ commit }, todo) {
      commit('deleteFavorite', todo);
    },
  },

  getters: {
    favoriteTodos: (state) => state.todos.filter(todo => todo.favorite),
    notFavoriteTodos: (state) => filters.notFavorite(state.todos),
  },
});