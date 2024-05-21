class Domicilio:
    def __init__(self, address, is_shipping=False):
        self.adress = address
        self.is_shipping = is_shipping
    def __str__(self):
        return f"Dirección: {self.adress}, Es fijo: {self.is_shipping} "