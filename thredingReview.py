import time
import threading
import multiprocessing

## GENERAL NOTES ---------------------------------------------------------
# When to use Threading
    # When initalization speed is important
    # When only 2 concurrent actions are needed
    # Tasks requiring easy transfer of information & communicationbetween threads
    # Tasks need to be run after specific delay (threading.Timer)
# When to use Multiprocessing
    # Everything else


## THREADING NOTES -------------------------------------------------------
# t = threading.Thread(name='name', target=functionToRun, args=(arg1, arg2))
    # name='name'            --> is optional, useful for debugging
    # target=functionToRun   --> is required
    # args=(arg1, arg2)      --> is optional, must be a tuple
# t.daemon = True         # Daemon threads are forced to end when the main function ends
# t.start()               # run the thread (only once!)
# t.join()                # forces calling process to wait for the thread to finish (blocks calling)
# t.join(n)               # wait n seconds for thread to finish, then continue


## EXAMPLE (basic threading) ---------------------------------------------
"""
def func():
    while True:
        print('func() is running')
        time.sleep(0.2)
t = threading.Thread(target=func)
t.daemon = True
t.start()
while True:
    print('main')
    time.sleep(1)
"""

## EXAMPLE (threading with arguments) ------------------------------------
"""
def func(x,y,z):
    while True:
        print(f"func(): {x}, {y}, {z['val']}") # display args
        time.sleep(0.2)
t = threading.Thread(target=func, args=('a',2,{'val':3})) # 3 arguments
t.daemon = True
t.start()
while True:
    print('main')
    time.sleep(1)
"""

## EXAMPLE (threading with global variable) ------------------------------
"""
glob = 0 # declare a global variable
def func():
    global glob # access global
    while True:
        print(f'glob in func = {glob}')
        time.sleep(0.2)
t = threading.Thread(target=func)
t.daemon = True
t.start()
while True:
    print(f'glob in main = {glob}')
    time.sleep(1)
"""

## THREAD SUBCLASS -------------------------------------------------------
"""
class Countdown(threading.Thread):
    def __init__(self, count, thread_name):
        threading.Thread.__init__(self, name=thread_name)
        self.count = count
    def run(self):
        print("Thread started")
        for i in self.count:
            print(i)
            time.sleep(0.5)
        print("Thread ended")

for i in range(3):
    t = Countdown([3,2,1], "name="+str(i))
    t.start()
    print('t.is_alive() =', t.is_alive())
    print(t.getName())
    t.join()
    print('t.is_alive() =', t.is_alive())
"""


## MULTIPROCESSING NOTES -------------------------------------------------
# p = multiprocessing.Process(name='myname',target=Countdown,args=(x,))
    # name='myname'          --> is optional, useful for debugging
    # target=Countdown       --> is required, must be a callable object (e.g. function or class with run() method)
    # args=(x,)              --> is optional, must be a tuple

# p.daemon = True           # Force process termination when main code ends
# p.start()                 # Start the process (only once!)
# p.terminate()             # Terminate the process (no equivalent for threads)
    # (always 'join' after termination)
# p.join()                  # Force the calling process to wait for the new process to end before continuing
# p.join(n)                 # Pause the calling process for up to n seconds, then join even if not ended


## EXAMPLE (basic multiprocessing) ---------------------------------------
"""
def fn():
    while True:
        print('fn')
        time.sleep(0.5)
if __name__ == '__main__':
    try:
        myProcess = multiprocessing.Process(target=fn)
        myProcess.start()
        while True:
            print('main')
            time.sleep(1)
    except:
        pass
    myProcess.terminate()
    myProcess.join()
"""

## EXAMPLE (process subclassing) -----------------------------------------
"""
class Countdown(multiprocessing.Process):
    def __init__(self, count, process_name):
        multiprocessing.Process.__init__(self, name=process_name)
        self.count = count
    def run(self):
        print("Process started")
        for i in self.count:
            time.sleep(0.5)
            print(i)
        print("Process ended")

if __name__ == '__main__': # Required!
    for i in range(3):
        p = Countdown([3,2,1], "name="+str(i))
        p.start()
        print('p.is_alive() =', p.is_alive())
        print(p.name)
        p.join()
        print('p.is_alive() =', p.is_alive())
"""
        
## EXAMPLE (shared memory) -----------------------------------------------
"""
myValue = multiprocessing.Value('i')
    # 'i' = integer, 'f' = float, 'd' = double, 'c' = char
myArray = multiprocessing.Array('f',3)
    # 'f' = float, 'd' = double, 'c' = char
    # 3 = number of elements in array

def fn(myArray, myValue):
    for (idx,n) in enumerate([3,2,1]):
        myArray[idx] = n**2
        myValue.value = int(sum(myArray))
        print("In the process, iter={}:".format(idx))
        print(" Array: {}".format(myArray[:]))
        print(" Value: {}".format(myValue.value))
if __name__ == '__main__': # Required!
    p1 = multiprocessing.Process(target=fn, args=(myArray, myValue))
    
    print("Before starting process:")
    print(" Array: {}".format(myArray[:]))
    print(" Value: {}".format(myValue.value))
    
    p1.start()
    print("\n\nImmediately after starting process:")
    print(" Array: {}".format(myArray[:]))
    print(" Value: {}\n\n".format(myValue.value))
    
    p1.join()
    print("\n\nAfter completing process:")
    print(" Array: {}".format(myArray[:]))
    print(" Value: {}".format(myValue.value))
"""