import json
import subprocess

class Question():
    def __init__(self, path, command):
        self.command = command
        with open(path) as dados:
            self.data = json.load(dados)

    def __verify_data(self):
        if self.data == '':
            print('Erro ao ler o arquivo')
            exit()

    def question(self, inicio, fim):
        self.__verify_data()

        for j in range(inicio, fim):
            print("Veja se conseque responder...")
            print("Pergunta: " + str(self.data['economics']['quests'][j]['pergunta']))
            input("Aperte a tecla Enter para ver a resposta")
            print("Resposta: " + str(self.data['economics']['quests'][j]['resposta']))
            input("Aperte a tecla Enter para a próxima pergunta")
            subprocess.run([self.command])
