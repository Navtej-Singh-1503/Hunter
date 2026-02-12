'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

13/02/2026


mail - navtejsingh15032011@gmail.com

'''

def score_behavior(report):
    score = 0

    if report["timeout"]:
        score += 20

    if report["created_files"]:
        score += 10

    if report["stderr"]:
        score += 5

    return min(score, 100)

