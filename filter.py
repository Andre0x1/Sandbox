import os
import json
import math
import datetime
import statistics

def calc_quant():
    with open('100K_questions.json', 'r') as file:
        data = file.read()
    
    objects = json.loads(data)

    sum_total = 0
    javascript = 0
    Go = 0
    Python = 0
    Java = 0
    other = 0
    RUST = 0

    for questions in objects: 
        sum_total += 1   
        if 'javascript' in questions['tags']:
            javascript += 1
        elif 'go' in questions['tags']:
            Go += 1
        elif 'python' in questions['tags']:
            Python += 1
        elif 'java' in questions['tags']:
            Java += 1
        elif 'rust' in questions['tags']:
            RUST += 1
        else: 
            other += 1

    
    data = {
        "Count_javascript" : javascript,
        "Count_go" : Go,
        "Count_Python" : Python,
        "Count_Java" : Java,
        "Count_RUST" : RUST,
        "Count_other": other,
        "Sum_total": sum_total
    }

    perc = (data['Count_RUST']* 100)/data['Sum_total']
    print("Porcentagem de perguntas Rust = " , perc ,"%")

    perc = (data['Count_Python']* 100)/data['Sum_total']
    print("Porcentagem de perguntas Python = " , perc ,"%")

    perc = (data['Count_go']* 100)/data['Sum_total']
    print("Porcentagem de perguntas go = " , perc ,"%")

    perc = (data['Count_javascript']* 100)/data['Sum_total']
    print("Porcentagem de perguntas javascript = " , perc ,"%")

    perc = (data['Count_Java']* 100)/data['Sum_total']
    print("Porcentagem de perguntas Java = " , perc ,"%")

    perc = (data['Count_other']* 100)/data['Sum_total']
    print("Porcentagem de perguntas other = " , perc ,"%")

def calc_visibility(name):
            filename = name + '_questions.json'
            with open(filename, 'r') as file:
                    data = file.read()
        
            objects = json.loads(data)
            list_date_dif = []
            date_dif = 0
            int = 0
            date = datetime.datetime(2022, 4, 2, 23, 28, 29)
            reversed_data = list(reversed(objects))
            z_score_data = []
            for questions in reversed_data:
                    if int == 0 :
                        list_date_dif.append(date_dif)
                        date = datetime.datetime.utcfromtimestamp(questions['creation_date'])
                        int +=1
                    else: 
                        new_date = datetime.datetime.utcfromtimestamp(questions['creation_date'])
                        date_dif = (new_date - date).seconds
                        date = new_date
                        list_date_dif.append(date_dif/60)
                
            mean = statistics.mean(list_date_dif)
            stdev = statistics.stdev(list_date_dif)
            variance = statistics.variance(list_date_dif)

            for data in list_date_dif:
                z_score = (data - mean) / stdev
                z_score_data.append(z_score)
            
            count = 0
            for number in z_score_data:
                if number > 0.25:
                    count += 1

            percentage = count / len(z_score_data) * 100

            print(mean)
            print(variance)
            print(f"{percentage:.2f}% foram criadas frequentemente")


def calc_answer():
    with open('100K_questions.json', 'r') as file:
        data = file.read()
    
        objects = json.loads(data)
    

    total = len(objects)
    rust_answer = 0
    rust_total = 0
    other_answer = 0
    others_total = 0
    for questions in objects:
        if 'rust' in questions['tags']:
            rust_total +=1
            if questions['is_answered'] is True:
                rust_answer += 1
        else:
            others_total +=1
            if questions['is_answered'] is True:
                other_answer +=1

    perc_rust = (rust_answer*100)/rust_total
    perc_normal = (other_answer*100)/others_total
    
    print("Porcentagem de questions respondidas de RUST ",perc_rust,"%")
    print("Porcentagem de questions respondidas de outras linguagens ",perc_normal,"%")


def get_data(type):

    with open('100K_questions.json', 'r') as file:
        data = file.read()
    
        objects = json.loads(data)
        
    list = []
    for questions in objects:
        if type in questions['tags']:
            list.append(questions)
    
    filename = type +"_questions.json"
    with open(filename, "w") as f:
        json.dump(list, f, indent=4)

        
def get_all_data():       
    get_data("rust")
    get_data("javascript")
    get_data("go")
    get_data("python")
    get_data("java")



if __name__ == '__main__':
    get_all_data()
 
