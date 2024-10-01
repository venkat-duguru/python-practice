import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for _ in range(5):
            print(threading.current_thread().getName(), "is running")


time.sleep(2)
thread1 = MyThread(name="Thread1")
thread2 = MyThread(name="Thread2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Main thread exiting")
