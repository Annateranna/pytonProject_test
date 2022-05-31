def ekz():
    emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
              'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
              'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
              'yandex.ru': ['surface', 'google'],
              'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
              'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

    emails_l = []

    for k in emails:
        for i in emails[k]:
            emails_l += [i + '@' + k]

    print(*sorted(emails_l), sep='\n')


