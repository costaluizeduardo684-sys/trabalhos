texto = """The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."""

texto = texto.lower()

texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace(":", "")

palavras = texto.split()

quantidade = 0

for palavra in palavras:
    if len(palavra) > 4:
        for letra in palavra:
            if letra in "python":
                quantidade = quantidade + 1
                break

print("Quantidade:", quantidade)
