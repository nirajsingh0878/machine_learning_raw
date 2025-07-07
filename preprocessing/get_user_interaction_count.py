from datetime import datetime,timedelta


def get_user_interaction_counts(search_interaction_df):
    latest_date_st = search_interaction_df.agg({'date':'max'}).collect()[0][0]
    latest_date = datetime.strptime(latest_date_st,'%Y-%m-%d')
    user_month_total = get_count(search_interaction_df,latest_date,30)
    user_week_total = get_count(search_interaction_df,latest_date,7)
    user_day_total = get_count(search_interaction_df,latest_date,1)

    user_month_total =user_month_total.withColumnRenamed('count','month_interaction_count')
    user_week_total =user_week_total.withColumnRenamed('count','week_interaction_count')
    user_day_total =user_day_total.withColumnRenamed('count','day_interaction_count')

    user_total = user_month_total.join(user_week_total,['user_id'],'left')
    user_total = user_total.join(user_day_total,['user_id'], 'left')
    user_total = user_total.na.fill(0)
    return user_total
    
    

def get_count(df,end_date,days_delta):
    start_date = end_date - timedelta(days=days_delta)
    temp = df.where(df['date'].between(start_date,end_date)).groupBy('user_id').count()
    return temp


'''
Category: Data Processing

Get User Interaction Counts 🟢 ⭐
Consider the following dataframe:

sql
Copy
Edit
+-------------+---------------------------+-------------+----------------+------------+
| request_path| search_term               | user_id     | ip_address     | date       |
+-------------+---------------------------+-------------+----------------+------------+
| search      | Saving Private Ryan       | 01b4076c    | 168.198.63.238 | 2021-04-07 |
| search      | Fear and Loathing         | 637f8480    | 116.103.0.64   | 2021-04-07 |
| search      | Legally Blonde            | 8137461f    | 9.47.206.231   | 2021-04-07 |
| search      | Legally Blonde            | 01b4076c    | 198.45.207.12  | 2021-04-07 |
| search      | The Hills Have Eyes       | 136f623b    | 248.212.242.192| 2021-04-07 |
| search      | Knives Out                | 8137461f    | 65.166.90.163  | 2021-04-01 |
+-------------+---------------------------+-------------+----------------+------------+
# ...
# More of the same kind of data.
It represents user interactions with movie search pages. Each interaction is represented by the user_id of the user who made it, the movie search term that they looked for, and the date of the interaction, amongst other things.

Use this interaction dataframe, accessible as search_interaction_df in the code, to create a features dataframe of the following form:

diff
Copy
Edit
+-------------+------------------------+------------------------+------------------------+
| user_id     | month_interaction_count| week_interaction_count| day_interaction_count |
+-------------+------------------------+------------------------+------------------------+
| 01b4076c    | xx                     | xx                     | xx                     |
| 31c73683    | xx                     | 11                     | xx                     |
| 8137461f    | 30                     | xx                     | 2                      |
| f77ad84c    | xx                     | xx                     | 2                      |
| 25480522    | xx                     | xx                     | xx                     |
| bfb267c5    | xx                     | 8                      | xx                     |
| 0963ca26    | xx                     | xx                     | xx                     |
| a27aacfe2   | xx                     | 1                      | 1                      |
| 637f8480    | xx                     | xx                     | 3                      |
| c8b81d47    | 24                     | xx                     | xx                     |
+-------------+------------------------+------------------------+------------------------+
Each user_id in the returned dataframe shall have entries in the month_interaction_count, week_interaction_count, and day_interaction_count columns representing the number of search page interactions that the user had over the past month, week, and day, respectively.

The past month, week, and day should be based off of the latest date present in search_interaction_df; specifically, they should be the last 30, 7, and 1 days before the latest date, respectively.

'''