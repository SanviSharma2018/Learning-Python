# dict name and score
# score  < 70 - Need Improvement
# score > 70 Satisfactory < 90
# score > 90 Excellent

dict = {"sanvi" :80, "madison" :65, "odin" :95}

for name,score in dict.items():
    if score < 70:
        print(f"{name} need improvement")
    elif score > 70 and score < 90:
        print(f"{name} Satisfactory")
    else:
        print(f"{name} Excellent")
