import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')

#C = df['vote_average'].mean()
#m = df['vote_count'].quantile(0.9)
#q_articles = df.copy().loc[df['vote_count'] >= m]
#
#def weighted_rating(x, m=m, C=C):
#    v = x['vote_count']
#    R = x['vote_average']
#    return (v/(v+m) * R) + (m/(m+v) * C)

#q_articles['total_events'] = q_articles.apply(weighted_rating, axis=1)

q_articles = df.sort_values('total_events', ascending=True)

output = q_articles[['title','eventType', 'meta', 'url', 'contentType']].head(20).values.tolist()

q_articles.to_csv('trial.csv')