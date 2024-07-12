import os
import shutil

def temp_klasorleri_temizle():
    # Geçici klasörlerin listesi
    temp_klasorler = [
        os.environ.get('TEMP'),      # Kullanıcı geçici dosya dizini
        os.environ.get('TMP'),       # Kullanıcı geçici dosya dizini (alternatif)
        os.environ.get('LOCALAPPDATA') + '\\Temp',  # Kullanıcı uygulama veri geçici dizini
        os.environ.get('SystemRoot') + '\\Temp',    # Sistem geçici dosya dizini
        os.environ.get('SystemRoot') + '\\Prefetch' # Sistem prefetch dizini
    ]

    # Her bir geçici klasörü temizleme işlemi
    for klasor in temp_klasorler:
        if klasor and os.path.exists(klasor):
            try:
                # Klasör içindeki dosyaları ve alt klasörleri silme
                for dosya in os.listdir(klasor):
                    dosya_yolu = os.path.join(klasor, dosya)
                    if os.path.isfile(dosya_yolu):
                        os.remove(dosya_yolu)
                        print(f"{dosya_yolu} dosyası silindi.")
                    elif os.path.isdir(dosya_yolu):
                        shutil.rmtree(dosya_yolu)
                        print(f"{dosya_yolu} klasörü ve içeriği silindi.")
            except PermissionError as e:
                print(f"İzin hatası: {e}")

if __name__ == "__main__":
    # Scriptin root olarak çalıştırılmasını kontrol etme
    if os.name == 'posix' and os.geteuid() != 0:
        print("Bu scripti root olarak çalıştırın.")
    else:
        temp_klasorleri_temizle()
