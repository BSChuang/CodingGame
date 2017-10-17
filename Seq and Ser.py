import random
import sympy
a, b, c, x, y, z = sympy.symbols('a b c x y z')
termN, num1, d, numN, Sn = sympy.symbols('termN num1 d numN Sn')
# ARITHMETIC SEQUENCE ------------------------------------------------------------------------------------------------------
termN = 3
num1 = 5
d = d
numN = 9
Sn = x





# numN term of sequence
def fNumN(termN, num1, d, numN, Sn):
    numN = num1 + (termN - 1) * d
    return Rest(termN, num1, d, numN, Sn)

# num1 of sequence
def fNum1(termN, num1, d, numN, Sn):
    num1 = numN - (termN - 1) * d
    return Rest(termN, num1, d, numN, Sn)

# Common difference of sequence
def fD(termN, num1, d, numN, Sn):
    d = (numN - num1) / (termN - 1)
    return Rest(termN, num1, d, numN, Sn)

# termN of sequence
def fTermN(termN, num1, d, numN, Sn):
    termN = (numN - num1 + d) / d
    return Rest(termN, num1, d, numN, Sn)

# Sum of sequence up to N
def fSn(termN, num1, d, numN, Sn):
    Sn = termN * (num1 + numN) / 2
    return Rest(termN, num1, d, numN, Sn)

def Rest(_termN, _num1, _d, _numN, _Sn):
    _numN = _num1 + (_termN - 1) * _d
    _d = (_numN - _num1) / (_termN - 1)
    _num1 = _numN - (_termN - 1) * _d
    _termN = (_numN - _num1 + _d) / _d
    _Sn = _termN * (_num1 + _numN) / 2
    return 'num' + str(_termN) + ' = ' + str(_numN) + '\nnum1 = ' + str(_num1) + '\nd = ' + str(_d) + '\ntermN = ' + str(_termN) + '\nSn = ' + str(_Sn)

#
if not sympy.sympify(numN).is_number:
    print(fNumN(termN, num1, d, numN, Sn))
elif not sympy.sympify(num1).is_number:
    print(fNum1(termN, num1, d, numN, Sn))
elif not sympy.sympify(d).is_number:
    print(fD(termN, num1, d, numN, Sn))
elif not sympy.sympify(termN).is_number:
    print(fTermN(termN, num1, d, numN, Sn))
elif not sympy.sympify(Sn).is_number:
    print(fSn(termN, num1, d, numN, Sn))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

