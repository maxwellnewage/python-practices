import requests


def get_simple():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f'Status Code: {response.status_code}')
    print(response.json())


def get_params():
    params = {
        'userId': 1
    }

    response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
    print(response.json())


def post_data():
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

    print(f'Status Code: {response.status_code}')
    print(response.json())


def get_headers():
    headers = {
        'Authorization': 'Bearer your_token_here',
        'Content-Type': 'application/json'
    }

    response = requests.get('https://jsonplaceholder.typicode.com/posts', headers=headers)
    print(response.json())


if __name__ == '__main__':
    get_params()
