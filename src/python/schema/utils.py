import aiohttp

token = 'AAA3HhYFxEBQAV3qW-eCBXNeyKndFu4fddGTs5KxbaGI7hXGs1LRFOY99C6W_sAFeamMb3lc8w6yPLN5ccWeGnyLkBbftL6ex8JLKbOBt59zGSYR7TUUp__4'

async def get_token(username, password):
    async with aiohttp.ClientSession(headers={"Accept": "application/json", "Content-Type": "application/json"}) as client:
        data = {
            "auth": {
                "RAX-AUTH:domain": {"name": "Rackspace"},
                "RAX-AUTH:rsaCredentials": {
                    "username": username,
                    "tokenKey": password
                }
            }
        }

        async with client.post("https://identity-internal.api.rackspacecloud.com/v2.0/tokens", json=data) as response:
            value = await response.json()
            return value['access']['token']

async def get_projects():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }
    async with aiohttp.ClientSession(headers=headers) as client:
        async with client.get('https://passwordsafe.corp.rackspace.com/projects') as response:
            value = await response.json(content_type = 'application/vnd.passwordsafe.project+json')
            return value

async def get_project(project_id):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }
    async with aiohttp.ClientSession(headers=headers) as client:
        async with client.get('https://passwordsafe.corp.rackspace.com/projects/{}'.format(project_id)) as response:
            value = await response.json(content_type = 'application/vnd.passwordsafe.project+json')
            return value

async def get_project_users(project_id):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }
    async with aiohttp.ClientSession(headers=headers) as client:
        async with client.get('https://passwordsafe.corp.rackspace.com/projects/{}/users'.format(project_id)) as response:
            value = await response.json(content_type = 'application/vnd.passwordsafe.user+json')
            return value

async def create_project(name, description):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }
    data = {
        'project': {
            'name': name,
            'description': description
        }
    }
    async with aiohttp.ClientSession(headers=headers) as client:
        async with client.post('https://passwordsafe.corp.rackspace.com/projects/', json=data) as response:
            value = await response.json(content_type = 'application/vnd.passwordsafe.project+json')
            return value

async def delete_project(project_id):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }
    async with aiohttp.ClientSession(headers=headers) as client:
        async with client.delete('https://passwordsafe.corp.rackspace.com/projects/{}'.format(project_id)) as response:
            print('Response code - {}'.format(response.status))
            return response.status == 204           
