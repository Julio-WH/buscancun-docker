<template>
  <table class="table table-bordered caption-top">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Nombre</th>
        <th scope="col">Numero de Placa</th>
        <th scope="col">Estado</th>
        <th scope="col">Asientos Disponibles</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(autobus, index) in autobuses" :key="index">
        <th scope="row">{{ autobus.id }}</th>
        <td>{{ autobus.nombre }}</td>
        <td>{{ autobus.numero_placa }}</td>
        <td>
          <span :class="claseEstado(autobus.estado)">{{ autobus.estado }}</span>
        </td>
        <td>{{ autobus.asientos_disponibles }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: "TableBusComponent",
  data() {
    return {
      ws: null,
      autobuses: [],
    };
  },
  mounted() {
    this.initWebSocket();
  },
  methods: {
    initWebSocket() {
      this.ws = new WebSocket("ws://" + window.location.host + "/ws/");
      this.ws.onopen = () => {
        this.ws.send(
          JSON.stringify({
            action: "list",
            request_id: new Date().getTime(),
          })
        );
        console.log("Conexión WebSocket establecida.");
      };
      this.ws.onmessage = (event) => {
        const allData = JSON.parse(event.data);
        if (allData.action === "list") {
          this.autobuses = allData.data;
        } else if (allData.action === "update") {
          const targetId = allData.data.id;
          const targetObject = this.autobuses.findIndex(
            (obj) => obj.id === targetId
          );
          if (targetObject !== -1) {
            this.autobuses[targetObject] = allData.data;
          }
        } else if (allData.action === "create") {
          const new_autobus = allData.data;
          this.autobuses.push(new_autobus);
        }
      };
    },
    claseEstado(estado) {
      let badge = "badge ";
      if (estado == "ABORDANDO") {
        badge += "badge-info";
      } else if (estado == "EN ESPERA") {
        badge += "badge-success";
      } else if (estado == "SALIENDO") {
        badge += "badge-warning";
      } else if (estado == "EN VIAJE") {
        badge += "badge-danger";
      } else {
        //LLEGANDO
        badge += "badge badge-primary";
      }
      return badge;
    },
  },
};
</script>

<style scoped></style>
