import csv
with open('//Users//apple//Desktop//YELP_REVIEWS//code//Review Data- test cases//TestCase4- Positive Reviews with less star//testcase4_ChicagoPart1_ReviewText_Data.csv', 'r',encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        review_text=row['formed_review_text']
        print(review_text)
        print()
        if("&#34;" in  review_text):
            review_text=review_text.replace("&#34;","'")
        if("&#39;" in  review_text):
            review_text=review_text.replace("&#39;","'")

        sentences=review_text.split(".")
        final_text=''
        for i in sentences:
            final_text=final_text +"." +i.capitalize()
        final_text=final_text.lstrip(".")+"."    
        print(final_text)
        print()
            
