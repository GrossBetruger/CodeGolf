from collections import deque 
import re 

arithmatic_exp = "* + 12 1 * 4 2"


def lexer(exp):
	return re.split("\s+", exp)


def eval_symbol(symbol):
	if symbol.isdigit():
		return symbol
	elif symbol == "+":
		return "add"
	elif symbol == "*":
		return "mul"


def read_exp(exp):
	interpreter_stack = deque()
	for symbol in lexer(exp):
		evaluated = eval_symbol(symbol)
		if evaluated:
			interpreter_stack.append(evaluated)
	return interpreter_stack


def interprete(interpreter_stack):
	operands_stack = deque()
	while interpreter_stack:
		next = interpreter_stack.pop()
		if is_operation(next):
			operands_stack.append(binary_operation(next, 
				operands_stack.pop(), operands_stack.pop()))
		else:
			operands_stack.append(next)
	return operands_stack.pop()


def is_operation(symbol):
	return symbol in ["add", "mul"]


def binary_operation(operation, operand_a, operand_b):
	if operation == "add":
		return int(operand_a) + int(operand_b)
	elif operation == "mul":
		return int(operand_a) * int(operand_b)



print interprete(read_exp(arithmatic_exp))