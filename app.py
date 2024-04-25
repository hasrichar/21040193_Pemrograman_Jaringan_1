jawaban_total = []

while True:
    ekor_besar = input("Apakah Berang-Berang memiliki ekor besar? (yes=1, no=0): ")

    jawaban = []

    if ekor_besar == "1":
        jawaban.append("Memiliki ekor besar (1)")
        kacamata = input("Apakah Berang-Berang memakai kacamata? (yes=1, no=0): ")
        jawaban.append(
            "Memakai kacamata (1)" if kacamata == "1" else "Tidak memakai kacamata (0)"
        )

        if kacamata == "1":
            blue_trousers = input("Apakah Berang-Berang memakai blue trousers? (yes=1, no=0): ")
            jawaban.append(
                "Memakai blue trousers (1)"
                if blue_trousers == "1"
                else "Tidak memakai blue trousers (0)"
            )
            jawaban.append(
                "Memakai topi kuning (1)"
                if blue_trousers == "1"
                else "Memakai topi merah (0)"
            )
        else:
            baju_hijau = input("Apakah Berang-Berang memakai baju hijau? (yes=1, no=0): ")
            jawaban.append(
                "Memakai baju hijau (1)"
                if baju_hijau == "1"
                else "Tidak memakai baju hijau (0)\n"
                "- Memakai Topi Biru"
            )
            if baju_hijau == "1":
                brown_trouser = input("Apakah Berang-Berang memakai brown trousers? (yes=1, no=0): ")
                jawaban.append(
                    "Memakai brown trousers (1)\n"
                    "- Memakai topi biru"
                    if brown_trouser == "1"
                    else "Tidak memakai brown trousers (0)\n"
                    "Memakai Topi Kuning"
                )
            # jawaban.append(
            #     "Memakai topi biru (0)"
            # )
    else:
        jawaban.append("Tidak memiliki ekor besar (0)")
        gigi_besar = input("Apakah Berang-Berang memiliki gigi besar? (yes=1, no=0): ")
        jawaban.append(
            "Memiliki gigi besar (1)"
            if gigi_besar == "1"
            else "Memakai Topi Biru"
        )

        if gigi_besar == "1":
            blue_trouser = input("Apakah Berang-Berang memakai blue trouser? (yes=1, no=0): ")
            jawaban.append(
                "Memakai blue trouser (1)"
                if blue_trouser == "1"
                else "Tidak memakai blue trouser (0)"
            )
            jawaban.append(
                "Memakai topi merah (1)"
                if blue_trouser == "1"
                else "Memakai topi Merah (0)"
            )
        else:
            jawaban.append("Tidak memakai blue trouser (0)")
            jawaban.append("Memakai topi Kuning (1)")

    jawaban_total.append(
        jawaban
    )

    jawab = input("Apakah Berang-Berang ingin mengulang pertanyaan? (yes=1, no=0): ")
    if jawab == "0":
        break

print("Jawaban:")
for idx, jawaban_iterasi in enumerate(jawaban_total, 1):
    print(f"Jawaban Iterasi {idx}:")
    for item in jawaban_iterasi:
        print("- " + item)

semua_sesuai = all(
    jawaban[0] == "Memiliki ekor besar (1)"
    and jawaban[1] == "Memakai kacamata (1)"
    and jawaban[2] == "Memakai blue trousers (1)"
    and jawaban[3] == "Memakai topi kuning (1)"
    for jawaban in jawaban_total
)
if semua_sesuai:
    print("Berang berang pakai baju yang benar.")
else:
    print("Berang berang tidak pakai baju yang benar.")
