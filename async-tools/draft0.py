import asyncio
import pytest

async def t1():
    print('t1')
    # await asyncio.sleep(.5)
    loop = asyncio.get_event_loop()

async def t2():
    print('t2')
    # await asyncio.sleep(.5)
    loop = asyncio.get_event_loop()

class test_class():
    def __init__(self):
        pass

    def standard(self):
        """
        USE THIS
        """
        return self

    @classmethod
    def cl(cls):
        return cls

class event():
    def __init__(self,task=None,t=0,lim=None,*args,**kwargs):
        self.t=t
        self.task = task
        self.lim = lim
        if self.lim != None:
            self.limit = True
        else:
            self.limit = False
        self.loop = asyncio.get_event_loop()

    async def __call__(self,*args,**kwargs):
        await self.task()
        if self.limit:
            self.lim = self.lim - 1
            if self.lim > 0:
                asyncio.ensure_future(self())
                pass
            else:
                self.loop.stop()
        else:
            asyncio.ensure_future(self())
            pass

# just feed this async/not async funcion/callable class instance
class scheduler():
    def __init__(self):
        """
        send list of events - include manager by default
        """
        self.task_list = []
        self.loop = asyncio.get_event_loop() 

    def add(self,new_task,*args,**kwargs):
        self.task_list.append(new_task)

    def launch(self):
        """
        """
        for new_task in self.task_list:
            asyncio.ensure_future(new_task())
        self.loop.run_forever()

if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # a = event(lim=3)
    # asyncio.ensure_future(a(loop))
    # loop.run_forever()
    # print(a.lim)
    z = scheduler()
    z.add(event(t1,lim=15))
    z.add(event(t2,lim=15))
    z.launch()
    print("end")

    m = test_class()
    print(m)
    print(m.cl())
    print(m.standard())


