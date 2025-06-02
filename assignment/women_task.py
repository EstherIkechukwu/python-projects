import ast

def is_empty_list(s):
    try:
        lst = ast.literal_eval(s)
        return isinstance(lst, list) and len(lst) == 0
    except:
        return False

input_str = input().strip()
print(is_empty_list(input_str))
