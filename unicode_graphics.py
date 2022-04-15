## pirmas sprendimas

rezultatas = map(lambda skaicius: skaicius * 2, [2, 4, 6, 8, 10])
for skaicius in rezultatas:
    print(skaicius)

print('\U0001F441 \U0001F43D \U0001F441')
## antras sprendimas

def dauginam_is_dvieju(skaicius):
    return skaicius * 2

rezultatas_2 = map(dauginam_is_dvieju, [2, 4, 6, 8, 10])
for skaicius in rezultatas_2:
    print(skaicius)

