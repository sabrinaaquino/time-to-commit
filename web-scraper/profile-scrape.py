import requests
import datetime
import json

today = datetime.datetime.today().strftime('%Y-%m-%d')

with open('config.json', 'r') as f:
    config = json.load(f)

token = config['GITHUB_ACCESS_TOKEN']

def check_user_contribution(username, date):
  headers = {'Authorization': f'bearer {token}'}
  
  query = f"""
  {{
    user(login: "{username}") {{
      contributionsCollection(from: "{date}T00:00:00Z", to: "{date}T23:59:59Z") {{
        contributionCalendar {{
          totalContributions
        }}
      }}
    }}
  }}
  """
  
  request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
  if request.status_code == 200:
    result = request.json()
    totalContributions = result['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']
    return totalContributions > 0
  else:
    raise Exception(f"Query failed with status code {request.status_code}")

def main(): 
  username = 'CharlieGreenman'
  date = today
  has_contributed = check_user_contribution(username, date)

  if has_contributed:
    print('The user has contributed to at least one repository on today\'s date.')
  else:
    print('The user has not contributed to any repository on today\'s date.')

if __name__ == '__main__':
  main()