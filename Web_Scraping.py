from bs4 import BeautifulSoup
import requests, openpyxl

excel=openpyxl.Workbook()              #to create a new excel workbook
sheet=excel.active
sheet.title="Mobile list under 30,000"
sheet.append(['Model Name','Price','Spec'])     # Excel column Titles
spec_row_num=2

try:
    web_link=requests.get("https://www.flipkart.com/search?q=mobile+under+30000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+under+30000&requestId=009430c2-223b-413c-9827-8410c8b69a25").text
    soup= BeautifulSoup(web_link,'lxml')                   # to read HTML tags
    product_names=soup.find_all("div",class_="_13oc-S")    #to find the required product name

    for name in product_names:                             #to get the product model name
        model = name.find("div", class_="_4rR01T")
        Model_name=model.get_text(strip=True)
        spec_list = name.find_all("li", class_="rgWa7D")
        spec=[]
        for items in spec_list:                            # to get the model specifications in list
            spec.append(items.get_text(strip=True))
        price_line= name.find("div", class_="_30jeq3 _1_WHN1")          # to get the model price
        price=price_line.get_text(strip=True)

        sheet.append([Model_name,price])          # linking with excel

        for index, item in enumerate(spec, start=spec_row_num):  # to write each spec in separate row
            sheet.cell(row=index, column=3, value=item)
        spec_row_num=index
        spec_row_num+=1

except Exception as e:
    print(e)

excel.save("FlipKart Mobile List.xlsx")                  # to save excel file
