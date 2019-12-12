import bibtexparser
import fnmatch
import requests
import json
import re
import scholarly

search_query = scholarly.search_author('Will Handley')
def citation_number(title):
    search_query = scholarly.search_pubs_query(title + 'Handley')
    return next(search_query).citedby

# Search for my ORCID bibcodes
token="KZS9f4psBs6gaNst2jSlX8fWI8jV9CWqnPm3E40E"
orcid="0000-0002-5866-0445"
r = requests.get("https://api.adsabs.harvard.edu/v1/search/query",
                 headers={'Authorization': 'Bearer ' + token},
                 params={"q":"orcid:"+orcid, "fl":"bibcode,title", "rows":1000}
                 )
bibcodes = [x['bibcode'] for x in r.json()['response']['docs']]

# Get my ORCID papers in bibtex format
r = requests.post("https://api.adsabs.harvard.edu/v1/export/bibtex", 
                  headers={'Authorization': 'Bearer ' + token},
                  data=json.dumps({"bibcode":bibcodes})
                  )
bibtex = r.json()['export']

# Correct bibtex errors
error = r"{Mac{\`\i}as-P\{{\'e}rez}"
correct = r"{Macias-Perez}"
bibtex = bibtex.replace(error,correct)

# Write to a raw bibtex file for reference
open("papers_raw.bib","w").write(bibtex)

# Read raw if necessary
with open('papers_raw.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Parse into database
#bib_database = bibtexparser.loads(bibtex)
#val = bib_database.entries_dict['2014PhRvD..89f3505H']



for key, val in bib_database.entries_dict.items():
    title = val['title']
    if 'Exploring cosmic origins with CORE' in title:
        del val['author']# = '{{CORE Collaboration}}'
    elif fnmatch.fnmatch(title, '*Planck*results*'):
        del val['author']# = '{{Planck Collaboration}}'
    elif fnmatch.fnmatch(val['author'], '*{Planck Collaboration}*'):
        del val['author']# = '{{Planck Collaboration}}'
    else:
        val['author'] = re.sub(r'{Handley},\s(.*?)\s*(and|}|$)', r'{\\textbf{Handley}}, {\\textbf{\1}} \2', val['author'])

    try:
        if val['journal'] == 'Journal of Cosmology and Astroparticle Physics':
            val['journal'] = r'\jcap'
        if val['journal'] == 'Journal of Cosmology and Astro-Particle Physics':
            val['journal'] = r'\jcap'
        if val['journal'] == 'Monthly Notices of the Royal Astronomical Society':
            val['journal'] = r'\mnras'
        if val['journal'] == 'The Journal of Open Source Software':
            val['journal'] = r'\joss'
        if val['journal'] == 'Journal of Mathematical Physics':
            val['journal'] = r'\jmap'
        if val['journal'] == 'Astronomy and Astrophysics':
            val['journal'] = r'\aap'
        if val['journal'] == 'Physical Review D':
            val['journal'] = r'\prd'
        if val['journal'] == 'arXiv e-prints':
            val['journal'] = r'arXiv'
            val['volume'] = val['pages'][6:]
            del val['pages']
    except KeyError:
        pass


with open('papers.bib', 'w') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)

