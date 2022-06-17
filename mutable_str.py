def mutate_string(string, position, character):
    lst=list(string)
    lst[position]=character
    return ''.join(lst)


print(mutate_string('salman',1 ,'f'))