# match-case Tutorial
# https://www.geeksforgeeks.org/python-match-case-statement/

# The match statement is use for pattern matching.
# PEP 634 - Structural Pattern Matching: Specification
# https://peps.python.org/pep-0634/
# PEP 635 - Structural Pattern Matching: Motivation and Rationale
# https://peps.python.org/pep-0635/
# PEP 636 - Structural Pattern Matching: Tutorial
#https://peps.python.org/pep-0636/

user = 'Marco'    

match user:
    case 'Marvin':
        print(f"Hello {user} !")
    case 'Mauricio':
        print(f"Hello {user} !")
    case 'Marco':
        print(f"Hello {user} !")
    case _ :
        print('None user')


values = 100

match values:

    case values if range(0,101):
        print(f'Result is { values }') 

    case "100" if 100 in values: 
        print(f"resultado {values*2}")
    
    case values if values > 10 :   
        print('if comparison')
