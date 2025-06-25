# Multithreading 🧵 is a concept in computer programming where a single process is divided into multiple threads 
# that can run concurrently (at the same time). 
# It’s commonly used to make programs faster and more efficient, especially when doing tasks that can happen in parallel.

#      🧠 What is a Thread?
#           A thread is the smallest unit of a process that can be scheduled by the operating system.


# 🔧 Why use multithreading?
# ✅ Improves performance on multi-core CPUs.

# ✅ Better resource utilization.

# ✅ Responsive user interfaces (UI doesn't freeze).

# ✅ Faster execution for tasks like downloading files, real-time games, etc.





# we gonna use it for featching apis

import threading
import time

def walk_dog():
    time.sleep(5)
    print("Walking out the dog ")

def trash_out():
    time.sleep(2)
    print("Throwing Out the trash done")

def Mail_box():
    time.sleep(3)
    print("Mail check done")


# normaly
walk_dog() 
trash_out()
Mail_box()
# Total time = 5 + 2 + 3 = 10 seconds
print("Now this")


# with threads
work1 = threading.Thread(target=walk_dog)
work1.start()

work2 = threading.Thread(target=trash_out)
work2.start()

work3 = threading.Thread(target=Mail_box)
work3.start()
# These will run in parallel, so total time ≈ longest task (5 seconds)


work1.join()
work2.join()
work3.join()
# Wait for all threads to complete before moving on
# `.join()` blocks the main program until the thread finishes




print("done")