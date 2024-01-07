from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'varshahindupur',
    'start_date': datetime(2024,1,4,10,00)
}

# dag = DAG(
#     'my_dag',
#     default_args=default_args,
#     schedule_interval='@daily',
# )

def get_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    # {'results': [{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Gabriel', 'last': 'Payne'}, 'location': {'street': {'number': 2752, 'name': 'Park Road'}, 'city': 'Roscrea', 'state': 'Wicklow', 'country': 'Ireland', 'postcode': 10840, 'coordinates': {'latitude': '3.2333', 'longitude': '-95.3523'}, 'timezone': {'offset': '+3:30', 'description': 'Tehran'}}, 'email': 'gabriel.payne@example.com', 'login': {'uuid': '5b949cf0-e20b-4f6e-b26a-fb3a38f1f3af', 'username': 'greenmouse987', 'password': 'brains', 'salt': '7kcT7A5S', 'md5': 'fe1d8aeb7d034668a46872517d434de6', 'sha1': '175d95e4f9e55ffbdfd0fa2c1f57e6f9a509f8dd', 'sha256': 'e2d85f822ed4dd77709071503570cb0f0e6c3ce6a8c3bd5fe254d5e9edfd6bf2'}, 'dob': {'date': '1983-10-04T02:06:52.513Z', 'age': 40}, 'registered': {'date': '2006-11-01T02:21:36.802Z', 'age': 17}, 'phone': '021-590-9269', 'cell': '081-045-0780', 'id': {'name': 'PPS', 'value': '0705979T'}, 'picture': {'large': 'https://randomuser.me/api/portraits/men/63.jpg', 'medium': 'https://randomuser.me/api/portraits/med/men/63.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/63.jpg'}, 'nat': 'IE'}], 'info': {'seed': 'c4906fb132f952f3', 'results': 1, 'page': 1, 'version': '1.4'}}
    res = res['results'][0]
    print(json.dumps(res, indent=1))
    return res

def format_data(res):
    data  = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {str(location['street']['name'])}, {str(location['city'])},  {str(location['state'])},  {str(location['country'])}"
    data['postcode'] = f"{str(location['postcode'])}"
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():
    import json
    res = get_data()
    res = format_data(res)
    # print(json.dumps(res, indent=3))
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_block_ms=5000)
    producer.send('users_created', json.dumps(res).encode('utf-8'))


with DAG('user_automation', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
        # dag=dag,
    )
    
# stream_data()