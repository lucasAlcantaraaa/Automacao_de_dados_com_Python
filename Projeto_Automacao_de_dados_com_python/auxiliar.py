import pyautogui
import time 

time.sleep(5) # O time sleep é o tempo de espera para ele medir o position e o 5 é que ele vai esperar 5 segundos para mostrar a posição 

print(pyautogui.position()) # Comando utilizado para mostrar a posição do mouse no sistema cartesiano (x e y)
