import requests
import json
import time

url = 'https://api.stackexchange.com/2.3/questions'

params = {
    'key' :'LvNpGbm8Cag)*kR76U5Bzw((',
    'page': 1,
    'pagesize': 100,
    'order': 'desc',
    'sort': 'creation',
    'site': 'stackoverflow'
}

def get_stackData():
    questions = []
    i=0
    
    for page in range(1, 1001):
        retry = True
        while retry: 
            params['page'] = page
            response = requests.get(url, params=params)
            if response.status_code == 200:
                retry = False
                questions += response.json()['items']
                i+= 1
                if(i%1000== 0):
                    print(i/1000,"% das perguntas obtidas")
            else:
                print("Timeout 10 min")
                time.sleep(360)
       
    filename = "100K_questions.json"
    with open(filename, "w") as f:
        json.dump(questions, f, indent=4)

if __name__ == '__main__':
    get_stackData()