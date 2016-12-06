> unique_users <- subset(reviewsData,!duplicated(reviewsData$username))
> unique_user_locations <- subset(unique_users,!duplicated(unique_users$user_location))
> histogram <- qplot(unique_users$no_of_reviews_posted,geom="histogram",binwidth=1,main="Histogram of Number of Reviews Per User",xlab="num_of_reviews (per user)",ylab="review count", xlim=c(0,2000),ylim=c(0,1250))
> histogram
Warning message:
  Removed 44 rows containing non-finite values
(stat_bin). 
> histogram <- histogram + ylim=c(0,600)
Error in histogram <- histogram + ylim = c(0, 600) : 
  could not find function "<-<-"
> histogram <- histogram + ylim(c(0,600))
Scale for 'y' is already present. Adding another scale for 'y', which will replace the existing scale.
> histogram
Warning messages:
  1: Removed 44 rows containing non-finite values (stat_bin). 
2: Removed 3 rows containing missing values (geom_bar). 
> histogram <- histogram + ylim(c(0,450))
Scale for 'y' is already present. Adding another scale for 'y', which will replace the existing scale.
> histogram
Warning messages:
  1: Removed 44 rows containing non-finite values (stat_bin). 
2: Removed 6 rows containing missing values (geom_bar). 
> histogram <- histogram + ylim(c(0,400))
Scale for 'y' is already present. Adding another scale for 'y', which will replace the existing scale.
> histogram
Warning messages:
  1: Removed 44 rows containing non-finite values (stat_bin). 
2: Removed 8 rows containing missing values (geom_bar). 

> head(unique_user_locations)
business_id     username                user_id
1 pinstripes-chicago-2 Stephanie L. aRdO2gkzbDDyun1JUyuT4Q
2 pinstripes-chicago-2     David C. 9YIEYRTM1-esrPtfTVU4LA
3 pinstripes-chicago-2    Andrea B. fAbKgdbKkn4Px8kG54OVDQ
5 pinstripes-chicago-2      Rana R. wRHdvRFEEvaOLTpNZHQxvA
6 pinstripes-chicago-2    Rachel W. BB82Cs08Os6RkB_e0tMTkw
8 pinstripes-chicago-2    Stacey L. wd3xoNaDLib8dhQ7BxUl6g
user_location elite_status hasprofile_pic no_of_checkins
1   Oak Lawn, IL            0              1              1
2 Pittsburgh, PA            1              1              1
3    Chicago, IL            1              1              0
5  San Diego, CA            1              1              1
6   Bartlett, IL            1              1              0
8    Madison, WI            1              1              1
no_of_friends no_of_reviews_posted              review_id star_rating
1            17                   22 OY121UUBaRZTQz6csd_4Xw           5
2            70                  109 2q7reEv6YV1Y_QbSocXq2w           4
3           140                  247 _xJH5ERBj9hTYNT5EXVRKw           3
5            74                  110 yTEmmxxeDwlNK05UEu6BkQ           5
6            61                  177 wRP6gyjk-HxpDSYdbK_PVw           4
8          1022                  457 wrP18hLvUrbx7EVnukLh4A           4
review_date
1  10/31/2016
2  11/15/2016
3    11/07/16
5    07/08/16
6  10/30/2016
8    06/06/16
... <truncated>
  1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ... <truncated>
  2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ... <truncated>
  3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ... <truncated>
  5                                                                                                                                                                                                                                                                                                                                                                         Dined at Pinstripes for the 4th of July. Pre-paid dinner $79, 4- course meal, taxes &amp; gratuity included. Awesome views of the fireworks away from the rowdy crowds is well worth it &amp; we left stuffed! Warning, the building is near the Pier, so you may want to wait for a couple of hours before leaving the building. \n\nGot there a little before 730PM &amp; was seated on the patio within minutes. Our server was great from beginning to end, made sure we were enjoying ourselves &amp; made sure to tell us not to rush anything since fireworks started at 930PM. We got bread upon sitting. Alcoholic beverages-of course- were not incl... <truncated>
  6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ... <truncated>
  8 While being touristy in Chicago with my boyfriend and his mom, we came to Pinstripes because it was within walking distance from Navy Pier and the Ogilvie train station. It was a solid find! \n\nIt&#39;s got an upscale twist on bar games with bowling, bocce, and decidedly not-bar-quality food. Unfortunately we didn&#39;t have time to enjoy a round of bocce before heading back to our train, but we did enjoy a leisurely meal. \n\nOn our way in we were given cards good for a free appetizer with entree purchase. Being Wisconsinites, we opted for the fried mozzarella. What&#39;s a meal without cheese, after all? It appeared they breaded and fried mozzarella pearls which made for a nice bite-sized snack without the unmanageable strings of melted cheese sticks tend to result in. \n\nFor my lunch I went for the Grilled Chicken Club. It was really tasty for the most part except for the bites that were heavy on the charbroil and/or fennel. A little fennel put an interesting spin on the common ... <truncated>
  > rm(unique_user_locations)
> user_location_count <- subset(unique_users,count(unique_users$user_location))
Error in subset.data.frame(unique_users, count(unique_users$user_location)) : 
  'subset' must be logical
> user_location_counts <- count(unique_users, "user_location")
> head(user_location_counts)
user_location freq
1                                     4
2 3̬me arrondissement, Lyon, France    1
3                      Abilene, TX    1
4                     Abingdon, MD    1
5                     Accokeek, MD    1
6                        Acton, MA    1
> user_location_counts_subset <- subset(user_location_counts,freq>2)
> user_location_counts_subset <- subset(user_location_counts,freq>10)
> user_location_counts_subset <- subset(user_location_counts,freq>20)
> head(user_location_counts_subset)
user_location freq
48         Ann Arbor, MI   36
58 Arlington Heights, IL   42
61         Arlington, VA   26
71           Atlanta, GA   67
78            Aurora, IL   50
80            Austin, TX   58
> barchart <- ggplot(data=user_location_counts_subset,aes(x=user_location,y=freq)) + geom_bar(stat="identity")
> barchart
> user_location_counts_subset <- subset(user_location_counts,freq>100)
> barchart <- ggplot(data=user_location_counts_subset,aes(x=user_location,y=freq)) + geom_bar(stat="identity")
> barchart
> user_location_counts_subset <- subset(user_location_counts,freq>50)
> barchart <- ggplot(data=user_location_counts_subset,aes(x=user_location,y=freq)) + geom_bar(stat="identity")
> barchart
> barchart <- barchart + theme(axis.text.x = element_text(angle=90))
> barchart
> histogram
Warning messages:
  1: Removed 44 rows containing non-finite values (stat_bin). 
2: Removed 8 rows containing missing values (geom_bar). 