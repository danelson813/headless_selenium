from helpers.helpers import get_soup, parse_soup, set_url
import pandas as pd


results = []
for i in range(1, 49):
    url = set_url(i)
    soup = get_soup(url)
    dic = parse_soup(soup)
    results.extend(dic)

df = pd.DataFrame(results)
df.to_csv('data/Results.csv')
