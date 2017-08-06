import json

with open('2.json', 'r') as f:
    data = json.load(f) 
    z = data['faces']
    j = z[0]['face_token']
    f.close

    f=open('4.txt','w+')
    f.write(j)
    f.close

