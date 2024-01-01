import pandas
data = pandas.read_csv("Squirrel_Data.csv")
data = data["Primary Fur Color"].value_counts()
data.to_csv("Fur_Color_with_value_count")
# counts "]=="Gray"])
# counts_cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])
# counts_black=len(data[data["Primary Fur Color"]=="Black"])
#
# data_dict ={
#     "Fur Color":["Gray","Cinnamon","Black"],
#     "Count":[counts_gray,counts_cinnamon,counts_black]
# }
# result = pandas.DataFrame(data_dict)
# result.to_csv("Fur Color")
