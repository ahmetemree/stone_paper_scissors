import random


def get_user_choice():
    choices = ["taş", "kağıt", "makas"]
    user_choice = input("Taş, Kağıt veya Makas seçin: ").lower()
    while user_choice not in choices:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
        user_choice = input("Taş, Kağıt veya Makas seçin: ").lower()
    return user_choice


def get_computer_choice():
    choices = ["taş", "kağıt", "makas"]
    return random.choice(choices)

def computer_wantsto_play():
    choices=[True,False]
    return random.choice(choices)

def user_wantsto_play():
    user_choice = input("Tekrar oynamak ister misiniz? Evet veya Hayır yazın.").lower()
    if user_choice == "evet":
        return True
    else:
        return False



def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == "taş" and computer_choice == "makas") or \
            (user_choice == "kağıt" and computer_choice == "taş") or \
            (user_choice == "makas" and computer_choice == "kağıt"):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"


def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Sizin seçiminiz: {user_choice}")
    print(f"Bilgisayarın seçimi: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result


def play_game():
    userchoice = True
    compchoice = True
    while userchoice and compchoice:
        print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
        user_score = 0
        computer_score = 0
        rounds = int(input("Kaç tur oynamak istersiniz? "))

        for _ in range(rounds):
            result = play_round()
            if result == "Kazandınız!":
                user_score += 1
            elif result == "Kaybettiniz!":
                computer_score += 1

            print(f"Skor: Siz {user_score} - {computer_score} Bilgisayar\n")

        if user_score > computer_score:
            print("Tebrikler! Oyunu kazandınız!")
        elif user_score < computer_score:
            print("Üzgünüm, oyunu kaybettiniz.")
        else:
            print("Oyun berabere bitti.")

        userchoice = user_wantsto_play()
        if userchoice==False:
            print("İyi günler :)")
        compchoice = computer_wantsto_play()
        if compchoice==False :
            print("Bilgisayar oynamak istemiyor")
            exit(1)


if __name__ == "__main__":
    play_game()
