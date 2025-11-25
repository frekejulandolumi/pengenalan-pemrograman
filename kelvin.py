def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_to_reamur(k):
    return (k - 273.15) * 4/5

# Program utama
kelvin = float(input("Masukkan suhu dalam Kelvin: "))

c = kelvin_to_celsius(kelvin)
f = kelvin_to_fahrenheit(kelvin)
r = kelvin_to_reamur(kelvin)

print(f"Kelvin ke Celsius    : {c:.2f} °C")
print(f"Kelvin ke Fahrenheit : {f:.2f} °F")
print(f"Kelvin ke Reamur     : {r:.2f} °R")