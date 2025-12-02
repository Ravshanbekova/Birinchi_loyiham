# To'g'ri parol
togri_parol = "Paython123"
# Urinishlar hisoblagichi
urinishlar = 3
# Muvafaqiyat bayrog'i
muvafaqiyat = False
print("Tizimga kirish")
print('-' * 30)
while urinishlar> 0:
    # Foydalanuvchidan parol so'rash
    kiritilgan_parol = input(f"Parol kiriting ({urinishlar} urinish qoldi): ")
    # Parolni tekshirish
    if kiritilgan_parol == togri_parol:
        print("Parol to'g'ri tizimga xush kelibsiz!")
        muvafaqiyat = True
        break
    else:
        urinishlar -= 1
        if urinishlar > 0:
            print(f"Parol noto'g'ri Yana {urinishlar} urinish qoldi.")
        else:
            print("Barcha urinishlar tugadi, Hisob bloklandi")
# Agar parol to'g'ri kiritilgan bo'lsa
if not muvafaqiyat:
    print("Iltimos, keyinroq urinib ko'ring adminga murojat qiling.")