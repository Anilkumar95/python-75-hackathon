import threading

class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
    def run(self):
        print(str(self.thread_name) +"  "+ str(self.thread_ID));

h1 = thread("onions -kg", 90)
h2 = thread("potatoes -kg", 60);

h1.start()
h2.start()

print("Exit")
