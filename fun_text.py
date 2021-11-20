import random

def parse_char(c: str):
    if random.randint(1, 3) == 2:
        return c.upper()
    return c.lower()
    
    
def make_fun_message(message):
    modified = ""
    for c in message:
        modified = modified + parse_char(c)
    
    return modified


