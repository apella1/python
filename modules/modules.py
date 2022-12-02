def greetingApp(time, name):
    if(time < 12):
        print(f'Good morning {name}')
    elif(time == 12):
        print(f'It is noon, {name}')
    elif(time < 16):
        print(f'Good afternoon {name}')
    else:
        print(f'Good evening {name}')


greetingApp(12, 'Malcolm')
