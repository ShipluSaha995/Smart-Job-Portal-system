def calculate_score(req, usr, exp):
    weigths={"python":10, "sql":8, "c++":6,"java":7}

    req_list=req.lower().split(",")
    usr_list=usr.lower().split(",")

    score=0

    for skill in req_list:
        skill=skill.strip()
        if skill in usr_list:
            score+=weigths.get(skill, 5)

    

    score+=exp*3
    return score



def top_k(data, k=3):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[j][1]>data[i][1]:
                data[i],data[j]=data[j],data[i]
    
    return data[:k]