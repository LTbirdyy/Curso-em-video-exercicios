lis=[]
c=p= 0
for x in range(0,5):
    a = int(input('Digite um valor: '))
    for n in lis:
        if n<a:
            p +=1
    lis.insert(p, a)
    p = 0
    if x==0:
        print('Adicionado ao final da lista...')
    else:
            if len(lis) == lis.index(a)+1:
                 print(f'Adicionado ao final da lista...')
            else:
              print(f'Adicionado a posição {lis.index(a)} da lista...')
print('-='*30)
print(f'Os valores digitados em ordem foram {lis}')