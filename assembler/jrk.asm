

# Dit is mijn eerste test programma
	push 5
	push 0

	loada
	loadb
	

:test
	teste
	jumpt :verder

:plus
	push 1
	add
	jump :test



:verder
	#ex
	decrementb
	ex
	testz
	ex 
	jumpt :einde
	jumpf :verder


:einde
	#push 0b1010
	#ex
	storea
	halt
	add
	halt