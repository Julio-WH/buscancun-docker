<template>
  <link
    rel="stylesheet"
    href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
  />
  <div id="map" style="height: 700px"></div>
</template>

<script>
import L from "leaflet";
export default {
  name: "MapComponent",
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      const map = L.map("map").setView(
        [21.162310281950226, -86.8530133090876],
        14
      );
      const tileLayer = L.tileLayer(
        "https://tile.thunderforest.com/atlas/{z}/{x}/{y}.png?apikey=51a31031f86a4699994325648e4af7f9",
        {
          maxZoom: 19,
          minZoom: 14,
        }
      );
      tileLayer.addTo(map);
    },
  },
};
</script>

<style scoped></style>
