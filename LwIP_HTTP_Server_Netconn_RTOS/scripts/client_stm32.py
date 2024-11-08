import requests

# URL de votre serveur HTTP
server_url = "http://192.168.0.11"

# Fonction pour allumer la LED
def turn_on_led():
    response = requests.get(f"{server_url}/STM32F7xx_files/LED_ON")
    if response.status_code == 200:
        print("LED allumée")
    else:
        print("Erreur lors de l'allumage de la LED")

# Fonction pour éteindre la LED
def turn_off_led():
    response = requests.get(f"{server_url}/STM32F7xx_files/LED_OFF")
    if response.status_code == 200:
        print("LED éteinte")
    else:
        print("Erreur lors de l'extinction de la LED")

# Menu interactif
def menu():
    while True:
        print("\nMenu:")
        print("1. Allumer la LED")
        print("2. Éteindre la LED")
        print("3. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            turn_on_led()
        elif choice == '2':
            turn_off_led()
        elif choice == '3':
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Exécution du menu
if __name__ == "__main__":
    menu()