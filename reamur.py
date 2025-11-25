# Program Konversi Suhu dari Reamur ke Celcius, Kelvin, dan Fahrenheit

def reamur_to_celsius(r):
    return r * 5/4

def reamur_to_kelvin(r):
    return (r * 5/4) + 273.15

def reamur_to_fahrenheit(r):
    return (r * 9/4) + 32

# Input dari pengguna
reamur = float(input("Masukkan suhu dalam Reamur: "))

# Konversi
celsius = reamur_to_celsius(reamur)
kelvin = reamur_to_kelvin(reamur)
fahrenheit = reamur_to_fahrenheit(reamur)

# Output
print(f"Suhu dalam Celcius    : {celsius:.2f} °C")
print(f"Suhu dalam Kelvin     : {kelvin:.2f} K")
print(f"Suhu dalam Fahrenheit : {fahrenheit:.2f} °F")