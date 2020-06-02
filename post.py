import datetime
import os

title = input('Post Title: ')

dt = datetime.datetime.now()

date = dt.strftime('%Y-%m-%d')
print(date)

f = open('./_posts/' + date + '-' + title + ".md", "w")

head = '---\nlayout: post\ntitle: "' + title + '"\ndate: ' + date + ' ' + dt.strftime('%X') + ' ' + '-0400' + '\ncategories: update\n---'

f.write(head)

print('Created new post')

f.close()

os.system('cd _posts && "' + date + '-' + title + '.md"')