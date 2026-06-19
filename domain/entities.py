class Currency:
    def __init__(self, code, name, symbol):
        self.code = code
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return f"{self.name} ({self.code})"
    
    def __image__(self):
        return f"{self.code}.png"