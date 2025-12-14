"""
Lexer for SimpleBASCAT Language

Tokenizes BASIC source code into a stream of tokens.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional


class TokenType(Enum):
    """Token types for SimpleBASCAT"""
    # Literals
    NUMBER = auto()
    VARIABLE = auto()

    # Keywords
    LET = auto()
    PRINT = auto()
    INPUT = auto()
    IF = auto()
    THEN = auto()
    GOTO = auto()
    FOR = auto()
    TO = auto()
    NEXT = auto()
    REM = auto()
    END = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    MULT = auto()
    DIV = auto()
    AND = auto()
    OR = auto()
    XOR = auto()
    NOT = auto()

    # Comparisons
    EQ = auto()
    NEQ = auto()
    LT = auto()
    GT = auto()
    LTE = auto()
    GTE = auto()

    # Structure
    LPAREN = auto()
    RPAREN = auto()
    NEWLINE = auto()
    EOF = auto()


@dataclass
class Token:
    """Represents a single token"""
    type: TokenType
    value: any
    line: int
    column: int

    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r}, {self.line}:{self.column})"


class Lexer:
    """
    Lexical analyzer for SimpleBASCAT.
    Converts source text into tokens.
    """

    KEYWORDS = {
        'LET': TokenType.LET,
        'PRINT': TokenType.PRINT,
        'INPUT': TokenType.INPUT,
        'IF': TokenType.IF,
        'THEN': TokenType.THEN,
        'GOTO': TokenType.GOTO,
        'FOR': TokenType.FOR,
        'TO': TokenType.TO,
        'NEXT': TokenType.NEXT,
        'REM': TokenType.REM,
        'END': TokenType.END,
        'AND': TokenType.AND,
        'OR': TokenType.OR,
        'XOR': TokenType.XOR,
        'NOT': TokenType.NOT,
    }

    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []

    def current_char(self) -> Optional[str]:
        """Get current character without advancing"""
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]

    def peek_char(self, offset=1) -> Optional[str]:
        """Peek ahead at character"""
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]

    def advance(self):
        """Move to next character"""
        if self.pos < len(self.source):
            if self.source[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1

    def skip_whitespace(self):
        """Skip spaces and tabs (but not newlines)"""
        while self.current_char() in (' ', '\t'):
            self.advance()

    def read_number(self) -> int:
        """Read a number literal"""
        start_col = self.column
        num_str = ''
        while self.current_char() and self.current_char().isdigit():
            num_str += self.current_char()
            self.advance()
        return int(num_str)

    def read_identifier(self) -> str:
        """Read an identifier or keyword"""
        ident = ''
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            ident += self.current_char()
            self.advance()
        return ident.upper()

    def read_comment(self) -> str:
        """Read a REM comment (rest of line)"""
        comment = ''
        while self.current_char() and self.current_char() != '\n':
            comment += self.current_char()
            self.advance()
        return comment.strip()

    def tokenize(self) -> List[Token]:
        """Convert source code into list of tokens"""
        self.tokens = []

        while self.pos < len(self.source):
            self.skip_whitespace()

            ch = self.current_char()
            if ch is None:
                break

            # Newline
            if ch == '\n':
                self.tokens.append(Token(TokenType.NEWLINE, '\\n', self.line, self.column))
                self.advance()
                continue

            # Numbers
            if ch.isdigit():
                start_col = self.column
                num = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, num, self.line, start_col))
                continue

            # Identifiers and keywords
            if ch.isalpha():
                start_col = self.column
                ident = self.read_identifier()

                # Check if it's a keyword
                if ident in self.KEYWORDS:
                    token_type = self.KEYWORDS[ident]

                    # Special handling for REM - read rest of line
                    if token_type == TokenType.REM:
                        comment = self.read_comment()
                        self.tokens.append(Token(TokenType.REM, comment, self.line, start_col))
                    else:
                        self.tokens.append(Token(token_type, ident, self.line, start_col))

                # Single letter = variable
                elif len(ident) == 1 and ident.isalpha():
                    self.tokens.append(Token(TokenType.VARIABLE, ident, self.line, start_col))

                else:
                    raise SyntaxError(f"Invalid identifier '{ident}' at {self.line}:{start_col}")

                continue

            # Operators and punctuation
            start_col = self.column

            if ch == '+':
                self.tokens.append(Token(TokenType.PLUS, '+', self.line, start_col))
                self.advance()

            elif ch == '-':
                self.tokens.append(Token(TokenType.MINUS, '-', self.line, start_col))
                self.advance()

            elif ch == '*':
                self.tokens.append(Token(TokenType.MULT, '*', self.line, start_col))
                self.advance()

            elif ch == '/':
                self.tokens.append(Token(TokenType.DIV, '/', self.line, start_col))
                self.advance()

            elif ch == '(':
                self.tokens.append(Token(TokenType.LPAREN, '(', self.line, start_col))
                self.advance()

            elif ch == ')':
                self.tokens.append(Token(TokenType.RPAREN, ')', self.line, start_col))
                self.advance()

            elif ch == '=':
                self.tokens.append(Token(TokenType.EQ, '=', self.line, start_col))
                self.advance()

            elif ch == '<':
                self.advance()
                if self.current_char() == '>':
                    self.tokens.append(Token(TokenType.NEQ, '<>', self.line, start_col))
                    self.advance()
                elif self.current_char() == '=':
                    self.tokens.append(Token(TokenType.LTE, '<=', self.line, start_col))
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.LT, '<', self.line, start_col))

            elif ch == '>':
                self.advance()
                if self.current_char() == '=':
                    self.tokens.append(Token(TokenType.GTE, '>=', self.line, start_col))
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.GT, '>', self.line, start_col))

            else:
                raise SyntaxError(f"Unexpected character '{ch}' at {self.line}:{start_col}")

        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens


# Example usage and testing
if __name__ == "__main__":
    # Test program
    source = """10 REM Simple test program
20 LET A = 5
30 LET B = 10
40 LET C = A + B
50 PRINT C
60 END
"""

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)
