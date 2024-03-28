<!-- AddTodo.vue -->
<template>
  <div>
    <h2>Add New TO-DO</h2>
    <form @submit.prevent="addTodo">
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" class="form-control" id="title" v-model="title" required>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea class="form-control" id="description" rows="3" v-model="description" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Add TO-DO</button>
    </form>
    <h2>Import Cat Facts</h2>
    <form @submit.prevent="importCatFacts">
      <div class="form-group">
        <label for="numberOfFacts">Number of Facts</label>
        <input type="number" class="form-control" id="numberOfFacts" v-model.number="numberOfFacts" required>
      </div>
      <button type="submit" class="btn btn-primary">Import Cat Facts</button>
    </form>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  data() {
    return {
      title: '',
      description: '',
      numberOfFacts: 1,
    };
  },
  methods: {
    ...mapActions(['addTodo', 'importCatFacts', 'persistState']),
    addTodo() {
      if (!this.title || !this.description) return;
      this.$store.commit('addTodo', { title: this.title, description: this.description });
      this.title = '';
      this.description = '';
      this.saveTodosToLocalStorage()
    },
    async importCatFacts() {
      if (this.numberOfFacts < 1) return;
      await this.$store.dispatch('importCatFacts', this.numberOfFacts);
      this.saveTodosToLocalStorage()
    },
    saveTodosToLocalStorage() {
      this.$store.commit('persistState');
    },
  },
};
</script>