<template>
  <table class="table table-bordered caption-top m-4">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Nombre</th>
        <th scope="col">Numero de Placa</th>
        <th scope="col">Capacidad de Pasajeros</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">1</th>
        <td>Mark</td>
        <td>Otto</td>
        <td>@mdo</td>
      </tr>
      <tr>
        <th scope="row">2</th>
        <td>Jacob</td>
        <td>Thornton</td>
        <td>@fat</td>
      </tr>
      <tr>
        <th scope="row">3</th>
        <td>Larry</td>
        <td>the Bird</td>
        <td>@twitter</td>
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
    },
  },
};
</script>

<style scoped></style>
