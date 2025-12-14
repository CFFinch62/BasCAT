"""
Parser for SimpleBASCAT Language

Builds Abstract Syntax Tree (AST) from tokens.
"""

from typing import List, Optional
from src.compiler.lexer import Token, TokenType
from src.compiler.ast_nodes import *


class Parser:
    """
    Recursive descent parser for SimpleBASCAT.
    Converts token stream into AST.
    """

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_line_number = 0

    def current_token(self) -> Token:
        """Get current token"""
        if self.pos >= len(self.tokens):
            return self.tokens[-1]  # Return EOF
        return self.tokens[self.pos]

    def peek_token(self, offset=1) -> Token:
        """Look ahead at token"""
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[pos]

    def advance(self):
        """Move to next token"""
        if self.pos < len(self.tokens) - 1:
            self.pos += 1

    def expect(self, token_type: TokenType) -> Token:
        """Consume token of expected type, or raise error"""
        token = self.current_token()
        if token.type != token_type:
            raise SyntaxError(
                f"Expected {token_type.name}, got {token.type.name} "
                f"at line {token.line}:{token.column}"
            )
        self.advance()
        return token

    def skip_newlines(self):
        """Skip any newline tokens"""
        while self.current_token().type == TokenType.NEWLINE:
            self.advance()

    def parse(self) -> Program:
        """Parse entire program"""
        statements = []

        self.skip_newlines()

        while self.current_token().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()

        return Program(statements)

    def parse_statement(self) -> Optional[ASTNode]:
        """Parse a single statement (line number + command)"""
        # Expect line number
        line_token = self.expect(TokenType.NUMBER)
        self.current_line_number = line_token.value

        # Parse command
        token = self.current_token()

        if token.type == TokenType.LET:
            return self.parse_let()
        elif token.type == TokenType.PRINT:
            return self.parse_print()
        elif token.type == TokenType.INPUT:
            return self.parse_input()
        elif token.type == TokenType.IF:
            return self.parse_if()
        elif token.type == TokenType.GOTO:
            return self.parse_goto()
        elif token.type == TokenType.FOR:
            return self.parse_for()
        elif token.type == TokenType.NEXT:
            return self.parse_next()
        elif token.type == TokenType.REM:
            return self.parse_rem()
        elif token.type == TokenType.END:
            return self.parse_end()
        else:
            raise SyntaxError(
                f"Unexpected token {token.type.name} at line {token.line}:{token.column}"
            )

    def parse_let(self) -> LetStatement:
        """Parse LET statement: LET A = expression"""
        self.expect(TokenType.LET)

        var_token = self.expect(TokenType.VARIABLE)
        variable = var_token.value

        self.expect(TokenType.EQ)

        expression = self.parse_expression()

        stmt = LetStatement(self.current_line_number, variable, expression)
        return stmt

    def parse_print(self) -> PrintStatement:
        """Parse PRINT statement: PRINT expression"""
        self.expect(TokenType.PRINT)
        expression = self.parse_expression()
        return PrintStatement(self.current_line_number, expression)

    def parse_input(self) -> InputStatement:
        """Parse INPUT statement: INPUT variable"""
        self.expect(TokenType.INPUT)
        var_token = self.expect(TokenType.VARIABLE)
        return InputStatement(self.current_line_number, var_token.value)

    def parse_if(self) -> IfStatement:
        """Parse IF statement: IF condition THEN GOTO line"""
        self.expect(TokenType.IF)

        condition = self.parse_comparison()

        self.expect(TokenType.THEN)
        self.expect(TokenType.GOTO)

        target_token = self.expect(TokenType.NUMBER)

        return IfStatement(self.current_line_number, condition, target_token.value)

    def parse_goto(self) -> GotoStatement:
        """Parse GOTO statement: GOTO line"""
        self.expect(TokenType.GOTO)
        target_token = self.expect(TokenType.NUMBER)
        return GotoStatement(self.current_line_number, target_token.value)

    def parse_for(self) -> ForStatement:
        """Parse FOR statement: FOR I = start TO end"""
        self.expect(TokenType.FOR)

        var_token = self.expect(TokenType.VARIABLE)
        variable = var_token.value

        self.expect(TokenType.EQ)

        start_expr = self.parse_expression()

        self.expect(TokenType.TO)

        end_expr = self.parse_expression()

        return ForStatement(self.current_line_number, variable, start_expr, end_expr)

    def parse_next(self) -> NextStatement:
        """Parse NEXT statement: NEXT variable"""
        self.expect(TokenType.NEXT)
        var_token = self.expect(TokenType.VARIABLE)
        return NextStatement(self.current_line_number, var_token.value)

    def parse_rem(self) -> RemStatement:
        """Parse REM statement: REM comment"""
        rem_token = self.expect(TokenType.REM)
        return RemStatement(self.current_line_number, rem_token.value)

    def parse_end(self) -> EndStatement:
        """Parse END statement"""
        self.expect(TokenType.END)
        return EndStatement(self.current_line_number)

    def parse_comparison(self) -> Comparison:
        """Parse comparison: expression op expression"""
        left = self.parse_expression()

        token = self.current_token()

        # Comparison operators
        if token.type in (TokenType.EQ, TokenType.NEQ, TokenType.LT,
                         TokenType.GT, TokenType.LTE, TokenType.GTE):
            op_token = token
            self.advance()
            right = self.parse_expression()

            op_map = {
                TokenType.EQ: '=',
                TokenType.NEQ: '<>',
                TokenType.LT: '<',
                TokenType.GT: '>',
                TokenType.LTE: '<=',
                TokenType.GTE: '>=',
            }

            return Comparison(self.current_line_number, op_map[op_token.type], left, right)
        else:
            raise SyntaxError(
                f"Expected comparison operator, got {token.type.name} "
                f"at line {token.line}:{token.column}"
            )

    def parse_expression(self) -> ASTNode:
        """
        Parse expression with operators.
        Simple left-to-right evaluation (no precedence).
        expression = term { (+ | - | AND | OR | XOR) term }
        """
        left = self.parse_term()

        while self.current_token().type in (TokenType.PLUS, TokenType.MINUS,
                                            TokenType.AND, TokenType.OR, TokenType.XOR):
            op_token = self.current_token()
            self.advance()
            right = self.parse_term()

            op_map = {
                TokenType.PLUS: '+',
                TokenType.MINUS: '-',
                TokenType.AND: 'AND',
                TokenType.OR: 'OR',
                TokenType.XOR: 'XOR',
            }

            left = BinaryOp(self.current_line_number, op_map[op_token.type], left, right)

        return left

    def parse_term(self) -> ASTNode:
        """
        Parse term (handles NOT and parentheses).
        term = NOT factor | factor
        """
        token = self.current_token()

        # Unary NOT
        if token.type == TokenType.NOT:
            self.advance()
            operand = self.parse_factor()
            return UnaryOp(self.current_line_number, 'NOT', operand)

        return self.parse_factor()

    def parse_factor(self) -> ASTNode:
        """
        Parse factor (atomic expression).
        factor = number | variable | (expression)
        """
        token = self.current_token()

        # Number literal
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberLiteral(self.current_line_number, token.value)

        # Variable
        elif token.type == TokenType.VARIABLE:
            self.advance()
            return Variable(self.current_line_number, token.value)

        # Parenthesized expression
        elif token.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr

        else:
            raise SyntaxError(
                f"Expected number, variable, or '(', got {token.type.name} "
                f"at line {token.line}:{token.column}"
            )


# Example usage and testing
if __name__ == "__main__":
    from src.compiler.lexer import Lexer

    source = """10 REM Test program
20 LET A = 5
30 LET B = 10
40 LET C = A + B
50 IF C > 10 THEN GOTO 80
60 PRINT 0
70 GOTO 90
80 PRINT C
90 END
"""

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    print("AST:")
    print_ast(ast)
