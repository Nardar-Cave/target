from flask import Flask, jsonify, json
import statistics

app = Flask(__name__)

@app.route('/dados', methods=['GET'])
def dados():
    try:
        with open('faturamento-api/dados.json') as f:
            dados = json.load(f)

        # Separe os dias com e sem valor
        faturamentos_diarios = [(dia['dia'], dia['valor']) for dia in dados if 'valor' in dia]
        sem_faturamento = [dia for dia in dados if 'valor' not in dia]

        # Calcule a média dos dias com faturamento
        valores = [float(dado[1]) for dado in faturamentos_diarios]
        media_faturamento_diario = statistics.mean(valores)

        # Calcule o menor e maior valor de faturamento diário, ignorando dias vazios
        valores = [float(dado[1]) for dado in faturamentos_diarios if dado[1] is not None]
        menor_valor = min(valores)
        maior_valor = max(valores)

        # Calcule a quantidade de dias com faturamento superior à média, ignorando dias vazios
        qtd_dias_superior_a_media = sum(1 for dado in faturamentos_diarios if float(dado[1]) > media_faturamento_diario)

        resposta = {
            "menor_valor": menor_valor,
            "maior_valor": maior_valor,
            "qtd_dias_superior_a_media": qtd_dias_superior_a_media
        }

        return jsonify(resposta)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
