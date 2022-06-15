import datetime
import glob
import os

import streamlit as st

path_to_entries = '/Users/connorguy/Documents/personal/daily_j/'

'''
# Daily Journal
'''

today = str(datetime.date.today())
st.subheader(today)

feeling = st.slider('How are you feeling today?', min_value=0, max_value=10, step=1)

accomplished = st.text_input('What\'s a win from yesterday?')

next30 = st.text_input('What\'s one thing you can work on in the next 30 minutes?')

todo = st.text_area('Needs to be done today:')

todo_md = ''
for line in todo.split('\n'):
    todo_md += '- [ ] ' + line.strip() + '\n'

md = f'# Entry: {today}\n### Feeling: {feeling}\n### Yesterday\'s Win:\n{accomplished}\n ### In The Next 30:\n{next30}\n ### Todo:\n{todo_md}'

if st.button('Let\'s get going!'):
    fileTitle = f'{today}.md'
    with open(path_to_entries+fileTitle, 'w') as f:
        f.write(md)
    st.balloons()
    st.success(f'Saved to {fileTitle}')


'''
---
## Previous Journal
'''

# get the most recent file from a directory
list_of_files = glob.glob(path_to_entries+'*.md')
latest_file = max(list_of_files, key=os.path.getctime)
# read file to string
with open(latest_file, 'r') as f:
    file_string = f.read()
st.write(file_string)
