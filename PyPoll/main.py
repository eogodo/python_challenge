import os
import csv

import_path = os.path.join('Resources','election_data.csv')

with open(import_path,'r',newline='') as csvfile:
    lines = csv.reader(csvfile, delimiter=",")

    csv_header = next(lines)

    candidates = []
    votes = 0

    for row in lines: 
        if len(candidates)== 0:
            candidates.append({'name':row[2],'votes':1})
        else:
            if any(candidate['name'] == row[2] for candidate in candidates):
                for candidate in candidates:
                    if candidate['name'] == row[2]:
                        candidate['votes'] += 1
                
            else:
                candidates.append({'name':row[2],'votes':1})

        votes += 1

    
    highestVote = 0
    winner=''

    for candidate in candidates:
        if highestVote < candidate['votes']:
            highestVote = candidate['votes']
            winner = candidate['name']

    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {votes}')
    print('-------------------------')
    for candidate in candidates: 
        print(f"{candidate['name']}: {'{:.3%}'.format((candidate['votes']/votes))} ({candidate['votes']})")
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
        


    output = open('output.txt','w')
    
    output.write('Election Results\n')
    output.write('-------------------------\n')
    output.write(f'Total Votes: {votes}\n')
    output.write('-------------------------\n')
    for candidate in candidates: 
        output.write(f"{candidate['name']}: {'{:.3%}'.format((candidate['votes']/votes))} ({candidate['votes']})\n")
    output.write('-------------------------\n')
    output.write(f'Winner: {winner}\n')
    output.write('-------------------------\n')
    output.close()

