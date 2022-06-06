# Dammit they're going to make me build a compiler aren't they

# https://ruslanspivak.com/lsbasi-part7/

class Lexer:
    line = ''
    tokens = []
    index = 0

    def __init__(self, line):
        self.line = line.strip()
        self.tokens = []
        for char in self.line:
            if char.isdecimal(): # Assuming single digit numbers
                self.tokens.append(int(char))
            elif char == '(':
                self.tokens.append(char)
            elif char == ')':
                self.tokens.append(char)
            elif char == '+':
                self.tokens.append(char)
            elif char == '*':
                self.tokens.append(char)

    def next_token(self):
        if (self.index < len(self.tokens)):
            token = self.tokens[self.index]
            self.index += 1
            return token


class NumNode:
    def __init__(self, input):
        if type(input) == int:
            self.value = input
        else:
            raise Exception('Non-number value node created')

    def evaluate(self):
        return self.value

class OpNode:
    def __init__(self, input, child1, child2):
        if input in ['+', '*']:
            self.op_type = input
            self.child1 = child1
            self.child2 = child2
        else:
            raise Exception('Invalid operator node created')

    def evaluate(self):
        if self.op_type == '+':
            return self.child1.evaluate() + self.child2.evaluate()
        elif self.op_type == '*':
            return self.child1.evaluate() * self.child2.evaluate()


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()

    def consume(self, token):
        if self.current_token == token:
            self.current_token = self.lexer.next_token()
        else:
            raise Exception(f'Syntax error: expected {token}, got {self.current_token}')

    def term(self):
        # term : INTEGER | LPAREN expr RPAREN
        token = self.current_token
        if type(token) == int:
            self.consume(token)
            return NumNode(token)
        elif token == '(':
            self.consume('(')
            node = self.expr()
            self.consume(')')
            return node

    def sum(self):
        # sum : term (PLUS term)*
        node = self.term()
        while self.current_token == '+':
            token = self.current_token
            self.consume('+')
            node = OpNode(token, node, self.term())
        return node

    def expr(self):
        # expr : sum (MUL sum)*
        node = self.sum()
        while self.current_token == '*':
            token = self.current_token
            self.consume('*')
            node = OpNode(token, node, self.sum())
        return node

    def build_tree(self):
        return self.expr()


def evaluate(line):
    lexer = Lexer(line)
    parser = Parser(lexer)
    tree = parser.build_tree()
    result = tree.evaluate()
    print(f'Result: {result}')
    return result


f = open('input.txt')
lines = f.readlines()
f.close()


answers = [evaluate(line) for line in lines]
print(f'Sum: {sum(answers)}')
