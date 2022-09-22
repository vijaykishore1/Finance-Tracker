lisst = [29, 42, 44, 66, 73, 91, 118, 121, 125, 141, 150, 157, 158, 170, 184, 198, 208, 213, 218, 223, 235, 243, 246,
         255, 259, 273, 280, 292, 305, 325, 328, 354, 384, 385, 397, 399, 404, 405, 417, 418, 418, 426, 446, 459, 460,
         464, 470, 482, 492, 509, 511, 531, 533, 536, 566, 574, 575, 582, 586, 596, 609, 611, 615, 622, 639, 642, 656,
         672, 703, 711, 727, 728, 728, 728, 731, 737, 761, 798, 799, 812, 823, 824, 836, 843, 879, 894, 896, 896, 909,
         913, 920, 925, 936, 940, 940, 941, 957, 966, 967, 971, 972, 991]
lisst.sort()
ub = len(lisst)
lb = 0


def binary_search(li, lb, ub):
    mid = int((lb + ub) / 2)
    if searchnum == li[mid]:
        print("element found at", mid)
    elif searchnum < li[mid]:
        ub = mid
        binary_search(li, lb, ub)
    elif searchnum > li[mid]:
        lb = mid + 1
        ub = len(li)
        binary_search(li, lb, ub)


searchnum = int(input("enter a number for searching: "))
binary_search(lisst, lb, ub)
