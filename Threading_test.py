import threading
import time
from multiprocessing import Queue

def thread_job():
        print("This is an added thread, number is %s" % threading.current_thread())
        print("T1 start \n")
        for i in range(10):
                time.sleep(0.1)
        print("T1 finish\n")

def T2_job():
        print("T2 starts\n")
        print("T2 stops \n")

def job(l,q):
        for i in range(len(l)):
                l[i] = l[i]**2
        q.put(l)

def multithreading():
        q = Queue()
        threads = []
        data = [[1,2,3],[3,4,5],[4,5,6],[6,7,8]]
        for i in range(4):
                t = threading.Thread(target = job, args = (data[i],q))
                t.start()
                threads.append(t)
        for thread in threads:
                thread.join()
        results = []
        for _ in range(4):
                results.append(q.get())
        print (results)

def job1():
        global A, lock
        lock.acquire()
        for i in range(10):
                A += 1
                print("job1=", A, "\n")
        lock.release()

def job2():
        global A, lock
        lock.acquire()
        for i in range(10):
                A += 10
                print("job2=", A, "\n")
        lock.release()
                

def main():
        added_thread = threading.Thread(target = thread_job, name = "T1")
        thread2 = threading.Thread(target = T2_job, name = "T2")
        print(threading.active_count())
        print(threading.enumerate())
        print(threading.current_thread())
        added_thread.start()
        thread2.start()
        added_thread.join()
        print("all done\n")
##        multithreading()

        
if __name__ == "__main__":
	main()
	multithreading()
	lock = threading.Lock()
	A = 0
	t1 = threading.Thread(target = job1)
	t2 = threading.Thread(target = job2)
	t1.start()
	t2.start()
	t1.join()
	t2.join()


