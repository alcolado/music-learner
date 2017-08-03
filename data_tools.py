import numpy as np

def sample_generator(data, go_time):
    # generate a sample from data of length 2*go_time + 2
    # want to predict sample[go_time + 1 : 2*go_time + 2]
    # from sample[0 : go_time + 1]
    r = 2*go_time+2
    while(True):
        a = np.random.randint(len(data) - r)
        yield np.array(data[a:a+r])

def batch_generator(data, go_time, batch_size):
    sample = sample_generator(data, go_time)
    while(True):
        yield np.array([next(sample) for _ in range(batch_size)])