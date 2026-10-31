import random
import string

def genera_password():
    print("========================================")
    print("      BENEVENUTO NEL PASSWORD GENERATOR ")
    print("========================================")

    while True:
        try:
            lunghezza = int(input("Inserisci la lunghezza della password (consigliato almeno 12): "))
            if lunghezza < 4:
                print("La password è troppo corta! Scegli almeno 4 caratteri.")
                continue
            break
        except ValueError:
            print("Errore: Inserisci un numero intero valido.")

    usa_numeri = input("Vuoi includere i numeri? (s/n): ").strip().lower() == 's'
    usa_simboli = input("Vuoi includere i simboli speciali? (s/n): ").strip().lower() == 's'

    caratteri = string.ascii_letters
    if usa_numeri:
        caratteri += string.digits
    if usa_simboli:
        caratteri += string.punctuation

    password_lista = []

    for _ in range(lunghezza):
        password_lista.append(random.choice(caratteri))

    password = "".join(password_lista)

    print("\n----------------------------------------")
    print(f"🔑 La tua password è: {password}")
    print("----------------------------------------")

if __name__ == "__main__":
    genera_password()
