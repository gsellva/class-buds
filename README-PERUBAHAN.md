# Peer Tutoring Platform — Perubahan Jadwal Tutor & Approval Request

## Fitur yang disesuaikan

### 1. Jadwal ketersediaan tutor
- Form `Become a Tutor` menyediakan checkbox untuk Senin–Minggu.
- Setiap hari yang dipilih memiliki input waktu mulai dan selesai (`type="time"`).
- JavaScript memvalidasi bahwa minimal satu hari dipilih dan jam selesai setelah jam mulai.
- Data dikirim ke FastAPI sebagai JSON melalui field `availability`, lalu disimpan pada kolom `tutors.availability`.
- Profil tutor menampilkan hari dan rentang jam yang tersimpan.
- Kolom database tetap memakai `TEXT`, sehingga tidak perlu membuat tabel baru hanya untuk jadwal.

### 2. Persetujuan request tutoring oleh admin
- Setiap request baru otomatis berstatus `pending`.
- Halaman `/admin` menampilkan status dan tombol Approve/Reject untuk request yang masih pending.
- Approve mengubah status menjadi `approved`; Reject mengubah status menjadi `rejected`.
- Halaman konfirmasi kepada siswa menjelaskan bahwa request masih menunggu persetujuan dan belum dikonfirmasi.

## File utama yang diubah
- `database.py` — menambahkan kolom `requests.status` saat inisialisasi jika belum ada.
- `routers/tutors.py` — validasi dan penyimpanan jadwal JSON, pengiriman jadwal ke halaman profil.
- `routers/requests.py` — request baru berstatus pending.
- `routers/admin.py` — endpoint approve/reject request tutoring.
- `templates/become-tutor.html` — pilihan hari dan jam.
- `templates/tutor-profile.html` — tampilan jadwal terstruktur.
- `templates/request-tutoring.html` — pesan bahwa request belum dikonfirmasi.
- `templates/admin.html` — status dan kontrol approval/rejection request.

## Cara menjalankan
1. Backup file database `tutors.db` yang sudah ada sebelum mengganti kode.
2. Salin file perubahan ke project, pertahankan file database yang sudah digunakan.
3. Install dependency: `pip install -r requirements.txt`.
4. Jalankan aplikasi dari folder `peer-tutoring`: `uvicorn main:app --reload`.
5. Saat aplikasi startup, `init_database()` akan menambahkan kolom `status` ke tabel `requests` jika database lama belum memilikinya.
6. Coba ajukan tutor baru, approve tutor melalui `/admin`, lalu buat request tutoring. Request harus terlihat sebagai Pending sampai admin memilih Approve atau Reject.

## Catatan penting
- Halaman `/admin` dilindungi login browser dengan username `admin` dan password dari environment variable `ADMIN_PASSWORD`. Tanpa variabel itu, halaman admin tetap terkunci. Hosting harus memakai HTTPS agar password tidak terkirim tanpa enkripsi.
- Setelah request disetujui, `/admin` menampilkan tombol WhatsApp Tutor dan WhatsApp Student berisi pesan siap kirim. Admin yang menekan kirim; belum ada pengiriman otomatis.
- Jadwal yang sudah ada sebagai teks biasa tetap bisa ditampilkan sebagai fallback di profil. Jadwal baru akan disimpan dalam JSON terstruktur.
