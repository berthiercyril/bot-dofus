import numpy as np
import pyautogui
import time
import pygetwindow as gw
import random
from script import start_turn, is_ready, check_end_combat, self_cast_spell, target_cast_spell, check_end_combat

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
    time.sleep(1)
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
    start_turn(0)

    # Clique sur la case 357, 430 puis passe son tour
    pyautogui.click(357, 430)
    time.sleep(2)
    print("Clicked at 357, 430")
    pyautogui.press('space')
    print("Turn skipped")

    # Vérifie le début du tour à nouveau
    start_turn(1)

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