import numpy as np

def calculate(list_9d):
    if len(list_9d) != 9:
        raise ValueError ( "List must contain nine numbers.")
    convd_list = np.array(list_9d).reshape(3, 3)

    ret_dict = {
        'mean': [convd_list.mean(axis=0).tolist(), convd_list.mean(axis=1).tolist(), convd_list.mean().tolist()],
        'variance': [convd_list.var(axis=0).tolist(), convd_list.var(axis=1).tolist(), convd_list.var().tolist()],
        'standard deviation': [convd_list.std(axis=0).tolist(), convd_list.std(axis=1).tolist(), convd_list.std().tolist()],
        'max': [convd_list.max(axis=0).tolist(), convd_list.max(axis=1).tolist(), convd_list.max().tolist()],
        'min': [convd_list.min(axis=0).tolist(), convd_list.min(axis=1).tolist(), convd_list.min().tolist()],
        'sum': [convd_list.sum(axis=0).tolist(), convd_list.sum(axis=1).tolist(), convd_list.sum().tolist()]
    }

    return ret_dict