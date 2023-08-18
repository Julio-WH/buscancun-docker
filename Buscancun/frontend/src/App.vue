<template>
  <div class="text-center">
    <h1>Bienvenido a Buscaribe</h1>
  </div>
  <div class="row">
    <div class="col-md-12 p-4">
      <TableBusComponent />
    </div>
    <div class="col-md-12">
      <MapComponent />
    </div>
  </div>
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
