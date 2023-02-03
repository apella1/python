# scope and namespaces

def scope_test():
    def do_local():
        spam = 'local spam'
    
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global ():
        global spam
        spam = 'global spam'
    
    spam = 'test spam'
    
    do_local()
    print(f'After local assignment, {spam}')
    do_nonlocal()
    print(f'After nonlocal assignment, {spam}')
    do_global()
    print(f'After global assignment, {spam}')

scope_test()
print('In global scope:', spam)