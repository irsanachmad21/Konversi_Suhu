# MENGKONVERSI SATUAN TEMPERATUR

# PROGRAM DARI CELCIUS KE SUHU LAIN
print("===PROGRAM KONVERSI CELCIUS===")

celcius = float(input("suhu celcius adalah = "))
print("suhunya celciusnya adalah = ", celcius, "celcius")

reamur = (4/5)*celcius
print("suhu reamurnya adalah = ", reamur, "reamur")

fahrenheit = (9/5)*celcius+32
print("suhu fahrenheitnya adalah = ", fahrenheit, "fahrenheit")

kelvin = celcius+273
print("suhu kelvinnya adalah = ", kelvin, "kelvin")

print("")

print("===FAHRENHEIT TO KELVIN===")
fahrenheit = float(input("masukan suhu fahrenheit = "))
print("suhu fahrenheit adalah = ", fahrenheit)

celcius = 5/9*(fahrenheit-32)
kelvin = celcius+273
print("suhu fahrenheit ke kelvin adalah = ", kelvin)

print("")

print("===KELVIN TO FAHRENHEIT===")
kelvin = float(input("masukan suhu kelvin = "))
celcius = kelvin-273
fahrenheit = (9/5)*celcius+32
print("suhu kelvin to fahrenheit adalah = ", fahrenheit)
