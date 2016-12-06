library("ggplot2")
library("plyr")

sentimentData <- rbind(sentimentData1,sentimentData3,sentimentData4,sentimentData5,sentimentData6,sentimentData7,sentimentData8,sentimentData9,sentimentData10,sentimentData11,sentimentData12,sentimentData13,sentimentData14,sentimentData15,sentimentData16,sentimentData17,sentimentData18,sentimentData19,sentimentData20,sentimentData21,sentimentData22,sentimentData23,sentimentData24,sentimentData25,sentimentData26,sentimentData27,sentimentData28,sentimentData29)

#load data individually w/ for loop
for (i in 1:29) 
  {
  sentiment_name <- paste("sentimentData", i, sep="") 
  assign(sentiment_name, read.csv(filepaths[i], stringsAsFactors = FALSE))
}

#select columns
for (i in 1:29) 
  {
        sentiment_name <- paste("sentimentData", i, sep="")
        new_sentiment_name <- paste("sentimentData_", i, sep="")
        assign(new_sentiment_name, data.frame(sentiment_name["review_id"], sentiment_name["total_words"], sentiment_name["review_rating"],sentiment_name["need_inspection"]))
        rm(sentiment_name)
}
#bind/append sentimentData
sentimentData <- rbind(sentimentData_1,sentimentData_2)
for(i in 3:29){
  new_sentiment_name <- paste("sentimentData_",i,sep="")
  sentimentData <- rbind(sentimentData,new_sentiment_name)
}

        
#load reviews data
filenames <- dir("~/Desktop/data/") #or enter directory where files are located
filepaths <- paste("~/Desktop/data/",filenames,sep="") #enter same direc as in filenames
reviewsData <- do.call("rbind",lapply(filepaths,read.csv))

#get unique users
unique_users <- subset(reviewsData,!duplicated(reviewsData$user_id))

#get locations of unique users and of reviews - these results will depend on business location region
unique_users_locations_count <- count(unique_users, "user_location")  
reviews_locations_count <- count(reviewsData, "user_location")
  
#plot bar chart: number of reviews posted per user account
rev_barchart_data <- count(userData$review_count)
reviews_per_account_barchart <- ggplot(userData,aes(review_count,)) +geom_bar(stat="identity",colour="#2ECC71") + coord_cartesian(xlim=c(0,2500),ylim=c(0,650)) + xlab("Number of Reviews Posted") + ylab("Number of User Accounts") + ggtitle("Number of Reviews Posted Per User Account")

#get non-IL locations
not_IL_users <- subset(unique_users,!(grepl("IL",unique_users$user_location)))
outside_IL_count <- count(not_IL_locations$user_location)


#Distribution of Star Ratings
star_rating_count <- count(reviewsData$star_rating)
star_rating_barchart <- ggplot(star_rating_count,aes(x,freq)) + geom_bar(stat="identity",colour="#2ECC71") + xlab("Star Rating") + ylab("Number of Reviews") + ggtitle("Distribution of Star Ratings")

#TODO - plot barcharts: unique user locations, and overall review locations

#sentimentData chart: 
