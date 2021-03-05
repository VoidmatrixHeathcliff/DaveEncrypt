# -*- coding: UTF-8 -*-

import _thread
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox

bg_color = '#D8BFD8'

window = tk.Tk()

window.title('DaveEncrypt - [歪比巴卜] 加密解密工具 - v1.1.0')
window['background'] = bg_color
window.geometry('800x475')
window.resizable(width=False, height=False)
window.iconbitmap("./icon.ico")

# 26个英文字母,大小写x2 = 52     ? ! , . ' " [ ] { } : ; @ = # $ % & * < > + - ( ) _ 空格 换行
encrypt_mapping_dict = {"a": "歪比巴卜", "A": "卜比歪巴", "b": "巴歪比卜", "B": "比比歪比", "c": "比歪歪歪", "C": "卜卜比卜", "d": "歪歪歪卜",
                        "D": "巴比比比",
                        "e": "歪比卜巴", "E": "卜比巴歪", "f": "巴歪卜比", "F": "比比比歪", "g": "歪比歪歪", "G": "卜卜卜比", "h": "卜巴巴巴",
                        "H": "比巴比比",
                        "i": "歪卜比巴", "I": "比歪巴卜", "j": "巴比歪卜", "J": "歪巴巴巴", "k": "歪歪比歪", "K": "卜比比比", "l": "巴卜巴巴",
                        "L": "比比巴比",
                        "m": "歪卜巴比", "M": "比歪卜巴", "n": "巴比卜歪", "N": "巴歪巴巴", "o": "歪歪歪比", "O": "比卜比比", "p": "巴巴卜巴",
                        "P": "比比比巴",
                        "q": "歪巴比卜", "Q": "比巴卜歪", "r": "歪歪歪歪", "R": "巴巴歪巴", "s": "比巴巴巴", "S": "比比卜比", "t": "巴巴巴卜",
                        "T": "巴卜卜卜",
                        "u": "歪巴卜比", "U": "比巴歪卜", "v": "巴巴巴巴", "V": "巴巴巴歪", "w": "巴比巴巴", "W": "比比比卜", "x": "巴歪歪歪",
                        "X": "卜巴卜卜",
                        "y": "卜歪巴比", "Y": "比卜巴歪", "z": "比比比比", "Z": "歪卜卜卜", "?": "巴巴比巴", "!": "卜歪歪歪", ",": "歪巴歪歪",
                        ".": "卜卜巴卜",
                        "'": "卜歪比巴", "\"": "比卜歪巴", "[": "卜卜卜卜", "]": "卜歪卜卜", ":": "巴巴巴比", ";": "歪卜歪歪", "@": "歪歪巴歪",
                        "#": "卜卜卜巴",
                        "$": "卜巴比歪",
                        "%": "巴卜歪比", "&": "歪比比比", "*": "卜卜歪卜", "<": "比卜卜卜", ">": "歪歪卜歪", "+": "歪歪歪巴", "-": "歪歪比巴",
                        "(": "卜巴歪比",
                        ")": "巴卜比歪", "_": "比歪比比", " ": "卜卜卜歪", "4": "比巴歪歪", "5": "比歪巴歪", "6": "巴歪比歪", "\n": "卜比卜卜",
                        "0": "歪歪巴比",
                        "1": "比歪歪巴", "2": "巴歪歪比", "3": "巴比歪歪", "7": "歪巴歪比", "8": "歪比歪巴", "9": "歪比巴歪", "=": "歪巴比歪"}

decrypt_mapping_dict = dict([val, key] for key, val in encrypt_mapping_dict.items())


def encrypt():
    ciphertext_input.delete('1.0', 'end')
    plaintext = plaintext_input.get("0.0", "end")
    ciphertext = ""
    for ch in plaintext:
        try:
            ciphertext = ciphertext + encrypt_mapping_dict[ch]
        except:
            tkinter.messagebox.showerror(title='错误', message='明文中含有不可转换字符！')
            return
    ciphertext_input.insert(1.0, ciphertext.strip("\n"))


def onClickEncrypt():
    _thread.start_new_thread(encrypt, ())


def decrypt():
    plaintext_input.delete('1.0', 'end')
    ciphertext = ciphertext_input.get("0.0", "end")
    plaintext = ""
    unit_list = []
    if (len(ciphertext) - 1) % 4 == 0:
        index = 0
        while ciphertext[index:-1] != "":
            unit_list.append(ciphertext[index:index + 4])
            index = index + 4
        for unit in unit_list:
            try:
                plaintext = plaintext + decrypt_mapping_dict[unit]
            except:
                tkinter.messagebox.showerror(title='错误', message='密文不符合转换规范！')
                return
    else:
        tkinter.messagebox.showerror(title='错误', message='密文不符合转换规范！')
        return

    plaintext_input.insert(1.0, plaintext.strip("\n"))


def onClickDncrypt():
    _thread.start_new_thread(decrypt, ())


canvas = tk.Canvas(window, bg=bg_color, height=475, width=330, highlightthickness=0)
tk_image = ImageTk.PhotoImage(Image.open('Dave.png').resize((330, 475), Image.ANTIALIAS))
image_dave = canvas.create_image(2, 2, anchor='nw', image=tk_image)

key_label = tk.Label(window, text="密钥：", font=('隶书', 16), bg=bg_color)
plaintext_label = tk.Label(window, text="明文：", font=('隶书', 16), bg=bg_color)
encrypt_btn = tk.Button(window, text="加密", font=('华文新魏', 16), bg="MediumTurquoise", command=onClickEncrypt)
decrypt_btn = tk.Button(window, text="解密", font=('华文新魏', 16), bg="#FFA07A", command=onClickDncrypt)
ciphertext_label = tk.Label(window, text="密文：", font=('隶书', 16), bg=bg_color)
plaintext_input = tk.Text(highlightcolor='RoyalBlue', font=('comic sans MS', 12), highlightthickness=1.5)
ciphertext_input = tk.Text(highlightcolor='Orange', font=('方正姚体', 12), highlightthickness=1.5)

canvas.place(x=0, y=0, anchor='nw')
plaintext_label.place(x=330, y=5, anchor='nw')
ciphertext_label.place(x=330, y=250, anchor='nw')
encrypt_btn.place(x=450, y=225, width=100)
decrypt_btn.place(x=575, y=225, width=100)
plaintext_input.place(x=330, y=35, anchor='nw', width=450, height=175)
ciphertext_input.place(x=330, y=280, anchor='nw', width=450, height=175)

plaintext_input.insert(1.0, "Hello, I'm crazy Dave !")
ciphertext_input.insert(1.0,
                        "比巴比比歪比卜巴巴卜巴巴巴卜巴巴歪歪歪比歪巴歪歪卜卜卜歪比歪巴卜卜歪比巴歪卜巴比卜卜卜歪比歪歪歪歪歪歪歪歪比巴卜比比比比卜歪巴比卜卜卜歪巴比比比歪比巴卜巴巴巴巴歪比卜巴卜卜卜歪卜歪歪歪卜比卜卜")

window.mainloop()
