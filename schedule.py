from utils import sendWechatMessage
from apscheduler.schedulers.background import BackgroundScheduler

class TaskSchedule():
    def __int__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def addTask(self, handler, time: str, args):
        """

        :param handler: 定时运行的函数
        :param time: 运行时间
        :param args: 函数参数
        :return: None
        """
        self.scheduler.add_job(handler, 'date', run_date=time, args=args)

s = TaskSchedule()