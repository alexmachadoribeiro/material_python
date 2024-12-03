# importa bibliotecas
import pyautogui
import time

# tempo que cada comando demora para executar
pyautogui.PAUSE = 1

# instruções
pyautogui.press('win')
pyautogui.write('vscode')
pyautogui.press('enter')

# espera 10 segundos para abrir o vscode e continuar com os comandos
time.sleep(10)

# continua as instruções
pyautogui.hotkey('ctrl', 'shift', "'")
pyautogui.write('git add .')
pyautogui.press('enter')
pyautogui.write('git commit -m "Repositório atualizado por automação."')

# espera 5 segundos para dar tempo de fazer o commit
time.sleep(5)

# continua as instruções
pyautogui.press('enter')
pyautogui.write('git push')