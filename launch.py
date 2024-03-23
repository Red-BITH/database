import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os

def launch_sms_bomb():
    os.system('qterminal -e "python3 system/sms.py"')

def launch_spider_gather():
    os.system('qterminal -e "python3 system/sgather.py"')

def launch_list_network():
    os.system('qterminal -e "python3 system/lnet.py"')

# Ana pencere oluştur
root = tk.Tk()
root.title("BloodFire")

# Pencere boyutunu ayarla
window_width = 750
window_height = 550
root.geometry("%dx%d" % (window_width, window_height))
root.resizable(False, False)  # Pencerenin boyutunu değiştiremezsiniz

# Pencere arka plan rengini beyaz yap
root.configure(bg="white")

# Resimleri yükle
image_path1 = r"resim1.png"
image_path2 = r"resim2.png"

# Resimleri aç ve boyutlandır
image1 = Image.open(image_path1)
image1 = image1.resize((200, 220), Image.LANCZOS)  # Resmi yeniden boyutlandır
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open(image_path2)
image2 = image2.resize((240, 220), Image.LANCZOS)  # Resmi yeniden boyutlandır
photo2 = ImageTk.PhotoImage(image2)

# Sol üst köşeye birinci resmi yerleştir
label1 = tk.Label(root, image=photo1, bg="white")
label1.grid(row=0, column=0, padx=(50, 10), pady=10)  # Sol boşluk ayarlandı

# Merkez üstte kırmızı yazıyı yerleştir
label3 = tk.Label(root, text="BLOODFIRE", font=("Helvetica", 24, "bold"), fg="red", bg="white")
label3.grid(row=0, column=1, padx=10, pady=10)  # Padding ayarlandı

# Üst sağda ikinci resmi yerleştir
label2 = tk.Label(root, image=photo2, bg="white")
label2.grid(row=0, column=2, padx=(10, 50), pady=10)  # Sağ boşluk ayarlandı

# Butonların arasındaki mesafeyi ve uzunluğunu ayarla
button_width = 13  # Uzunluk azaltıldı
button_padx = 10    # Aralık azaltıldı
for i in range(9):  # Toplam 9 buton ekledim, 3 satırda 3'er buton
    button = tk.Button(root, text=f"Button {i+1}", font=("Helvetica", 12), bg="red", width=button_width)
    button.grid(row=i // 3 + 1, column=i % 3, padx=button_padx, pady=5)

# Button 1 (SmsBomb)
button_1 = tk.Button(root, text="SmsBomb", font=("Helvetica", 13), bg="red", width=button_width, command=launch_sms_bomb)
button_1.grid(row=1, column=0, padx=button_padx, pady=5)

# Button 2 (Spider Gather)
button_2 = tk.Button(root, text="Spider Gather", font=("Helvetica", 13), bg="red", width=button_width, command=launch_spider_gather)
button_2.grid(row=1, column=1, padx=button_padx, pady=5)

# Button 3 (List Network)
button_3 = tk.Button(root, text="List Network", font=("Helvetica", 13), bg="red", width=button_width, command=launch_list_network)
button_3.grid(row=1, column=2, padx=button_padx, pady=5)

# Exit butonu
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12, "bold"), bg="orange", fg="black", command=root.destroy)
exit_button.grid(row=4, column=1, padx=button_padx, pady=10)  # Orta hizalandı

# Github etiketi
github_label = tk.Label(root, text="Github: github.com/Red-BITH", font=("Arial", 10, "bold"), fg="black", bg="white")
github_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Copyright etiketi
copyright_label = tk.Label(root, text="© Copyright 2024 RedTools Project", font=("Arial", 10, "bold"), fg="black", bg="white")
copyright_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

root.mainloop()
