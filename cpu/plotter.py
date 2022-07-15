import time
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, memory):
        self.memory = memory
        self.online = False


    def start(self, IObuff):
        self.online = True
        plt.ion()
        self.fig = plt.figure(figsize=(8,5))
        self.ax =  self.fig.add_subplot(111)

        while self.online:
            bufValues = self.memory.readIObuff(IObuff)
            if bufValues == []:
                pass
            else:
                x = range(len(bufValues))
                y = bufValues

                line = self.ax.plot(x,y,'o')

                self.fig.canvas.draw()
                self.fig.canvas.flush_events()

            time.sleep(5)

        plt.close('all')

    def stop(self):
        self.online = False