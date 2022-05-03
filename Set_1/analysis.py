def analyse(fileName, letter):

    file = open(fileName, 'r')
    text = file.read()
    print(text)

    return text.count(letter)


wished_letter = input('Welchen Buchstaben wollen sie suchen? ')

print('So oft wurde der Buchstabe', wished_letter, 'im Text gefunden: ', analyse('analysis.txt', wished_letter))
