n = str(input('Digite uma frase: '))
#mostra caracteres dentro de um determinado range
print(n[9:21])
print(n[1:7])
print(n[1:21:2])
print(n[1::3])
print(n[:5])
print(n[15:])
#mostra o comprimento da seq. string
print(len(n))
#conta quantas x aparece determinado caractere
print(n.count('o'))
print(n.count('o', 0, 13))
#mostra a posição onde se encontra determinado caractere
print(n.find('re'))
#mostra a seq. string em caracteres maiúsculos
print(n.upper())
#somente o primeiro caractere maiúsculo
print(n.capitalize())
#mostra a seq. string como um titulo
print(n.title())
#mostra a seq. string em caracteres minúsculos
print(n.lower())
#troca uma seq. string por outra
print(n.replace('rei', 'imperador'))
#remove espaços "inuteis"
print(n.strip())
print(n.rstrip())
print(n.lstrip())