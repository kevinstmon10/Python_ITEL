text = input("Ingrese una palabra: ")
text = list(text.replace(' ',''))
textReversed = list(text)
textReversed.reverse()

if text == textReversed:
    print("es palindromo")
else:
    print("no es palindromo")

########################
