speed 5

push 24
push 12

multi

halt

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