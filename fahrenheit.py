# ==================================================== #
#          Fungsi Konversi dari Fahrenheit             #
# ==================================================== #

def fahrenheit_ke_celsius(f):
    """Mengkonversi Fahrenheit ke Celsius"""
    return (f - 32) * 5/9

def fahrenheit_ke_kelvin(f):
    """Mengkonversi Fahrenheit ke Kelvin"""
    return (f - 32) * 5/9 + 273.15

def konversi_suhu():
    """Fungsi utama untuk konversi dari Fahrenheit"""
    print("=" * 50)
    print("KONVERSI SUHU DARI FAHRENHEIT".center(50))
    print("=" * 50)
    
    while True:
        print("\nPilih jenis konversi:")
        print("1. Fahrenheit → Celsius")
        print("2. Fahrenheit → Kelvin")
        print("3. Keluar")
        
        pilihan = input("\nMasukkan pilihan (1-3): ")
        
        if pilihan == '3':
            print("\nTerima kasih!")
            break
        
        if pilihan in ['1', '2']:
            try:
                suhu = float(input("Masukkan nilai suhu dalam Fahrenheit: "))
                
                if pilihan == '1':
                    hasil = fahrenheit_ke_celsius(suhu)
                    print(f"\n{suhu}°F = {hasil:.2f}°C")
                else:
                    hasil = fahrenheit_ke_kelvin(suhu)
                    print(f"\n{suhu}°F = {hasil:.2f}K")
                    
            except ValueError:
                print("\nError: Masukkan angka yang valid!")
        else:
            print("\nPilihan tidak valid! Silakan pilih 1-3.")

if __name__ == "__main__":
    konversi_suhu()
