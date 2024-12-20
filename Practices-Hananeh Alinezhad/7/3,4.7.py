from _thread import start_new_thread
num_threads = 0
def herona():
    global num_threads
    num_threads += 1 
    
    num_threads -= 1
    