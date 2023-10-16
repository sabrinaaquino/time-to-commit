import requests
from bs4 import BeautifulSoup
import datetime

today = datetime.datetime.today().strftime('%Y-%m-%d')

def check_user_contribution(username, date):
  """Checks if a user has contributed to any GitHub repository on a specific day.

  Args:
    username: The username of the user to check.
    date: The date to check (in YYYY-MM-DD format).

  Returns:
    True if the user has contributed to at least one repository on the specified date, False otherwise.
  """

  url = f'https://github.com/{username}/contributions?from={date}&to={date}'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Check if the user has any contributions on the specified date.
  contributions = soup.find_all('rect', class_='contribution calendar-day')
  for contribution in contributions:
    if contribution['data-date'] == date:
      return True

  return False

def main():
  """Checks if the user Sabrina has contributed to any repository on today's date."""

  username = 'sabrinaaquino'
  date = today

  has_contributed = check_user_contribution(username, date)

  if has_contributed:
    print('The user has contributed to at least one repository on today\'s date.')
  else:
    print('The user has not contributed to any repository on today\'s date.')

if __name__ == '__main__':
  main()