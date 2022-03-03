# %%
import re
# %%
def get_meeting_ids_from_line(line):
    """
    find all meeting ids in a string using regex, return a set
    """
    regex = r'Data-Science-Discussion-Auckland\/events\/([a-z0-9]{7,20})\/\"'
    ids = re.findall(regex, line)
    return set(ids)
# %%
# fn: created by going to 'https://www.meetup.com/Data-Science-Discussion-Auckland/events/past/'
# and scrolling to the bottom so all is showing in html - then saving the html locally
fn = 'raw_html/Past Events _ Data Science Discussion Auckland (Auckland, New Zealand) _ Meetup.html'

meeting_ids = set()
with open(fn) as f:
    for line in f:
        new_ids = get_meeting_ids_from_line(line)
        meeting_ids = meeting_ids.union(new_ids)
# %%
meeting_ids.discard('calendar')
meeting_ids
# %%
with open("raw_data/meeting_ids.csv", 'w') as f:
    f.write("\n".join(map(str, sorted(list(meeting_ids)))))
# %%
"""
Next copy meeting_ids.csv to a new file, open in as a spreadsheet
then get meetup info for each id using https://www.meetup.com/api/playground/#graphQl-playground

Event fields docs here: https://www.meetup.com/api/schema/#Event


query($eventId: ID) {
    event(id: $eventId) {
        title
        description
        dateTime
        eventUrl
        going
        waiting
        eventType
    }
}

{"eventId":"<meeting_id>"}
"""