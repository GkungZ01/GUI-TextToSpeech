import threading

class Thread(object):
    def __init__(self,target, args = ()):
        if target is None:
            print("Error: target")
            return False
        self.__threadPlaying = False
        self.__StoppedObjects = None
        self.__thread = threading.Thread(target=target, args=args)
        
    def __startThread(self):
        if self.__threadPlaying : return
        self.__threadPlaying = True
        self.__thread.start()
        self.__thread.join()
        self.__stopThread()
        
    def __stopThread(self):
        self.__threadPlaying = False
        if self.__StoppedObjects is not None:
            self.__StoppedObjects()
        
    def Start(self):
        threading.Thread(target=self.__startThread).start()
        
    def Stopped(self, callback):
        self.__StoppedObjects = callback
        