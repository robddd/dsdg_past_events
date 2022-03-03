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
def write_lines_to_file(out_fn, lines_list):
    with open(out_fn, 'w') as f:
        for l in lines_list:
            f.write(f'{l}\n')


def make_event_page(row):
    date = pd.Timestamp(row['dateTime'])
    event_lines = [
        f'## {row["title"]}',
        f'### {date.day} {date.month_name()} {date.year}',
        f'RSVPs: {row["going"]} | Waiting: {row["waiting"]} | Event Type: {row["eventType"]} | [Meetup Event Link]({row["eventUrl"]})',
        '',
        row['description']
        ]
    write_lines_to_file(f'events/{row["meeting_id"]}.md', event_lines)
# %%

lines = [
    '# Data Science Discussion Group Auckland - Past Events'
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
    make_event_page(row)

# %%

write_lines_to_file('README.md', lines)
# %%
