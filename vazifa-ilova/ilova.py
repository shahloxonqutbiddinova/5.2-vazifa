from vazifa import load_tasks, save_tasks, add_task, show_tasks, delete_task

tasks = []

def menyu():
    print("===Vazifa Menyusi===")
    print("1 - Vazifa qo‘shish")
    print("2 - Ro‘yxatni ko‘rish")
    print("3 - Vazifani o‘chirish")
    print("0 - Chiqish")

def main():
    filename = "malumotlar.txt"
    tasks = load_tasks(filename)
    print(f"Vazifalar '{filename}' dan yuklandi. Jami: {len(tasks)} ta.")
    try:
        while True:
            menyu()
            tanlov = input("Tanlang: ").strip()
            if tanlov == "1":
                task = input("Yangi vazifa: ")
                if add_task(tasks, task):
                    print("Vazifa qo'shildi.")
                else:
                    print("Bo'sh vazifa qabul qilinmaydi.")
            elif tanlov == "2":
                show_tasks(tasks)
            elif tanlov == "3":
                if not tasks:
                    print("Ro'yxatda vazifa yo'q.")
                    continue
                show_tasks(tasks)
                raqam = input("O'chirish uchun raqam kiriting: ").strip()
                if not raqam.isdigit():
                    print("Faqat raqam kiriting.")
                    continue
                idx = int(raqam)
                if delete_task(tasks, idx):
                    print("Vazifa o'chirildi.")
                else:
                    print("Bunday raqam mavjud emas.")
            elif tanlov == "0":
                print("Vazifalar saqlanmoqda...")
                save_tasks(tasks, filename)
                print("Saqlandi. Dastur tugadi.")
                break
            else:
                print("Noto'g'ri tanlov.")
    except KeyboardInterrupt:
        print("\nCtrl+C. Vazifalar saqlanmoqda...")
        save_tasks(tasks, filename)
        print("Saqlandi.")

main()