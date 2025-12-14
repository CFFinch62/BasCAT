"""
Tests for Phase 5: Dual-Level Debugging & Visualization

Tests the integration of BASIC compiler with the dual-editor interface.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.compiler.compiler import SimpleBASCATCompiler
from src.core.assembler import Assembler


def test_basic_compilation():
    """Test that BASIC code compiles to assembly successfully"""
    basic_code = """10 REM Test program
20 LET A = 5
30 LET B = 10
40 LET C = A + B
50 PRINT C
60 END
"""

    compiler = SimpleBASCATCompiler()
    result = compiler.compile(basic_code)

    assert result.success, f"Compilation failed: {result.error}"
    assert result.assembly, "No assembly code generated"
    assert result.bytecode, "No bytecode generated"
    assert result.line_map, "No line mapping generated"

    # Check that all BASIC lines are mapped
    assert 10 in result.line_map, "Line 10 not mapped"
    assert 20 in result.line_map, "Line 20 not mapped"
    assert 30 in result.line_map, "Line 30 not mapped"
    assert 40 in result.line_map, "Line 40 not mapped"
    assert 50 in result.line_map, "Line 50 not mapped"
    assert 60 in result.line_map, "Line 60 not mapped"

    print("✓ BASIC compilation test passed")
    print(f"  Generated {len(result.assembly.splitlines())} lines of assembly")
    print(f"  Bytecode size: {len(result.bytecode)} bytes")
    print(f"  Mapped lines: {len(result.line_map)}")


def test_line_mapping():
    """Test that BASIC-to-assembly line mapping is correct"""
    basic_code = """10 LET A = 5
20 PRINT A
30 END
"""

    compiler = SimpleBASCATCompiler()
    result = compiler.compile(basic_code)

    assert result.success, f"Compilation failed: {result.error}"

    # Each BASIC line should map to one or more assembly lines
    for basic_line, asm_lines in result.line_map.items():
        assert isinstance(asm_lines, list), f"Line {basic_line} mapping is not a list"
        assert len(asm_lines) > 0, f"Line {basic_line} has no assembly mappings"

    print("✓ Line mapping test passed")
    for basic_line in sorted(result.line_map.keys()):
        asm_lines = result.line_map[basic_line]
        print(f"  BASIC line {basic_line} → Assembly lines {asm_lines}")


def test_assembly_execution():
    """Test that generated assembly can be assembled and has valid line mapping"""
    basic_code = """10 LET A = 0
20 LET A = A + 1
30 END
"""

    compiler = SimpleBASCATCompiler()
    result = compiler.compile(basic_code)

    assert result.success, f"Compilation failed: {result.error}"

    # Assembly should be valid and assemble-able (already done in compile)
    bytecode, asm_error, asm_line_map = Assembler.assemble(result.assembly)

    assert asm_error is None, f"Assembly error: {asm_error}"
    assert bytecode, "No bytecode generated from assembly"
    assert asm_line_map, "No line map from assembler"

    print("✓ Assembly execution test passed")
    print(f"  Bytecode: {len(bytecode)} bytes")
    print(f"  Assembly line map: {len(asm_line_map)} entries")


def test_for_loop_compilation():
    """Test FOR loop compilation"""
    basic_code = """10 FOR I = 0 TO 5
20   PRINT I
30 NEXT I
40 END
"""

    compiler = SimpleBASCATCompiler()
    result = compiler.compile(basic_code)

    assert result.success, f"Compilation failed: {result.error}"
    assert "loop" in result.assembly.lower(), "FOR loop label not found in assembly"
    assert "jnz" in result.assembly.lower() or "jz" in result.assembly.lower(), "Loop jump not found"

    print("✓ FOR loop compilation test passed")


def test_conditional_compilation():
    """Test IF statement compilation"""
    basic_code = """10 INPUT A
20 IF A > 50 THEN GOTO 50
30 PRINT 0
40 GOTO 60
50 PRINT 1
60 END
"""

    compiler = SimpleBASCATCompiler()
    result = compiler.compile(basic_code)

    assert result.success, f"Compilation failed: {result.error}"
    assert "cmp" in result.assembly.lower(), "CMP instruction not found"
    assert "l50" in result.assembly.lower(), "GOTO label L50 not found"

    print("✓ Conditional compilation test passed")


def run_all_tests():
    """Run all Phase 5 integration tests"""
    print("\n" + "="*60)
    print("Phase 5 Integration Tests")
    print("="*60 + "\n")

    tests = [
        test_basic_compilation,
        test_line_mapping,
        test_assembly_execution,
        test_for_loop_compilation,
        test_conditional_compilation,
    ]

    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            return False
        except Exception as e:
            print(f"✗ {test.__name__} ERROR: {e}")
            import traceback
            traceback.print_exc()
            return False

    print("\n" + "="*60)
    print("All Phase 5 integration tests passed! ✅")
    print("="*60 + "\n")
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
