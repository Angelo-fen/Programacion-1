def FactorialRec(n:int) -> int:
	if n == 0:
		return 1
	return n * FactorialRec(n-1)
############################################
n = int(input("Numero para sacar factorial:"))
print(FactorialRec(n))