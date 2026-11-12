from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id

@register_plugin("ewallet")
class EWallet(PaymentMethod):
    def __init__(self, saldo: float = 0, penyedia: str = "GoPay"):
        super().__init__(f"E-Wallet {penyedia}")
        self.saldo = saldo

    def validasi(self, jumlah: float) -> bool:
        return self.saldo >= jumlah

    def bayar(self, jumlah: float) -> str:
        biaya = self.biaya_admin(jumlah)
        self.saldo -= (jumlah + biaya)
        return buat_id("EWL")

    def biaya_admin(self, jumlah: float) -> float:
        return jumlah * 0.01