import csv

with open('C:/Users/ykutta2/Desktop/YELP_REVIEWS/code/Review Data- test cases/TestCase5- Negative Reviews with more stars/testcase5_ChicagoPart1_ReviewText_Data.csv', 'r',encoding='utf8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        review_text=row['formed_review_text']
        char_count=len(review_text)
        if(char_count >=2000 or char_count <= 350):
            print(row['business_id'])
            print(review_text)
            print(char_count)
            print()
