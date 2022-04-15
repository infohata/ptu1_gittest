def ar_keliamieji(metai):
    if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
        return("Keliamieji")
    else:
        return("Nekeliamieji")


def ar_keliamieji_true(metai):
    if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
        return True
    else:
        return False
