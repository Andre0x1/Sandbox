import os
import json
import math
from datetime import datetime
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

def calc_visibility():
    
    with open('100K_questions.json', 'r') as file:
        data = file.read()
    
        objects = json.loads(data)
    
    visibility_normal = []
    visibility_rust = []
    for questions in objects:
        if 'rust' in questions['tags']:
            visibility_rust.append(questions['view_count'])
        else:
            visibility_normal.append(questions['view_count'])
    
    normal_mean = statistics.mean(visibility_normal)
    rust_mean = statistics.mean(visibility_rust)

    print("Media normal", normal_mean, "Media Rust", rust_mean)

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



    
        



if __name__ == '__main__':
    calc_quant()
    calc_visibility()
    calc_answer()