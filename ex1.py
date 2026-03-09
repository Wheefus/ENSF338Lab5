import sys

exp = ""

for i in sys.argv[1:]:
    exp += i + " "

exp.strip()
exp = exp.replace("'", "")

stack_expr = []

def get_int(str_int:str, start):
    end = 0
    for i in range(start, len(str_int)):
        if not str_int[i].isnumeric():
            end = i
            break

    return int(str_int[start:end]), end

skip_till = 0
for i in range(len(exp)):
    if skip_till > i:
        continue
    elif exp[i] == ' ' or exp[i] == '(':
        continue
    elif exp[i] == ')':
        #calculate from stack
        e2 = stack_expr.pop()
        e1 = stack_expr.pop()
        op = stack_expr.pop()

        val = 0
        if op == '+':
            val = e1 + e2
        elif op == '-':
            val = e1 - e2
        elif op == '*':
            val = e1 * e2
        elif op == '/':
            val = e1 // e2
        stack_expr.append(val)

        continue
    elif exp[i].isnumeric():
        val, skip_till = get_int(exp, i)
        stack_expr.append(val)
    else:
        stack_expr.append(exp[i])

print(stack_expr.pop())