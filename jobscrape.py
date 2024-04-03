from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_filter(url):
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    company_name = []
    positions = []
    locations = []
    links = []
    table1 = soup.findAll('table')[0]
    table2 = soup.findAll('table')[1]
    tables = [table1, table2]

    lst = []  # Create an empty list to store dictionaries

    for table in tables:
        for row in table.tbody.findAll('tr'):
            first_column = row.findAll('td')[0].text
            company_name.append(first_column)
            second_column = row.findAll('td')[1].text
            positions.append(second_column)
            third_column = row.findAll('td')[2].text
            locations.append(third_column)
            fourth_column = row.findAll('td')[3].a.get('href')
            links.append(fourth_column)

    for index, location in enumerate(locations):
        if "Australia" in location:
            print(f"location: {location}\nRole: {positions[index]}\nCompany: {company_name[index]}\nApply: {links[index][2:-2]}")
            print("")

            # Create a dictionary for each row
            row_dict = {'Location': location, 'Role': positions[index], 'Company': company_name[index], 'Apply': links[index][2:-2]}
            lst.append(row_dict)  # Append the dictionary to the list

    df = pd.DataFrame(lst, columns=['Location', 'Role', 'Company', 'Apply'])
    df.to_csv('jobs.csv')
    print(df)

if __name__ == "__main__":
    url1 = "https://github.com/speedyapply/swe-college-jobs/blob/main/NEW_GRAD_INTL.md"
    url2 = "https://github.com/speedyapply/swe-college-jobs/blob/main/INTERN_INTL.md"
    urls = [url1, url2]
    for url in urls:
        get_filter(url)