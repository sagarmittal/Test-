from bs4 import BeautifulSoup

SIMPLE_HTML = ''' <html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. asdfkaljsdfjlasd</p>
<p>Here's something to tell you that I am the Best</p>
<ul>
      <li>sagar1</li>
      <li>sagar2</li>
      <li>sagar3</li>
      <li>sagar4</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


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


def find_paragraph():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)
    print("These are the <p> which aren't in subtitle class :", end=' ')
    paragraph = simple_soup.find_all('p')
    print([p.string.title() for p in paragraph if 'subtitle' not in p.attrs.get('class', [])])


find_list_items()
find_title()
find_paragraph()
