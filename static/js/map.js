// Inicializa o mapa
var map = L.map('map').setView([-14.96438272586658, 36.98546722682962], 8);

// Camadas do mapa
var main = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
});
var terrainLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

// Adiciona a camada de terreno (mapa padrão)
main.addTo(map);

// Adiciona um controle para alternar entre as camadas
var baseMaps = {
    "Map v1.1": main,
    "Map v1.0": terrainLayer
};
L.control.layers(baseMaps).addTo(map);

// Variável para a linha férrea
var railwayLine = [];

// Obtém os dados da linha férrea de um arquivo JSON
$.getJSON('/static/js/railway.json', function(data) {
    railwayLine = data;
    var polyline = L.polyline(railwayLine.map(point => [point.lat, point.lon]), {color: 'blue'}).addTo(map);
});

// Função para criar ícone de trem com base no train_id e cor condicional
function createTrainIcon(train_id) {
    var lastDigit = parseInt(train_id.toString().slice(-1), 10);
    var iconColor = (lastDigit % 2 === 0) ? 'black' : 'green';
    var train_idColor = (lastDigit % 2 === 0) ? 'black' : 'green';
    
    return L.divIcon({
        html: `<div><span style="color: ${train_idColor}; font-size: 12px; font-weight: bold">${train_id}</span> <i class="fa-solid fa-train-subway" style="font-size: 20px; color: ${iconColor};"></i></div>`,
        className: 'train-icon',
        iconSize: [22, 22],
        iconAnchor: [12, 40]
    });
}

// Variável para armazenar marcadores de trens
var markers = {};

// Lista de torres com coordenadas específicas
var towers = [
    {lat: -14.91258, lon: 36.39096, name: 'Camela'},
    {lat: -15.97811, lon: 33.99734, name: 'CL1'},
    {lat: -14.96525, lon: 35.68938, name: 'CL10 Namanja'},
    {lat: -14.97670, lon: 35.86836, name: 'CL11 Nayuci'},
    {lat: -15.02217, lon: 36.07788, name: 'CL12 To-Bue'},
    {lat: -14.96648, lon: 36.24467, name: 'CL13 Coronga'},
    {lat: -14.85351, lon: 36.46654, name: 'CL14 Cuamba New'},
    {lat: -14.78694, lon: 36.69003, name: 'CL15 Murissa'},
    {lat: -14.80011, lon: 36.83015, name: 'CL16 Lurio'},
    {lat: -14.82236, lon: 36.99824, name: 'CL17 Mutuali'},
    {lat: -14.93167, lon: 37.16289, name: 'CL18 Nacata New'},
    {lat: -14.93428, lon: 37.43718, name: 'CL19 Malema New'},
    {lat: -15.81956, lon: 34.28012, name: 'CL2'},
    {lat: -14.93895, lon: 37.65310, name: 'CL20 Namacuna'},
    {lat: -15.01058, lon: 37.86273, name: 'CL21 Mussa'},
    {lat: -15.02593, lon: 38.04251, name: 'CL22 Iapala'},
    {lat: -15.08666, lon: 38.20425, name: 'CL23 Outeiro'},
    {lat: -15.03000, lon: 38.43851, name: 'CL24 CAIAIA'},
    {lat: -14.94438, lon: 38.68801, name: 'CL25 Namina'},
    {lat: -14.98333, lon: 38.83823, name: 'CL26 Caramaja'},
    {lat: -15.02005, lon: 39.14014, name: 'CL27 Rapale'},
    {lat: -15.11958, lon: 39.34800, name: 'CL28 Nampula New'},
    {lat: -15.08425, lon: 39.54103, name: 'CL29 Muizia'},
    {lat: -15.76925, lon: 34.49161, name: 'CL3'},
    {lat: -14.95840, lon: 39.81426, name: 'CL30 Meconta'},
    {lat: -14.89303, lon: 40.10438, name: 'CL31 Metochera New'},
    {lat: -14.91004, lon: 40.32030, name: 'CL32 Monapo'},
    {lat: -14.82100, lon: 40.46729, name: 'CL33 Namarral New'},
    {lat: -14.73686, lon: 40.60039, name: 'CL34'},
    {lat: -15.56105, lon: 34.66759, name: 'CL4'},
    {lat: -15.42186, lon: 34.80625, name: 'CL5'},
    {lat: -15.26133, lon: 34.92838, name: 'CL6'},
    {lat: -15.10936, lon: 35.07743, name: 'CL7 Nakaya New'},
    {lat: -15.05426, lon: 35.32118, name: 'CL8 Molipa'},
    {lat: -14.99914, lon: 35.51685, name: 'CL9 Lambulila'},
    {lat: -14.91123, lon: 40.01613, name: 'Crusher Siding'},
    {lat: -14.91840, lon: 40.21152, name: 'Evate'},
    {lat: -15.41053, lon: 34.82083, name: 'Facilities Zalewa'},
    {lat: -16.17556, lon: 33.79136, name: 'Moatize Vodacom'},
    {lat: -14.92175, lon: 39.99300, name: 'MRR 10 Namialo'},
    {lat: -14.94939, lon: 37.41767, name: 'MRR 5 Malema'},
    {lat: -15.06288, lon: 35.23377, name: 'MRR2 Liwonde'},
    {lat: -14.98916, lon: 35.89300, name: 'MRR3 Entre Lagos'},
    {lat: -14.80371, lon: 36.53350, name: 'MRR4 Quele'},
    {lat: -14.82610, lon: 38.19465, name: 'MRR7 Murrumbala'},
    {lat: -15.08112, lon: 35.07104, name: 'MRR8 Madimba'},
    {lat: -14.93406, lon: 37.16200, name: 'MRR9 Machanga'}
];

// Variável para armazenar marcadores de torres
var towerMarkers = [];

// Função para criar ícone de torre
function createTowerIcon(towerName) {
    return L.divIcon({
        html: `
            <div style="text-align: center;">
                <i class="fa-solid fa-map-pin" style="color: rgba(255, 0, 0, 0.3); font-size: 24px;"></i>
                <div style="padding: 4px; border-radius: 4px; font-size: 13px; color: rgba(0, 0, 0, 0.4); font-weight: bold;">${towerName}</div>
            </div>
        `,
        className: 'tower-icon',
        iconSize: [60, 60], // Ajuste o tamanho conforme necessário
        iconAnchor: [30, 30] // Ajuste para centralizar o ícone corretamente
    });
}

// Adiciona torres ao mapa e armazena os marcadores, mas mantém as torres ocultas inicialmente
towers.forEach(function(tower) {
    var marker = L.marker([tower.lat, tower.lon], {icon: createTowerIcon(tower.name)})
        .bindPopup("Site: " + tower.name);
    towerMarkers.push(marker);
    // As torres são criadas, mas não são adicionadas ao mapa
});

// Função para atualizar os marcadores dos trens
function updateMarkers() {
    $.getJSON('/data', function(data) {
        data.forEach(function(train) {
            var key = train.prefixo;

            // Verificar se o prefixo começa com 'k' (opcional)
            if (key[0].toLowerCase() === 'k') {
                if (markers[key]) {
                    // Atualiza a posição do marcador existente
                    markers[key].setLatLng([train.latitude, train.longitude], { animate: true, duration: 1.5 })
                        .setPopupContent("Block: " + train.bloco + "<br>Start Km: " + train.km_fim + "<br>End Km: " + train.km_ini, { className: 'custom-popup' })
                        .getPopup().options.className = 'custom-popup';
                } else {
                    // Cria um novo marcador
                    var marker = L.marker([train.latitude, train.longitude], {icon: createTrainIcon(train.prefixo)})
                        .bindPopup("Block: " + train.bloco + "<br>Start Km: " + train.km_fim + "<br>End Km: " + train.km_ini, { className: 'custom-popup' })
                        .addTo(map);
                    markers[key] = marker;
                }
            }
        });
    });
}


// Função para alternar a visibilidade das torres e atualizar o texto do botão
var towersVisible = false; // Inicia com as torres ocultas
document.getElementById("toggleTowers").addEventListener("click", function() {
    towersVisible = !towersVisible;
    
    if (towersVisible) {
        towerMarkers.forEach(function(marker) {
            map.addLayer(marker);  // Mostra as torres
        });
        document.getElementById("toggleTowers").innerText = "Hide Locations";  // Atualiza o texto do botão
    } else {
        towerMarkers.forEach(function(marker) {
            map.removeLayer(marker);  // Oculta as torres
        });
        document.getElementById("toggleTowers").innerText = "Show Locations";  // Atualiza o texto do botão
    }
});

// Variável para armazenar marcadores dos ativos
var hbhwMarkers = [];

// Função para criar ícone de ativo
function createAtivoIcon(ativoName, status) {
    const color = status === 'ok' ? 'green' : 'red'; // Verde para 'ok', vermelho para 'nok'

    return L.divIcon({
        html: `
            <div style="text-align: center;">
                <i class="fa-solid fa-heading" style="color: ${color}; font-size: 20px;"></i>
                <div style="padding: 4px; border-radius: 4px; font-size: 9px; color: rgba(0, 0, 0, 0.6);">HBHW<br>${ativoName}</div>
            </div>
        `,
        className: 'ativo-icon',
        iconSize: [25, 25], // Tamanho do ícone
        iconAnchor: [30, -4] // Posição do ícone
    });
}

// Função para buscar os dados da rota Flask
function fetchHBHWData() {
    $.getJSON('/hbhw', function(data) {
        // Remove marcadores antigos se necessário
        hbhwMarkers.forEach(function(marker) {
            map.removeLayer(marker); // Remove o marcador do mapa
        });
        hbhwMarkers = []; // Limpa a lista de marcadores

        // Adiciona os ativos ao mapa
        data.forEach(function(hbhw) {
            var marker = L.marker([hbhw.lat, hbhw.lon], {icon: createAtivoIcon(hbhw.name, hbhw.status)});
            hbhwMarkers.push(marker);
            marker.addTo(map);  // Adiciona o ativo ao mapa
        });
    }).fail(function(error) {
        console.error('Erro ao buscar dados:', error);
    });
}

// Chama a função para buscar os dados
fetchHBHWData();

// Atualiza marcadores a cada 5 segundos
updateMarkers();
setInterval(updateMarkers, 5000);