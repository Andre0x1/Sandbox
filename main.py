import requests
import json
import time

url = 'https://api.stackexchange.com/2.3/questions'

params = {
    'page': 1,
    'pagesize': 100,
    'order': 'desc',
    'sort': 'creation',
    'site': 'stackoverflow'
}

def get_stackData():
    questions = []
    i=0
    
    for page in range(1, 101):
        retry = True
        while retry: 
            params['page'] = page
            response = requests.get(url, params=params)
            if response.status_code == 200:
                retry = False
                questions += response.json()['items']
                i+= 1
                print(i,"% das perguntas obtidas")
            else:
                print("Timeout 30 segs")
                time.sleep(1)
       
    filename = "questions.json"
    with open(filename, "w") as f:
        json.dump(questions, f, indent=4)

if __name__ == '__main__':
    get_stackData()