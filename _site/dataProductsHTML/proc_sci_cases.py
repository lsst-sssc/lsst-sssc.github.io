
import sys

with open('sciCaseTemplate.html') as han:
    html = han.readlines()

with open('HH_sciCases_Feb20.txt') as han:
    data = han.readlines()

lines = []
for i in range(len(data)):
    s = data[i].split()
    if len(s) == 1:
        try:
            ind = int(float(s[0]))

            title = " ".join(data[i+1].split()[:])

            s = data[i+2].split()
            if len(s) <2:
                summary = 'TBD'
            else:
                summary = " ".join(s[1:])

            s = data[i+4].split()
            if len(s) < 2:
                procedure = 'TBD'
            else:
                procedure = " ".join(s[1:])

            s = data[i+6].split()

            obsMetadata = ['None']
            L1L2Prod = ['None']
            obsGeo = ['None']
            L3Prod = ['None']
            if len(s) < 4:
                obsMetadata = ['None']
                L1L2Prod = ['None']
                obsGeo = ['None']
                L3Prod = ['None']
            else:
                if 'observation metadata' in data[i+6]:
                    obsMetadata = data[i+6].split('observation metadata ')[1].split(')')[0][1:].split(',')
                else:
                    obsMetadata = ['None']
                if 'L1/L2 products ' in data[i+6]:
                    L1L2Prod = data[i + 6].split('L1/L2 products ')[1].split(')')[0][1:].split(',')
                else:
                    L1L2Prod = ['None']
                if 'observation geometry' in data[i+6]:
                    obsGeo = data[i + 6].split('observation geometry ')[1].split(')')[0][1:].split(',')
                else:
                    obsGeo = ['None']
                if 'custom derived detection parameters' in data[i+6]:
                    L3Prod = data[i + 6].split('custom derived detection parameters ')[1].split(')')[0][1:].split(';')
                else:
                    L3Prod = ['None']

            print 'Index:', ind
            print 'Title:', title
            print 'Summary: ',summary
            print 'Procedure:', procedure
            print 'Obs Metadata:',obsMetadata
            print 'L1/L2 Products:',L1L2Prod
            print 'Obs. Geom.:',obsGeo
            print 'L3 Products:',L3Prod
            print

            #title
            s = html[35].split('h4')
            s[1] = '> {} </'.format(title)
            html[35] = "h4".join(s)+'\n'

            #summary
            s = html[36].split('</b>')
            s[-1] = "</b> {} </p>".format(summary)
            html[36] = "".join(s)+'\n'

            #procedure
            s = html[37].split('</b>')
            s[-1] = "</b> {} </p>".format(procedure)
            html[37] = "".join(s)+'\n'

            #observation metadata
            s = ''
            for j in range(len(obsMetadata)):
                s +='<li> {} </li>\n'.format(obsMetadata[j])
            html[40] = s


            #l1/l2 products
            s = ''
            for j in range(len(L1L2Prod)):
                s +='<li> {} </li>\n'.format(L1L2Prod[j])
            html[45] = s

            #observation geometry
            s = ''
            for j in range(len(obsGeo)):
                s +='<li> {} </li>\n'.format(obsGeo[j])
            html[50] = s

            #L3 outputs
            s = ''
            for j in range(len(L3Prod)):
                s +='<li> {} </li>\n'.format(L3Prod[j])
            html[55] = s



            with open('{}.html'.format(ind), 'w+') as outHan:
                for i in range(len(html)):
                    print >> outHan, html[i],

            lines.append(  '<li><a href = "dataProductsHTML/{}.html">{}</a></li>'.format(ind,title)  )
            #line = '<li><a href = "dataProductsHTML/1.html">Phase functions of asteroids</a></li>'
        except:
            pass


for i in range(len(lines)):
    print lines[i]