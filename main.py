import pypdf, re, os, webbrowser, tkinter as tk, tkinter.filedialog

isfile = False

sched = {'A': {
    'text': "",
    'schedule': {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
        16: None,
        17: None,
        18: None,
        19: None,
        20: None,
        21: None,
        22: None,
        23: None,
        24: None,
        25: None,
        26: None
    }},
    'B': {
    "text": "",
    'day': 'B',
    'schedule': {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
        16: None,
        17: None,
        18: None,
        19: None,
        20: None,
        21: None,
        22: None,
        23: None,
        24: None,
        25: None,
        26: None
    }},
    'C': {
    'text': "",
    'day': 'C',
    'schedule': {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
        16: None,
        17: None,
        18: None,
        19: None,
        20: None,
        21: None,
        22: None,
        23: None,
        24: None,
        25: None,
        26: None
    }},
    "D": {
    'text': "",
    'day': 'D',
    'schedule': {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
        16: None,
        17: None,
        18: None,
        19: None,
        20: None,
        21: None,
        22: None,
        23: None,
        24: None,
        25: None,
        26: None
    }},
    "E": {
    'text': "",
    'day': 'E',
    'schedule': {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
        16: None,
        17: None,
        18: None,
        19: None,
        20: None,
        21: None,
        22: None,
        23: None,
        24: None,
        25: None,
        26: None
    }},
    "F": {
    'text': "",
    'day': 'F',
    'schedule': {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
        16: None,
        17: None,
        18: None,
        19: None,
        20: None,
        21: None,
        22: None,
        23: None,
        24: None,
        25: None,
        26: None
    }},
    "G": {
    'text': "",
    'day': 'G',
    'schedule': {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
        16: None,
        17: None,
        18: None,
        19: None,
        20: None,
        21: None,
        22: None,
        23: None,
        24: None,
        25: None,
        26: None
    }},
    "H": {
    'text': "",
    'day': 'H',
    'schedule': {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
        16: None,
        17: None,
        18: None,
        19: None,
        20: None,
        21: None,
        22: None,
        23: None,
        24: None,
        25: None,
        26: None
    }}
}

def getmod(time):
    if time == "08:30 AM":
        return 0
    elif time == "08:45 AM":
        return 1
    elif time == "09:00 AM":
        return 2
    elif time == "09:15 AM":
        return 3
    elif time == "09:30 AM":
        return 4
    elif time == "09:45 AM":
        return 5
    elif time == "10:00 AM":
        return 6
    elif time == "10:15 AM":
        return 7
    elif time == "10:30 AM":
        return 8
    elif time == "10:45 AM":
        return 9
    elif time == "11:00 AM":
        return 10
    elif time == "11:15 AM":
        return 11
    elif time == "11:30 AM":
        return 12
    elif time == "11:45 AM":
        return 13
    elif time == "12:00 PM":
        return 14
    elif time == "12:15 PM":
        return 15
    elif time == "12:30 PM":
        return 16
    elif time == "12:45 PM":
        return 17
    elif time == "01:00 PM":
        return 18
    elif time == "01:15 PM":
        return 19
    elif time == "01:30 PM":
        return 20
    elif time == "01:45 PM":
        return 21
    elif time == "02:00 PM":
        return 22
    elif time == "02:15 PM":
        return 23
    elif time == "02:30 PM":
        return 24
    elif time == "02:45 PM":
        return 25
    elif time == "03:00 PM":
        return 26
    elif time == "03:10 PM":
        return 27

root = tk.Tk()
root.title("reSchedule")

filepath = ""

def openfile():
    global filepath
    filepath = tkinter.filedialog.askopenfilename(
        initialdir = "/",
        title='File Select',
        filetypes=(("PDF Files", "*.pdf"),)
    )
    if filepath:
        convert["state"] = 'active'

def process():
    if filepath != "":
        reader = pypdf.PdfReader(filepath)
        full = ""
        for page in reader.pages:
            full += page.extract_text()
        full = full[full.find("A Day"):]
        full = full.replace(")0",")\n0").replace(")1", ")\n1")
        for i in re.findall('Day', full):
            # print(full[full.find("Day")-2])
            if full.find("Day", full.find("Day")+1) != -1:
                sched[full[full.find("Day")-2]]['text'] = full[full.find("Day")+4:full.find("Day", full.find("Day")+1)-3]
            else:
                sched[full[full.find("Day")-2]]['text'] = full[full.find("Day")+4:]
            # print(sched["A"]['text'])
            full = full[full.find("Day", full.find("Day")+1)-2:]
            # print(full)
        for day in sched.keys():
            print(day)
            clas = {}
            dtext = sched[day]['text']
            for line in dtext.splitlines():
                print(line)
                starttime = line[0:8]
                firstmod = getmod(starttime)
                endtime = line[line.find("M - ")+4:line.find("M - ")+12]
                lastmod = getmod(endtime)-1
                classname = line[line.find("    ")+4:line.find(" - ", line.find(" - ")+1)]
                room = line[line.find("(")+1:line.find(")")]
                subabbr = line[line.find(" - ", line.find(" - ")+1)+3:line.find(" - ", line.find(" - ")+1)+5]
                accabbrs = ['ss', 'la', 'ad', 'th', 'en', 'pe', 'sc', 'ma']
                if subabbr.lower() not in accabbrs:
                    subabbr = "OT"
                summary = {
                    'name': classname,
                    'firstmod': getmod(line[0:8]),
                    'lastmod': getmod(endtime)-1,
                    'room': room,
                    'sub': subabbr
                }
                print(f"starts at {firstmod} ends at {getmod(endtime)} name is {classname} room is {room} subject is {subabbr}")
                for mod in sched[day]['schedule'].keys():
                    if mod >= firstmod and mod <= lastmod:
                        sched[day]['schedule'][mod] = summary

        days = sched.keys()
        table = []
        r1 = ["Mod"]
        for day in days:
            r1.append(day)
        table.append(r1)
        for num in range(26):
            row = [num]
            for day in days:
                if sched[day]['schedule'][num] != None:
                    if sched[day]['schedule'][num]['firstmod'] == num:
                        cla = sched[day]['schedule'][num]
                        summary = {
                            'name': cla['name'],
                            'room': cla['room'],
                            'sub': cla['sub'],
                            'length': cla['lastmod']-cla['firstmod']+1
                        }
                        row.append(summary)
                else: 
                    row.append("")
            table.append(row)
        table.pop(0)
        html = "<table>"
        html += "<thead><tr>"
        for i in r1:
            html += f"<th>{i}</th>"
        html+="</tr></thead><tbody>"
        for row in table:
            html += "<tr>"
            for cel in row:
                if type(cel) == dict:
                    html += f"<td rowspan=\"{cel['length']}\" class=\"{cel['sub']}\"><p><strong>{cel['name']}</strong></p><p>{cel['room']}</p></td>"
                elif type(cel) == int:
                    html += f"<td>{cel}</td>"
                elif cel == '':
                    html += '<td></td>'
            html += "</tr>"
        html += "</tbody></table>"
        fullhtml = """<!DOCTYPE html>
        <html>
            <head>
                <title>Schedule</title>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        print-color-adjust: exact;
                    }
                    table {
                        margin-left: 0.5in;
                        margin-right: 0.5in;
                        width: 7.5in;
                    }
                    tr {
                        height: 0.33in;
                    }
                    td {
                        font-size: 13px;
                        margin: 0;
                        text-align: center;
                    }
                    table, tr, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                    }
                    .SS {
                        background-color: #81ccec;
                    }
                    .LA {
                        background-color: #b2a2a4;
                    }
                    .AD {
                        background-color: #ffc65e;
                    }
                    .TH {
                        background-color: #f35a78;
                    }
                    .EN {
                        background-color: #f3dcb0;
                    }
                    .PE {
                        background-color: #3d91d1;
                    }
                    .SC {
                        background-color: #75ddb8;
                    }
                    .MA {
                        background-color: #90abe0;
                    }
                    .OT {
                        background-color: #f2a8b5;
                    }
                </style>
            </head>
            <body>
                """+html+"""
            </body>
        </html>"""

        path = os.path.abspath('temp.html')
        url = f"file://{path}"

        with open(path, 'w') as f:
            f.write(fullhtml)
        webbrowser.open(url)



label = tk.Label(root, text="Select your file. Blackbaud -> Resources -> My A-H Schedule")
label.pack()

select = tk.Button(root, text="Choose file", command=openfile)
select.pack()

convert = tk.Button(root, text="Convert file", command=process)
convert.pack()

def switch():
    if isfile == False:
        convert["state"] = 'disabled'
    else:
        convert['state'] = 'active'

switch()

root.mainloop()