n = str(input('Digite uma frase: '))
#mostra caracteres dentro de um determinado range
print(n[1:7])
print(n[1:7:2])
print(n[1::2])
print(n[:5])
print(n[3:])
#mostra o comprimento da seq. string
print(len(n))
#mesma coisa, mas sem espaços
print(len(n) - n.count(' '))
#conta quantas x aparece determinado caractere
print(n.count('o'))
print(n.count('o', 0, 13))
#mostra a posição onde se encontra determinado caractere
print(n.find('a'))
#mesma coisa, mas começa do lado direito
print(n.rfind('a'))
#mostra a seq. string em caracteres maiúsculos
print(n.upper())
#somente o primeiro caractere maiúsculo
print(n.capitalize())
#mostra a seq. string como um titulo
print(n.title())
#mostra a seq. string em caracteres minúsculos
print(n.lower())
#troca uma str por outra
print(n.replace('a', 'b'))
#remove espaços "inuteis"
print(n.strip())
print(n.rstrip())
print(n.lstrip())
#separa a seq. em listas
print(n.split())