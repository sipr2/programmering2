vokaler = ["A", "E", "I", "O", "U", "Y", "Å", "Ä", "Ö"]

ordet = input().upper()

antal_vokaler = 0



for bokstäver in ordet:
    if bokstäver in vokaler:
        antal_vokaler += 1
print(ordet, "har", antal_vokaler)

