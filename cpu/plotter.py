import time
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, memory):
        self.memory = memory


    def plot(self, IObuff):
        plt.ion()
        fig = plt.figure()
        ax =  fig.add_subplot(111)

        while True:
            bufValues = self.memory.readIObuff(IObuff)
            if bufValues == []:
                pass
            else:
                x = range(len(bufValues))
                y = bufValues

                line = ax.plot(x,y,'o')

                fig.canvas.draw()
                fig.canvas.flush_events()

            time.sleep(5)