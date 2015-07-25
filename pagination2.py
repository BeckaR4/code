import math
class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection=collection
      self.items_per_page=items_per_page
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)      
  
  # returns the number of pages
  def page_count(self):
      return math.ceil(float(self.item_count())/float(self.items_per_page)) 

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      return math.ceil(page_index/self.items_per_page) if page_index<=self.collection else -1
     # return (self.item_count%self.items_per_page if page_index==self.page_count() else self.items_per_page)


collection = range(1,25)
helper = PaginationHelper(collection, 10)

print helper.page_index(23)
