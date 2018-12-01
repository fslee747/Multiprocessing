import multiprocessing as mp
import threading as td
##from multiprocessing import Queue

def job(q,a,b):
        print("This is the job for a+b = ", a+b, "\n")
        res = 0
        for i in range(1000):
                res += i+i**2+i**3
        q.put(res)
def multithread():               
        q = mp.Queue()
        t1 = td.Thread(target = job, args=(q,1,2,))
        t2 = td.Thread(target = job, args=(q,3,4,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        res1 = q.get()
        res2 = q.get()
        res = res1+res2
        print("multithread res = ", res)
def multiprocess():
        q = mp.Queue()
        p1 = mp.Process(target = job, args=(q,5,6,))
        p2 = mp.Process(target = job, args=(q,7,8,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        res1 = q.get()
        res2 = q.get()
        res = res1+res2
        print("multiprocess res = ", res)
if __name__ == "__main__":
        multithread()
        multiprocess()
