def group_by_count(df, X, column, value, name):
    temp = df[['id', column]]
    temp = temp[temp[column] == value] 
    X = X.join(temp.groupby(['id']).count())
    X.rename(columns = {column:name}, inplace = True)
    return X
