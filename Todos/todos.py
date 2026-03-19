import json
import os

DATEI = "todos.json"

def todos_laden():
    if os.path.exists(DATEI):
        with open(DATEI, "r") as f:
            return json.load(f)
    return []

def todos_speichern(todos):
    with open(DATEI, "w") as f:
        json.dump(todos, f)

def todos_löschen(todos, nummer):
    if nummer < 1 or nummer > len(todos):
        print("❌ Diese Nummer existiert nicht")
        return
    entfernt = todos.pop(nummer-1)
    todos_speichern(todos)
    print(f"✓ '{entfernt['aufgabe']}' gelöscht")

def todo_hinzufügen(todos, aufgabe):
    todos.append({"aufgabe": aufgabe, "erledigt": False})
    todos_speichern(todos)
    print(f"✓ '{aufgabe}' hinzugefügt")

def todos_anzeigen(todos):
    if len(todos) == 0:
        print("Keine Todos vorhanden")
        return
    for i, todo in enumerate(todos):
        status = "✅" if todo["erledigt"] else "⬜"
        print(f"{i+1}. {status} {todo['aufgabe']}")

def todo_erledigen(todos, nummer):
    if nummer < 1 or nummer > len(todos):
        print("❌ Diese Nummer existiert nicht")
        return
    todos[nummer-1]["erledigt"] = True
    todos_speichern(todos)
    print(f"✓ Aufgabe {nummer} als erledigt markiert")

# Todos beim Start laden
todos = todos_laden()

# Hauptschleife
while True:
    print("\n--- TODO LISTE ---")
    print("1 - Todo hinzufügen")
    print("2 - Todos anzeigen")
    print("3 - Todo erledigen")
    print("4 - Todo löschen")
    print("q - Beenden")

    auswahl = input("\nWas möchtest du tun? ")

    if auswahl == "1":
        aufgabe = input("Aufgabe: ")
        todo_hinzufügen(todos, aufgabe)
    elif auswahl == "2":
        todos_anzeigen(todos)
    elif auswahl == "3":
        todos_anzeigen(todos)
        nummer = int(input("Welche Nummer? "))
        todo_erledigen(todos, nummer)
    elif auswahl == "4":
        todos_anzeigen(todos)
        nummer = int(input("Welche Nummer? "))
        todos_löschen(todos, nummer)
    elif auswahl == "q":
        print("Tschüss!")
        break