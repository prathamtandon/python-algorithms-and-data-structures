# Given an arithmetic equation consisting of positive integers,+,-,*
# and / (no parantheses), compute the result.
# EXAMPLE: 2*3+5/6*3+15
# OUTPUT: 23.5

from enum import Enum

class Operator(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    BLANK = 5

def compute(sequence):
    numberStack = []
    operatorStack = []
    i = 0
    
    while i < len(sequence):
        # Get number and push
        value = parseNextNumber(sequence, i)
        numberStack.append(float(value))

        # Move to the operator
        i += len(str(value))
        if i >= len(sequence):
            break

        # Get operator, collapse top as needed, push operator.
        op = parseNextOperator(sequence,i)
        collapseTop(op, numberStack, operatorStack)
        operatorStack.append(op)
        
        i += 1


    # Do final collapse.
    collapseTop(Operator.BLANK, numberStack, operatorStack)
    if len(numberStack) == 1 and len(operatorStack) == 0:
        return numberStack.pop()

    return 0

def parseNextNumber(seq, index):
    sb = []
    while index < len(seq) and seq[index].isdigit():
        sb.append(seq[index])
        index += 1
    
    return int("".join(sb))

def parseNextOperator(seq, index):
    if index < len(seq):
        op = seq[index]
        if op == '+':
            return Operator.ADD
        elif op == '-':
            return Operator.SUBTRACT
        elif op == '*':
            return Operator.MULTIPLY
        elif op == '/':
            return Operator.DIVIDE

    return Operator.BLANK

# Collapse top until priority(futureTop) > priority(currentTop). Collapsing
# means to pop the top 2 numbers and apply the operator popped from top of
# operator stack and then push that onto the numbers stack.
def collapseTop(futureTop, numberStack, operatorStack):
    while len(operatorStack) > 0 and len(numberStack) > 1:
        if priorityOfOperator(futureTop) <= priorityOfOperator(operatorStack[len(operatorStack)-1]):
            second = numberStack.pop()
            first = numberStack.pop()
            op = operatorStack.pop()
            collapsed = applyOp(first,op,second)
            numberStack.append(collapsed)
        else:
            break

# Return priority of operator. Mapped so that:
# addition == subtraction < multiplication == division
def priorityOfOperator(op):
    if op == Operator.ADD:
        return 1
    elif op == Operator.SUBTRACT:
        return 1
    elif op == Operator.MULTIPLY:
        return 2
    elif op == Operator.DIVIDE:
        return 2
    else:
        return 0

# Apply operator: left [op] right
def applyOp(left,op,right):
    if op == Operator.ADD:
        return left + right
    elif op == Operator.SUBTRACT:
        return left - right
    elif op == Operator.MULTIPLY:
        return left * right
    elif op == Operator.DIVIDE:
        return left / right
    else:
        return right
