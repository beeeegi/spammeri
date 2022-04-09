from typing import Text
import pyautogui
import time

print("spami daiwyeba 5 wamshi.")
print("spamis shesawyvetad gatishe es fanjara.\n")
time.sleep(5)

text = open("text", 'r')

for word in text:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    print('vspamav, gatishet es fanjara rom shewyvitot spami')

print('\nspami morcha, tu gindat rom gagrdzeldes waikitxet instruqcia.')
text.close() 