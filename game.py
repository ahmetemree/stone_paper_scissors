import random


def kullanici_secimi():
    choices = ["taş", "kağıt", "makas"]
    user_choice = input("Taş, Kağıt veya Makas seçin: ").lower()
    while user_choice not in choices:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
        user_choice = input("Taş, Kağıt veya Makas seçin: ").lower()
    return user_choice


def bilgisayar_secimi():
    choices = ["taş", "kağıt", "makas"]
    return random.choice(choices)

def bilgisayar_oynamak_istiyor_mu():
    choices=[True,False]
    return random.choice(choices)

def kullanici_oynamak_istiyor_mu():
    user_choice = input("Tekrar oynamak ister misiniz? Evet veya Hayır yazın.").lower()
    if user_choice == "evet":
        return True
    else:
        return False



def kazanan_oyuncu(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == "taş" and computer_choice == "makas") or \
            (user_choice == "kağıt" and computer_choice == "taş") or \
            (user_choice == "makas" and computer_choice == "kağıt"):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"


def donen_sonuc():
    kullanici_secti = kullanici_secimi()
    bilgisayar_secti = bilgisayar_secimi()

    print(f"Sizin seçiminiz: {kullanici_secti}")
    print(f"Bilgisayarın seçimi: {bilgisayar_secti}")

    result = kazanan_oyuncu(kullanici_secti, bilgisayar_secti)
    print(result)
    return result


def tas_kagit_makas_AHMETEMRE_CAKMAK():
    kullanici_istegi = True
    bilgisayar_istegi = True
    while kullanici_istegi and bilgisayar_istegi:
        print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
        user_score = 0
        computer_score = 0
        rounds = int(input("Kaç tur oynamak istersiniz? "))

        for _ in range(rounds):
            sonuc = donen_sonuc()
            if sonuc == "Kazandınız!":
                user_score += 1
            elif sonuc == "Kaybettiniz!":
                computer_score += 1

            print(f"Skor: Siz {user_score} - {computer_score} Bilgisayar\n")

        if user_score > computer_score:
            print("Tebrikler! Oyunu kazandınız!")
        elif user_score < computer_score:
            print("Üzgünüm, oyunu kaybettiniz.")
        else:
            print("Oyun berabere bitti.")

        kullanici_istegi = kullanici_oynamak_istiyor_mu()
        if kullanici_istegi==False:
            print("İyi günler :)")
        bilgisayar_istegi = bilgisayar_oynamak_istiyor_mu()
        if bilgisayar_istegi==False :
            print("Bilgisayar oynamak istemiyor")
            exit(1)


if __name__ == "__main__":
    tas_kagit_makas_AHMETEMRE_CAKMAK()
