from bs4 import BeautifulSoup

SIMPLE_HTML = ''' <html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. asdfkaljsdfjlasd<\p>
<p>Here's something to tell you that iam the best</p>
<ul>
      <li>sagar1</li>
      <li>sagar2</li>
      <li>sagar3</li>
      <li>sagar4</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')

print(simple_soup.find('h1'))
print(simple_soup.find('h1').string)



def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)

def find_list_items():
    """

    :rtype: nothing
    """
    list_items = simple_soup.find_all('li')
    print(list_items)
    list_contents = [temp.string for temp in list_items]
    print(list_contents)

def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)

def find_other_paragraph():
    paragraph = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraph if 'subtitle' not in p.attrs.get('class', [])]
    
    # we use get as it doesnt raise a key error like a dictionary and returns None (default) but we can change that 
    # change : by simply writing what to return next to the (',')


find_list_items()
find_title()
find_subtitle()


