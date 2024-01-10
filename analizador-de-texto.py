lista_texto= (str(input("Ingrese un texto:  ")))
letras=[]
letras.append(str(input("Ingrese 1° letra al azar:  ")).lower())
letras.append(str(input("Ingrese 2° letra al azar:  ")).lower())
letras.append(str(input("Ingrese 3° letra al azar:  ")).lower())

lista_texto = lista_texto.lower()

print(f"La letra {letras[0]} esta en su texto {lista_texto.count(letras[0])} vez")
print(f"La letra {letras[1]} esta en su texto {lista_texto.count(letras[1])} vez")
print(f"La letra {letras[2]} esta en su texto {lista_texto.count(letras[2])} vez")
print(f"La longitud de su cadena de texto es {len(lista_texto)}")
print(f"La primer letra de su texto es la {lista_texto[0]} Y la ultima letra de su texto es la {lista_texto[-1]}")
print(f"Su texto escrito al inverso quedaria asi: {lista_texto[::-1]}")

palabra = "python"
if palabra in lista_texto:
    print("La palabra PYTHON esta en su texto")
else:
    print("La palabra PYTHON___ NO ____esta en su texto")

