#program to grade results
#run module

def grade(score):
    if score>= 70:
        letter = '1st'
    elif score >= 60:
        letter = '2:1'
    elif score >= 50:
        letter = '2:2'
    elif score >= 40:
        letter = '3rd'
    else:
        letter = 'F'
    return letter
        
