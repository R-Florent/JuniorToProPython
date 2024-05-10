def sting_first(str1, str2):
    def inside_f():
        cocanetated = str1 + str2
        return cocanetated

    z = inside_f()
    return z

def join(string):
    join_string = string + 'Developers'
    return join_string


conateation = sting_first('Emma', 'Kelly')
print(join(conateation))