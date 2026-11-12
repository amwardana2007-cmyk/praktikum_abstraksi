from core.protocols import Notifier
from core.notifiers import ConsoleNotifier, EmailNotifier, WhatsAppNotifier

c = ConsoleNotifier()
e = EmailNotifier()
w = WhatsAppNotifier()

# Memeriksa apakah kelas-kelas tersebut memenuhi Protocol Notifier saat runtime
print("Apakah ConsoleNotifier adalah Notifier?", isinstance(c, Notifier))
print("Apakah EmailNotifier adalah Notifier?", isinstance(e, Notifier))
print("Apakah WhatsAppNotifier adalah Notifier?", isinstance(w, Notifier))

# Menguji fungsi kirim
c.kirim("andi@utr.ac.id", "Pembayaran Rp250.000 via Transfer BCA berhasil. ID: TRF-8284371E")
e.kirim("andi@utr.ac.id", "Pembayaran Rp300.000 via E-Wallet DANA berhasil. ID: EWL-A8F83B16")