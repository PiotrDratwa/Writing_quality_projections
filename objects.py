import os
import pandas as pd

class DataFramesLoader:
    def __init__(self, train_logs_filename, test_logs_filename, train_scores_filename):
        current_directory = os.getcwd()

        self.df_train_logs = pd.read_csv(os.path.join(current_directory + "\\data\\", train_logs_filename))
        self.df_test_logs = pd.read_csv(os.path.join(current_directory + "\\data\\", test_logs_filename))
        self.df_train_scores = pd.read_csv(os.path.join(current_directory + "\\data\\", train_scores_filename))

class XData:
    def __init__(self, df, columns):
        self.df = df[columns]
    
    def group_by_mean(self, grouped):
        self.df = self.df.groupby([grouped]).mean()
    
    def get_words_count(self, df):
        self.df = self.df.join(df[['id', 'word_count']].groupby(['id']).max())
        
    def group_by_count(self, df, column, value, name):
        temp = df[['id', column]]
        temp = temp[temp[column] == value] 
        self.df = self.df.join(temp.groupby(['id']).count())
        self.df.rename(columns = {column:name}, inplace = True)
