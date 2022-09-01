def member_questions(problems):
    members = ["Harrison", "Cable", "Daniely", "Joshua", "Izaiah", "Nathan", "Destiny"]
    m_index = 3
    for p in range(1, problems):
        if p % 2 == 0:
            print(p, end=": ")
            if m_index != 6:
                print(members[m_index])
                m_index += 1
            else:
                print(members[m_index])
                m_index = 0
        else:
            continue