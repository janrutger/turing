alltapes = {"ST", "RA", "RB", "S"}
print(type(alltapes))#library = {}
        
import microcode as mc

library = mc.loadlibrary()

LDA = (library["LDA"])

print(LDA[0][0])

for rule in LDA:
    state       = rule[0]
    tapevalue   = rule[1]
    turingrule  = rule[2]
    

    print("=======")
    print("GET    turingrule :", state, tapevalue)
    print("RETURN turingrule :", turingrule)
    print(" ")
    print(">> DO write :", turingrule[0])
    print(">> DO move  :", turingrule[1])
    print(">> NEXTSTATE:", turingrule[2])

