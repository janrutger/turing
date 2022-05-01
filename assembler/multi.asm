speed 3

push 5
push 3

multi

#halt

:loop
    storea
    storeb
    push 0
    loadb


    multi
jump :loop

halt