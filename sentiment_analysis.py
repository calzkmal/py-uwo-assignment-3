"""
CS1026A 2023
Assignment 03 
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
November 12, 2023
"""

# This function read every single keywords and scores, then return a dictionary
def read_keywords(keyword_file_name):
    # Initialize an empty dictionary to store keywords and their scores
    keywords_dict = {}
    
    
    try:
        # Open the keyword file for reading
        keywords = open(keyword_file_name, "r")
        
        # Iterate over each line in the keyword file
        for line in keywords:
            # Split the line into keyword and score using tab as the delimiter
            keyword, score_str = line.strip().split("\t")
            score = int(score_str)

            # Check if the keyword is already in the dictionary
            if keyword in keywords_dict:
                # If yes, append the score to the existing list of scores
                keywords_dict[keyword].append(score)
            else:
                # If not, create a new entry in the dictionary with the keyword and its score
                keywords_dict[keyword] = score
        
        # Return the populated keywords dictionary
        return keywords_dict

    except IOError:
        # Handle the case where the file cannot be opened
        print(f"Could not open file {keyword_file_name}")
        # Clear the dictionary and return it
        return {}


# Cleans tweet text by removing non-alphanumeric characters and converting to lowercase
def clean_tweet_text(tweet_text):
    try:
        # Check if passed parameter is a String or not.
        if not isinstance(tweet_text, str):
            raise ValueError("Input must be a String.")

        # Initialize a variable to store the argument
        tweet = tweet_text

        # Initialize an empty list to store cleaned characters
        cleaned_tweet = []

        # Iterate over each character in the tweet
        for s in tweet:
            # Check if the character is alphanumeric or a space
            if s.isalpha() or s.isspace():
                cleaned_tweet.append(s)
        
        # Join the cleaned characters into a single string
        cleaned_tweet = "".join(cleaned_tweet).lower()     
        # Return the result of lowering and joining characters
        return cleaned_tweet
    
    except ValueError as err:
        # Handle the case where the input is not a string
        print(f"Error, {str(err)}") 


# Calculates sentiment score for a tweet using a provided keyword dictionary
def calc_sentiment(tweet_text, keyword_dict):
    # Initialize sentiment score to 0
    sentiment_score = 0

    # Split the tweet text into multiple words
    words = tweet_text.split()

    # Iterate over each word in the tweet
    for word in words:
        # Check if the word is in the keyword dictionary
        if word in keyword_dict and keyword_dict[word] != "NULL":
            sentiment_score += keyword_dict[word]
    
    # Return the final sentiment score for the tweet
    return sentiment_score


# Classifies sentiment score into "Positive," "Negative," or "Neutral."
def classify(score):
    # Initialize a variable to store the final classification
    classify_score = score
    final_classification = ""

    # Determine the final classification based on the sentiment score
    if classify_score > 0:
        final_classification = "Positive"
    elif classify_score == 0:
        final_classification = "Neutral"
    else:
        final_classification = "Negative"

    # Return the final classification
    return final_classification


# Reads tweets from a file, processes them, and returns a list of dictionaries.
def read_tweets(tweet_file_name):
    # Initialize an empty list to store tweet dictionaries
    tweet_list = []

    try:
        # Open the tweet file for reading
        tweet_data = open(tweet_file_name, "r")
    
        # Iterate over each line in the tweet file
        for tweet in tweet_data:
            # Split the line into individual fields using comma as the delimiter
            tweets = tweet.strip().split(",")

            try:
                # Extract values for date, text, user, retweet, favorite, lang, country, state, city, lat, lon
                date, text, user, retweet, favorite, lang, country, state, city, lat, lon = (
                    str(tweets[0]),
                    str(tweets[1]),
                    str(tweets[2]),
                    int(tweets[3]) if tweets[3] != 'NULL' else 'NULL',
                    int(tweets[4]) if tweets[4] != 'NULL' else 'NULL',
                    str(tweets[5]),
                    str(tweets[6]),
                    str(tweets[7]),
                    str(tweets[8]),
                    float(tweets[9]) if tweets[9] != 'NULL' else 'NULL',
                    float(tweets[10]) if tweets[10] != 'NULL' else 'NULL'
                )
                
            except ValueError:
                # Handle the case where conversion to int or float fails
                date, text, user, retweet, favorite, lang, country, state, city, lat, lon = (
                    "NULL",
                    "NULL",
                    "NULL",
                    0,
                    0,
                    "NULL",
                    "NULL",
                    "NULL",
                    "NULL",
                    "NULL",
                    "NULL"
                )

            # Check if the lowered text is not "null"
            if text.strip().lower() != "null":
                # If yes, use the lowercase version of the text
                text = text.lower()
            else:
                # If not, set text to "null"
                text = "null"

            # Check if the content of retweet is not "NULL"
            if retweet != "NULL":
                # If yes, change the type of retweet to int
                retweet = int(retweet)

            # same goes for this
            if favorite != "NULL":
                favorite = int(favorite)

            # Create a dictionary for the current tweet
            uninserted_tweet = {
                'date': date,
                'text': clean_tweet_text(text),
                'user': user,
                'favorite': favorite,
                'retweet': retweet,
                'lang': lang,
                'country': country,
                'state': state,
                'city': city,
                'lat': lat,
                'lon': lon
            }

            # Copy the uninserted_tweet dictionary to a new dictionary
            new_tweet = {}
            for key, value in uninserted_tweet.items():
                new_tweet[key] = value
            # Append the new_tweet dictionary to the tweet_list
            tweet_list.append(new_tweet)

        # Return the newly modified tweet_list
        return tweet_list

    except IOError:
        # Handle the case where the file cannot be opened
        print(f"Could not open file {tweet_file_name}")
        # Clear the tweet_list and return it
        return []


# Generates a sentiment report based on provided tweet data and keyword dictionary
def make_report(tweet_list, keyword_dict):
    # Initialize variables for statistics and lists to store data
    keywords = keyword_dict
    total_tweet = len(tweet_list)
    avg_favorite = 0
    avg_retweet = 0
    avg_sentiment = 0
    favorite_tweet = 0
    retweet_tweet = 0
    negative_tweet = 0
    neutral_tweet = 0
    positive_tweet = 0
    total_favorite_sentiment = 0
    total_retweet_sentiment = 0
    total_sentiment = 0
    country_sentiment_data = {}

    # Iterate over each tweet in the tweet_list
    for tweet in tweet_list:
        tweet_text = tweet['text']

        # Check if the tweet text is not "null"
        if tweet_text != "null":
            # Calculate the sentiment score for the tweet
            sentiment_score = calc_sentiment(tweet_text, keywords)
            # Classify the sentiment score into positive, negative, or neutral
            tweet_value = classify(sentiment_score)

            # Increment the counters based on sentiment classification
            if tweet_value == "Positive":
                positive_tweet += 1
            elif tweet_value == "Negative":
                negative_tweet += 1
            else:
                neutral_tweet += 1
            
            # Check if the tweet has at least one favorite
            if tweet['favorite'] != 0:
                favorite_tweet += 1
                total_favorite_sentiment += sentiment_score
            
            # Check if the tweet has at least one retweet
            if tweet['retweet'] != 0:
                retweet_tweet += 1
                total_retweet_sentiment += sentiment_score
            
            # Check if the file has at least one tweet
            if tweet['text'] != 0:
                total_sentiment += sentiment_score

            # Check if the tweet has location information (country)
            if tweet['country'] != 'NULL':
                country = tweet['country']

                # Update the sentiment data for the country
                if country in country_sentiment_data:
                    country_sentiment_data[country]['count'] += 1
                    country_sentiment_data[country]['sentiment_score'] += sentiment_score
                else:
                    country_sentiment_data[country] = {'count': 1, 'sentiment_score': sentiment_score}

    # Calculate averages for favorite,
    if favorite_tweet != 0:
        avg_favorite = round(total_favorite_sentiment / favorite_tweet, 2)
    else:
        avg_favorite = "NAN"

    # retweet,
    if retweet_tweet != 0:
        avg_retweet = round(total_retweet_sentiment / retweet_tweet, 2)
    else:
        avg_retweet = "NAN"

    # and average sentiment
    if total_tweet != 0:
        avg_sentiment = round(total_sentiment / total_tweet, 2)
    else:
        avg_sentiment = "NAN"
    
    # Calculate the average sentiment for each country
    country_avg_sentiments = {}
    for country, data in country_sentiment_data.items():
        each_country_avg_sentiment = round(data['sentiment_score'] / data['count'], 2)
        country_avg_sentiments[country] = each_country_avg_sentiment

    # Sort the countries based on average sentiment in descending order
    sorted_countries = sorted(country_avg_sentiments.items(), key=lambda x: x[1], reverse=True)

    # Take the top five countries (or less if there are fewer than five)
    top_five_countries = sorted_countries[:5]

    # Create a string representation of the top five countries
    top_five_string = ', '.join([f"{country}" for country, avg_sentiment in top_five_countries])

    # Create the final sentiment report dictionary
    sentiment_report = {
        'avg_favorite': avg_favorite,
        'avg_retweet': avg_retweet,
        'avg_sentiment': avg_sentiment,
        'num_favorite': favorite_tweet,
        'num_negative': negative_tweet,
        'num_neutral': neutral_tweet,
        'num_positive': positive_tweet,
        'num_retweet': retweet_tweet,
        'num_tweets': total_tweet,
        'top_five': top_five_string
    }

    # Return the sentiment report
    return sentiment_report


# Writes a sentiment report to an output file
def write_report(report, output_file):
    try:
        # Open the output file for writing
        file_report = open(output_file, "w")
        
        # Write various statistics to the file
        file_report.write(f"Average sentiment of all tweets: {report['avg_sentiment']}\n")
        file_report.write(f"Total number of tweets: {report['num_tweets']}\n")
        file_report.write(f"Number of positive tweets: {report['num_positive']}\n")
        file_report.write(f"Number of negative tweets: {report['num_negative']}\n")
        file_report.write(f"Number of neutral tweets: {report['num_neutral']}\n")
        file_report.write(f"Number of favorited tweets: {report['num_favorite']}\n")
        file_report.write(f"Average sentiment of favorited tweets: {report['avg_favorite']}\n")
        file_report.write(f"Number of retweeted tweets: {report['num_retweet']}\n")
        file_report.write(f"Average sentiment of retweeted tweets: {report['avg_retweet']}\n")
        file_report.write(f"Top five countries by average sentiment: {report['top_five']}\n")
    
        # Print a message indicating the successful writing of the report
        print(f"Wrote report to {output_file}")

    except IOError:
        # Handle the case where the file cannot be opened
        print(f"Could not open file {output_file}")
    
    finally:
        # Close the file, whether the operation was successful or not
        file_report.close()