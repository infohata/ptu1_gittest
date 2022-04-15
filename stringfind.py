def ieskom(ko, kur):
    return kur.find(ko)

ko = "Ge"
kur = "Geras Gyvenimas"
radau = ieskom(ko, kur)
if radau >= 0:
    print(f"radau cia: {radau}")
else:
    print("neradau")
