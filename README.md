# 🚗👋 GTA V Hand Gesture Controller

Proyek seru untuk mengendalikan mobil di GTA V (atau game balap lainnya) hanya dengan menggunakan gerakan tangan di depan webcam. Dibuat dengan Python, OpenCV, dan MediaPipe.

---

## ✨ Fitur Utama

-   **Kontrol Setir**: Belok kiri dan kanan berdasarkan posisi horizontal tanganmu.
-   **Kontrol Gas**: Gunakan gestur tangan **mengepal** ✊ untuk melaju.
-   **Kontrol Rem**: Gunakan gestur **telapak tangan terbuka** 🖐️ untuk mengerem atau mundur.
-   **Tampilan Status**: Dapatkan umpan balik *real-time* langsung di layar *debug* (Maju, Mundur, Belok Kiri, dll.).
-   **Ringan**: Didesain agar tidak terlalu membebani CPU dengan menurunkan resolusi webcam.

---

## ⚙️ Kebutuhan & Instalasi

Pastikan kamu sudah menginstal **Python 3.8** atau versi yang lebih baru.

1.  **Clone Repositori Ini**
    ```bash
    git clone https://github.com/irgidev/gta-hand-controller.git
    cd gta-hand-controller
    ```

2.  **Install Library yang Dibutuhkan**
    Jalankan perintah ini di terminal atau command prompt:
    ```bash
    pip install opencv-python mediapipe pydirectinput
    ```

---

## 🚀 Cara Menggunakan

1.  Buka game kamu (contoh: GTA V) dan pastikan tampilannya dalam mode **Windowed** atau **Borderless Windowed**. Ini penting agar skrip bisa mengirim perintah ke game.
2.  Masuk ke dalam mobil di dalam game.
3.  Jalankan skrip melalui terminal:
    ```bash
    python main_script.py
    ```
4.  Kamu akan punya waktu 3 detik. **Segera klik jendela game** agar menjadi window yang aktif.
5.  Posisikan tanganmu di depan webcam dan mulailah mengemudi!

---

## 🖐️ Peta Kontrol Gerakan

| Gerakan | Aksi Game | Tombol Keyboard |
| :--- | :--- | :--- |
| Tangan di **Sisi Kiri** Layar | Belok Kiri | `A` (sekali tekan) |
| Tangan di **Sisi Kanan** Layar | Belok Kanan | `D` (sekali tekan) |
| **Tangan Mengepal** ✊ | Gas / Maju | `W` (tahan) |
| **Telapak Tangan Terbuka** 🖐️ | Rem / Mundur | `S` (tahan) |
| Gestur Lain / Tangan Netral | Diam | Tombol gas & rem dilepas |

---

## ⚠️ Peringatan Penting!

Proyek ini dibuat untuk tujuan **edukasi dan eksperimen**. Menggunakan skrip eksternal untuk mengontrol game di server online (seperti **FiveM**) **dapat dianggap sebagai *cheating*** dan berisiko membuat akun Anda di-banned.

**Gunakan dengan bijak dan tanggung jawab ada pada diri Anda sendiri.** Disarankan untuk hanya digunakan dalam mode *single-player* atau di server pribadi.

