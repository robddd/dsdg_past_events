# %%
import json
import re

import pandas as pd
# %%
def make_data_tabular(df):
    """
    Convert JSON response to tabular data
    """
    new_cols = [
        'title', 'description', 'dateTime', 'eventUrl',
        'going', 'waiting', 'eventType'
    ]
    for nc in new_cols:
        df[nc] = ''

    for mid, mjson in zip(df['meeting_id'], df['meeting_json']):
        m_info = json.loads(mjson)
        for c in new_cols:
            df.loc[ df['meeting_id'] == mid, c ] = m_info['data']['event'][c]
    return df


# %%
def write_lines_to_file(out_fn, lines_list):
    """
    write a list of lines to a file
    """
    with open(out_fn, 'w') as f:
        for l in lines_list:
            f.write(f'{l}\n')


def make_md_link(display_text, url):
    return f'[{display_text}]({url})'

# %%
def is_url(text):
    url_re = r'^(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])$'
    if re.match(url_re, text) is None:
        return False
    else:
        return True


test_url1 = 'https://docs.python.org/3/library/re.html'
test_url2 = 'this.is.not.a.url.unfortunately'

assert is_url(test_url1)
assert is_url(test_url2) == False
# %%

def make_markdown_links(text):
    """
    Take some text, find any URLs and replace them with
    the markdown for a link
    """
    text_lines = text.split('\n')
    new_text_lines = []
    for line in text_lines:
        line_split = line.split(' ')
        new_line_split = []
        for word in line_split:
            if is_url(word):
                new_line_split.append(make_md_link(word, word))
            else:
                new_line_split.append(word)
        new_text_lines.append(' '.join(new_line_split))
    return '\n'.join(new_text_lines)


def make_event_page(row):
    """
    Make a markdown page for one event
    """
    date = pd.Timestamp(row['dateTime'])
    description = make_markdown_links(row['description'])
    event_lines = [
        f'## {row["title"]}',
        f'### {date.day} {date.month_name()} {date.year}',
        f'RSVPs: {row["going"]} | Waiting: {row["waiting"]} | Event Type: {row["eventType"]} | [Meetup Event Link]({row["eventUrl"]})',
        '',
        description
        ]
    write_lines_to_file(f'events/{row["meeting_id"]}.md', event_lines)
# %%

def generate_markdown_pages():
    df = pd.read_csv('raw_data/meeting_records.csv', low_memory=False)
    df = make_data_tabular(df)
    df['dateTime'] = pd.to_datetime(df['dateTime'])
    df = df.sort_values(by='dateTime', ascending=False)
    lines = ['# Data Science Discussion Group Auckland - Past Events']
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

    write_lines_to_file('README.md', lines)
# %%
if __name__ == '__main__':
    generate_markdown_pages()
# %%
