import json

# Exemplo de dados fictícios no formato JSON
faturamento_json = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722}
]
'''

# Carregar os dados do faturamento
faturamento = json.loads(faturamento_json)

# Filtrar apenas os dias com faturamento > 0
faturamento_valido = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

# Cálculos
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

# Dias acima da média
dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_faturamento])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
