from core.processor import PaymentProcessor
from core.notifiers import ConsoleNotifier
from plugins.transfer_bank import TransferBank
from plugins.ewallet import EWallet

email = "andi@utr.ac.id"
processor = PaymentProcessor(notifier=ConsoleNotifier())

# 1. Transaksi Berhasil
bca = TransferBank(saldo=500_000, bank="BCA")
processor.checkout(bca, 250_000, email)

# 2. Transaksi Gagal (Saldo E-Wallet tidak cukup)
gopay = EWallet(saldo=100_000, penyedia="GoPay")
processor.checkout(gopay, 150_000, email)