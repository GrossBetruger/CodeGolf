from collections import deque, defaultdict
import re 

polish_notation = "* + 12 1 * 4 2"
reverse_polish = "3 2 3 4 * + *"


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


def eval_tree(tree):
	operation = get_root(tree)
	first_operand = tree[get_root(tree)][0]

	if type(first_operand)==dict:
		second_operand = tree[get_root(tree)][1]
		return binary_operation(operation, eval_tree(first_operand), second_operand)
	else:
		first_operand = tree[get_root(tree)][0]
		second_operand = tree[get_root(tree)][1]
		return binary_operation(operation, first_operand, second_operand)


def get_root(tree):
	try:
		return tree.keys()[0]
	except AttributeError:
		pass


def read_rev(exp):
	root = exp[-1]
	right = exp[-2]
	left = exp[0]
	if is_operation(right):
		return {root: [read_rev(exp[1:-1]), left]}
	else:
		return {root: [right, left]}


if __name__=="__main__":
	lexed = list(read_exp(reverse_polish))
	print "polish notation result:", interprete(read_exp(polish_notation))
	tt = read_rev(lexed)
	print "reverse polish tree structure", tt
	print "reverse polish result:", eval_tree(tt)