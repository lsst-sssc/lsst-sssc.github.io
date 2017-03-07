
import sys

def cmp1(a,b):
    return cmp(a[1],b[1])
with open('memberTemplate.html') as han:
    o_html = han.readlines()

with open('LSST-SSSC-SI-Responses_March717.csv') as han:
    data = han.readlines()

lines = []
for i in range(1, len(data)):
    html = o_html[:]
    s = data[i].split(',')
    #print s
    name = s[2]
    lastName = name.split()[-1]
    fileName = name.replace(' ','').replace('.','')
    email = s[4]
    if email == '':
        email = s[1]
    affil = s[3]
    sciInterests = "".join(s[5:]).replace('"','')

    #name
    html[36] = '                            '+html[36].replace("The member's name.", name)
    #affill
    html[37] = html[37].replace("The member's affiliation.", affil)[4:]
    #contact
    html[38] = html[38].replace("Email address.", email)[4:]
    #summary
    html[39] = html[39].replace("A short 3-4 sentence description of the member's science interests.", sciInterests)[4:]

    with open('{}.html'.format(fileName),'w+') as outHan:
        for j in range(len(html)):
            print >> outHan, html[j],

    lines.append([ '<li><a href = "membersHTML/{}.html">{}</a></li>'.format(fileName,name),lastName] )

lines.sort(cmp1)

print 'Remember to insert the following lines into membership.html'
print
for i in range(len(lines)):
    print lines[i][0]
