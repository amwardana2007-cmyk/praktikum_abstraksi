from core.processor import PaymentProcessor
from core.notifiers import ConsoleNotifier
from core.registry import buat_metode, daftar_plugin
from plugins import muat_semua_plugin

# Memuat semua plugin secara otomatis
muat_semua_plugin()

print("Daftar plugin yang terdaftar:", daftar_plugin())

processor = PaymentProcessor(notifier=ConsoleNotifier())
email = "andi@utr.ac.id"

# Membuat instance plugin langsung dari registry berdasarkan kodenya
qris_kantin = buat_metode("qris", merchant="Kantin Utama")
processor.checkout(qris_kantin, 50_000, email)