import  requests


response = requests.post('http://127.0.0.1:5000/advertisements',
                          json= {'title': 'test',
                                'description': 'test adv',
                                'owner': ',Elena',
                             })
print(response.status_code)
print(response.json())

response = requests.get('http://127.0.0.1:5000/advertisements/41')
print(response.status_code)
print(response.json())


response = requests.delete('http://127.0.0.1:5000/advertisements/7')
print(response.status_code)
print(response.json())

