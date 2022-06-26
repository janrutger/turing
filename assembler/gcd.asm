speed 1

push 4452
push 18396

loada
loadb
testz
jumpt :done
ex
#loada
testz
jumpt :done

:while
    teste
    jumpt :done

    testg
    jumpf :Asmaller
    storeb
    storea
    storeb
    jump :subtract
:Asmaller
    storea
    storeb
    storea

:subtract
    clra
    clrb
    sub
    ex
    loadb
    jump :while


:done
    storea
    prt
    halt