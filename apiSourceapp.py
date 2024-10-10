from flask import Flask, request, jsonify

app = Flask(__name__)

# Variável para armazenar os dados enviados
positions_data = {}

@app.route('/update_positions', methods=['POST'])
def update_positions():
    """
    Endpoint para receber dados enviados do script local.
    """
    try:
        # Receber dados JSON enviados pelo script local
	data = request.get_json()
        print(f'Dados recebidos: {data}')
	if data:
	    positions_data = {}
            positions_data.update(data)  # Atualizar dados armazenados
            return jsonify({"message": "Dados recebidos e atualizados com sucesso"}), 200
        return jsonify({"message": "Nenhum dado recebido"}), 400
    except Exception as e:
        return jsonify({"message": f"Erro: {e}"}), 500

@app.route('/', methods=['GET'])
def get_locomotives():
    """
    Endpoint para visualizar os dados armazenados.
    """
    return jsonify(positions_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

