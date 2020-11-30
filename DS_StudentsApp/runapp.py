import requests
import json

DS_Students = {"student01":"Juan Peralta","course01":"data science","grade01":98,\
     "student02":"Luis Alejo","course02":"data science","grade02":97,\
         "student03":"Janet Perez","course03":"data science","grade3":95}

# POST request
headers = {"Content-Type": "application/json"}
r = requests.post("http://127.0.0.1:5000/", params=DS_Students, headers=headers)
json_resp = json.loads(r.text)
json_resp

# POST request
new_student = {"student04": "Elston Bell", "course04":"data science", "grade4": 98}
headers = {"Content-Type": "application/json"}
r = requests.post("http://127.0.0.1:5000/", params=new_student, headers=headers)
json_resp = json.loads(r.text)
json_resp

# DELETE request
delete_student = {"student03":"Janet Perez","course03":"data science","grade3":95}
headers = {"Content-Type": "application/json"}
r = requests.delete("http://127.0.0.1:5000/", params=delete_student, headers=headers)
json_resp = json.loads(r.text)
json_resp
