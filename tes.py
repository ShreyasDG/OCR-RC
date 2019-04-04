import subprocess
"""
cmd = ['echo', 'I like potatos']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: '  + e.decode('ascii'))
print('code: ' + str(proc.returncode))
"""

def returnImageText(path):
    #Pass the path to the tesseract api
    tess_list = ['1','5','12']
    for i in tess_list :
        cmd = ['tesseract',str(path),'op'+str(i),'--psm'+str(i)]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()
        print('Output : '+o.decode('ascii'))

#returnImageText('G:\Hackathon\opencv-text-recognition\images\example_01.jpg')