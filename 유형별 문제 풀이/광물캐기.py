def calculate_fai(group, target):
    
    score_table = {
        "dia":{"diamond":1,"iron":1,"stone":1},
        "iron": {"diamond": 5, "iron": 1, "stone": 1},
        "stone": {"diamond": 25, "iron": 5, "stone": 1}
    }
    
    return sum(score_table[target][mineral] for mineral in group)

def solution(picks, minerals):
    answer = 0
    
    groups = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]
    
    # 각 그룹의 피로도를 계산하여 저장
    group_fatigues = []
    for group in groups:
        group_fatigues.append({
            "dia": calculate_fai(group, "dia"),
            "iron": calculate_fai(group, "iron"),
            "stone": calculate_fai(group, "stone")
            #"group": group
        })
    
    print(group_fatigues)
    
    group_fatigues.sort(key=lambda x: (x["stone"], x["iron"], x["dia"]), reverse=True)
    
    total_fatigue = 0
    
    # 곡괭이를 사용하여 피로도 계산
    for group_info in group_fatigues:
        if picks[0] > 0:  # 다이아몬드 곡괭이 사용
            total_fatigue += group_info["dia"]
            picks[0] -= 1
        elif picks[1] > 0:  # 철 곡괭이 사용
            total_fatigue += group_info["iron"]
            picks[1] -= 1
        elif picks[2] > 0:  # 돌 곡괭이 사용
            total_fatigue += group_info["stone"]
            picks[2] -= 1
        else:
            break
    
    answer = total_fatigue
    return answer

print(solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))