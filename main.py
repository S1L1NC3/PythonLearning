import os


def switch_case(case):
    return {
        '1': os.system('python TryCatch.py')
    }[case]


switch_case(input("Pick Page To Run: "))
