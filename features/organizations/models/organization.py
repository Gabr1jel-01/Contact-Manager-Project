


class Organization:
    def __init__(self, name: str, vat_id:str) -> None:
        self.name = name
        self.vat_id = vat_id
    def __str__(self) -> str:
        return f'{self.name} {self.vat_id}'
        

