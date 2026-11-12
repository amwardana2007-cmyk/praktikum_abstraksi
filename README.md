LAPORAN PRAKTIKUM
PEMROGRAMAN BERORIENTASI OBJEK MERANCANG SISTEM PEMBAYARAN / PLUGIN DENGAN ABC DAN PROTOCOL

DISUSUN OLEH:
ADITYA MUKTI WARDANA (25130210003)

PROGRAM STUDI TEKNOLOGI INFORMASI
FAKULTAS TEKNIK
UNIVERSITAS TANGERANG RAYA
2026

1. TUJUAN PRAKTIKUM
   Praktikum ini bertujuan untuk memberikan pemahaman mendalam serta keterampilan praktis mengenai perancangan arsitektur perangkat lunak yang modular, fleksibel, dan extensible menggunakan Python. Melalui praktikum ini, mahasiswa mempelajari pembuatan Abstract Base Class (ABC) dengan dekorator @abstractmethod, penegakan pola Template Method, serta penerapan structural subtyping dengan Protocol dan @runtime_checkable. Selain itu, praktikum ini melatih penerapan prinsip Open/Closed dan Dependency Injection melalui arsitektur plugin terdaftar (registry) dan autodiscovery.

2.	HASIL PERCOBAAN 1: KONTRAK PEMBAYARAN DENGAN ABC
   Percobaan pertama bertujuan untuk membuat kelas abstrak PaymentMethod sebagai kontrak dasar metode pembayaran dan membuktikan bahwa kelas abstrak tidak dapat diinstansiasi secara langsung.
 
  - KODE PROGRAM
    Berkas core/utils.py:
  	<img width="897" height="338" alt="image" src="https://github.com/user-attachments/assets/8328aa39-dce5-4b5c-ab83-5e0ad4f7688c" />

    Berkas core/base.py:
  	<img width="887" height="150" alt="image" src="https://github.com/user-attachments/assets/a0edc67c-3e1e-45e6-9dac-1071cb3fbf65" />
    <img width="900" height="343" alt="image" src="https://github.com/user-attachments/assets/0cbd3725-3468-440e-81e4-e8134ba16558" />

    Berkas plugins/transfer_bank.py:
  	<img width="894" height="466" alt="image" src="https://github.com/user-attachments/assets/f00564cd-3965-479d-b438-0d6a589ef71b" />
  
  - TANGKAPAN LAYAR HASIL ANALISIS PERCOBAAN 1
    <img width="900" height="173" alt="image" src="https://github.com/user-attachments/assets/a8ee7a89-f3eb-4b22-bdfe-f91efb21f082" />

  - JAWABAN PERTANYAAN ANALISIS PERCOBAAN 1
    1.	Mengapa PaymentMethod("uji") gagal, padahal konstruktornya sudah benar?
       Jawaban: 
          Karena PaymentMethod mewarisi kelas ABC dan memiliki method abstrak (validasi dan bayar) yang belum diimplementasikan. Python secara ketat mencegah instansiasi kelas abstrak agar tidak ada objek 'setengah matang' yang dibuat tanpa implementasi method abstrak tersebut.
    2.	Apa yang terjadi pada Setengah dan mengapa pesan galatnya hanya menyebut bayar?
        Jawaban: 
          Kelas Setengah gagal diinstansiasi karena hanya mengimplementasikan validasi(), sedangkan bayar() belum diimplementasikan. Python hanya menyebutkan bayar() dalam pesan galat karena validasi() sudah berhasil dipenuhi oleh kelas turunan tersebut.
    3.	Mengapa proses() ditulis di kelas induk dan bukan di tiap subclass? Keuntungan apa yang didapat?
        Jawaban:
          proses() menerapkan pola Template Method yang menentukan urutan alur kerja pembayarannya (pemeriksaan nominal > 0 -> validasi -> eksekusi bayar). Keuntungannya adalah mencegah duplikasi kode di setiap subclass, menjaga konsistensi alur transaksi, serta memastikan validasi dasar selalu dieksekusi sebelum pembayaran dilakukan.

3. HASIL PERCOBAAN 2: KONTRAK NOTIFIKASI DENGAN PROTOCOL
   Percobaan kedua melatih penggunaan Protocol dari modul typing untuk menetapkan kontrak struktural (duck typing) pada kanal notifikasi tanpa memerlukan pewarisan kelas.

   - KODE PROGRAM
     Berkas core/protocols.py:
     <img width="900" height="289" alt="image" src="https://github.com/user-attachments/assets/094fab0d-4a01-4578-b7b4-48f3656bbc73" />

     Berkas core/notifiers.py:
     <img width="900" height="482" alt="image" src="https://github.com/user-attachments/assets/db98596a-7535-4823-a3a8-732eb2906738" />

   - TANGKAPAN LAYAR HASIL EKSEKUSI PERCOBAAN 2
     <img width="899" height="219" alt="image" src="https://github.com/user-attachments/assets/7cca1f50-90d0-406b-9c85-28e4927d9e15" />

   - JAWABAN PERTANYAAN ANALISIS PERCOBAAN 2
     1.	Mengapa EmailNotifier dianggap Notifier padahal tidak mewarisinya?
        Jawaban: 
          Karena Protocol menggunakan konsep structural subtyping (duck typing). Selama sebuah kelas memiliki method kirim(self, penerima, pesan), kelas tersebut secara otomatis dianggap memenuhi kontrak Notifier tanpa harus melakukan pewarisan eksplisit.
     2.	Apa yang terjadi saat @runtime_checkable dihapus? Mengapa Python mewajibkannya untuk isinstance()?
        Jawaban: 
          Jika @runtime_checkable dihapus, eksekusi isinstance(n, Notifier) akan melempar TypeError. Python mewajibkan dekorator tersebut agar pemeriksaan tipe Protocol dapat dilakukan saat runtime menggunakan inspeksi struktur method.
     3.	Jika kirim() pada WhatsAppNotifier diubah menjadi kirim(self), apakah isinstance() tetap bernilai True? Jelaskan.
        Jawaban: 
          Ya, isinstance() tetap mengembalikan nilai True. Hal ini karena pemeriksaan runtime pada @runtime_checkable di Python hanya memeriksa keberadaan nama atribut/method (apakah ada atribut 'kirim'), dan tidak memeriksa kesesuaian jumlah parameter atau jenis argumennya secara menyeluruh saat runtime.


4.	HASIL PERCOBAAN 3: MERANGKAI PAYMENTPROCESSOR
    Percobaan ketiga menyatukan ABC PaymentMethod dan Protocol Notifier ke dalam kelas PaymentProcessor menggunakan prinsip Dependency Injection.

   - Kode Program
     Berkas core/processor.py:
     <img width="900" height="97" alt="image" src="https://github.com/user-attachments/assets/f3941186-ff32-4cc9-849f-b350a5d3f733" />
     <img width="900" height="685" alt="image" src="https://github.com/user-attachments/assets/cd6d8a7f-9482-456e-86be-9ad463cdec7b" />

   - TANKAPAN LAYAR HASIL EKSEKUSI PERCOBAAN 3
     <img width="900" height="111" alt="image" src="https://github.com/user-attachments/assets/1f92369e-1ef3-43cc-853b-a458ab9a9b1a" />

   - Jawaban Pertanyaan Analisis Percobaan 3
      1.	Bagian mana pada checkout() yang membuktikan pemroses tidak bergantung pada metode pembayaran tertentu?
          Jawaban: 
            Pemanggilan metode.proses(jumlah) dalam checkout() hanya mengandalkan abstraksi PaymentMethod. Pemroses tidak perlu tahu apakah metode tersebut TransferBank, EWallet, atau QRIS.
      2.	Pembayaran GoPay Rp150.000 ditolak. Apa penyebabnya, dan di method mana penolakan itu diputuskan?
          Jawaban: 
            Penolakan disebabkan oleh saldo GoPay (Rp100.000) yang tidak mencukupi untuk pembayaran Rp150.000. Penolakan ini diputuskan di method validasi() milik kelas EWallet.
      3.	Mengapa PaymentProcessor cukup meminta Notifier (Protocol) dan bukan sebuah kelas dasar notifikasi (ABC)?
          Jawaban: 
            Karena Notifier hanya memerlukan satu aksi (kirim). Menggunakan Protocol memberikan fleksibilitas tinggi bagi pihak ketiga untuk memasukkan kelas notifikasi milik mereka sendiri tanpa harus memaksa mereka mewarisi kelas abstrak tertentu.


5.	HASIL PERCOBAAN 4: SISTEM PLUGIN DENGAN REGISTRY
    Percobaan keempat mengimplementasikan pola arsitektur plugin menggunakan registry terpusat dan fungsi autodiscovery modul.

    - Kode Program
      Berkas core/registry.py:
      <img width="900" height="432" alt="image" src="https://github.com/user-attachments/assets/9634fe1c-8a86-451b-ab4e-ec89f3767ead" />
      <img width="900" height="218" alt="image" src="https://github.com/user-attachments/assets/d0f5d11a-544b-4569-b1cb-32dd2419465e" />
      
      Berkas plugins/__init__.py:
      <img width="888" height="236" alt="image" src="https://github.com/user-attachments/assets/7b391c2a-e2fb-40d4-b17c-d4232bdc4b2d" />

    - Tangkapan Layar Hasil Eksekusi Percobaan 4
      <img width="888" height="125" alt="image" src="https://github.com/user-attachments/assets/bd45e9f9-ec63-40b4-93c8-01cf302a414a" />

    - Jawaban Pertanyaan Analisis Percobaan 4
      1.	Apa yang terjadi bila dekorator @register_plugin("ewallet") dihapus dari ewallet.py?
          Jawaban: 
            •	Kelas EWallet tidak akan terdaftar ke dalam modul _REGISTRY. 
            •	Ketika aplikasi memanggil buat_metode("ewallet"), program akan melempar KeyError karena kode plugin "ewallet" tidak dikenal.
      2.	Mengapa muat_semua_plugin() perlu dipanggil sebelum buat_metode()?
          Jawaban: 
            Karena dekorator @register_plugin baru akan dieksekusi saat modul file plugin diimpor ke memori. muat_semua_plugin() bertugas mengimpor seluruh berkas di folder plugins/ agar semua dekorator pendaftaran berjalan.
      3.	Jelaskan bagaimana rancangan ini menerapkan prinsip Open/Closed.
          Jawaban: 
            Inti sistem tertutup untuk perubahan (Closed for modification), artinya core/ dan main.py tidak perlu diubah sama sekali ketika menambah metode pembayaran baru. Namun, sistem terbuka untuk perluasan (Open for extension) karena metode pembayaran baru cukup ditambahkan sebagai berkas modul baru di folder plugins/.


6.	HASIL TUGAS MANDIRI

     1. Tugas Mandiri 1: Plugin QRIS
        Implementasi plugin QRIS di plugins/qris.py:
        <img width="877" height="647" alt="image" src="https://github.com/user-attachments/assets/dbef3a53-8742-42a3-9feb-c91ad38eaac9" />
        <img width="877" height="105" alt="image" src="https://github.com/user-attachments/assets/09e3a29e-e3f4-4e7a-8b12-0121422edfed" />


 
     2. Tugas Mandiri 2: TelegramNotifier
        Implementasi TelegramNotifier di core/notifiers.py tanpa pewarisan:
        <img width="888" height="203" alt="image" src="https://github.com/user-attachments/assets/e6e0185d-c749-48e3-b933-3ab9dd57c18d" />
        <img width="888" height="122" alt="image" src="https://github.com/user-attachments/assets/81d36b7b-ed0d-47b5-b323-7d74ff2856e1" />


     3. Tugas Mandiri 3: Biaya Admin sebagai Method Abstrak
        1.	Dampak Penambahan Method Abstrak Sebelum Plugin Diubah:
              Saat method abstrak biaya_admin(self, jumlah: float) -> float ditambahkan pada PaymentMethod, seluruh subclass (TransferBank, EWallet, QRIS) langsung gagal diinstansiasi dengan TypeError. Hal ini membuktikan penegakan kontrak ABC yang sangat ketat.
        2.	Implementasi biaya_admin() pada Setiap Plugin:
              •	TransferBank: Mengembalikan biaya tetap Rp2.500.
              •	EWallet: Mengembalikan 1% dari jumlah transaksi (jumlah * 0.01).
              •	QRIS: Mengembalikan 0,7% dari jumlah transaksi (jumlah * 0.007).
        3. Pembaharuan proses() di core/base.py:
     
     
     4. Tugas Mandiri 4: Analisis Tertulis
          Pada sistem ini, PaymentMethod lebih tepat diimplementasikan sebagai Abstract Base Class (ABC) karena seluruh metode pembayaran berbagi logika urutan eksekusi yang sama via pola Template Method pada method proses(). Selain itu, ABC menegakkan kontrak secara rinci saat runtime instansiasi. Sebaliknya, Notifier lebih cocok sebagai Protocol karenaNotifikasi bersifat heterogen dan berfokus tunggal pada satu aksi yaitu method kirim(). Menggunakan Protocol memungkinkan kelas dari library eksternal langsung digunakan tanpa perlu melakukan inheritance eksplisit.
        PaymentMethod dapat diubah menjadi Protocol apabila seluruh metode pembayaran tidak lagi memerlukan kode bersama (seperti Template Method) dan hanya bertindak sebagai antarmuka murni. Sebaliknya, Notifier lebih cocok menjadi ABC jika semua kanal notifikasi memerlukan atribut bersama, logika percobaan ulang (retry mechanism), atau manajemen koneksi terpusat di kelas induk.
          Risiko utama penggunaan Protocol dengan @runtime_checkable adalah pemeriksaan runtime yang bersifat dangkal: isinstance() hanya mengecek apakah nama atribut/method ada, tanpa memverifikasi jumlah argumen atau tipe data kembaliannya. Untuk mengurangi risiko ini pada proyek, ditambahkan validasi eksplisit saat pemrosesan serta pengetikan tipe data yang ketat (type hinting) yang diverifikasi menggunakan alat analisis statis seperti mypy.


7.	KESIMPULAN
      Berdasarkan seluruh praktikum yang telah dilaksanakan, dapat disimpulkan bahwa:
      1.	Abstract Base Class (ABC) sangat cocok digunakan untuk membangun kerangka kelas yang saling berbagi logika dasar (shared behavior) dan memerlukan penegakan kontrak yang ketat pada saat instansiasi objek.
      2.	Protocol (Structural Subtyping) memberikan fleksibilitas yang sangat tinggi untuk kontrak antarmuka sederhana (seperti Notifier) karena tidak mengharuskan pewarisan hirarki kelas secara ketat.
      3.	Kombinasi antara dekorator registry dan autodiscovery modul mampu menciptakan arsitektur plugin yang mematuhi prinsip Open/Closed secara sempurna, di mana metode pembayaran baru dapat ditambahkan tanpa pernah mengubah kode inti sistem.
