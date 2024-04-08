grocery_list=[
    "egg tart"
    "potato chips"
    "sandwich"
    "sausage"
    "rtx 4070 super"
] 
# for every item in the list:
#     * {grocery item}
#     * {grocery item}
#     * {grocery item}
for item in grocery_list:
    if item.lower()== "rtx 4070 super":
        print ("Hugo can't buy the 4070")
        break
    print(f,"* {item}")
