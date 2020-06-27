import shutil

shutil.copyfile('boxerase.py', 'boxerase3.py')

with open('boxerase3.py') as f:
    newText=f.read().replace('MYGROUP', 'MYGROUP3')
with open('boxerase3.py', "w") as f:
    f.write(newText)

with open('boxerase3.py') as f:
    newText2=f.read().replace('MYBOX', 'MYBOX3')
with open('boxerase3.py', "w") as f:
    f.write(newText2)