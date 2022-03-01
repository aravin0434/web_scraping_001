from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=13840;type=tournament')
soup = BeautifulSoup(html_text.text, 'lxml')

runs_table = soup.table

columns = []
for column_title in runs_table.find_all('th'):
    columns.append(column_title.text)

runs_data = runs_table.find_all("td")

table_list = []
start = 0
end = 3

for i in range(20):
    Player, Mat, Inns= runs_data[start:end]
    Runs = runs_data[end + 1]
    Team = runs_data[start + 14]
    table_list.append([Player.text, Mat.text, Inns.text, Runs.text, Team.text])
    start += 15
    end += 15


cols = columns[0:3]
cols.append(columns[4])
cols.append('Team')
top_20_scorers = pd.DataFrame(table_list, columns=cols)
print(top_20_scorers)