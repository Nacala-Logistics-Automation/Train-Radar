import pandas as pd
import random
import json
from draw.railway import railway_line  # Importando a linha ferroviária
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Função para simular leitura do JSON com dados dos trens
def read_trains_data():
    try:
        # Substitua a URL pela URL correta da sua API externa
        response = requests.get('http://98.83.198.121:5000')
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            data = response.json()  # Converte a resposta para formato JSON
            return data
        else:
            print(f"Erro ao acessar a API: {response.status_code}")
            return []
    except Exception as e:
        print(f"Erro ao fazer a requisição: {e}")
        return []

def get_position_on_line(coord_id, line):
    """Obtém a posição na linha baseada no ID da coordenada."""
    for point in line:
        if point['id'] == coord_id:
            return point
    return line[0]  # Se o ID não for encontrado, retorna o ponto inicial

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Lendo os dados dos trens
    trains_data = read_trains_data()

    # Correlacionando as posições dos trens com os IDs das coordenadas
    for train in trains_data:
        print(train['id_bloco'])
        position = get_position_on_line(train['id_bloco'], railway_line)
        train['latitude'] = position['lat']
        train['longitude'] = position['lon']

    return jsonify(trains_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
