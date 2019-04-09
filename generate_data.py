import names
import random

def generate_data(list):
    names_total = int(list[0])
    tests_total = int(list[1])
    

def get_user_input():
    params = []
    students = input("For how many students do you want data? ")
    tests = input("For how many tests do you want data? ")

    params.append(students)
    params.append(tests)

    return params

def main():
    data = get_user_input()
    payload = generate_data(data)
    

if __name__ == '__main__':
    main()
