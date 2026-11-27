def grade(score):
    if score >= 90:
        return "优"
    elif score >= 80:
        return "良"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

print(grade(95), grade(85), grade(50))