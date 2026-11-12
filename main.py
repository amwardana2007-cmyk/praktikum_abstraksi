from core.processor import PaymentProcessor
from core.notifiers import ConsoleNotifier, EmailNotifier, TelegramNotifier
from core.protocols import Notifier
from core.registry import buat_metode
from plugins import muat_semua_plugin

def main():
    # Load semua modul plugin secara otomatis
    muat_semua_plugin()

    print("=== PENGUJIAN PROTOCOL NOTIFIER ===")
    tg_notifier = TelegramNotifier()
    print("Apakah TelegramNotifier memenuhi Protocol Notifier?", isinstance(tg_notifier, Notifier))

    processor = PaymentProcessor(notifier=ConsoleNotifier())
    processor_tg = PaymentProcessor(notifier=tg_notifier)

    print("\n=== EKSEKUSI TRANSAKSI PEMBAYARAN ===")
    email = "andi@utr.ac.id"
    
    # Memuat instance plugin dari registry
    bca = buat_metode("transfer_bank", saldo=1_000_000, bank="BCA")
    gopay = buat_metode("ewallet", saldo=100_000, penyedia="GoPay")
    dana = buat_metode("ewallet", saldo=500_000, penyedia="DANA")
    qris_kantin = buat_metode("qris", merchant="Kantin Utama")

    # 1. Transfer Bank Berhasil
    processor.checkout(bca, 250_000, email)

    # 2. E-Wallet Gagal (Saldo tidak mencukupi setelah ditambah biaya admin)
    processor.checkout(gopay, 150_000, email)

    # 3. E-Wallet Berhasil via Telegram Notifier
    processor_tg.checkout(dana, 300_000, "@andi_telegram")

    # 4. QRIS Berhasil
    processor.checkout(qris_kantin, 50_000, "budi@utr.ac.id")

    # 5. Uji Coba validasi Notifier (Memicu TypeError jika bukan Notifier)
    try:
        PaymentProcessor(notifier="bukan notifier")
    except TypeError as e:
        print("\nError (Berhasil ditangkap):", e)

if __name__ == "__main__":
    main()