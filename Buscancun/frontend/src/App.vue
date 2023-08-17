<template>
  <div class="text-center">
    <h1>Bienvenido a Buscaribe</h1>
  </div>
  <TableBusComponent />
  <MapComponent />
</template>

<script>
import MapComponent from "./components/MapComponent.vue";
import TableBusComponent from "./components/TableBusComponent.vue";

export default {
  name: "App",
  components: {
    MapComponent,
    TableBusComponent,
  },
};
</script>
