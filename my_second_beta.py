from datetime import datetime
import time
import schedule

todos_dict = {
    '03': "Janob Tahajjud nafl namoz vaqti böldi!",
    '04': "Uyg'oning Janob sizni buyuk ishlar kutmoqda!.\nBomdod namoz vaqti böldi",
    '05': "Bugun Namozlaringizni Alloh Taolo o'z dargohida qabul qilsin!",
    '06': "Bugungi ishlarizga chin dildan omad tilayman",
    '07': "Janob sizni buyuk ishlar kutmoqda!\nKuningiz hayrli bo'lsin, Janob",
    '08': "Nonushta qilib oldingizmi Janob?",
    '09': "Darsingizga kech qolmadingizmi Janob?",
    '10': "",
    '11': "Yaxshi dam oldingizmi Janob?",
    '12': "Salovat aytish esingizdan chiqmadimi?",
    '13': "",
    '14': "Darsingiz tugadimi Janob?",
    '15': "",
    '16': "Bugungilik kunga atalgan darslaringizni qilishni boshlang Janob!",
    '17': "Ishlaringiz qanday ketmoqda Janob?",
    '18': "Kuningiz qanday o'tdi, Janob?\nSalovat aytish esingizdan chiqmadimi?",
    '19': "",
    '20': "Bugungi yumushlaringizni hammasini tugatdingizmi?",
    '21': "Vaqtingizni to'g'ri taqsimladingizmi?\nEndi ertangi kuningizni rejalashtiring!",
    '22': "Bilaman bugungi 'Kun' Sizga oson bo'lmadi, lekin siz uddaldingiz!\nEndi yotib dam oling!",
    '23': "",
    '24': "",
}

def t_info():
    time_now = datetime.now()
    for k, v in todos_dict.items():
        if int(k) == time_now.hour:
            print(f"Soat {k} bo'ldi. {v}")
            if v == "":
                print(f"Bu qatorga hech nima belgilanmagan!")
def main():
    #schedule.every(5).seconds.do(t_info)
    schedule.every().hour.do(t_info)
    
    while True:
        schedule.run_pending()
        
if __name__ == '__main__':
    main()