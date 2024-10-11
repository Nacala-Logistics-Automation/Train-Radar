import pandas as pd
import random
import json
from draw.railway import railway_line  # Importando a linha ferroviária
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import requests
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'seu_segredo_aqui'  # Chave secreta para gerenciamento de sessão

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

@app.route('/data')
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
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Nome de usuário ou senha incorretos.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
