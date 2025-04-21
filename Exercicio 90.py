dados = {'nome': input('Fale o nome do aluno:'),
         'media': float(input('Fale a média desse aluno:'))
         }
if dados['media'] >= 7:
    dados['status'] = 'Aprovado'
else:
    dados['status'] = 'Reprovado'
print(f'O aluno {dados["nome"]} com média {dados["media"]} está: \033[32m{dados["status"]}.')
