<template>
  <div class="text-center">
    <h1>Bienvenido a Buscaribe</h1>
  </div>
  <div class="row" style="margin-right: 0px; margin-left: 0px">
    <div class="col-12">
      <TableBusComponent />
    </div>
    <div class="col-12">
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
