help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

with open('converted.txt','w') as sourcefile:
    for row in sourcefile:
        result = ''.join(help_dict[ele] for ele in row)
        print(result)
        import pdb;pdb.set_trace()