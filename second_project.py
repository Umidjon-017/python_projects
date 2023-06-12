time = int(input("1 dan 24 gacha bo'lgan sonlardan birini kiriting!: "))

if time == 3:
    print("Janob  nafl namozi vaqti bo'ldi!")
#Namoz vaqtlariga vibratsiya qöshish kerak(faqat shu joyiga, balki har biriga)
elif time == 4:
    print("Uyg'oning Janob sizni buyuk ishlar kutmoqda!")
elif time == 5:
    print("Uyg'oning Janob sizni buyuk ishlar kutmoqda!")
    print("Bugun o'qiydigan Namozlaringizni Alloh Taolo o'z dargohida qabul qilsin!")
elif time == 6:
    print("Uyg'oning Janob sizni buyuk ishlar kutmoqda!")
elif time == 7:
    print("Yaxshi dam oldingizmi Janob?")
elif time == 8:
    print("Nonushta qilib oldingizmi Janob?")
    print("Darsingizga kech qolmadingizmi Janob?")
elif time == 12:
    print("Salovat aytish esingizdan chiqmadimi?")
elif time == 14:
    sa = input("Darsingiz tugadimi Janob?: ")
    print(sa)
    if sa == "ha" or "Ha":
        print("Uyga yaxshi yetvoling Janob!")
    elif sa == "yöq" or "Yöq":
        print("Unday bölsa sizga omad tilayman, Janob")
    else:
        print("Siz ha yoki yöq buyruqlaridan birini kiritishingiz kerak!")
    print("Janob qaydlar daftarchangizga bir nazar tashlab qo'yishni unutmang!")
elif time == 16:
    print("Bugungilik kunga atalgan darslaringizni qilishni boshlang Janob!")
elif time == 17:
    print("Ishlaringiz qanday ketmoqda Janob?")
elif time == 18:
    print("Kuningiz qanday o'tdi, Janob?")
    print("Salovat aytish esingizdan chiqmadimi?")
elif time == 20:
    Quest = int(input("Bugungi yumushlaringizni hammasini tugatdingizmi? :"))
    print(Quest)
    if Quest == 1:
        print("Молодец!, Ты самый лучший!, Я люблю тебя!")
    elif Quest == 2:
        print("Maqsadingizga bir kun kech qoldingiz!")
    elif Quest == 3:
        print("Keyingi safar yaxshiroq harakat qiling!")
    else:
        print("1 dan 4 gacha bölgan sonlardan birini tanglang!")
elif time == 21:
    print("Vaqtingizni to'g'ri taqsimladingizmi? ")
    print("Endi ertangi kuningizni rejalashtiring! ")
elif time == 22:
    print("Bilaman bugungi 'Kun' Sizga oson bo'lmadi, lekin siz uddaldingiz!")
    print("Endi yotib dam oling!")
elif time != int and time <= 24:
    print("Bu qatorga hech nima belgilanmagan!")

if time >= 7 and time <= 18:
        print("Kuningiz hayrli bo'lsin!")

elif time >= 18 and time <= 21:
    print("Hayrli kech!")

elif time >= 21 and time <= 5:
    print("Xayrli Tun Janob, yaxshi dam oling!")

elif time >= 24:
    
    print("Noto'g'ri son tanlangan!")

else:
    print("Xayrli Tun Janob, yaxshi dam oling!")