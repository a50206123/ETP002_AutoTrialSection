import time

def output_str(s: str, p: int) -> str :
    if p > 6 or p < 1 :
        return None
    
    p -= 1
    ps = [
        f'{"":-^1s} ',  f'{"":-^3s} ', f'{"":-^5s} ', f'{"":-^7s} ', f'{"":-^9s} ', f'{"":-^11s} '
    ]
    return ps[p] + s

def logging(log:str) -> str :
    
    print(log)

    return log + '\n'

def output_log(log) -> None :
    t = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

    with open(f'log_{t}.txt','w') as f :
        f.write(log)


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
    print(output_str('It\'s OK!!!', 1))

    log = ''

    log += logging('123')
    log += logging('345')
    output_log(log)