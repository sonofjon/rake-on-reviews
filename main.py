from requests_html import HTMLSession
from rake_nltk import Rake

# English example
def extract_text():
    s = HTMLSession()
    url = 'https://career.odevo.com/jobs/1652504-linux-sys-admin'
    r = s.get(url)
    # Select an element with a CSS selector
    # return r.html.find('body > main > section > div.mx-auto.prose.font-company-body.overflow-hidden', first=True).text
    # Select an element with search
    return r.html.find('div', containing='Zabbix', first=True).text
    # Select an element with XPath
    # return r.html.xpath('/html/body/main/section[2]/div', first=True).text


# Swedish example
# def extract_text():
#     s = HTMLSession()
#     url = 'https://www.arbetsgivarverket.se/jobba-statligt/jobb/databasadministrator/'
#     r = s.get(url)
#     # Select an element with XPath
#     return r.html.xpath('/html/body/div/div/div/div[2]/article/div[1]', first=True).text


print(extract_text())

r = Rake()
# r = Rake(language='swedish')

r.extract_keywords_from_text(extract_text())
for rating, keyword in r.get_ranked_phrases_with_scores():
    if rating > 5:
        print(round(rating), keyword)
