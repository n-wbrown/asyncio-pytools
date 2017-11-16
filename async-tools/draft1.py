import asyncio
import pytest
import datetime

async def t1():
    print('t1:',datetime.datetime.utcnow())
    await asyncio.sleep(.1)
    loop = asyncio.get_event_loop()

async def t2():
    print('t2:',datetime.datetime.utcnow())
    await asyncio.sleep(.1)
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
    """event is like a wrapper for an sync function that makes it repeatable
    """
    def __init__(self,task=None,interval=None,lim=None,*args,**kwargs):
        self.interval=interval
        self.task = task
        self.lim = lim
        if self.lim != None:
            self.limit = True
        else:
            self.limit = False
        self.loop = asyncio.get_event_loop()

    async def __call__(self,time_target=None,*args,**kwargs):
        if time_target==None:
            time_target=datetime.datetime.utcnow()
        await self.task()
        if self.limit:
            self.lim = self.lim - 1
            if self.lim <= 0:         
                self.loop.stop()
                return

        if self.interval:
            delay = self.interval - (datetime.datetime.utcnow()-time_target)
            print(delay)
            await asyncio.sleep(delay.total_seconds())
            next_target = delay + time_target
        asyncio.ensure_future(self(time_target=next_target))



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
    z.add(event(t1,lim=15,interval=datetime.timedelta(seconds=3)))
    z.add(event(t2,lim=15,interval=datetime.timedelta(seconds=3)))
    z.launch()
    print("end")

    m = test_class()
    print(m)
    print(m.cl())
    print(m.standard())


