import sys
import timeit

def list_comprehension():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
              'anna@live.com', 'philipp@gmail.com'] * 5
    gmail = [i for i in emails if i.split('@')[1] == 'gmail.com']
    return gmail

def loop_append():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
              'anna@live.com', 'philipp@gmail.com'] * 5
    gmail = []
    for i in emails:
        if i.split('@')[1] == 'gmail.com':
            gmail.append(i)
    return gmail

def map_filter():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
              'anna@live.com', 'philipp@gmail.com'] * 5
    gmail = list(filter(None, map(lambda x: x if x.split('@')[1] == 'gmail.com' else None, emails)))
    return gmail

def filter_func():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
              'anna@live.com', 'philipp@gmail.com'] * 5
    gmail = list(filter(lambda x: x.split('@')[1] == 'gmail.com', emails))
    return gmail 

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise Exception('Неверное количество аргументов: имя функции, количество вызовов')
    
        function_name = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise Exception("Второй аргумент должен быть числом")
 
        funcs = {
            'loop_append': loop_append,
            'list_comprehension': list_comprehension,
            'map_filter': map_filter,
            'filter_func': filter_func
            }

        if function_name not in funcs:
            raise Exception('Неизвестная функция')

        t = timeit.timeit(lambda: funcs[function_name](), number=n)


        print(t)

    except Exception as e:
        print(e)



