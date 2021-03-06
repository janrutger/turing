schema = {}

def loadSchema():

    schema["push"]      = ("PUSH", "b")
    schema["pull"]      = ("PULL", None)
    schema["halt"]      = ("HALT", None)

    schema["jump"]      = ("JP", "n")
    schema["jumpt"]     = ("JPT", "n")
    schema["jumpf"]     = ("JPF", "n")

    schema["storea"]    = ("STA", None)
    schema["storeb"]    = ("STB", None)
    schema["storem"]    = ("STM", "s")
    
    schema["loada"]     = ("LDA", None)
    schema["loadb"]     = ("LDB", None)
    schema["loadm"]     = ("LDM", "s")

    schema["decrementb"]= ("DECB", None)    
    schema["add"]       = ("ADD", None)

    schema["ex"]        = ("EX", None)
    schema["testz"]     = ("TSTZ", None)
    schema["teste"]     = ("TSTE", None)

    return(schema)


print(loadSchema())