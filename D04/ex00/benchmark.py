import timeit

def list_comprehension():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com'] * 5

    gmail = [i for i in emails if i.split('@')[1] == 'gmail.com']
    return gmail

def  loop_append():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com'] * 5

    gmail = []

    for i in emails:
        if i.split('@')[1] == 'gmail.com':
            gmail.append(i)
    return gmail


if __name__ == '__main__':
    n = 90000000
    
    time_loop = timeit.timeit('loop_append()', setup='from __main__ import loop_append', number=n)
    
    time_list = timeit.timeit('list_comprehension()', setup='from __main__ import list_comprehension', number=n)
    
    if time_list <= time_loop:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop and append")
    
    times = [time_loop, time_list]
    times.sort()
    print(f"{times[0]} vc {times[1]}")