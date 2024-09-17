//var map = L.map('map').setView([-15.976325035981864, 34.185983799178736], 20);
var map = L.map('map').setView([-14.96438272586658, 36.98546722682962], 8);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var railwayLine = [];

$.getJSON('/static/js/railway.json', function(data) {
    railwayLine = data;
    var polyline = L.polyline(railwayLine.map(point => [point.lat, point.lon]), {color: 'blue'}).addTo(map);
});

var markers = {};

// Função para criar ícone com train_id e cor condicional
function createTrainIcon(train_id) {
    var lastDigit = parseInt(train_id.toString().slice(-1), 10);
    var iconColor = (lastDigit % 2 === 0) ? 'black' : 'green';
    var train_idColor = (lastDigit % 2 === 0) ? 'black' : 'green';
    
    return L.divIcon({
        //html: `<div><span style="color: black; font-size: 12px;">${train_id}</span> <i class="fa-solid fa-map-pin" style="font-size: 18px; color: ${iconColor};"></i></div>`,
        html: `<div><span style="color: ${train_idColor}; font-size: 11px; font-weight: bold">${train_id}</span> <i class="fa-solid fa-train-subway" style="font-size: 18px; color: ${iconColor};"></i></div>`,
        className: 'train-icon',
        iconSize: [20, 20],
        iconAnchor: [12, 40]
    });
}

function updateMarkers() {
    $.getJSON('/data', function(data) {
        data.forEach(function(train) {
            var key = train.train_id;

            if (markers[key]) {
                // Atualiza a posição do marcador existente com uma transição suave
                markers[key].setLatLng([train.latitude, train.longitude], { animate: true, duration: 1.5 })
                    .setPopupContent("Train ID: " + train.train_id + "<br>Local: " + train.local + "<br>Coord ID: " + train.coord_id);
            } else {
                // Cria um novo marcador
                var marker = L.marker([train.latitude, train.longitude], {icon: createTrainIcon(train.train_id)})
                    .bindPopup("Train ID: " + train.train_id + "<br>Status: " + train.status + "<br>Coord ID: " + train.coord_id)
                    .addTo(map);
                markers[key] = marker;
            }
        });
    });
}

updateMarkers();
setInterval(updateMarkers, 5000);
