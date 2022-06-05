from pyodide import create_proxy

from js import setInterval, clearInterval


class Timer:
    def __init__(self, time, on_tick, on_end_timer):
        self.time = time
        self.on_tick = on_tick
        self.on_end_timer = on_end_timer

        self.__count = 0

        self.__timer = None

    def __increase_count(self):
        self.__count = self.__count + 1

    def stop(self):
        clearInterval(self.__timer)

        self.__timer = None

        self.on_end_timer()

    def __tick(self):
        self.__increase_count()
        self.on_tick(self.__count, self.time - self.__count)

        if self.time == self.__count:
            self.stop()
        else:
            pass

    def start(self):
        self.__timer = setInterval(create_proxy(self.__tick), 1000)
