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

    library["STA"] =    (
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"1", "RA":"1"}, {"ST":"L", "RA":"S"}, "START")),
        ("START", {"ST":"0", "RA":"1"}, ({"ST":"0", "RA":"1"}, {"ST":"L", "RA":"S"}, "START")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"1", "RA":"0"}, {"ST":"L", "RA":"S"}, "START")),
        ("START", {"ST":"0", "RA":"0"}, ({"ST":"0", "RA":"0"}, {"ST":"L", "RA":"S"}, "START")),
        ("START", {"ST":"_", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"S"}, "toend")),
        ("START", {"ST":"_", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"S"}, "toend")),

        ("toend", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"R"}, "toend")),
        ("toend", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "toend")),        
        ("toend", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"L", "RA":"L"}, "write")),

        ("write", {"ST":"_", "RA":"1"}, ({"ST":"1", "RA":"1"}, {"ST":"L", "RA":"L"}, "write")),
        ("write", {"ST":"_", "RA":"0"}, ({"ST":"0", "RA":"0"}, {"ST":"L", "RA":"L"}, "write")),
        ("write", {"ST":"_", "RA":"_"}, ({"ST":"_", "RA":"_"}, {"ST":"R", "RA":"R"}, "HALT")),
    )

    library["STB"] =    (
        ("START", {"ST":"1", "RB":"1"}, ({"ST":"1", "RB":"1"}, {"ST":"L", "RB":"S"}, "START")),
        ("START", {"ST":"0", "RB":"1"}, ({"ST":"0", "RB":"1"}, {"ST":"L", "RB":"S"}, "START")),
        ("START", {"ST":"1", "RB":"0"}, ({"ST":"1", "RB":"0"}, {"ST":"L", "RB":"S"}, "START")),
        ("START", {"ST":"0", "RB":"0"}, ({"ST":"0", "RB":"0"}, {"ST":"L", "RB":"S"}, "START")),
        ("START", {"ST":"_", "RB":"1"}, ({"ST":"#", "RB":"1"}, {"ST":"S", "RB":"S"}, "toend")),
        ("START", {"ST":"_", "RB":"0"}, ({"ST":"#", "RB":"0"}, {"ST":"S", "RB":"S"}, "toend")),

        ("toend", {"ST":"#", "RB":"0"}, ({"ST":"#", "RB":"0"}, {"ST":"S", "RB":"R"}, "toend")),
        ("toend", {"ST":"#", "RB":"1"}, ({"ST":"#", "RB":"1"}, {"ST":"S", "RB":"R"}, "toend")),        
        ("toend", {"ST":"#", "RB":"_"}, ({"ST":"#", "RB":"_"}, {"ST":"L", "RB":"L"}, "write")),

        ("write", {"ST":"_", "RB":"1"}, ({"ST":"1", "RB":"1"}, {"ST":"L", "RB":"L"}, "write")),
        ("write", {"ST":"_", "RB":"0"}, ({"ST":"0", "RB":"0"}, {"ST":"L", "RB":"L"}, "write")),
        ("write", {"ST":"_", "RB":"_"}, ({"ST":"_", "RB":"_"}, {"ST":"R", "RB":"R"}, "HALT")),
    )

    library["INCB"] =  (
        ("START", {'RB': '1', "S": "0"}, ({"RB":"1", "S":"_"}, {"RB":"S", "S":"S"}, "START")),
        ("START", {'RB': '1', "S": "1"}, ({"RB":"1", "S":"_"}, {"RB":"S", "S":"S"}, "START")),
        ("START", {'RB': '0', "S": "0"}, ({"RB":"0", "S":"_"}, {"RB":"S", "S":"S"}, "START")),
        ("START", {'RB': '0', "S": "1"}, ({"RB":"0", "S":"_"}, {"RB":"S", "S":"S"}, "START")),

        ("START", {'RB': '1', "S": "_"}, ({"RB":"0", "S":"_"}, {"RB":"R", "S":"S"}, "eind")),
        ("START", {'RB': '0', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"R", "S":"S"}, "leen")),

        ("leen",  {'RB': '1', "S": "_"}, ({"RB":"0", "S":"_"}, {"RB":"R", "S":"S"}, "eind")),
        ("leen",  {'RB': '0', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"R", "S":"S"}, "leen")),
        ("leen",  {'RB': '_', "S": "_"}, ({"RB":"_", "S":"_"}, {"RB":"L", "S":"S"}, "isnul")),

        ("eind",  {'RB': '0', "S": "_"}, ({"RB":"0", "S":"_"}, {"RB":"R", "S":"S"}, "eind")),
        ("eind",  {'RB': '1', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"R", "S":"S"}, "eind")),
        ("eind",  {'RB': '_', "S": "_"}, ({"RB":"_", "S":"_"}, {"RB":"L", "S":"S"}, "terug")),

        ("terug", {'RB': '0', "S": "_"}, ({"RB":"_", "S":"_"}, {"RB":"L", "S":"S"}, "terug")),
        ("terug", {'RB': '1', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"L", "S":"S"}, "terug1")),
        ("terug", {'RB': '_', "S": "_"}, ({"RB":"_", "S":"_"}, {"RB":"L", "S":"S"}, "isnul")),

        ("terug1",{'RB': '1', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"L", "S":"S"}, "terug1")),
        ("terug1",{'RB': '0', "S": "_"}, ({"RB":"0", "S":"_"}, {"RB":"L", "S":"S"}, "terug1")),
        ("terug1",{'RB': '_', "S": "_"}, ({"RB":"_", "S":"0"}, {"RB":"R", "S":"S"}, "HALT")),

        ("isnul", {'RB': '_', "S": "_"}, ({"RB":"0", "S":"1"}, {"RB":"S", "S":"S"}, "HALT")),
        ("isnul", {'RB': '1', "S": "_"}, ({"RB":"0", "S":"1"}, {"RB":"S", "S":"S"}, "HALT"))
    )

    library["ADD"] =    (
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("START", {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("START", {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD")),
          
        ("ADD",   {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "ADD")), 
        ("ADD",   {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"0", "RA":"_"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD",   {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"S"}, "RWD-A")),
          
        ("ADD1",  {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD1",  {'ST':"0", 'RA':"_"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
          
        ("ADD1",  {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"1", "RA":"_"}, ({"ST":"#", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "ADD")),
        ("ADD1",  {'ST':'#', 'RA':'0'}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "ADD")),
          
        ("RWD-A", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"L"}, "RWD-A")),
        ("RWD-A", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"L"}, "loop")),
        ("RWD-A", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"L"}, "loop")),
          
        ("loop" , {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"L"}, "loop")),
        ("loop" , {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"L"}, "loop")),
        ("loop" , {"ST":"#", "RA":"_"}, ({"ST":"_", "RA":"_"}, {"ST":"R", "RA":"R"}, "HALT"))
    )


    library["LDA"] =    (
        ("START", {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "START")),
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "START")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "START")),

        ("START", {"ST":"0", "RA":"_"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "START")),
        ("START", {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "START")),
        ("START", {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "START")),
          
        ("START", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"R"}, "START")),
        ("START", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"R"}, "START")),
        ("START", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"R"}, "RWD-A")),
          
        ("RWD-A", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"L"}, "RWD-A")),
        ("RWD-A", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"L"}, "loop")),
        ("RWD-A", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"L"}, "loop")),
          
        ("loop" , {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"L"}, "loop")),
        ("loop" , {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"L"}, "loop")),
        ("loop" , {"ST":"#", "RA":"_"}, ({"ST":"_", "RA":"_"}, {"ST":"R", "RA":"R"}, "HALT"))
    )

    library["LDB"] =    (
        ("START", {"ST":"1", "RB":"_"}, ({"ST":"_", "RB":"1"}, {"ST":"R", "RB":"R"}, "START")),
        ("START", {"ST":"1", "RB":"1"}, ({"ST":"_", "RB":"1"}, {"ST":"R", "RB":"R"}, "START")),
        ("START", {"ST":"1", "RB":"0"}, ({"ST":"_", "RB":"1"}, {"ST":"R", "RB":"R"}, "START")),

        ("START", {"ST":"0", "RB":"_"}, ({"ST":"_", "RB":"0"}, {"ST":"R", "RB":"R"}, "START")),
        ("START", {"ST":"0", "RB":"1"}, ({"ST":"_", "RB":"0"}, {"ST":"R", "RB":"R"}, "START")),
        ("START", {"ST":"0", "RB":"0"}, ({"ST":"_", "RB":"0"}, {"ST":"R", "RB":"R"}, "START")),
          
        ("START", {"ST":"#", "RB":"1"}, ({"ST":"#", "RB":"_"}, {"ST":"S", "RB":"R"}, "START")),
        ("START", {"ST":"#", "RB":"0"}, ({"ST":"#", "RB":"_"}, {"ST":"S", "RB":"R"}, "START")),
        ("START", {"ST":"#", "RB":"_"}, ({"ST":"#", "RB":"_"}, {"ST":"S", "RB":"R"}, "RWD-A")),
          
        ("RWD-A", {"ST":"#", "RB":"_"}, ({"ST":"#", "RB":"_"}, {"ST":"S", "RB":"L"}, "RWD-A")),
        ("RWD-A", {"ST":"#", "RB":"1"}, ({"ST":"#", "RB":"1"}, {"ST":"S", "RB":"L"}, "loop")),
        ("RWD-A", {"ST":"#", "RB":"0"}, ({"ST":"#", "RB":"0"}, {"ST":"S", "RB":"L"}, "loop")),
          
        ("loop" , {"ST":"#", "RB":"1"}, ({"ST":"#", "RB":"1"}, {"ST":"S", "RB":"L"}, "loop")),
        ("loop" , {"ST":"#", "RB":"0"}, ({"ST":"#", "RB":"0"}, {"ST":"S", "RB":"L"}, "loop")),
        ("loop" , {"ST":"#", "RB":"_"}, ({"ST":"_", "RB":"_"}, {"ST":"R", "RB":"R"}, "HALT"))
    )

    return(library)


