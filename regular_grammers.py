
# floating numbers language

N = {"S", "A", "B", "C", "D", "E", "F"}
SIG = {"0", "1", "2", "3", "4" ,"5" ,"6" ,"7", "8" ,"9" ,"+" ,"-" , ".", "e"}

grammer = \
{"S": ["+A", "-A","A"], 
 "A": ["0A", "1A", "2A", "3A", "4A", "5A", "6A", "7A", "8A", "9A", "B", ".B"],
 "B": ["0C", "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C"],
 "C": ["0C", "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "eD", "#"],
 "D": ["+E", "-E", "E"],
 "E": ["0F", "1F", "2F", "3F", "4F", "5F", "6F", "7F", "8F", "9F"],
 "F": ["0F", "1F", "2F", "3F", "4F", "5F", "6F", "7F", "8F", "9F", "#"]}


def check_float(float_str, grammer, sigma):
	head = "S"
	if float_str[0] not in sigma:
		return False
	while len(float_str) > 1:
		next_char = float_str[1]
		# print next_char
		allowed = set([chars[0] for chars in grammer[head]])
		skippers = [exp for exp in grammer[head] if len(exp) == 1]
		# print "skippers:", skippers
		# print "allowed:", allowed
		# print "next char:", next_char
		if next_char in allowed:
			head = [x[1] for x in grammer[head] if x[0] == next_char][0]
			print "head:", head
			float_str = float_str[1:]
		elif len(skippers) > 0 and next_char in sigma:
			head = skippers[0]
			print "head:", head
			float_str = float_str[1:]
		else:
			return False
	return True 


float_exp =  "2.333222e2311"
irregular_float_exp = "2.333r222e2311"
print check_float(float_exp, grammer, SIG)