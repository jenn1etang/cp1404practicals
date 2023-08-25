"""

Estimate time: 2hours
Actual time: 59mins
"""
from wikipedia import wikipedia

is_title_blank = False
while not is_title_blank:
    try:
        title = str(input(">>> "))
        if title == '':
            is_title_blank = True
        else:
            page = wikipedia.page(title, auto_suggest=False)
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)
    except wikipedia.PageError as error:
        print(error)
    except wikipedia.DisambiguationError as error:
        print(error)

