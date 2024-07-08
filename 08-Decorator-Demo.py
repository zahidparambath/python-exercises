# Exercise Name:
# 	08-Decorator-Demo
# Description:
# 	Create a decorator called 'time_this' and use it to measure time taken to run functions

# For example, running:
# 	@time_this
# 	def sleeper_func(sleeptime):
# 	    print(f'sleeping for {sleeptime}')
# 	    sleep(sleeptime)
# 	    return 'Woke up!'

# 	sleeper_func(2)

# Sould output the following in the console:
# 	--> Running sleeper_func
# 	sleeping for 2
# 	--> sleeper_func ran in 2.002105236053467 seconds

def time_this(original_function):
    import time
    def wrapper(*args):
        t1=time.time()
        result = original_function(*args)
        t2 = time.time() - t1
        print('Running {} function'.format(original_function.__name__))
        print('Running for {}'.format(args[0]))
        print('{} function ran in {} seconds'.format(original_function.__name__, t2))
        return result
    return wrapper

import time

@time_this
def sleeper_func(sleeptime):
    time.sleep(sleeptime)
    
sleeptime = 2
sleeper_func(sleeptime)



