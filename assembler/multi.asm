speed 5

push 9
push 5

multi

#halt

:loop
    storea
    storeb
    push 0
    push 0
    loada
    loadb

    multi
jump :loop

halt