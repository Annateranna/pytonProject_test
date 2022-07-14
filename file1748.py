with open('logfile.txt', 'r', encoding='utf-8') as log_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    data = log_file.readlines()
    result = {}
    for line in data:
        line = line.split(', ')
        result[line[0]] = line[1] + ' ' + line[2].strip()
    for k in result.keys():
        times = result[k].split()
        hour_in = times[0].split(':')
        hour_out = times[1].split(':')
        if (int(hour_out[0]) * 60 + int(hour_out[1])) - (int(hour_in[0]) * 60 + int(hour_in[1])) >= 60:
            print(k, file=output_file)
        