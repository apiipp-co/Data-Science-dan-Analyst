nama = input("Nama: ")
bb = float(input("Berat badan (kg): "))
tb = float(input("Tinggi badan (cm): ")) / 100

bmi = bb / (tb * tb)

print(nama, "- BMI:", round(bmi, 1))

if bmi < 18.5:
    print("Kategori: Underweight")
elif bmi < 25:
    print("Kategori: Normal")
elif bmi < 30:
    print("Kategori: Overweight")
else:
    print("Kategori: Obesity")