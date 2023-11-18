amigos=[['João',25,'Câncer'], ['Maria',23,'Áries'], ['Ana',31,'Aquário'], ['Mário']]
for x in amigos:
	if isinstance (x,list):
		for y in x:
			print(y)
	else:
		print(x)