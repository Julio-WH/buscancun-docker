<template>
  <link
    rel="stylesheet"
    href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
  />
  <div id="map" style="height: 700px"></div>
</template>

<script>
import L from "leaflet";
import { initializeApp } from "firebase/app";
import { getDatabase, ref as firbaseRef, onValue } from "firebase/database";
export default {
  name: "MapComponent",
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      let data = { lat: 21.151115, lng: -86.904942 };
      const firebaseConfig = JSON.parse(process.env.VUE_APP_FIRE_CONFIG);

      var myIcon = L.icon({
        iconUrl: require("@/assets/bus-stop.png"),
        iconSize: [40, 40],
        iconAnchor: [19, 35],
        popupAnchor: [0, -20],
      });
      const coordenadas = [data.lat, data.lng];
      const map = L.map("map").setView(coordenadas, 14);
      const tileLayer = L.tileLayer(
        "https://tile.thunderforest.com/atlas/{z}/{x}/{y}.png?apikey=" +
          process.env.VUE_APP_API_MAPS,
        {
          maxZoom: 19,
          minZoom: 14,
        }
      );
      let market1 = L.marker(coordenadas, { icon: myIcon })
        .addTo(map)
        .bindPopup("<p>Ruta:44</p><p>Placa:xl33aaaa</p>");
      tileLayer.addTo(map);

      var latlngs = [
        coordenadas,
        [21.151115, -86.904942],
        [21.151237, -86.904776],
        [21.151085, -86.904705],
        [21.150891, -86.904632],
        [21.150832, -86.90463],
        [21.150707, -86.90453],
        [21.150636, -86.90451],
        [21.150584, -86.904436],
      ];

      L.polyline(latlngs, { color: "red" }).addTo(map);
      // Initialize Firebase
      const firebaseApp = initializeApp(firebaseConfig);
      const database = getDatabase(firebaseApp);
      const dbRef = firbaseRef(database, `/autobuses`);
      onValue(dbRef, (snapshot) => {
        data = snapshot.val()[1];
        var latlng = L.latLng(data.lat, data.lng);
        market1.setLatLng(latlng);
      });
    },
  },
};
</script>

<style scoped>
.leaflet-div-icon {
  background-color: red;
}
</style>
