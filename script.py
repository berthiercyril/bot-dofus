import numpy as np
import pyautogui
import time
import pygetwindow as gw
import cv2
import random

# Utilisation de la variable globale
global turn_counter

# Bouftou function
def bouftou():
    window_title = find_dofus_window()
    if window_title is not None:
        resize_window(window_title, 900, 900)
    else:
        print("Dofus window not found, stopping the script.")
        return
    
    # show_rel_mouse_coords(window_title) # Affiche les coordonnées de la souris par rapport à la fenêtre Dofus

    
    while True:  # Boucle infinie
        if check_pods():  # Vérifie l'état des pods
            travel_to_bank()  # Voyage à la banque si les pods sont pleins
            continue  # Revenir au début de la boucle pour vérifier à nouveau
        
        combat_success = initiate_combat()
        
        if not combat_success:
            print("The fight cannot start, no monster found.")
            continue  # Sort de la boucle si aucun monstre n'est trouvé
        
        ready_success = check_ready()
        
        if not ready_success:
            print("The fight cannot start, 'ready' check failed.")
            continue  # Sort de la boucle si le is_ready échoue
        
        execute_spell_bouftou()



# djforgeron function
def djforgeron():
    window_title = find_dofus_window()
    if window_title is not None:
        resize_window(window_title, 900, 900)
    else:
        print("Dofus window not found, stopping the script.")
        return
    
    # show_rel_mouse_coords(window_title) # Affiche les coordonnées de la souris par rapport à la fenêtre Dofus

    room_counter = 13  # Compteur de salle

    while True:  # Boucle infinie jusqu'à la fin du donjon
        combat_success = initiate_combat()
        
        if not combat_success:
            print("The fight cannot start, no monster found.")
            continue  # Sort de la boucle si aucun monstre n'est trouvé
        
        ready_success = check_ready()
        
        if not ready_success:
            print("The fight cannot start, 'ready' check failed.")
            continue  # Sort de la boucle si le is_ready échoue

        room_counter += 1  # Incrémente le compteur de salle
        print(f"The fight can start in room {room_counter}.")
        
        if room_counter == 1:
            execute_spell_room1()
        elif room_counter == 2:
            execute_spell_room2()
        elif room_counter == 3:
            execute_spell_room3()
        elif room_counter == 4:
            execute_spell_room4()
        elif room_counter == 5:
            execute_spell_room5()  #probleme de tour 
        elif room_counter == 6:
            execute_spell_room6()
        elif room_counter == 7:
            execute_spell_room7()
        elif room_counter == 8:
            execute_spell_room8()
        # elif room_counter == 9:
        #     execute_spell_room9()
        elif room_counter == 10:
            execute_spell_room10()
        elif room_counter == 11:
            execute_spell_room11()
        elif room_counter == 12:
            execute_spell_room12()
        elif room_counter == 13:
            execute_spell_room13()
        elif room_counter == 14:
            execute_spell_room14()

        if room_counter >= 14:  # Changez ce nombre selon le nombre total de salles dans le donjon
            print("Donjon terminé.")
            break  # Sort de la boucle quand le donjon est terminé


    # execute_spell_room1()
    # execute_spell_room2()
    # execute_spell_room3()
    # execute_spell_room4()
    # execute_spell_room5()
    # execute_spell_room6()
    # execute_spell_room7() #optionnal
    # execute_spell_room8() #optionnal
    # # execute_spell_room9() #optionnal
    # execute_spell_room10()
    # execute_spell_room11()
    # execute_spell_room12()  #soucis avec l'ini
    # execute_spell_room13()
    # execute_spell_room14()

# Functions

def initiate_combat():
    dofus_rect = get_dofus_window()
    if dofus_rect is None:
        return False

    x1, y1, x2, y2 = dofus_rect.left, dofus_rect.top, dofus_rect.right, dofus_rect.bottom

    color_list = ["#FCEBC4", "#645446"] # #24283C = boulanger sombre | #C69E44 = bandit | #D5AA64 = mineur sombre | #7194A6 = forgeron | #FCEBC4 = bouftou & boufton blanc | #645446 = boufton noir
    while True:
        screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
        screenshot_np = np.array(screenshot)
        image = screenshot_np[..., :3]

        for hex_color in color_list:
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

            indices = np.where(np.all(image == rgb, axis=-1))
            coords = list(zip(indices[1], indices[0]))

            if coords:
                x, y = coords[0]
                x += x1  # Ajustement pour les coordonnées globales
                y += y1  # Ajustement pour les coordonnées globales
                pyautogui.click(x, y)
                print(f"Combat initié avec la couleur {hex_color}")
                return True

        print("Aucune couleur trouvée, nouvelle tentative dans 0,1 secondes...")
        time.sleep(0.8)


def is_ready():
    while True:
        ready_position = detect_image("images/pret.png")
        if ready_position is not None:
            print("Image 'ready' found, the fight can start.")
            time.sleep(1)
            pyautogui.press('f1')
            return True
        else:
            print("Image 'ready' not found, retrying in 5 seconds...")
            time.sleep(0.5)

def check_ready():
    ready_position = detect_image("images/pret.png")
    if ready_position is not None:
        print("Image 'ready' found, the fight can start.")
        return True
    else:
        print("Image 'ready' not found.")
        return False


def detect_image(image_path):
    position = pyautogui.locateOnScreen(image_path, confidence=0.7)
    if position is not None:
        center_x = position.left + position.width // 2
        center_y = position.top + position.height // 2
        return (center_x, center_y)
    return None

def find_dofus_window():
    titles = gw.getAllTitles()
    for title in titles:
        if "Dofus" in title:
            return title
    return None

def get_dofus_window():
    dofus_window = None
    for window in gw.getWindowsWithTitle('Dofus'):
        dofus_window = window
        break

    if dofus_window is None:
        print("Fenêtre Dofus non trouvée.")
        return None
    
    return dofus_window._rect


def show_rel_mouse_coords(window_title, duree=1000):
    fin = time.time() + duree  # Durée pendant laquelle la fonction va s'exécuter
    while time.time() < fin:
        # Obtenez la fenêtre par son titre
        fenetre = gw.getWindowsWithTitle(window_title)
        if fenetre:
            fenetre = fenetre[0]
            
            # Obtenez les coordonnées globales de la souris
            x_global, y_global = pyautogui.position()
            
            # Obtenez les coordonnées du coin supérieur gauche de la fenêtre
            x_fenetre, y_fenetre = fenetre.left, fenetre.top
            
            # Calculez les coordonnées de la souris par rapport à la fenêtre
            x_relative = x_global - x_fenetre
            y_relative = y_global - y_fenetre
            
            print(f'Coordonnées de la souris par rapport à la fenêtre : x = {x_relative}, y = {y_relative}')
        else:
            print(f"Fenêtre avec le titre '{window_title}' non trouvée.")
        
        time.sleep(0.1)  # Cette ligne permet de ne pas surcharger la console

def resize_window(window_title, width, height):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window = window[0]
        window.resizeTo(width, height)
        window.moveTo(0, 0)
        print("Window resized")
    else:
        print("Window not found")

def transparency_mode():
    print("Vérification de la transparence..")
    # Vérifie si la couleur spécifique est présente à l'écran
    if find_color("#FCEBC4") is None:
        pyautogui.hotkey('t')  # Si la couleur n'est pas trouvée, appuyez sur "Maj + é"
        print("Transparence Désactivée.")


def find_color(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    image = screenshot_np[..., :3]

    indices = np.where(np.all(image == rgb, axis=-1))
    coords = list(zip(indices[1], indices[0]))

    if coords:
        return coords[0]
    return None

def check_end_combat():
    global turn_counter  # Déclaration de la variable globale
        # Boucle pour attendre la fin du combat
    while True:
        position_cbt_end = detect_image("images/cbt_end.png")  # Remplacez par le chemin de votre image de fin de combat
        if position_cbt_end is not None:
            pyautogui.press('esc')  # Appuie sur la touche 'espace' pour passer le tour
            print("Combat terminé.")
            turn_counter = 0  # Réinitialise le compteur de tours
            transparency_mode()  # Appelle la fonction qui vérifie la présence de la couleur
            break  # Sortir de la boucle lorsque le combat est terminé
        else:
            print("Combat en cours, passage du tour...")
            pyautogui.press('space')  # Appuie sur la touche 'espace' pour passer le tour
            time.sleep(1)  # Attend 3 secondes avant de vérifier à nouveau

last_hex_color = None  # Variable pour stocker la dernière couleur
turn_counter = 0  # Variable pour compter les tours

def start_turn(expected_turn=1):
    global last_hex_color  # Utilisation de la variable globale
    global turn_counter  # Utilisation de la variable globale

    while True:
        x, y = 533, 670
        pixel_color = pyautogui.pixel(x, y)
        
        # Convertit la couleur RGB en format hexadécimal
        current_hex_color = '#{:02x}{:02x}{:02x}'.format(pixel_color[0], pixel_color[1], pixel_color[2]).upper()

        if current_hex_color != last_hex_color:  # Si la couleur actuelle est différente de la dernière couleur
            last_hex_color = current_hex_color  # Mettre à jour la dernière couleur

            if current_hex_color == '#FF6600':  # Si la couleur actuelle est celle attendue pour le début du tour
                turn_counter += 1
                print(f"Tour {turn_counter} détecté.")
                if turn_counter == expected_turn:
                    print(f"Le tour {expected_turn} peut commencer.")
                    break
                else:
                    print(f"Tour détecté, mais ce n'est pas le tour attendu ({expected_turn}). Tour actuel : {turn_counter}.")
                    time.sleep(1)

        else:
            print(f"En attente du début du tour, couleur actuelle: {current_hex_color}")
            time.sleep(1)  # Attente d'une seconde avant de vérifier à nouveau


def self_cast_spell(key):
    while True:
        character_position = detect_image("images/perso.png")
        if character_position is not None:
            print("Character found.")
            break
        else:
            print("Character not found, retrying in 1 second...")
            time.sleep(1)

    pyautogui.press(key)
    print(f"Key {key} pressed.")
    time.sleep(random.uniform(0.5, 1))

    pyautogui.click(*character_position)
    print("Spell target selected.")

def target_cast_spell(key, x, y):
    pyautogui.press(key)
    print(f"Key {key} pressed.")
    time.sleep(random.uniform(0.5, 1))

    pyautogui.click(x, y)
    print(f"Spell target selected at coordinates {x}, {y}.")


def check_pods(x=465, y=678, target_color='#60BE34'): # 465 678  | #60BE34
    # Prendre une capture d'écran des coordonnées spécifiées
    pixel_color = pyautogui.screenshot().getpixel((x, y))
    
    # Convertir la couleur du pixel en hexadécimal
    pixel_color_hex = '#{:02x}{:02x}{:02x}'.format(pixel_color[0], pixel_color[1], pixel_color[2]).upper()

    # Vérifier si la couleur du pixel est égale à la couleur cible
    if pixel_color_hex == target_color.upper():
        print("Les pods sont pleins.")
        return True
    else:
        return False
    
def travel_to_bank():
    print("Voyage à la banque...")
    time.sleep(random.randint(2,3))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.doubleClick(772, 721)
    time.sleep(random.randint(0.5,1.5))  # Attendre un peu pour être sûr que l'interface réagisse

    pyautogui.click(440, 328)
    time.sleep(random.randint(0.5,1.5))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.click(486, 360)
    time.sleep(random.randint(1.5,2.5))

    pyautogui.click(305, 221)
    time.sleep(random.randint(1,2))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.click(309, 299)
    time.sleep(random.randint(1,2))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.click(479, 316)
    time.sleep(random.randint(4,5))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.click(541, 383)
    time.sleep(random.randint(0.5,1))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.click(563, 395)
    time.sleep(random.randint(1.5,2.5))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.click(163, 415)
    time.sleep(random.randint(0.5,1.5))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.click(726, 275)
    time.sleep(random.randint(0.5,1.5))  # Attendre un peu pour être sûr que l'interface réagisse
    
    pyautogui.keyDown('ctrl')
    for _ in range(20):
        pyautogui.doubleClick(680, 342)
        time.sleep(random.randint(0.3,0.9))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.keyUp('ctrl')

    pyautogui.press('esc')
    time.sleep(random.randint(0.5,1.5))  # Attendre un peu pour être sûr que l'interface réagisse
    pyautogui.doubleClick(741, 725)
    time.sleep(random.randint(0.5,1.5))  # Attendre un peu pour être sûr que l'interface réagisse

    pyautogui.click(484, 147)
    time.sleep(random.randint(4,5))

    pyautogui.click(862, 563)
    time.sleep(random.randint(4,5))

    pyautogui.click(673, 147)
    time.sleep(random.randint(8,9))

    pyautogui.click(104, 146)
    time.sleep(random.randint(10,11))

    pyautogui.click(860, 371)
    time.sleep(random.randint(8,9))


# Add this function to execute the spell sequence
def execute_spell_bouftou():
    print("Starting combat...")

    # Clique à la première position avant 'ready'
    pyautogui.click(327, 386)
    print("Clicked at 327, 386")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Lance le spell 1 et 2, puis passe son tour
    self_cast_spell('1')
    time.sleep(random.randint(2, 3))
    self_cast_spell('2')
    pyautogui.press('space')
    print("Turn finished")

    check_end_combat()

def execute_spell_room1():
    print("Starting room 1...")
    # Clique à la première position avant 'ready'
    pyautogui.click(196, 542)
    print("Clicked at 196, 542")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Clique sur la case 328, 478 et passe son tour
    pyautogui.click(328, 478)
    print("Clicked at 328, 478")
    time.sleep(2)
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour
    start_turn(2)
    # Clique sur la case 392, 449, lance le spell 1 et 2, puis passe son tour
    pyautogui.click(392, 449)
    time.sleep(2)
    print("Clicked at 392, 449")
    self_cast_spell('1')
    time.sleep(random.uniform(2, 3))
    self_cast_spell('2')
    pyautogui.press('space')
    print("Turn finished")

    check_end_combat()

def execute_spell_room2():
    print("Starting room 2...")
    # Clique à la première position avant 'ready'
    pyautogui.click(199, 545)
    print("Clicked at 199, 545")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Déplacement en 352, 461, lance le spell 1 et 2, puis passe son tour
    pyautogui.click(352, 461)
    time.sleep(random.uniform(2, 3))
    print("Clicked at 352, 461")
    self_cast_spell('1')
    time.sleep(random.uniform(2, 3))
    self_cast_spell('2')
    pyautogui.press('space')
    print("Turn finished")   

    check_end_combat()

def execute_spell_room3():
    print("Starting room 3...")
    # Clique à la première position avant 'ready'
    pyautogui.click(449, 415)
    print("Clicked at 449, 415")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Passe le tour
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Lance le sort 1 et 2, puis passe son tour
    self_cast_spell('1')
    time.sleep(random.uniform(2, 3))
    self_cast_spell('2')
    pyautogui.press('space')
    print("Turn finished")  

    check_end_combat()

def execute_spell_room4():
    print("Starting room 4...")
    # Clique à la première position avant 'ready'
    pyautogui.click(421, 371)
    print("Clicked at 421, 371")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Clique sur la case 422, 436, attend 1 seconde, puis passe son tour
    pyautogui.click(422, 436)
    print("Clicked at 422, 436")
    time.sleep(2)
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Lance les sorts 1, 2 et 3, puis passe son tour
    self_cast_spell('1')
    time.sleep(random.uniform(2, 2.3))
    self_cast_spell('2')
    time.sleep(random.uniform(2, 2.3))
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    check_end_combat()

def execute_spell_room5():
    print("Starting room 5...")
    # Clique à la première position avant 'ready'
    pyautogui.click(295, 332)
    print("Clicked at 295, 332")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Clique sur la case 388, 314, attend 2 secondes, puis passe son tour
    pyautogui.click(388, 314)
    print("Clicked at 388, 314")
    time.sleep(2)
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Clique sur la case 453, 318, attend 2 secondes, puis lance les sorts 1, 2 et 3 et passe son tour
    pyautogui.click(453, 318)
    print("Clicked at 453, 318")
    time.sleep(3)
    self_cast_spell('1')
    time.sleep(random.uniform(2, 3))
    self_cast_spell('2')
    time.sleep(random.uniform(2, 3))
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    check_end_combat()

def execute_spell_room6():
    print("Starting room 6...")
    # Clique à la première position avant 'ready'
    pyautogui.click(263, 286)
    print("Clicked at 263, 286")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Lance le sort 4 sur des coordonnées spécifiques, deux fois
    target_cast_spell('4', 131, 284)
    time.sleep(random.uniform(2, 2.3))
    target_cast_spell('4', 131, 284)
    time.sleep(random.uniform(2, 2.3))

    # Clique au coordonnée 296, 336 puis passe son tour
    pyautogui.click(296, 336)
    print("Clicked at 296, 336")
    time.sleep(2)
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Clique sur la case 355, 396, lance le spell 1, 2 et 3, puis passe son tour
    pyautogui.click(355, 396)
    time.sleep(random.uniform(2, 2.3))
    print("Clicked at 355, 396")
    self_cast_spell('1')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('2')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('3')
    time.sleep(random.uniform(1, 2))
    pyautogui.press('space')
    print("Turn finished")

    # Vérifie la fin du combat
    check_end_combat()

def execute_spell_room7():
    print("Starting room 7...")
    # Clique à la première position avant 'ready'
    pyautogui.click(228, 561)
    print("Clicked at 228, 561")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Clique sur la case 356, 499 puis passe son tour
    pyautogui.click(356, 499)
    print("Clicked at 356, 499")
    time.sleep(2)
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Clique sur la case 416, 433, lance le spell 1, 2 et 3, puis passe son tour
    pyautogui.click(416, 433)
    time.sleep(random.uniform(1, 2))
    print("Clicked at 416, 433")
    self_cast_spell('1')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('2')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    # Vérifie la fin du combat
    check_end_combat()

def execute_spell_room8():
    print("Starting room 8...")
    # Clique à la première position avant 'ready'
    pyautogui.click(357, 466)
    print("Clicked at 357, 466")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Clique sur la case 449, 415 puis passe son tour
    pyautogui.click(449, 415)
    print("Clicked at 449, 415")
    time.sleep(2)
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Lance le spell 1, 2 et 3, puis passe son tour
    self_cast_spell('1')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('2')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    # Vérifie la fin du combat
    check_end_combat()

def execute_spell_room10():
    print("Starting room 10...")
    # Clique à la première position avant 'ready'
    pyautogui.click(478, 466)
    print("Clicked at 478, 466")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Passe le tour
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Lance le sort 1, 2 et 3, puis passe son tour
    self_cast_spell('1')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('2')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    # Vérifie la fin du combat
    check_end_combat()

def execute_spell_room11():
    print("Starting room 11...")
    # Clique à la première position avant 'ready'
    pyautogui.click(406, 418)
    print("Clicked at 406, 418")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Lance le sort 1, 2 et 3, puis passe son tour
    self_cast_spell('1')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('2')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    # Vérifie la fin du combat
    check_end_combat()


def execute_spell_room12():
    print("Starting room 12...")
    # Clique à la première position avant 'ready'
    pyautogui.click(783, 256)
    print("Clicked at 783, 256")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Lance le sort 1, 2 et 3, puis passe son tour
    self_cast_spell('1')
    time.sleep(2)
    self_cast_spell('2')
    time.sleep(2)
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    # Vérifie la fin du combat
    check_end_combat()

def execute_spell_room13():
    print("Starting room 13...")
    # Clique à la première position avant 'ready'
    pyautogui.click(258, 578)
    print("Clicked at 258, 578")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Clique sur la case 260, 513 puis passe son tour
    pyautogui.click(260, 513)
    time.sleep(2)
    print("Clicked at 260, 513")
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Clique sur la case 326, 446 puis passe son tour
    pyautogui.click(326, 446)
    time.sleep(2)
    print("Clicked at 326, 446")
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour encore une fois
    start_turn(3)

    # Lance le sort 1, 2 et 3, puis passe son tour
    self_cast_spell('1')
    time.sleep(2)
    self_cast_spell('2')
    time.sleep(2)
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    # Vérifie la fin du combat
    check_end_combat()

def execute_spell_room14():
    print("Starting room 14...")
    # Clique à la première position avant 'ready'
    pyautogui.click(294, 436)
    print("Clicked at 294, 436")

    # Vérifie si le joueur est prêt
    if not is_ready():
        print("The fight cannot start, 'ready' check failed.")
        return

    # Vérifie le début du tour
    start_turn(1)

    # Clique sur la case 357, 430 puis passe son tour
    pyautogui.click(357, 430)
    time.sleep(2)
    print("Clicked at 357, 430")
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(2)

    # Clique sur la case 386, 414, lance le sort 1, 2 et 3, puis passe son tour
    pyautogui.click(386, 414)
    time.sleep(random.uniform(1, 2))
    print("Clicked at 386, 414")
    self_cast_spell('1')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('2')
    time.sleep(random.uniform(1, 2))
    self_cast_spell('3')
    pyautogui.press('space')
    print("Turn finished")

    # Vérifie la fin du combat
    check_end_combat()







if __name__ == "__main__":
    bouftou()


#Room 1:  196 / 542 => check start turn 328 / 478 => 392 / 449 spell 1 + 2 skip turn
#Room 2: 199 / 545 => 352 / 461 spell 1 + 2 skip turn
#Room 3: 449 / 415 skip turn => spell 1 + 2 skip turn ::validé
#Room 4: 421 / 371 => 422 / 436 skip turn => spell 1 + 2 + 3 skip turn  ::validé
#Room 5: 295 / 332 => 388 / 314 skip turn => 453 / 318 spell 1 + 2 + 3 skip turn ::validé
#Room 6: 263 / 286 => spell 4 + 4 (131 / 284) 296 / 336 skip turn => 355 / 396 spell 1 + 2 + 3 skip turn ::problème a la double atk (verifier la fonction)
#Room 7: 228/561 => 356 / 499 skip turn => 416 / 433 spell 1 + 2 + 3 skip turn ::validé
#Room 8: 357/ 466 => 449/415 skip turn => spell 1 + 2 + 3 skip turn ::validé 
#Room 9:  292 / 498 => 321/464 skip turn => skip turn => skip turn => spell 1 + 2 + 3 skip turn (voir pour cibler les boulanger avec des ronces) ::a faire plus tard
#Room 10:  478/466 skip turn => spell 1 + 2 + 3 skip turn  :: au start du cbt il faut se mettre a gauche
#Room 11: 406/418 => spell 1 + 2 + 3 skip turn ::validé
#Room 12: 783/256 => spell 1 + 2 + 3 skip turn ::seulment le spell 3 a ete cast
#Room 13: 258/578 => 260/513 skip turn => 326/446 skip turn => spell 1 + 2 + 3 skip turn ::position souris avant le verif turn
#Room 14: 294/436 => 357/430 skip turn => 386/414 spell 1 + 2 + 3 skip turn
