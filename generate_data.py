import names
import random
import json
import requests

r = random.SystemRandom()
url = 'http://127.0.0.1:5000/data/persist'
header = {'content-type': 'application/json'}

def generate_data(list):
    names_total = int(list[0])
    tests_total = int(list[1])
    payload = { "students": []}
    rng = random.Random(42)

    for x in range(names_total):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        payload['students'].append( {
            "firstName": first_name,
            "lastName": last_name,
            "tests": {}
        } )

        test_var = payload['students'][x]['tests']
        for y in range(tests_total):
            test_result = rng.randint(25,101)
            test_score_val = "test" + str(y + 1)
            test_var[test_score_val] = test_result

    return json.dumps(payload)

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

    response = requests.post(url,json=payload,headers=header)

    print(response)

if __name__ == '__main__':
    main()
