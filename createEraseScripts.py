import shutil

for z in range (9):
    for y in range (20):
        for x in range (20):
            if (z >= 7 and z <= 8):
                shutil.copyfile ('boxeraseE.py', 'boxeraseE%d%d%d.py' % (x, y, z))
                with open ('boxeraseE%d%d%d.py' % (x, y, z)) as f:
                    newText = f.read ().replace ('MYGROUP', 'MYGROUP%d%d%d' % (x, y, z))
                with open ('boxeraseE%d%d%d.py' % (x, y, z), "w") as f:
                    f.write (newText)
                with open ('boxeraseE%d%d%d.py' % (x, y, z)) as f:
                    newText2 = f.read ().replace ('MYBOX', 'MYBOX%d%d%d' % (x, y, z))
                with open ('boxeraseE%d%d%d.py' % (x, y, z), "w") as f:
                    f.write (newText2)
            elif (z >= 4 and z <= 6):
                shutil.copyfile ('boxeraseD.py', 'boxeraseD%d%d%d.py' % (x, y, z))
                with open ('boxeraseD%d%d%d.py' % (x, y, z)) as f:
                    newText = f.read ().replace ('MYGROUP', 'MYGROUP%d%d%d' % (x, y, z))
                with open ('boxeraseD%d%d%d.py' % (x, y, z), "w") as f:
                    f.write (newText)
                with open ('boxeraseD%d%d%d.py' % (x, y, z)) as f:
                    newText2 = f.read ().replace ('MYBOX', 'MYBOX%d%d%d' % (x, y, z))
                with open ('boxeraseD%d%d%d.py' % (x, y, z), "w") as f:
                    f.write (newText2)
            else:
                shutil.copyfile ('boxeraseP.py', 'boxeraseP%d%d%d.py' % (x, y, z))
                with open ('boxeraseP%d%d%d.py' % (x, y, z)) as f:
                    newText = f.read ().replace ('MYGROUP', 'MYGROUP%d%d%d' % (x, y, z))
                with open ('boxeraseP%d%d%d.py' % (x, y, z), "w") as f:
                    f.write (newText)
                with open ('boxeraseP%d%d%d.py' % (x, y, z)) as f:
                    newText2 = f.read ().replace ('MYBOX', 'MYBOX%d%d%d' % (x, y, z))
                with open ('boxeraseP%d%d%d.py' % (x, y, z), "w") as f:
                    f.write (newText2)

		