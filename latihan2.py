data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa.append({
        "Nama": nama,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })

    tambah = input("Tambah data lagi? (y/t): ").lower()
    if tambah == 't':
        break

print("\nDaftar Data Mahasiswa:")
print("=" * 60)
print(f"{'No':<5}{'Nama':<15}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Akhir':<10}")
print("=" * 60)

for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"{i:<5}{mhs['Nama']:<15}{mhs['Tugas']:<10}{mhs['UTS']:<10}{mhs['UAS']:<10}{mhs['Nilai Akhir']:<10.2f}")

print("=" * 60)
print("Program selesai.")
