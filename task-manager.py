import json
import os


TASKS_FILE = "tasks.json" #Nom du fichier où seront stockées les tâches


# Charger les tâches existantes
def load_tasks():
    if not os.path.exists(TASKS_FILE):  # Vérifie si le fichier existe
        return []  # Si non, retourne une liste vide
    with open(TASKS_FILE, "r") as file:  # Ouvre le fichier en mode lecture
        return json.load(file)  # Charge les tâches et les retourne

# Sauvegarder les tâches
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:  # Ouvre le fichier en mode écriture
        json.dump(tasks, file, indent=4)  # Écrit la liste des tâches en JSON


def add_task(description):
    tasks = load_tasks()  # Charge les tâches existantes
    tasks.append({"description": description, "completed": False})  # Ajoute une nouvelle tâche non complétée
    save_tasks(tasks)  # Sauvegarde la liste mise à jour
    print(f"Tâche ajoutée : {description}")  # Confirmation


def list_tasks():
    tasks = load_tasks()  # Charge les tâches
    if not tasks:  # Vérifie s’il y a des tâches
        print("Aucune tâche enregistrée.")  # Message si la liste est vide
        return
    for i, task in enumerate(tasks):  # Boucle sur les tâches
        status = "✔" if task["completed"] else "❌"  # Affiche un check si complété
        print(f"{i + 1}. {task['description']} [{status}]")  # Affiche le numéro, la description et le statut


def complete_task(index):
    tasks = load_tasks()  # Charge les tâches
    if 0 <= index < len(tasks):  # Vérifie que l’index est valide
        tasks[index]["completed"] = True  # Marque la tâche comme complétée
        save_tasks(tasks)  # Sauvegarde les modifications
        print(f"Tâche {index + 1} complétée !")  # Confirmation
    else:
        print("Index invalide.")  # Message d'erreur si l'index est incorrect


def delete_task(index):
    tasks = load_tasks()  # Charge les tâches
    if 0 <= index < len(tasks):  # Vérifie que l’index est valide
        removed_task = tasks.pop(index)  # Supprime la tâche de la liste
        save_tasks(tasks)  # Sauvegarde la nouvelle liste sans cette tâche
        print(f"Tâche supprimée : {removed_task['description']}")  # Confirmation
    else:
        print("Index invalide.")  # Message d'erreur si l'index est incorrect


def modify_task(index, new_description) :
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks[index]["description"] = new_description
        save_tasks(tasks)
        print(f"Tâche {index + 1} modifiée avec succès !")
    else:
        print("Index invalide.")

def main():
    while True:
        print("\nGestionnaire de tâches")
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Marquer une tâche comme complétée")
        print("4. Supprimer une tâche")
        print("5. Modifier une tâche")  # Avant "Quitter"
        print("6. Quitter")  # Le chiffre change car on ajoute une nouvelle option


        choice = input("Choisissez une option : ")  # Demande un choix
        
        if choice == "1":
            description = input("Nom de la tâche : ")  # Demande une description
            add_task(description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            user_input = input("Numéro de la tâche à compléter :").strip()

            if not user_input.isdigit() :
                print("Erreur : Veuillez entrer un numéro valide.")
            else:
                index = int(user_input) - 1  # Convertit en index
                complete_task(index)
        elif choice == "4":
            user_input = input("Numéro de la tâche à supprimer : ").strip()

            if not user_input.isdigit() :
                print("Erreur : Veuillez entrer un numéro valide.")
            else:
                index = int(user_input) -1
                delete_task(index)
        elif choice == "5":
            user_input = input("Numéro de la tâche à modifier : ").strip()

            if not user_input.isdigit() :
                print("Erreur : Veuillez entrer un nombre valide.")
            else:
                index = int(user_input) -1
                new_description = input("Nouvelle description : ")
                modify_task(index, new_description)
        elif choice == "6":
            print("Fermeture du gestionnaire de tâches.")
            break
        else:
            print("Option invalide, essayez encore.")


if __name__ == "__main__":
    main()
