import pyautogui
import time
import random

pyautogui.PAUSE = 0.9

# Abre Chrome pelo menu iniciar
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Espera entre 6 a 8 segundos para o Chrome abrir (mais natural)
time.sleep(random.uniform(6, 8))

# Foca na barra de endereço e digita seu perfil no GitHub
pyautogui.hotkey("ctrl", "l")
pyautogui.write("github.com/ma4c89")
pyautogui.press("enter")

# Espera entre 7 a 10 segundos para carregar o perfil (varia dependendo da internet)
time.sleep(random.uniform(7, 10))

# Clica no botão "Repositories"
pyautogui.click(x=213, y=161)

# Espera entre 5 a 7 segundos para carregar os repositórios
time.sleep(random.uniform(5, 7))
