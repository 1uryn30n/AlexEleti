from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/estados')
def get_data():
    # URL da API externa que você quer consumir
    api_url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

    # Realiza a requisição GET para a API
    response = requests.get(api_url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Obtém os dados da API como JSON
        dados_api = response.json()
        # Renderiza o template HTML passando os dados da API
        return render_template('estados.html', estados=dados_api)
        #return jsonify(dados_api)
    else:
        # Caso contrário, retorna uma mensagem de erro
        return jsonify({'message': 'Erro ao acessar a API'}), 500
    
@app.route('/<estado_id>')
def get_info_estado(estado_id):
    # Aqui você teria a lógica para obter as informações do estado com base no estado_id
    # Por exemplo, fazer uma requisição à API com o ID do estado
    estado = {'id': estado_id, 'nome': 'iury', 'sigla': 'LUry'}
    return jsonify(estado)

if __name__ == '__main__':
    app.run(debug=True)
