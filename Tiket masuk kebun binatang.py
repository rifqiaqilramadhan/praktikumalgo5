total_harga = 0

print("Selamat datang di Kebun Binatang Moon ZOoooo!")
while True:
    umur_input = input("Umur pengunjung (atau ketik 'selesai'): ")

    if umur_input.lower() == 'selesai':
        break

    if umur_input.isdigit():
        umur = float(umur_input)
        if umur <= 2:
            harga_tiket = 0
        elif 3 <= umur <= 12:
            harga_tiket = 14000
        elif umur >= 65:
            harga_tiket = 18000
        else:
            harga_tiket = 23000
        total_harga += harga_tiket
        print(f"Harga tiket: Rp.{harga_tiket}")
    else:
        print("Umur yang dimasukkan tidak valid. Coba lagi.")

print(f"Total harga tiket: Rp.{total_harga}")

pembayaran = 0
while pembayaran < total_harga:
    pembayaran_input = input("Masukkan pembayaran: Rp.")
    
    if pembayaran_input.replace('.', '', 1).isdigit():
        pembayaran = float(pembayaran_input)
        if pembayaran < total_harga:
            print("Maaf, pembayaran tidak mencukupi. Silakan tambahkan uang.")
    else:
        print("Pembayaran yang dimasukkan tidak valid. Coba lagi.")

kembalian = pembayaran - total_harga
print(f"Terima kasih! Kembalian Anda: ${kembalian:.2f}")
