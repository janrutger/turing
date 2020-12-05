# Dit is mijn eerste test programma
	jump :init

:start

	add
	jump :end


:init
	push 9
	push 6
	loada
	jump :start
:end
	storea