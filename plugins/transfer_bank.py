from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id

@register_plugin("transfer_bank")
class TransferBank(PaymentMethod):
    def __init__(self, saldo: float = 0, bank: str = "BCA"):
        super().__init__(f"Transfer {bank}")
        self.saldo = saldo

    def validasi(self, jumlah: float) -> bool:
        return self.saldo >= jumlah

    def bayar(self, jumlah: float) -> str:
        biaya = self.biaya_admin(jumlah)
        self.saldo -= (jumlah + biaya)
        return buat_id("TRF")

    def biaya_admin(self, jumlah: float) -> float:
        return 2500.0