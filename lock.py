import os
user_file_path = "/tmp/usr.txt"
pass_file_path = "/tmp/pass.txt"

u = "yes"
if u == "yes":
    print(" ")
else:
    # Doğru bilgileri alınana kadar döngü devam edecek
    while True:
        # Kullanıcıdan giriş alalım
        a = input("Adınız: ")
        b = input("Şifreniz: ")

        with open(user_file_path, "r") as user_file:
            correct_username = user_file.read().strip()

        with open(pass_file_path, "r") as pass_file:
            correct_password = pass_file.read().strip()

        # Giriş bilgilerini kontrol edelim
        if a == correct_username and b == correct_password:
            print("Giriş başarılı!")
            break
        else:
            print("\033[0;31mINCORRECT!!! TRY AGAİN!!!")
