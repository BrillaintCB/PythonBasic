print((1800-1440)/60)

"""
w
"""



def solution(record):
    answer = []
    userDict = dict()
    chatLog = []
    enterMsg = "%s님이 들어왔습니다."
    exitMsg = "%s님이 나갔습니다."
    for info in record:
        infoLst = info.split(' ')
        if infoLst[0] == 'Enter':
            userDict[infoLst[1]] = infoLst[2]
            chatLog.append([enterMsg,infoLst[1]])
        elif infoLst[0] == 'Leave':
            chatLog.append([exitMsg,infoLst[1]])
        elif infoLst[0] == 'Change':
            userDict[infoLst[1]] = infoLst[2]
    for log in chatLog:
        answer.append(log[0] % userDict[log[1]])
    return answer


#print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))


def solution1(record):
    answer = []
    userDict = dict()
    chatLogs = []
    enterMsg = "%s님이 들어왔습니다."
    leaveMsg = "%s님이 나갔습니다."
   
    for info in record:
        infoLists = info.split(" ")
        if infoLists[0] == 'Enter':
            userDict[inforlists[1]] = inforLists[2]
            chatLogs.append([enterMsg, infoLists[1]])
        print(infoLists[1])
    for log in chatLogs:
        answer.append(log[0] % userDict[log[1]])
    return answer


    #9:30 - 13:30       4 hours        32
    #14:30  - 18:00      3:30       8     28hours    


"""

"""

print(solution1(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))