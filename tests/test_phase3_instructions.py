import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.memory import Memory
from src.core.cpu import CPU
from src.core.assembler import Assembler
from src.core.signals import signals

def test_logic_and():
    """Test AND instruction"""
    mem = Memory()
    cpu = CPU(mem)

    # Load A with 0xF0 and AND with 0x0F
    code = """
    LOAD A, 0xF0
    AND A, 0x0F
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    # Load bytecode into memory
    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    # Execute LOAD A, 0xF0
    cpu.execute_instruction()
    assert cpu.registers["A"] == 0xF0

    # Execute AND A, 0x0F
    cpu.execute_instruction()
    assert cpu.registers["A"] == 0x00  # 0xF0 & 0x0F = 0x00
    assert cpu.alu.flags["Z"] == 1  # Zero flag should be set

def test_logic_or():
    """Test OR instruction"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    LOAD A, 0xF0
    OR A, 0x0F
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # LOAD
    cpu.execute_instruction()  # OR

    assert cpu.registers["A"] == 0xFF  # 0xF0 | 0x0F = 0xFF

def test_logic_xor():
    """Test XOR instruction"""
    mem = Memory()
    cpu = CPU(mem)

    # Use values that fit in 7-bit immediate mode (0-127)
    code = """
    LOAD A, 0x5A
    XOR A, 0x5A
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # LOAD
    cpu.execute_instruction()  # XOR

    assert cpu.registers["A"] == 0x00  # 0x5A ^ 0x5A = 0x00
    assert cpu.alu.flags["Z"] == 1

def test_logic_not():
    """Test NOT instruction"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    LOAD A, 0xF0
    NOT A
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # LOAD
    cpu.execute_instruction()  # NOT

    assert cpu.registers["A"] == 0x0F  # NOT 0xF0 = 0x0F

def test_cmp_instruction():
    """Test CMP instruction sets flags correctly"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    LOAD A, 10
    CMP A, 10
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # LOAD
    cpu.execute_instruction()  # CMP

    assert cpu.registers["A"] == 10  # CMP doesn't modify register
    assert cpu.alu.flags["Z"] == 1  # 10 - 10 = 0, Zero flag set

def test_conditional_jz():
    """Test JZ (Jump if Zero) instruction"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    LOAD A, 0
    CMP A, 0
    JZ 9
    LOAD B, 99
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # LOAD A, 0
    cpu.execute_instruction()  # CMP A, 0 (sets Z flag)
    cpu.execute_instruction()  # JZ 9 (should jump)

    assert cpu.PC == 9  # Should have jumped
    assert cpu.registers["B"] == 0  # B should not be loaded

def test_conditional_jnz():
    """Test JNZ (Jump if Not Zero) instruction"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    LOAD A, 5
    CMP A, 10
    JNZ 9
    LOAD B, 99
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # LOAD A, 5
    cpu.execute_instruction()  # CMP A, 10 (clears Z flag)
    cpu.execute_instruction()  # JNZ 9 (should jump)

    assert cpu.PC == 9  # Should have jumped

def test_stack_push_pop():
    """Test PUSH and POP instructions"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    LOAD A, 42
    PUSH A
    LOAD A, 0
    POP A
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    initial_sp = cpu.SP

    cpu.execute_instruction()  # LOAD A, 42
    assert cpu.registers["A"] == 42

    cpu.execute_instruction()  # PUSH A
    assert cpu.SP == (initial_sp - 1) & 0xFF  # SP decremented
    assert mem.read(initial_sp) == 42  # Value on stack

    cpu.execute_instruction()  # LOAD A, 0
    assert cpu.registers["A"] == 0

    cpu.execute_instruction()  # POP A
    assert cpu.registers["A"] == 42  # Got value back
    assert cpu.SP == initial_sp  # SP back to original

def test_memory_ldm_stm():
    """Test LDM and STM instructions"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    LOAD A, 123
    STM 50, A
    LOAD A, 0
    LDM A, 50
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # LOAD A, 123
    cpu.execute_instruction()  # STM 50, A

    assert mem.read(50) == 123  # Value stored in memory

    cpu.execute_instruction()  # LOAD A, 0
    assert cpu.registers["A"] == 0

    cpu.execute_instruction()  # LDM A, 50
    assert cpu.registers["A"] == 123  # Value loaded from memory

def test_mov_register_to_register():
    """Test MOV instruction with register source"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    LOAD A, 88
    MOV B, A
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # LOAD A, 88
    cpu.execute_instruction()  # MOV B, A

    assert cpu.registers["B"] == 88  # B should equal A

def test_mov_immediate():
    """Test MOV instruction with immediate value"""
    mem = Memory()
    cpu = CPU(mem)

    code = """
    MOV A, 55
    HALT
    """
    bytecode, error, _ = Assembler.assemble(code)
    assert error is None

    for i, byte in enumerate(bytecode):
        mem.write(i, byte)

    cpu.reset()
    cpu.execute_instruction()  # MOV A, 55

    assert cpu.registers["A"] == 55

if __name__ == "__main__":
    try:
        test_logic_and()
        test_logic_or()
        test_logic_xor()
        test_logic_not()
        test_cmp_instruction()
        test_conditional_jz()
        test_conditional_jnz()
        test_stack_push_pop()
        test_memory_ldm_stm()
        test_mov_register_to_register()
        test_mov_immediate()
        print("All Phase 3 instruction tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
