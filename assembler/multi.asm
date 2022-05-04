speed 3

push 0
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