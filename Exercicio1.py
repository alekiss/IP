Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> CustoRefeicao = 44.50
>>> Impostos = 6.75%
SyntaxError: invalid syntax
>>> Impostos = 6.75
>>> Gorjeta = 15
>>> CustoTotal = Impostos * CustoRefeicao / 100
>>> print(CustoTotal)
3.00375
>>> Custo = CustoRefeicao * Impostos
>>> print(Custo)
300.375
>>> ValorTotal = CustoRefeicao + CustoTotal
>>> print(ValorTotal)
47.50375
>>> ValorGorjeta = ValorTotal * Gorjeta / 100
>>> print(ValorGorjeta)
7.1255625
>>> CTotal = ValorGorjeta + ValorTotal
>>> print(CTotal)
54.6293125
>>> 
