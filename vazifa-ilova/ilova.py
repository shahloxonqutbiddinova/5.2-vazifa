tasks = []

def menyu():
    print("===Vazifa Menyusi===")
    print("1 - Vazifa qo‘shish")
    print("2 - Ro‘yxatni ko‘rish")
    print("3 - Vazifani o‘chirish")
    print("0 - Chiqish")

menyu()

def task_qoshish():
    task = input("Vazifani kiriting: ")
    tasks.append(task)
    print("Vazifa qo'shildi.")

def tasklarni_korsatish():
    if not tasks:
        print("Vazifalar yoq")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

 while True:
        menyu()
        tanlov = input("Tanlang: ")
        if tanlov == "1":
            task_qoshish()
        elif tanlov == "2":
            tasklarni_korsatish()
        elif tanlov == "0":
            print("Dastur tugadi.")
            break