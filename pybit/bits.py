class Bits:
    def __init__(self, size: int) -> None:
        self.bits = [0 for i in range(size)]
    
    def __getitem__(self, key: int) -> int:
        return self.bits[key]
    
    def __setitem__(self, key: int, val: int) -> int:
        self.bits[key] = val
    
    def __len__(self) -> int:
        return len(self.bits)
    
    
