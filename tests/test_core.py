import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.memory import Memory
from src.core.cpu import CPU
from src.core.alu import ALU
from src.core.signals import signals

def test_memory_read_write():
    mem = Memory()
    mem.write(0x00, 0xAB)
    assert mem.read(0x00) == 0xAB
    
def test_alu_add():
    alu = ALU()
    res = alu.operate("ADD", 10, 20)
    assert res == 30
    assert alu.flags["Z"] == 0

def test_cpu_fetch():
    mem = Memory()
    cpu = CPU(mem)
    
    # Load instruction 0x12 into address 0x00
    mem.write(0x00, 0x12)
    
    # Reset CPU (PC=0)
    cpu.reset()
    
    # Fetch
    opcode = cpu.fetch()
    
    assert opcode == 0x12
    assert cpu.PC == 1

if __name__ == "__main__":
    try:
        test_memory_read_write()
        test_alu_add()
        test_cpu_fetch()
        print("All core tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
