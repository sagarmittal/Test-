import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-6">
    <article class="product_pod">
        <div class="image_container">
                    <a href="url"><img src="relativePath" alt="A Light In The Attic" class="thumbnail"></a>
                    # alt is the alternative text to show if image doesnt load
                    #This contains the name of the object
        </div>          
        <p class="star-Rating Three">
                 <i class="icon-star"></i>  
                 <i class="icon-star"></i>  
                 <i class="icon-star"></i>  
                 <i class="icon-star"></i>  
                 <i class="icon-star"></i>
        </p>
        <h3><a href="url" title="A Light In The Attic">A Light In The...</a><h3>
        #the title has the name of the book as well
        <div class="product_price">
    <p class="price_color">$51.77</p>
<p class="instock availabilty">
    <i class="icon-ok"></i>
        In Stock
        #so this tells the availability of the stock
</p>
    <form>
         <button type="submit" class="btn btn-primary">
    </form> 
        </div>
    </article>
</li>

</body></html>
'''

soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_name():
    locator = 'article.product_pod h3 a'  # CSS Locator
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['title']
    # item_name = item_link.attrs.get('title', [])
    # both will work just fine
    print(item_name)


def find_item_nlink():
    locator = 'article.product_pod h3 a'  # CSS Locator
    item_link = soup.select_one(locator).attrs['href']
    print(item_link)


def find_item_price():
    locator = 'article.product_pod p.price_color'
    item_price = soup.select_one(locator).string  # $51.77

    print(item_price)
    pattern = '$([0-9]+\.[0-9]+)'
    matcher = re.search(pattern, item_price)
    print(matcher.group[0])  # $51.77
    print(float(matcher.group[1]*0.8))  # 51.77


def find_item_rating():
    locator = 'article.product_pod p.star-Rating'
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs['class']
    print(classes, " :", end=' ')
    rating_classes = [r for r in classes if r != 'star-Rating']
    print(rating_classes)
    print(rating_classes[0])


find_item_name()
find_item_nlink()
# find_item_price()
find_item_rating()
