from unicodedata import name

#classe de peças e computador 
class Pecas_de_Pc:
    def __init__(self, CPU, GPU, mem_ram, placa_mae, fonte):
        self.CPU = CPU
        self.GPU = GPU
        self.mem_ram = mem_ram
        self.placa_mae = placa_mae
        self.fonte = fonte
    
config_pc = input("Coloque as configs do teu pc: ")

print(config_pc)
    