def add(a=None, b=None):
    if a == None or b == None:
        print("parameter tidak lengkap")
        return

    total = a + b
    return total


def substract(a=None, b=None):
    if a == None or b == None:
        print("parameter tidak lengkap")
        return

    total = a - b
    return total


def bmi(bb=None, tb=None):
    if bb == None or tb == None:
        print("parameter tidak lengkap")
        return

    return bb / (tb * tb)


def bmi_check(bmi):
    if bmi < 18.5:
        print("kamu termasuk kategori kurus")
    elif bmi < 25:
        print("kamu termasuk kategori Normal")
    elif bmi < 30:
        print("kamu termasuk kategori Overweight")
    else:
        print("kamu termasuk kategori Obesity")