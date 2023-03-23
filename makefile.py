from datetime import datetime

date = datetime.now().strftime('#Today\'s Date: %Y-%m-%d')

myFileName = 'README.md'

#print(myFileName)

file = open('/home/anindya/.datetoday/DateToday/'+myFileName, 'w')

file.write(date)

file.close()
