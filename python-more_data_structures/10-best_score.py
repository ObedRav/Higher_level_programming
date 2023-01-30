#!/usr/bin/python3
def best_score(a_dictionary):
    if (not a_dictionary):
        return None
    temp = 0
    best_score_student = ""
    for key, value in a_dictionary.items():
        if (temp < value):
            best_score_student = key
        temp = value
    return best_score_student


'''
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
'''
