from threading import Thread

def addition_of_number(x, y):
    result = x + y
    print('Addition of {} + {} = {}'.format(x, y, result))


def cube_number(i):
    result = i ** 3 
    print('Cube of {} = {}'.format(i, result))


def basic_function():
    print('This is a basic function')



Thread(target=addition_of_number, args=(2, 3)).start()
Thread(target=cube_number, args=(3,)).start()
Thread(target=basic_function).start()