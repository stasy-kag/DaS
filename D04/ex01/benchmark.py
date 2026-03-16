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


if __name__ == '__main__':
    n = 90000000
    
    time_loop = timeit.timeit('loop_append()', setup='from __main__ import loop_append', number=n)
    time_list = timeit.timeit('list_comprehension()', setup='from __main__ import list_comprehension', number=n)
    time_map  = timeit.timeit('map_filter()', setup='from __main__ import map_filter', number=n)

    if time_map <= time_loop and time_map <= time_list:
        print("it is better to use a map")
    elif time_list <= time_loop and time_list <= time_map:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop and append")
    
    print(f"loop_append: {time_loop} vc list_comprehension: {time_list} vc map: {time_map}")