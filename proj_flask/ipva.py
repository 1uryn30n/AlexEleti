from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def get_data():
    apiEstados = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    apiFipe = 'https://parallelum.com.br/fipe/api/v1/'
    response = requests.get(apiEstados)
    
    if response.status_code == 200:
        dados_api = response.json()
        # return jsonify(dados_api)
        # dados_api = jsonify(dados_api)
        estado = request.args.get('estado')
        tipoVeiculo = request.args.get('tipoVeiculo')
        if tipoVeiculo:
            apiFipe = apiFipe+tipoVeiculo+'/marcas'
            responseTwo = requests.get(apiFipe)
            if responseTwo.status_code == 200:
                dados_marca = responseTwo.json()
            else:
                return jsonify({'message': 'Erro ao acessar a API'}), 500
        return render_template('estados.html', estados = dados_api, estado = estado, dados_marca = dados_marca)
    else:
        return jsonify({'message': 'Erro ao acessar a API'}), 500

if __name__ == '__main__':
    app.run(debug=True)
