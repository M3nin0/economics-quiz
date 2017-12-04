import platform
import subprocess
from util.question import Question

def set_command():
    sys = platform.system()
    if sys == 'Linux' or sys == 'darwin':
        return 'clear'
    elif sys == 'Windows':
        return 'cls'

if __name__ == '__main__':
    command = set_command()
    question = Question('./data/economia.json', command)

    subprocess.run([command])
    choose = int(input("Escolha:\n1 - Responder as questões do primeiro bimestre\n2 - Responder as questões do segundo bimestre\n3 - Todas as questões\n"))

    if choose == 1:
        question.question(0, 100)
    elif choose == 2:
        # 101 até 177
        question.question(100, 177)
    elif choose == 3:
        question.question(0, 177)
    else:
        print("Nada foi escolhido")

    subprocess.run([command])
