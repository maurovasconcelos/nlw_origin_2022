#function return simple image in google images
from xml.etree.ElementTree import tostring


def get_image_url(query):
    url = 'https://www.google.com/search?q=' + query + '&source=lnms&tbm=isch'
    print(url)
    return url
  
get_image_url('abraço')

#create generic function to redirect to youtube
def generic_youtube_function(query):
    url = 'https://www.youtube.com/results?search_query=' + query
    print(url)
    return url
  
 



