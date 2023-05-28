def caesar_cipher(text, shift):
    # Inisialisasi variabel kosong untuk hasil enkripsi
    encrypted_text = ""

    # Loop melalui setiap karakter dalam plaintext
    for char in text:
        # Mengabaikan karakter selain huruf
        if not char.isalpha():
            encrypted_text += char
            continue

        # Mengubah huruf menjadi angka dengan ASCII code
        # Jumlahkan pergeseran ke ASCII code
        # Ubah angka menjadi karakter lagi
        shifted_char = chr((ord(char) + shift - 65) % 26 + 65)
        encrypted_text += shifted_char

    return encrypted_text

# Meminta input dari pengguna
plaintext = input("Masukkan teks yang ingin dienkripsi: ")
shift = int(input("Masukkan jumlah pergeseran: "))

# Enkripsi plaintext
ciphertext = caesar_cipher(plaintext, shift)

# Tampilkan hasil enkripsi
print("Teks Terenkripsi:", ciphertext)
