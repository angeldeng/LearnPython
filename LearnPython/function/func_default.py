def say(message,times=1):
    print(message*times)
say('Hello')    #没有指定默认times次数则只执行一次
say('world',5)  #指定次数则打印5次