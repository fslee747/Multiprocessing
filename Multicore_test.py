import multiprocessing as mp
import threading as td
##from multiprocessing import Queue
import time

def job(q):
        res = 0
        for i in range(100000):
                res += i+i**2+i**3
        q.put(res)

def multicore():
        q = mp.Queue() 
        p1 = mp.Process(target = job, args=(q,))
        p2 = mp.Process(target = job, args=(q,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()        
        res1 = q.get()
        res2 = q.get()
        res = res1 + res2
        print("multicore: ", res)

def  normal():
        res = 0
        for _ in range(2):
                for i in range(100000):
                        res += i+i**2+i**3
        print("normal: ", res)

def multithread():
        q = mp.Queue() 
        t1 = td.Thread(target = job, args=(q,))
        t2 = td.Thread(target = job, args=(q,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()        
        res1 = q.get()
        res2 = q.get()
        res = res1+res2
        print("multithread: ", res)

if __name__ == '__main__':
        st = time.time()
        normal()
        st1=time.time()
        print("normal time: ", st1 -st)
        multithread()
        st2 = time.time()
        print("multithread time: ", st2 - st1)
        multicore()
        st3 = time.time()
        print("multicore time: ", st3 - st2)
        
       

##t1 = td.Thread(target = job, args=(1,2))
##t2 = td.Thread(target = job, args=(3,4))
##t1.start()
##t2.start()
##t1.join()
##t2.join()

        
