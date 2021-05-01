import schedule
import time
import webbrowser
import pyautogui

def pclass():
    print("working")
    webbrowser.open("https://us04web.zoom.us/j/8678581469?pwd=VUFUcFExS2R6dEVKZzlNTkdSa3lSdz09", new=1)
    time.sleep(3)

   
    joinbtn=pyautogui.locateCenterOnScreen("sq.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    

    joinbtn=pyautogui.locateCenterOnScreen("launch.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(3)
    

    joinbtn=pyautogui.locateCenterOnScreen("chat.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1);
    print("here now")
    pyautogui.hotkey('alt', 'h')
    joinbtn=pyautogui.locateCenterOnScreen("type.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(60);
    pyautogui.write("parth Ghumatkar 12 th C")
    pyautogui.press('Enter')
    time.sleep(1)

    



schedule.every().day.at("22:17").do(pclass)


while True:
    schedule.run_pending()
    time.sleep(1)
