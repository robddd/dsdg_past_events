# %%
import json

import pandas as pd
# %%
df = pd.read_csv('raw_data/meeting_records.csv', low_memory=False)
# %%
def make_data_tabular(df)
    new_cols = ['title', 'description', 'dateTime', 'eventUrl',
        'going', 'waiting', 'eventType'
    ]
    for nc in new_cols:
        df[nc] = ''

    for mid, mjson in zip(df['meeting_id'], df['meeting_json']):
        m_info = json.loads(mjson)
        for c in new_cols:
            df.loc[ df['meeting_id'] == mid, c ] = m_info['data']['event'][c]
    return df

df = make_data_tabular(df)

# %%
df['dateTime'] = pd.to_datetime(df['dateTime'])
df = df.sort_values(by='dateTime', ascending=False)
df.head()
# %%
lines = [
    '# Data Science Discussion Group Auckland',
    '## Past Events'
]

current_year = None
for i, row in df.iterrows():
    date = pd.Timestamp(row['dateTime'])
    if date.year != current_year:
        current_year = date.year
        lines.append('')
        lines.append(f'### {current_year}')
    link_name = f'{date.day} {date.month_name()} - {row["title"]}'
    link_url = f'events/{row["meeting_id"]}'
    lines.append(f'* [{link_name}]({link_url})')

# %%
with open('README.md', 'w') as f:
    for l in lines:
        f.write(f'{l}\n')
# %%
