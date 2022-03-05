import pyautogui
import time
import requests


def check_internet():
    url = 'https://www.google.com'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except Exception.ConnectionError:
        return False

pyautogui.alert('Por favor não mexer no computador, programa abrira hbo em friends')

# abrindo o windows e entrando no chrome
pyautogui.hotkey('win', 'd')
time.sleep(2)
pyautogui.press('win')
time.sleep(2)
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')

# entrando no perfil 1 do chrome
pyautogui.moveTo(673, 427)
time.sleep(2)
pyautogui.click(clicks=2)
time.sleep(4)

if not check_internet():
    pyautogui.alert('internet fora do ar, bye bye')
else:

    # abrindo hbo pelo navegador
    pyautogui.moveTo(244, 55)
    pyautogui.write('hbo', interval=0.15)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(222, 341)
    pyautogui.click()
    time.sleep(10)

    # entrando no perfil Ayumi
    pyautogui.moveTo(532, 508)
    pyautogui.click()

'''
<<script para pesquisar friends>>
ideias: 1. mudar o codigo para que o usuario pode escolher o que assistir e dps o codigo continuar executando

    # pesquisando Friends
    pyautogui.moveTo(171, 173)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write('Friends')
    time.sleep(4)

    # precionando e dando play
    pyautogui.moveTo(257, 360)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(100, 911)
    pyautogui.click()
    time.sleep(3)
'''
