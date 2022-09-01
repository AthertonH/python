# script to assign questions to my Math 181 (Calc 1) group

def member_questions(problems):
    members = ["Harrison", "Cable", "Daniely", "Joshua", "Izaiah", "Nathan", "Destiny"]
    m_index = 0
    for p in range(1, problems):
       f p % 2 == 0:
            print(p, end=": ")
            if m_index/7 != 1:
                print(members[m_index])
                m_index += 1
            else:
                m_index = 0
                print(members[m_index])
        else:
            continue

