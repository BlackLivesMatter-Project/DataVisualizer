"""Used to parse data from CSV into """

from .DataParserException import *

import pandas as pd
from os import access, R_OK
from os.path import exists
from pathlib import Path


class DataParser:
    """
    Used for parsing tweet data from data that 
    has already been parsed from structured twitter data.

    Attributes:
    csv_file -- csv file containing twitter data. 
    """

    def __init__(self,csv_file):
        """Used to initialize the DataParser Class"""
        self.validate_file(csv_file)
        self.tweet_data = pd.read_csv(csv_file)
        
        
    @staticmethod
    def validate_file(file):
        """Used to validate if a file exists, and is readble by this process."""
        if not exists(file):
            raise DataParserFileNotExist(file)
        if not Path(file).is_file():
            raise DataParserNotAFile(file)
        if not access(file, R_OK):
            raise DataParserFileNotReadable(file)

    @staticmethod
    def validate_int(number, raise_error=False):
        """validate integer"""
        if not isinstance(number, int):
            if raise_error:
                raise DataParserNotAnInteger(number)
            else:
                return False
        else:
            return True

    def collect_users_by_followers(self, min_followers=None, max_followers=None):
        """Display all user handles with x amount of followers or more."""
        # create dataframe to return collected
        follower_dataframe = pd.DataFrame(columns = ['user', 'number_of_followers'])

        for user in self.tweet_data['u_screen_name'].unique():
            # collect dataframe row by user screen name
            row_number = self.tweet_data[self.tweet_data['u_screen_name'] == user].index
            
            # check min_followers
            if (self.validate_int(min_followers, False) and
                self.tweet_data.loc[row_number[0]]['u_followers'] < min_followers):
                continue
            
            #check max_followers
            if (self.validate_int(max_followers, False) and
                self.tweet_data.loc[row_number[0]]['u_followers'] >= max_followers):
                continue
            
            # append data to follower_dataframe
            follower_dataframe = follower_dataframe.append({
                'user': user,
                'number_of_followers': self.tweet_data.loc[row_number[0]]['u_followers']
            },ignore_index=True)

        #sort dataframe
        follower_dataframe = follower_dataframe.sort_values('number_of_followers',ascending=False,ignore_index=True)

        return follower_dataframe

    def collect_retweets(self, max_count=None):
        """display top x retweeted tweets in dataset."""

        retweet_dataframe = pd.DataFrame(columns = ['retweet_id','user','number_of_retweets']) 

        for retweet_id in self.tweet_data['rt_id'].unique():
            if pd.isnull(retweet_id):
                continue
            retweet_id_index = self.tweet_data[self.tweet_data['rt_id'] == retweet_id].index

            retweet_dataframe = retweet_dataframe.append({
                'retweet_id': retweet_id,
                'user': self.tweet_data.loc[retweet_id_index[0]]['rt_screen_name'],
                'number_of_retweets': len(retweet_id_index)
            },ignore_index=True)

        # sort dataframe
        retweet_dataframe = retweet_dataframe.sort_values('number_of_retweets',ascending=False,ignore_index=True)

        # if max_count set, return max_count, else return dataframe.    
        if self.validate_int(max_count):
            return retweet_dataframe.head(max_count)
        else:
            return retweet_dataframe

    