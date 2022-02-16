from typing import List



def flatten_list(list_to_flatten):
    l = list()
    for el in list_to_flatten:
        if isinstance(el, (List)):
            for e in flatten_list(el):
                l.append(e)
        else:
            l.append(el)
    return l

