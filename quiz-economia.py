import subprocess
import json

with open('economia.json') as dados:
    data = json.load(dados)

for i in data['economics']['quests']:
    
    print("Veja se conseque responder...")
    print("Pergunta: " + str(i['pergunta']))
    input("Aperte qualquer tecla para ver a resposta")
    print("Resposta: " + str(i['resposta']))
    input("Aperte qualquer tecla para a próxima pergunta")
    subprocess.run(['clear'])