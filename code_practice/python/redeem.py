import json
import csv
from datetime import datetime
# current date and time

filename = 'redeem_1582869158'
file1 = open(filename, 'r') 
Lines = file1.readlines() 
 
count = 0
csvList = []
# Strips the newline character 
for line in Lines: 
    # print(line.strip()) 
    my_dict = json.loads(line)
    new_dict = {
        "wmid":my_dict["wmid"].encode("utf-8"),
        "mail_addr":my_dict["others"]["mailInfo"]["mail_addr"].encode("utf-8"),
        "email":my_dict["others"]["mailInfo"]["email"].encode("utf-8"),
        "phone_num":my_dict["others"]["mailInfo"]["phone_num"].encode("utf-8"),
        "username":my_dict["others"]["mailInfo"]["username"].encode("utf-8"),
        "product_id":my_dict["others"]["mailInfo"]["product_id"].encode("utf-8"),
        "product_title":my_dict["others"]["product_title"].encode("utf-8"),
        "create_time":datetime.fromtimestamp(my_dict["create_time"] ).strftime('%Y-%m-%d-%H:%M:%S'),
        "create_time_ts":my_dict["create_time"]   
    }
    csvList.append(new_dict)
    # print(new_dict)
    
    # print("Line{}: {}".format(count, line.strip())) 
    
csv_columns = [] 
# csv_columns = ['wmid','mail_addr','email','phone_num','username','product_id','product_title','create_time','create_time_ts']

for k,v in csvList[0].items():
    csv_columns.append(k)


now = datetime.now()
ts = now.strftime('%Y-%m-%d-%H:%M:%S')
print("now: ",ts)
csv_file = ts+"_redeem.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in csvList:
            # print(data)
            writer.writerow(data)
except IOError:
    print("I/O error")