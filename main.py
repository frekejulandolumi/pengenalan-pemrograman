# ==================================================== #
#               PROGRAM KONVERSI SUHU                  #
# ==================================================== #

# Fungsi konversi dari Celsius
def celsius_ke_fahrenheit(c):
    """Mengkonversi Celsius ke Fahrenheit"""
    return (c * 9/5) + 32

def celsius_ke_kelvin(c):
    """Mengkonversi Celsius ke Kelvin"""
    return c + 273.15

def celsius_ke_reamur(c):
    """Mengkonversi Celsius ke Reamur"""
    return c * 4/5

#================================
# Fungsi konversi dari Fahrenheit
def fahrenheit_ke_celsius(f):
    """Mengkonversi Fahrenheit ke Celsius"""
    return (f - 32) * 5/9

def fahrenheit_ke_kelvin(f):
    """Mengkonversi Fahrenheit ke Kelvin"""
    return (f - 32) * 5/9 + 273.15

def fahrenheit_ke_reamur(f):
    """Mengkonversi Fahrenheit ke Reamur"""
    return (f - 32) * 4/9

#============================
# Fungsi konversi dari Kelvin
def kelvin_ke_celsius(k):
    """Mengkonversi Kelvin ke Celsius"""
    return k - 273.15

def kelvin_ke_fahrenheit(k):
    """Mengkonversi Kelvin ke Fahrenheit"""
    return (k - 273.15) * 9/5 + 32

def kelvin_ke_reamur(k):
    """Mengkonversi Kelvin ke Reamur"""
    return (k - 273.15) * 4/5

#============================
# Fungsi konversi dari Reamur
def reamur_ke_celsius(r):
    """Mengkonversi Reamur ke Celsius"""
    return r * 5/4

def reamur_ke_fahrenheit(r):
    """Mengkonversi Reamur ke Fahrenheit"""
    return (r * 9/4) + 32

def reamur_ke_kelvin(r):
    """Mengkonversi Reamur ke Kelvin"""
    return (r * 5/4) + 273.15

def lanjut():
    tanya = input("\nApakah ingin lanjut atau tidak? ").lower()
    return tanya == "y"

#PROGRAM UTAMA

#KONVERSI DARI CELCIUS
def konversi_dari_celsius():
    try:
        suhu = float(input("MASUKKAN SUHU: "))
        print(f"{suhu}°C sama dengan:")
        print(f"  - Fahrenheit : {celsius_ke_fahrenheit(suhu):.2f}°F")
        print(f"  - Kelvin     : {celsius_ke_kelvin(suhu):.2f}K")
        print(f"  - Reamur     : {celsius_ke_reamur(suhu):.2f}°R")
        print(f"{'='*50}")
        if not lanjut():
            exit()
    except ValueError:
        print("\nError: Masukkan angka yang valid!")

#KONVERSI DARI FAHRENHEIT
def konversi_dari_fahrenheit():
    try:
        suhu = float(input("MASUKKAN SUHU: "))
        print(f"\n{'='*50}")
        print(f"{suhu}°F sama dengan:")
        print(f"  - Celsius    : {fahrenheit_ke_celsius(suhu):.2f}°C")
        print(f"  - Kelvin     : {fahrenheit_ke_kelvin(suhu):.2f}K")
        print(f"  - Reamur     : {fahrenheit_ke_reamur(suhu):.2f}°R")
        print(f"{'='*50}")
        if not lanjut():
            exit()
    except ValueError:
        print("\nError: Masukkan angka yang valid!")

#KONVERSI DARI KELVIN
def konversi_dari_kelvin():
    try:
        suhu = float(input("MASUKKAN SUHU: "))
        if suhu < 0:
            print("\nError: Suhu Kelvin tidak boleh negatif!")
            return
        print(f"\n {'='*50}")
        print(f"{suhu}K sama dengan:")
        print(f"  - Celsius    : {kelvin_ke_celsius(suhu):.2f}°C")
        print(f"  - Fahrenheit : {kelvin_ke_fahrenheit(suhu):.2f}°F")
        print(f"  - Reamur     : {kelvin_ke_reamur(suhu):.2f}°R")
        print(f"{'='*50}")
        if not lanjut():
            exit()
    except ValueError:
        print("\nError: Masukkan angka yang valid!")

#KONVERSI DARI REAMUR
def konversi_dari_reamur():
    try:
        suhu = float(input("MASUKKAN SUHU: "))
        print(f"\n{'='*50}")
        print(f"{suhu}°R sama dengan:")
        print(f"  - Celsius    : {reamur_ke_celsius(suhu):.2f}°C")
        print(f"  - Fahrenheit : {reamur_ke_fahrenheit(suhu):.2f}°F")
        print(f"  - Kelvin     : {reamur_ke_kelvin(suhu):.2f}K")
        print(f"{'='*50}")
        if not lanjut():
            exit()
    except ValueError:
        print("\nError: Masukkan angka yang valid!")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#FUNGSI UTAMA PROGRAM
def main():
    while True:
        print("\n" + "="*50)
        print("PROGRAM KONVERSI SUHU".center(50))
        print("="*50)
        print("\nPilih satuan suhu awal:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        print("4. Reamur")
        print("5. Keluar")
        print("="*50)
        
        pilihan = input("\nMasukkan pilihan (1-5): ")
        
        if pilihan == '1':
            konversi_dari_celsius()
        elif pilihan == '2':
            konversi_dari_fahrenheit()
        elif pilihan == '3':
            konversi_dari_kelvin()
        elif pilihan == '4':
            konversi_dari_reamur()
        elif pilihan == '5':
            print("="*50)
            print("\nTerima kasih telah menggunakan program ini!")
            print("="*50)
            break
        else:
            print("\nPilihan tidak ada! Silakan pilih 1-5.")

if __name__== "__main__":
    main()