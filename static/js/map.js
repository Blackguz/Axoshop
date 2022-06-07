/* Apartado de mapa */
var map = L.map('map').setView([22.7693347, -102.6472768], 17);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([22.7693347, -102.6472768]).addTo(map)
    .bindPopup('Oficinas de Axolud.')
    .openPopup();

/* Fin apartado de mapa */