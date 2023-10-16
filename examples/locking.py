import threading, time


class SharedVar:
    def __init__(self) -> None:
        self.var = {}
        self.cv = threading.Condition()

    
class producer:
    def __init__(self, shared: SharedVar) -> None:
        self.shared_variable = shared

    def func(self):
        self.shared_variable.cv.acquire()
        try:
            self.shared_variable.var+= 1
            time.sleep(2*10)
            self.shared_variable.cv.notify()
        finally:
            self.shared_variable.cv.release()

        

class consumer:
    def __init__(self, shared: SharedVar, msg: str) -> None:
        self.shared_variable = shared
        self.msg = msg

    def func(self):
        timestamp = time.time()
        # while not self.shared_variable.cv.acquire():
        #     self.shared_variable.cv.wait(10)
        self.shared_variable.cv.acquire()
        print(time.time() - timestamp)
        print(self.msg)
        print(self.shared_variable.var)
        self.shared_variable.cv.release()
            

if __name__ == '__main__':
    shared = SharedVar()
    shared = SharedVar()
    producer = producer(shared)
    consumerA = consumer(shared, 'A')
    consumerB = consumer(shared, 'B')
    print(id(producer.shared_variable))
    print(id(consumerA.shared_variable))
    print(id(consumerB.shared_variable))
    t1 = threading.Thread(target=producer.func)
    t2 = threading.Thread(target=consumerA.func)
    t3 = threading.Thread(target=consumerB.func)
    t1.start()
    t2.start()
    t3.start()

        
