def inverter_string(s):
    string_invertida = ''
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

texto = input("Informe a string: ")
print(f"String invertida: {inverter_string(texto)}")
