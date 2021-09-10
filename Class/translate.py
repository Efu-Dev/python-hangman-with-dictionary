def translate(word, data):
    if word in data:
        definitions = data[word]
    elif word.title() in data:
        definitions = data[word.title()]
    elif word.upper() in data:
        definitions = data[word.upper()]
    j = 1
    for definition in definitions:
        print(str(j) + ". " + definition)
        j += 1
    print("\n")