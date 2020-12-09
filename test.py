
def try_get_fio(fio):
    try:
        c = 0
        mas = fio.split()
        print(mas, 'dad')
        if 2 <= len(mas) <= 3:
            for elem in mas:

                for let in elem:
                    if let in "1234567890":
                        print("Неверный ввод")
                        c = 1

        else:
            print("Неверный ввод2")
            c = 1

    except:
        print("Неверный ввод3")
        c = 1
    return c



