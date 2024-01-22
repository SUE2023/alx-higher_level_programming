#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    rel = 0
    for n in range(0, x):
        try:
            print("{}".format(my_list[n]), end='')
            ret += 1
        except (ValueError, TypeError):
            continue
        print("")
        return (rel)
