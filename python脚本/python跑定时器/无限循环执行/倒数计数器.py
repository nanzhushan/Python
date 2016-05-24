#coding:utf8
#倒数计数器
import threading
import time
class Timer(threading.Thread):
    """
    very simple but useless timer.
    """

    def __init__(self, seconds):
        self.runTime = seconds
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.runTime)
        print "Buzzzz!! Time's up!"


class CountDownTimer(Timer):
    """
    a timer that can counts down the seconds，一个计时器可以数秒
    """

    def run(self):
        counter = self.runTime
        for sec in range(self.runTime):
            print counter
            time.sleep(2.0)  #相隔时间,相隔2秒
            counter -= 1
        print "Done"


class CountDownExec(CountDownTimer):
    """
    a timer that execute an action at the end of the timer run.
    """

    def __init__(self, seconds, action, args=[]):
        self.args = args
        self.action = action
        CountDownTimer.__init__(self, seconds)

    def run(self):
        CountDownTimer.run(self)
        self.action(self.args)


def myAction(args=[]):
    print "执行我的动作和参数:"
    print args


if __name__ == "__main__":
    t = CountDownExec(10, myAction, ["hello", "world"])    #执行的总共次数
    t.start()