from abc import ABC, abstractmethod
from core.utils import rupiah

class PembayaranGagal(Exception):
    """Dilempar saat pembayaran ditolak atau tidak valid."""
    pass

class PaymentMethod(ABC):
    """Kontrak (abstract base class) untuk semua metode pembayaran."""

    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def validasi(self, jumlah: float) -> bool:
        pass

    @abstractmethod
    def bayar(self, jumlah: float) -> str:
        pass

    @abstractmethod
    def biaya_admin(self, jumlah: float) -> float:
        """Menghitung biaya admin berdasarkan nominal pembayaran."""
        pass

    def proses(self, jumlah: float) -> str:
        if jumlah <= 0:
            raise PembayaranGagal("Jumlah pembayaran harus lebih dari 0")
        
        biaya = self.biaya_admin(jumlah)
        total = jumlah + biaya

        if not self.validasi(total):
            raise PembayaranGagal(
                f"{self.nama} menolak total pembayaran {rupiah(total)} (termasuk biaya admin {rupiah(biaya)})"
            )
            
        return self.bayar(jumlah)