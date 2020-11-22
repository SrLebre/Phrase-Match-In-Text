from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm

def psa(phrase,text,min_word_size=3):
    if not (isinstance(phrase, str) and isinstance(text, str) and isinstance(min_word_size, int)):
        print("Um dos argumentos é inválido, digite enter para encerrar:")
        end = input("")
        return
    non_relevant_char = [",",".",":",";","?","/","'",'"',"!","<",">","@","#","$","%","^","&","*","(",")","_","=","+","~","`"]
    #removendo palavras com menos de x letras
    phrase = phrase.split()
    text = text.split()
    for word in phrase:
        if len(word) <= min_word_size - 1:
            phrase.remove(word)
    for word in text:
        if len(word) <= min_word_size - 1:
            text.remove(word)
    phrase = " ".join(phrase)
    text = " ".join(text)
    #removendo caracteres especiais das strings
    for character in non_relevant_char:
        text.replace(character, " ")
        phrase.replace(character, " ")
    #remover espaços duplos
    while text.find("  ") != -1:
        text.replace("  ", " ")
    while phrase.find("  ") != -1:
        phrase.replace("  ", " ")
    #separados de novo
    print(phrase)
    print(text)
    phrase = phrase.split()
    if text.find("\n") != -1:
        paragraphs = [text]
    else:
        paragraphs = text.splitlines()
    highest_match_ratio = [0]
    for paragraph in paragraphs:
        print("ao menos entrou?")
        paragraph = paragraph.split()
        print(paragraph)
        #pegar as palavras similares no texto
        matches = []
        for pword in phrase:
            print("Inicio do loop de frases")
            close_matches = gcm(pword, paragraph)
            print(close_matches)
            for index in range(0, len(paragraph) - 1):
                if (paragraph[index] in close_matches) and (not index in matches):
                    matches.append(index)
        print(matches)
        for match in matches:
            print("Início do Loop de Matches")
            if match - int(len(phrase)/2) < 0:
                begin = 0
                print("begin = 0")
            else:
                begin = match - int(len(phrase)/2)
                print("begin != 0")
            if match + int(len(phrase)/2) + len(phrase) > len(paragraph) - 1:
                end = len(paragraph) - 1
                print("end é no final")
            else:
                end =  match + int(len(phrase)/2) + len(phrase)
                print("end não é no final")
            match_ratio = sm(None, " ".join(phrase), " ".join(paragraph[begin:end])).ratio()
            print(match_ratio)
            print(" ".join(phrase) + "braia")
            print(" ".join(paragraph[begin:end]))
            if match_ratio > highest_match_ratio[0]:
                print("Aumentou")
                highest_match_ratio[0] = match_ratio
            else:
                print("Não aumentou")
    result = highest_match_ratio[0]**(1/len(phrase))
    return result
