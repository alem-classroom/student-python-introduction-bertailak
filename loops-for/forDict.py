def reverse_dict(dict):
    # swap keys and values within dict and return dict
    dict2 = {}
    for i in dict.keys():
        dict2[dict[i]]= i
    return dict2
