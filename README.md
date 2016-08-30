<a href="https://baikal.io/ajeetrocks100/predictive-spell-checker"><img src="https://s3-us-west-2.amazonaws.com/nerpa-static/baikal-banner.svg" alt="Sponsored by Baikal"/></a>

# Spell-checker
 <a href="https://baikal.io/ajeetrocks100/predictive-spell-checker"><img alt="support" src="https://baikal.io/badges/ajeetrocks100/predictive-spell-checker"/></a>
The aim is to make a self sufficient application that can detect errors and suggest with precision

A spell checker is needed because if the search query is spelled wrong, there will be no pertinent results found. Searching a database for an unrelated topic will not return useful results. We can help the user include useful search terms.
The spell checker that is currently used with string matching also has many problems. First, it does not detect if two letters in the search query are switched. It would detect a switch of two letters as two errors, and not one. Also, the spelling suggestions it gives are less than stellar. For instance, the search “appel” and the best match it found was “appear,” and not “apple.” This best match is a verb, which would not be searched on much. The current spell checker also does not take similar sounding syllables into account when searching for a good match.

LIMITATION of Predictive Spell Checker only checks the spelling of the query, it does actually provide any searching functionality. It does not provide any functionality for the actual searching, and only helps the user type what they mean to type. Also, algorithm cannot be perfect because a computer can never know what a user is thinking.
Biggest constraint is computational time. I might not have enough time to complete a professional grade spell checker. This time constraint poses as a larger problem, the more I create intermediate algorithms, such as the string matching algorithms. This spell checker will be implemented only to provide one word of text in the actual search engine asking if the user meant another search term.
