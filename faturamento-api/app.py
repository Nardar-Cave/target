from flask import Flask, jsonify

app = Flask(__name__)

with open('dados.json') as arquivo:
    dados = json.load(arquivo)

@app.route('/faturamento', methods=['GET'])
def calcular_faturamento():
    valores_faturamento_diario = [x['valor'] for x in dados['faturamento'] if x['valor'] is not None]

    menor_valor_faturamento = min(valores_faturamento_diario)

    maior_valor_faturamento = max(valores_faturamento_diario)

    media_mensal = sum(valores_faturamento_diario) / len(valores_faturamento_diario) if valores_faturamento_diario else 0

    num_dias_superior_media = sum(1 for x in dados['faturamento'] if x['valor'] is not None and x['valor'] > media_mensal)

    return jsonify({
        'menor_valor_faturamento': menor_valor_faturamento,
        'maior_valor_faturamento': maior_valor_faturamento,
        'num_dias_superior_media': num_dias_superior_media
    })

if __name__ == '__main__':
    app.run(debug=True)