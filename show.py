import rational_numbers


def show_line(L):
    for nums in L:
        if (type(nums) != rational_numbers.rationals):
            print('NA', end = ' ')
        else:
            rational_numbers.rationals.disp(nums)
    print()


def show(L):
    for  line in L:
        for nums in line:
            if (type(nums) != rational_numbers.rationals):
                print('NA', end = ' ')
            else:
                rational_numbers.rationals.disp(nums)
        print()
    print()
