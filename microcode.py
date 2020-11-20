library = {}

def loadlibrary():

    library["_LDA"] =   (
        ("START", {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "HALT")),
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "START")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "START"))
    )

    library["_ADD"] =   ( 
        ("STadd", {"ST":"1", "Rb":"_"}, ({"ST":"_", "Rb":"1"}, {"ST":"L", "Rb":"L"}, "START")),
        ("STadd", {"ST":"1", "Rb":"1"}, ({"ST":"_", "Rb":"1"}, {"ST":"L", "Rb":"L"}, "START")),
        ("STadd", {"ST":"1", "Rb":"0"}, ({"ST":"_", "Rb":"1"}, {"ST":"L", "Rb":"L"}, "DONE"))
    )

    library["LDA"] =    (
        ("START", {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "START")),
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "START")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "START")),

        ("START", {"ST":"0", "RA":"_"}, ({"ST":"_", "RA":"0"}, {"ST":"L", "RA":"L"}, "START")),
        ("START", {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"L", "RA":"L"}, "START")),
        ("START", {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"L", "RA":"L"}, "START")),
          
        ("START", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"L"}, "START")),
        ("START", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"L"}, "START")),
        ("START", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"L"}, "RWD-A")),
          
        ("RWD-A", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"R"}, "RWD-A")),
        ("RWD-A", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "loop")),
        ("RWD-A", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"R"}, "loop")),
          
        ("loop" , {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "loop")),
        ("loop" , {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"R"}, "loop")),
        ("loop" , {"ST":"#", "RA":"_"}, ({"ST":"_", "RA":"_"}, {"ST":"L", "RA":"L"}, "HALT"))
    )

    return(library)


