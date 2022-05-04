speed 3

push 3
push 2

multi

halt

:loop
    storea
    storeb
    push 0
    loadb


    multi
jump :loop

halt