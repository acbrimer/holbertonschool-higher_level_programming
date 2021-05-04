#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divided_list = []
    for i in range(list_length):
        res = 0
        try:
            item_1 = my_list_1[i]
            item_2 = my_list_2[i]
            try:
                "{0:d}{1:d}".format(item_1, item_2)
                try:
                    res = item_1 / item_2
                except:
                    print("division by 0")
            except:
                print("wrong type")
        except:
            print("out of range")
        finally:
            divided_list.append(res)
    return divided_list
