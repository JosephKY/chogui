import chogui as cg
cg.borderless(True)
cg.windowsizemethod(2)
cg.windowsize(80,65)

menu = {
    "Meals": {
        "__config__":{
            'headercolor':'FF0000'
        },
        "Cheeseburger":{
            "price":150,
            "features":["Bread","Meat","Ketchup","Mustard","Onions"]
        },
        "Bacon Burger":{
            "price":270,
            "features":["Bread","Bacon","Meat","Ketchup","Mustard","Onions"]
        },
        "Big Burger":{
            "price":350,
            "features":["Bread","Meat","Meat","Ketchup","Mustard","Onions"]
        },
        "Chicken Sandwich":{
            "price":300,
            "features":["Bread","Chicken","Mayonaise","Lettuce","Pickles"]
        },
        "Spicy Chicken Sandwich":{
            "price":350,
            "features":["Bread","Chicken","Spicy Sauce","Pickles"]
        },
        "Chicken Nuggets":{
            "price":300,
            "features":["Sauce"]
        },
        "Chicken Tenders":{
            "price":370,
            "features":["Sauce"]
        },
    },
    "Sides": {
        "__config__":{
            'headercolor':'19BC00'
        },
        "Fries":{
            "price":200,
            "features":["Salt","Ketchup"]
        },
        "Fry Basket":{
            "price":430,
            "features":["Salt","Ketchup"]
        },
        "Mac and Cheese":{
            "price":320,
            "features":[]
        },
        "Mashed Potatoes":{
            "price":350,
            "features":["Gravy","Salt"]
        },
        "Red Beans and Rice":{
            "price":300,
            "features":[]
        },
    },
    "Drinks": {
        "__config__":{
            'headercolor':'0000FF'
        },
        "Coca-Cola":{
            "price":100,
            "features":["Ice"]
        },
        "Dr. Pepper":{
            "price":100,
            "features":["Ice"]
        },
        "Sprite":{
            "price":100,
            "features":["Ice"]
        },
        "Mountain Dew":{
            "price":150,
            "features":["Ice"]
        },
        "Root Beer":{
            "price":100,
            "features":["Ice"]
        },
        "Sweet Iced Tea":{
            "price":150,
            "features":["Ice"]
        },
        "Unsweet Iced Tea":{
            "price":130,
            "features":["Ice"]
        },
    },
    "Desserts": {
        "__config__":{
            'headercolor':'FF00FF'
        },
        "Ice Cream Cone":{
            "price":160,
            "features":["Chocolate Dunked"]
        },
        "Sundae":{
            "price":350,
            "features":["Chocolate Fudge","Sprinkles","Cherry"]
        },
        "Funnel Cake":{
            "price":480,
            "features":["Powdered Sugar","Chocolate Drizzle","Sprinkles"]
        },
        "Apple Pie":{
            "price":700,
            "features":[]
        },
    }
}

categoryIndexCount = 0

for categoryRawIndex,categoryName in enumerate(menu):
    categoryObject = menu[categoryName]
    categoryLabel = cg.Label()
    categoryLabel.content(categoryName)
    categoryLabel.fontcolor("FFFFFF")
    categoryLabel.color(categoryObject["__config__"]['headercolor'])
    categoryLabel.pos(0,0,0,8*categoryIndexCount)
    categoryLabel.size(0,15,0,len(menu))
    categoryLabel.bordersize(0)
    categoryLabel.render()
    categoryIndexCount += 1

cg.finish()
