import subprocess
import platform
import json

sys = platform.system()

if sys == 'Linux' or sys == 'darwin':
    command = 'clear'
elif sys == 'Windows':
    command = 'cls'

with open('economia.json') as dados:
    data = json.load(dados)

subprocess.run([command])

for i in data['economics']['quests']:

    print("Veja se conseque responder...")
    print("Pergunta: " + str(i['pergunta']))
    input("Aperte qualquer tecla para ver a resposta")
    print("Resposta: " + str(i['resposta']))
    input("Aperte qualquer tecla para a próxima pergunta")
    subprocess.run([command])

print("Fim =D")