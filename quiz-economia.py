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


def question(inicio, fim):
    for j in range(inicio, fim):
        print("Veja se conseque responder...")
        print("Pergunta: " + str(data['economics']['quests'][j]['pergunta']))
        input("Aperte a tecla Enter para ver a resposta")
        print("Resposta: " + str(data['economics']['quests'][j]['resposta']))
        input("Aperte a tecla Enter para a próxima pergunta")
        subprocess.run([command])

subprocess.run([command])

choose = int(input("Escolha:\n1 - Responder primeiras 50 questões\n2 - Responder as ultimas 50 questões\n3 - Todas as questões\n"))

if choose == 1:
    question(0, 50)

elif choose == 2:
    question(51, 100)

elif choose == 3:
    question(0, 100)
        
print("Fim =D")