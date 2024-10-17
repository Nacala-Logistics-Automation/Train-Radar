import pandas as pd
import random
import json
from draw.railway import railway_line  # Importando a linha ferroviária
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import requests
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'EIEIROW2003204J32O2SO3E2K3434530O0R'  # Chave secreta para gerenciamento de sessão

# Mapeamento de nomes e coordenadas para cada IP
ip_mapping = {
    "12.12.120.210": {"name": "Loop2<br>Loop3", "lat": -15.823275, "lon": 34.404031},
    "12.12.120.209": {"name": "Loop6<br>Zalewa", "lat": -15.333761, "lon": 34.870483},
    "12.12.120.208": {"name": "Molipa<br>Lambulila", "lat": -15.050083, "lon": 35.393167},
    "12.12.120.207": {"name": "Caronga<br>Tóbue", "lat": -15.003522, "lon": 36.138242},
    "12.12.120.206": {"name": "Murissa<br>Lúrio", "lat": -14.799725, "lon": 36.786500},
    "12.12.120.205": {"name": "Malema New<br>Nataleia", "lat": -14.927942, "lon": 37.496081},
    "12.12.120.204": {"name": "Outeiro<br>Iapala", "lat": -15.040847, "lon": 38.135464},
    "12.12.120.203": {"name": "Caramaja<br>Namina", "lat": -14.914528, "lon": 38.756850},
    "12.12.120.202": {"name": "Anchilo<br>Muizia", "lat": -15.097806, "lon": 39.452244},
    "12.12.120.201": {"name": "Evate<br>Metocheria", "lat": -14.899569, "lon": 40.177997},
}

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Defina a rota de login

# Usuários simulados (em um sistema real, isso viria de um banco de dados)
users = {
    'admin': {'password': '1234'}  # Usuário de exemplo
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username)
    return None

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

# Função para simular leitura do JSON com dados dos trens
def read_hbhw_data():
    try:
        # Substitua a URL pela URL correta da sua API externa
        response = requests.get('http://98.83.198.121:5000/hbhw')
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
@login_required  # Protegendo a rota
def index():
    return render_template('index.html')

@app.route('/hbhw', methods=['POST'])
@login_required  # Protegendo a rota
def hbhw():
    # Lendo os dados do corpo da requisição
    data = read_hbhw_data()

    # Criando uma lista para armazenar os resultados
    result = []

    # Verificando o status e adicionando as informações correspondentes
    for item in data:
        ip = item["ip"]
        if ip in ip_mapping:  # Verifica se o IP está no mapeamento
            mapping = ip_mapping[ip]
            result.append({
                "ip": ip,  # Mantém o IP original
                "status": item["status"],  # Mantém o status original
                "name": mapping["name"],  # Nome do mapeamento
                "lat": mapping["lat"],  # Latitude do mapeamento
                "lon": mapping["lon"]   # Longitude do mapeamento
            })

    return jsonify(result)

@app.route('/positions')
@login_required  # Protegendo a rota
def data():
    # Lendo os dados dos trens
    trains_data = read_trains_data()

    # Filtrando os trens que começam com 'k'
    filtered_trains = [train for train in trains_data if train.get('prefixo', '').lower().startswith('k')]

    # Correlacionando as posições dos trens com os IDs das coordenadas
    for train in filtered_trains:
        position = get_position_on_line(train['id_bloco'], railway_line)
        train['latitude'] = position['lat']
        train['longitude'] = position['lon']

    return jsonify(filtered_trains)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Name or Password Incorrect.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are disconnected.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
