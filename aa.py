import schedule
import time
import webbrowser
import pyautogui
import pywhatkit

def physicsclass():
    print("working")
    webbrowser.open("https://us04web.zoom.us/j/5157443831?pwd=MTdiNldDWnV4VU8zY2tLNTQ5MVZadz09", new=1)
    time.sleep(3)

   
    joinbtn=pyautogui.locateCenterOnScreen("sq.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    

    joinbtn=pyautogui.locateCenterOnScreen("launch.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)


    joinbtn=pyautogui.locateCenterOnScreen("chat.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1);
    pyautogui.hotkey('alt', 'h')
    joinbtn=pyautogui.locateCenterOnScreen("type.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(3*60);
    pyautogui.write("Parth Ghumatkar 12 th C")
    pyautogui.press('Enter')
    time.sleep(1)

    pywhatkit.sendwhatmsg("+919975767607","Parth's class of 7:40 has started!",7,40)



def engclass():
    print("working")
    webbrowser.open("https://us04web.zoom.us/j/75427487673?pwd=ZEtwU25EbXdxZVpzQkdZeVBSbVlrdz09", new=1)
    time.sleep(3)

   
    joinbtn=pyautogui.locateCenterOnScreen("sq.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    

    joinbtn=pyautogui.locateCenterOnScreen("launch.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    joinbtn=pyautogui.locateCenterOnScreen("chat.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1);
    pyautogui.hotkey('alt', 'h')
    joinbtn=pyautogui.locateCenterOnScreen("type.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(3*60);
    pyautogui.write("Parth Ghumatkar 12 th C")
    pyautogui.press('Enter')
    time.sleep(1)
    
    pywhatkit.sendwhatmsg("+919975767607","Parth's class of English at 8:30am has started!",8,30)


def mathsclass():
    print("working")
    webbrowser.open("https://us04web.zoom.us/j/2942235217?pwd=WmxnYUZDSGxIelRIbnhzNTNZZzVlZz09", new=1)
    time.sleep(3)

   
    joinbtn=pyautogui.locateCenterOnScreen("sq.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    

    joinbtn=pyautogui.locateCenterOnScreen("launch.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    joinbtn=pyautogui.locateCenterOnScreen("chat.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1);
    pyautogui.hotkey('alt', 'h')
    joinbtn=pyautogui.locateCenterOnScreen("type.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(3*60);
    pyautogui.write("Parth Ghumatkar 12 th C")
    pyautogui.press('Enter')
    time.sleep(1)
    
    pywhatkit.sendwhatmsg("+919975767607","Parth's class of Maths at 9:20 has started!",9,20)

def chemclass():
    print("working")
    webbrowser.open("https://us04web.zoom.us/j/5080834026?pwd=QlpIRFVKNzF4cWtwU2ozellublJGUT09", new=1)
    time.sleep(3)

   
    joinbtn=pyautogui.locateCenterOnScreen("sq.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    

    joinbtn=pyautogui.locateCenterOnScreen("launch.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    joinbtn=pyautogui.locateCenterOnScreen("chat.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1);
    pyautogui.hotkey('alt', 'h')
    joinbtn=pyautogui.locateCenterOnScreen("type.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(3*60);
    pyautogui.write("Parth Ghumatkar 12 th C")
    pyautogui.press('Enter')
    time.sleep(1)

    pywhatkit.sendwhatmsg("+919975767607","Parth's class of Chemistry at 10:10am has started!",7,40)


def Itclass():
    print("working")
    webbrowser.open("https://us05web.zoom.us/j/3574392189?pwd=eWhsNHBtb2srQU9Ka2xzM3kwL1gwQT09", new=1)
    time.sleep(3)

   
    joinbtn=pyautogui.locateCenterOnScreen("sq.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    

    joinbtn=pyautogui.locateCenterOnScreen("launch.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

    joinbtn=pyautogui.locateCenterOnScreen("chat.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1);
    pyautogui.hotkey('alt', 'h')
    joinbtn=pyautogui.locateCenterOnScreen("type.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(3*60);
    pyautogui.write("Parth Ghumatkar 12 th C")
    pyautogui.press('Enter')
    time.sleep(1)
    
    pywhatkit.sendwhatmsg("+919975767607","Parth's class of Chemistry at 10:10am has started!",7,40)


schedule.every().day.at("07:40").do(physicsclass)
schedule.every().day.at("08:30").do(physicsclass)
schedule.every().day.at("09:20").do(mathsclass)
schedule.every().day.at("10:10").do(chemclass)
schedule.every().day.at("11:00").do(Itclass)


while True:
    schedule.run_pending()
    time.sleep(1)
