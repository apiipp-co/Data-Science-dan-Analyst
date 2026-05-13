import arimatika as f

bb = float(input("Masukan berat badan (kg): "))
tb = float(input("Masukan tinggi badan (meter): "))

bmi = f.bmi(bb, tb)

print("BMI kamu adalah:", bmi)

f.bmi_check(bmi)