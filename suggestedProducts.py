# Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of searchWord is typed.

# Input: products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mouse"
# Output: [
#     ["mobile", "moneypot", "monitor"],
#     ["mobile", "moneypot", "monitor"],
#     ["mouse", "mousepad"],
#     ["mouse", "mousepad"],
#     ["mouse", "mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile", "moneypot", "monitor", "mouse", "mousepad"]
# After typing m and mo all products match and we show user["mobile", "moneypot", "monitor"]
# After typing mou, mous and mouse the system suggests["mouse", "mousepad"]

from typing import List
from itertools import islice

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    # Strategy:
    # Sort the list of products
    # For each char added of searchWord -> check if prefix exists and get first 3

    products = sorted(products)

    prefix = ""
    suggestions = []

    for c in searchWord:
        prefix += c
        filter = (product for product in products if product.startswith(prefix))

        topHits = list(islice(filter, 3))
        suggestions.append(topHits)
    
    return suggestions

if __name__ == "__main__":
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(suggestedProducts(products, searchWord))
