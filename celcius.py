# ============================================================
#   Fungsi Konversi dari Celsius
# ============================================================

def celsius_ke_fahrenheit(c):
    """Mengkonversi Celsius ke Fahrenheit"""
    return (c * 9/5) + 32

def celsius_ke_kelvin(c):
    """Mengkonversi Celsius ke Kelvin"""
    return c + 273.15

def konversi_suhu():
    """Fungsi utama untuk konversi dari Celsius"""
    print("=" * 50)
    print("KONVERSI SUHU DARI CELSIUS".center(50))
    print("=" * 50)
    
    while True:
        print("\nPilih jenis konversi:")
        print("1. Celsius → Fahrenheit")
        print("2. Celsius → Kelvin")
        print("3. Keluar")
        
        pilihan = input("\nMasukkan pilihan (1-3): ")
        
        if pilihan == '3':
            print("\nTerima kasih!")
            break
        
        if pilihan in ['1', '2']:
            try:
                suhu = float(input("Masukkan nilai suhu dalam Celsius: "))
                
                if pilihan == '1':
                    hasil = celsius_ke_fahrenheit(suhu)
                    print(f"\n{suhu}°C = {hasil:.2f}°F")
                else:
                    hasil = celsius_ke_kelvin(suhu)
                    print(f"\n{suhu}°C = {hasil:.2f}K")
                    
            except ValueError:
                print("\nError: Masukkan angka yang valid!")
        else:
            print("\nPilihan tidak valid! Silakan pilih 1-3.")

if __name__ == "__main__":
    konversi_suhu()