from core.base import PaymentMethod
from plugins.transfer_bank import TransferBank

# Uji instansiasi langsung PaymentMethod (akan gagal dan memunculkan TypeError)
try:
    p = PaymentMethod("Uji")
except TypeError as e:
    print(f"Error berhasil ditangkap: {e}")

# Uji instansiasi kelas turunan yang valid
bca = TransferBank(saldo=500_000, bank="BCA")
print(f"Berhasil membuat metode: {bca.nama}")
print(f"Validasi saldo cukup: {bca.validasi(250_000)}")