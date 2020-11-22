from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm

def pmit(phrase,text,min_word_size=3):
    if not (isinstance(phrase, str) and isinstance(text, str) and isinstance(min_word_size, int)):
        print("One of the arguments is not valid")
        end = input("")
        return
    non_relevant_char = [",",".",":",";","?","/","'",'"',"!","<",">","@","#","$","%","^","&","*","(",")","_","=","+","~","`"]
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
    for character in non_relevant_char:
        text.replace(character, " ")
        phrase.replace(character, " ")
    while text.find("  ") != -1:
        text.replace("  ", " ")
    while phrase.find("  ") != -1:
        phrase.replace("  ", " ")
    phrase = phrase.split()
    if text.find("\n") != -1:
        paragraphs = [text]
    else:
        paragraphs = text.splitlines()
    highest_match_ratio = [0]
    for paragraph in paragraphs:
        paragraph = paragraph.split()
        matches = []
        for pword in phrase:
            close_matches = gcm(pword, paragraph)
            for index in range(0, len(paragraph) - 1):
                if (paragraph[index] in close_matches) and (not index in matches):
                    matches.append(index)
        for match in matches:
            if match - int(len(phrase)/2) < 0:
                begin = 0
            else:
                begin = match - int(len(phrase)/2)
            if match + int(len(phrase)/2) + len(phrase) > len(paragraph) - 1:
                end = len(paragraph) - 1
            else:
                end =  match + int(len(phrase)/2) + len(phrase)
            match_ratio = sm(None, " ".join(phrase), " ".join(paragraph[begin:end])).ratio()
            if match_ratio > highest_match_ratio[0]:
                highest_match_ratio[0] = match_ratio
    result = highest_match_ratio[0]**(1/len(phrase))
    return result
