##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import smtplib
import random


my_email = "sben199604@gmail.com"
password = "ayrjldndsfyoocas"
my_name = "Ben"



today = dt.datetime.now()
today_tuple = (today.month , today.day)

data = pandas.read_csv("birthdays.csv")

#data_day_list = data["day"].tolist()
#data_month_list = data["month"].tolist()
#data_name_list = data["name"].tolist()

birthdays_dict  = {(data_row["month"], data_row.day):data_row for (index,data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    random_num = random.randint(1,3)
    file_path = f"letter_templates/letter_{random_num}.txt"
    
    with open(file_path) as context_blessing:
        contents= context_blessing.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email , password=password)
            connection.sendmail(
                    from_addr=my_email , 
                    to_addrs=birthday_person["email"] ,
                    msg=f"Subject:Happy Birthday!\n\n{contents}"
                )   



"""
if current_Month in data_month_list:
    if current_day in data_day_list:
        


        #row = data[data[current_day]]

        random_num = random.randint(1,3)
        #print(random_num)
        #print(random_num)
        with open(f"letter_templates/letter_{random_num}.txt") as context_blessing:
            data_blessing = context_blessing.read()
            #print(type(data_blessing))

            new_data_blessing = data_blessing.replace("[NAME]",my_name)
            #print(new_data_blessing)


            
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email , password=password)

                connection.sendmail(
                    from_addr=my_email , 
                    to_addrs="shar.ben@yahoo.com" , 
                    msg=f"Subject:Happy birthday!\n\n{new_data_blessing}"
                )   

            
"""

"""

for day in data_day_list:
    if day == current_day:
        print("true")

if data["day"] == current_day and data["month"] == current_Month:
    random_num = random.randint(3) + 1

"""


#print(data[data["name"] == "Ben"])



"""
with open("birthdays.csv") as data_of_births:
    data = pandas.DataFrame(data_of_births)
    print(data[])


"""


