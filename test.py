
def try_get_fio(fio):
    try:
        c = 0
        mas = fio.split()
        if 2 <= len(mas) <= 3:
            for elem in mas:

                for let in elem:
                    if let in "1234567890":
                        c = 1

        else:
            c = 1

    except:
        c = 1
    return c



