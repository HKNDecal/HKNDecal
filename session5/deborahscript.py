from __future__ import print_function

# DeborahScript has no functions because Deborah doesn't function
# DeborahScript has conditionals
# Variables in DeborahScript are defined carefully, same
# DeborahScript doesn't have class

# Deborah Types: Str, Int, LookupTables

# Loops are defined with drink (condition) coffee

# Cats Everywhere
import ast
from textx import metamodel


class DeborahException(BaseException):
    pass


class Program(ast.AST):
    _fields = ['lines']


class Loop(ast.AST):
    _fields = ['cond', 'stmts']


class Assignment(ast.AST):
    _fields = ['lhs', 'rhs']


class Declaration(ast.AST):
    _fields = ['defn']


class Print(ast.AST):
    _fields = ['exp']


class Expression(ast.AST):
    _fields = ['val']


class BinaryExpression(ast.AST):
    _fields = ['lhs', 'op', 'rhs']


class Variable(ast.AST):
    _fields = ['name']


class StringLiteral(ast.AST):
    _fields = ['s']


class NumberLiteral(ast.AST):
    _fields = ['n']


class LUT(ast.AST):
    _fields = ['tbl']


class IntInput(ast.AST):
    _fields = ['in']


class StrInput(ast.AST):
    _fields = ['in']


class Evaluator(ast.NodeVisitor):
    def __init__(self):
        self.environment = {}

    def visit_Declaration(self, node):
        if node.defn.lhs.var:
            if node.defn.lhs.var.name in self.environment:
                raise DeborahException("Re-declared Variable: " + node.defn.lhs.var.name)
            self.environment[node.defn.lhs.var.name] = None
        self.generic_visit(node)

    def visit_Assignment(self, node):
        if node.lhs.var:
            if node.lhs.var.name not in self.environment:
                raise DeborahException("Variable not defined: " + node.lhs.var.name)
            self.environment[node.lhs.var.name] = self.visit(node.rhs)
        if node.lhs.lut:
            key = self.visit(node.lhs.lut.exp)
            lookup_name = node.lhs.lut.var.name
            if lookup_name not in self.environment:
                raise DeborahException("Variable not defined: " + node.lhs.var.name)
            self.environment[lookup_name][key] = self.visit(node.rhs)


    def visit_Print(self, node):
        value = self.visit(node.exp)
        print(value)

    def visit_Expression(self, node):
        return self.visit(node.val)

    def visit_BinaryExpression(self, node):
        left = self.visit(node.lhs)
        right = self.visit(node.rhs)
        if node.op == "+":
            return left + right
        if node.op == "-":
            return left - right
        if node.op == "@":
            return right[left]
        if node.op == ">":
            return int(left > right)

    def visit_Variable(self, node):
        if node.name not in self.environment:
            raise DeborahException("Variable not defined: " + node.name)
        return self.environment[node.name]

    def visit_StringLiteral(self, node):
        return node.s

    def visit_NumberLiteral(self, node):
        return node.n

    def visit_LUT(self, node):
        return {}

    def visit_Loop(self, node):
        while self.visit(node.cond):
            for line in node.stmts:
                self.visit(line)

    def visit_IntInput(self, node):
        return int(raw_input())

    def visit_StrInput(self, node):
        return raw_input()


if __name__ == "__main__":
    model = metamodel.metamodel_from_file("deborahscript.tx", classes=[Program, Loop, Assignment, Declaration,
                                                                       Print, Expression, BinaryExpression,
                                                                       Variable, LUT, IntInput, StrInput])

    p = model.model_from_file("gcd.ds")
    evaluator = Evaluator()
    evaluator.visit(p)