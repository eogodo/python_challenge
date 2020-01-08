import os
import csv
import datetime

import_path = os.path.join('employee_data.csv')

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5)

with open(import_path,'r',newline='') as csvfile, open('output.csv', 'w', newline='') as csvexport:
    employees = csv.reader(csvfile, delimiter=",")
    csv_header = next(employees)
    csvwriter = csv.writer(csvexport, delimiter=",")
    csvwriter.writerow(['Emp Id', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    for employee in employees:
        name = employee[1].split()
        date = datetime.datetime.strptime(employee[2],'%Y-%m-%d').strftime('%m/%d/%Y')
        ssn = employee[3].split('-')
        
        csvwriter.writerow([employee[0],name[0],name[1],date, f'****-**-{ssn[2]}',us_state_abbrev[employee[4]]])
    

