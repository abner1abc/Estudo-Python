from collections import deque

q=deque()			     #cria o deque
q.append('b')		     #insere no final
q.append('c')
q.appendleft('a')
print(q)			     #imprime o deque
print(q.popleft())	     #remove do inicio
print(q.pop())	     	 #remove do final

maxDeque=10
deque=[None]*maxDeque
inicioDeque=None
finalDeque=None