import mercari

# for item in mercari.search("東方 ふもふも"):
for item in mercari.search("hioki"):
    print("{}, {}".format(item.productName, item.productURL))