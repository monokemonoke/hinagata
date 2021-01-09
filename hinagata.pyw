# ライブラリのインポート
import pyautogui
import time
import tkinter as tk

click_xy = [
    [200,300],  #「問題を直接見る」ボタンの座標
    [200,300],  # 段プリのアプリの無難なところをクリック
    [-10,-10],  # ctrl+p + enterSs
    [200,300],  # 「解説を印刷」ボタンの座標
    [200,300],  # 段プリのアプリの無難なところをクリック
    [200,300],  # 「問題一覧から選ぶ」をクリック
]

sleep_time = 0.5    #操作ごとの休憩時間

def a():
    process = 0
    for values in click_xy:
        if values[0] >= 0 and values[1] >= 0:
            pyautogui.moveTo(values[0],values[1],duration=0.1)
            pyautogui.click(values[0],values[1])
        else:
            pyautogui.hotkey('ctrl','p')
            time.sleep(sleep_time)
            pyautogui.press('enter')
        process += 100/len(click_xy)
        print('{}%'.format(process))
        time.sleep(sleep_time)

def b():
    pyautogui.moveTo(200,300,duration=0.1)
    pyautogui.click(200,300)
    pyautogui.hotkey('command','p')
    time.sleep(sleep_time)
    pyautogui.press('enter')

root = tk.Tk()
root.title('ツール')
root.geometry('300x300')
# bt = tk.Button(master=root,text='OK',height=300,width=300,command=a)
# bt.pack()
bt2 = tk.Button(master=root,text='TEST',height=300,width=300,font=('',60))
bt2.pack()
root.mainloop()