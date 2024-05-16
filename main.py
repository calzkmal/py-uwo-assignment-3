"""
CS1026A 2023
Assignment 03 
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
November 12, 2023
"""

# Import the sentiment_analysis module
from sentiment_analysis import *

# Get user input for keyword, and tweet file name, and process the result to report file
def main():
    
    # Get the keyword filename from the user
    keyword_filename = input("Input keyword filename (.tsv file): ")
    
    # Check if the filename has a ".tsv" extension,
    if not keyword_filename.endswith(".tsv"):
        raise Exception("Must have tsv file extension!")
    
    # same one for this,
    tweet_filename = input("Input tweet filename (.csv file): ")
    if not tweet_filename.endswith(".csv"):
        raise Exception("Must have csv file extension!")

    # and the same one for this
    report_filename = input("Input report filename (.txt file): ")
    if not report_filename.endswith(".txt"):
        raise Exception("Must have txt file extension!")

    # Read tweets from the tweet file and keywords from the keyword file
    tweet_list = read_tweets(tweet_filename)
    keyword_dict = read_keywords(keyword_filename)

    # Generate and then write the sentiment report using the provided functions
    final_report = make_report(tweet_list, keyword_dict)
    write_report(final_report, report_filename)
    
# Call the main function to execute the program
main()