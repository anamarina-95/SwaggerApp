import requests

def get_json():
    provided_input = input("Please provide a json form input:")

    response = requests.get(provided_input)
    res_json = response.json()
    r = res_json
    # print(r)
    print("............................................")
    a = r['paths']
    # print(a)
    for i in a.items():
        b = list(i)
        # print(".........................................")
        # print(b)
        c = b[0]
        print(c)

get_json()