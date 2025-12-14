"""
Abstract Syntax Tree (AST) Node Definitions

Represents the structure of SimpleBASCAT programs.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ASTNode:
    """Base class for all AST nodes"""
    line_number: int


@dataclass
class Program(ASTNode):
    """Root node - represents entire program"""
    statements: List[ASTNode]

    def __init__(self, statements: List[ASTNode]):
        super().__init__(0)  # Program has no line number
        self.statements = statements


# Expressions

@dataclass
class NumberLiteral(ASTNode):
    """Numeric literal (0-255)"""
    value: int


@dataclass
class Variable(ASTNode):
    """Variable reference (A-Z)"""
    name: str


@dataclass
class BinaryOp(ASTNode):
    """Binary operation (A + B, A AND B, etc.)"""
    op: str  # '+', '-', 'AND', 'OR', 'XOR'
    left: ASTNode
    right: ASTNode


@dataclass
class UnaryOp(ASTNode):
    """Unary operation (NOT A)"""
    op: str  # 'NOT', '-'
    operand: ASTNode


@dataclass
class Comparison(ASTNode):
    """Comparison expression (A = 5, B > 10)"""
    op: str  # '=', '<>', '<', '>', '<=', '>='
    left: ASTNode
    right: ASTNode


# Statements

@dataclass
class LetStatement(ASTNode):
    """LET A = expression"""
    variable: str
    expression: ASTNode


@dataclass
class PrintStatement(ASTNode):
    """PRINT expression"""
    expression: ASTNode


@dataclass
class InputStatement(ASTNode):
    """INPUT variable"""
    variable: str


@dataclass
class IfStatement(ASTNode):
    """IF condition THEN GOTO line"""
    condition: Comparison
    target_line: int


@dataclass
class GotoStatement(ASTNode):
    """GOTO line"""
    target_line: int


@dataclass
class ForStatement(ASTNode):
    """FOR variable = start TO end"""
    variable: str
    start_expr: ASTNode
    end_expr: ASTNode


@dataclass
class NextStatement(ASTNode):
    """NEXT variable"""
    variable: str


@dataclass
class RemStatement(ASTNode):
    """REM comment"""
    comment: str


@dataclass
class EndStatement(ASTNode):
    """END"""
    pass


# Helper function to print AST
def print_ast(node: ASTNode, indent=0):
    """Pretty-print AST for debugging"""
    prefix = "  " * indent
    if isinstance(node, Program):
        print(f"{prefix}Program:")
        for stmt in node.statements:
            print_ast(stmt, indent + 1)
    elif isinstance(node, LetStatement):
        print(f"{prefix}LET {node.variable} = ")
        print_ast(node.expression, indent + 1)
    elif isinstance(node, PrintStatement):
        print(f"{prefix}PRINT:")
        print_ast(node.expression, indent + 1)
    elif isinstance(node, InputStatement):
        print(f"{prefix}INPUT {node.variable}")
    elif isinstance(node, IfStatement):
        print(f"{prefix}IF ... THEN GOTO {node.target_line}")
        print_ast(node.condition, indent + 1)
    elif isinstance(node, GotoStatement):
        print(f"{prefix}GOTO {node.target_line}")
    elif isinstance(node, ForStatement):
        print(f"{prefix}FOR {node.variable} = ... TO ...")
        print_ast(node.start_expr, indent + 1)
        print_ast(node.end_expr, indent + 1)
    elif isinstance(node, NextStatement):
        print(f"{prefix}NEXT {node.variable}")
    elif isinstance(node, RemStatement):
        print(f"{prefix}REM {node.comment}")
    elif isinstance(node, EndStatement):
        print(f"{prefix}END")
    elif isinstance(node, BinaryOp):
        print(f"{prefix}BinaryOp({node.op})")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
    elif isinstance(node, UnaryOp):
        print(f"{prefix}UnaryOp({node.op})")
        print_ast(node.operand, indent + 1)
    elif isinstance(node, Comparison):
        print(f"{prefix}Comparison({node.op})")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
    elif isinstance(node, NumberLiteral):
        print(f"{prefix}Number({node.value})")
    elif isinstance(node, Variable):
        print(f"{prefix}Variable({node.name})")
    else:
        print(f"{prefix}{node}")
