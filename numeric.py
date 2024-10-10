
var = []

with open('file.txt', 'r') as obj:
    conteudo = obj.readlines()
    for dado in conteudo[1:-1]: # limitei para desconsiderar a primeira e ultima linhas
        remover = dado[0:27]
        if remover in var:
            # Se tiver mais de uma linha da mesma transação passa a linha duplicada percorrendo até localizar nova transação, considerando que a transação foi processada
            pass
        else:
            var.append(remover)
            x = dado.replace(remover, '')[0:11]
            decimal = dado.replace(remover, '')[12:14]
            valor = x + '.' + decimal
            valor = int(x) * 1
            print(valor)
            # xx = 0
            # for y in x:
            #     if y == '0':
            #         xx += 1
            #     else:
            #         break
            # valor=valor[xx:]
            # print(valor)