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


class ParsedItemLocator:
    """
    Locator for the item in the HTML page.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-Rating'


class ParsedItem:
    """
    Takes in HTML Page and finds properties and items in it
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocator.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocator.LINK_LOCATOR  # CSS Locator
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string  # $51.77

        print(item_price)
        pattern = '$([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group[1] * 0.8)  # 51.77

    @property
    def rating(self):
        locator = ParsedItemLocator.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-Rating']
        return rating_classes[0]


item = ParsedItem(ITEM_HTML)
print(item.rating)
print(item.link)