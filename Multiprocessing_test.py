import multiprocessing as mp
##import threading as td
from queue import Queue

def job(q, a,b):
        print("This is a job for a+b= ", a+b, "\n")
        
        for i in range(1000):
                res += i+i**2+i**3
        q.put(res)
                

##t1 = td.Thread(target = job, args=(1,2))
##t2 = td.Thread(target = job, args=(3,4))
##t1.start()
##t2.start()
##t1.join()
##t2.join()

if __name__ == "__main()__":
        q = mp.Queue() 
        p1 = mp.Process(target = job, args=(q,5,6, ))
        p2 = mp.Process(target = job, args=(q,7,8, ))
        p1.start()
        p2.start()
        p1.join()
        p2.join()        
        res1 = q.get()
        res2 = q.get()
        print("res1+res2= ", res1+res2)
