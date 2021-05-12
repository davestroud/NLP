#%%
import nltk
import urllib.request
nltk.download()

#%%
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
# %%
html = response.read
print(html)
# %%
