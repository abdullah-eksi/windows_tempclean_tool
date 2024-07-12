
#Windows Temp Klasör Temizleme Scripti

Bu Python scripti, kullanıcı ve sistem geçici dosya klasörlerini temizlemek için tasarlanmıştır. Script, belirtilen geçici klasörlerdeki dosyaları ve alt klasörleri silerek disk alanı yönetimine yardımcı olur.

## Kullanım

### Gereksinimler

- Python 3.x
- `shutil` modülü

### Çalıştırma

Scripti aşağıdaki komutla çalıştırabilirsiniz:

```bash
python main.py
```

### Dikkat Edilmesi Gerekenler

- Script root (admin) yetkileriyle çalıştırılmalıdır, özellikle Windows'ta bazı klasörler erişim kısıtlamalarına sahip olabilir.
- Scriptin çalıştırıldığı dizindeki geçici dosyaları siler, bu yüzden dikkatli kullanılmalıdır.

## Desteklenen Geçici Klasörler

Script, aşağıdaki geçici klasörleri temizler:

- Kullanıcı geçici dosya dizini (`TEMP`, `TMP`)
- Kullanıcı uygulama veri geçici dizini (`LOCALAPPDATA\Temp`)
- Sistem geçici dosya dizini (`SystemRoot\Temp`)
- Sistem prefetch dizini (`SystemRoot\Prefetch`)





