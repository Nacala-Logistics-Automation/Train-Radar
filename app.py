from flask import Flask, render_template, jsonify
import pandas as pd
import random
import json
from draw.railway import railway_line  # Importando a linha ferroviária

app = Flask(__name__)

# Função para simular leitura do JSON com dados dos trens
def read_trains_data():
    with open('source\\trains_data.json', 'r') as f:
        data = json.load(f)
    return data

def get_position_on_line(coord_id, line):
    """Obtém a posição na linha baseada no ID da coordenada."""
    for point in line:
        if point['id'] == coord_id:
            return point
#    return line[0]  # Se o ID não for encontrado, retorna o ponto inicial

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Lendo os dados dos trens
    trains_data = read_trains_data()

    # Correlacionando as posições dos trens com os IDs das coordenadas
    for train in trains_data:
        position = get_position_on_line(train['coord_id'], railway_line)
        train['latitude'] = position['lat']
        train['longitude'] = position['lon']

    return jsonify(trains_data)

if __name__ == '__main__':
    app.run(debug=True, port=80)
