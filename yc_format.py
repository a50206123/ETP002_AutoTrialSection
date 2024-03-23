import time

def logging(log:str, level:int = 0) -> str :
    if level != 0 :
        level -= 1

        pre_string = [
            f'{"":-^1s} ',  f'{"":-^3s} ', f'{"":-^5s} ', f'{"":-^7s} ', f'{"":-^9s} ', f'{"":-^11s} '
        ]

        try :
            log = pre_string[level] + str(log)
        except :
            raise Exception(f'{"Level ERROR":*^30s}')

    print(log)
    return log + '\n'


def output_log(log:str, mode:int = 0) :
    #### mode = 0 --> To write the all log to file now
    #### mode = 1 --> Return IO to add log any time 
    t = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

    if mode == 0 :   
        with open(f'log_{t}.txt','w') as f :
            f.write(log)

    elif mode == 1 :
        f = open(f'log_{t}.txt','a')
        f.write(log)
        return f


def sub_trial(trial) -> str:
    sub_trial = 'th'

    if trial in [11, 12] :
        pass
    elif trial % 10 == 1 :
        sub_trial = 'st'
    elif trial % 10 == 2 :
        sub_trial = 'nd'
    elif trial % 10 == 3 :
        sub_trial == 'rd'

    return sub_trial

if __name__ == '__main__' :
    ####################################
    #### TEST ZONE
    ### logging with level
    ### output_log & mode = 0 (default)
    # log = ''

    # log += logging('123', level = 7)
    # log += logging(456, level = 2)
    # # output_log(log)

    # print(log)

    ####################################
    #### TEST ZONE
    ### output_log & mode = 1
    # f = output_log("123", mode = 1)
    # f.write('1111')