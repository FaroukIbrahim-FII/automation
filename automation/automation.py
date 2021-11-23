import re

with open("assets/potential-contacts.txt" ,"r") as f:
    content = f.read()

found_phone_num = re.findall(r"[\+\d]?(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",content)
found_phone_num.sort()
phone_nums = []
for phone_num in found_phone_num:
    if phone_num not in phone_nums:
        if len(phone_num) == 7:
            phone_num = "206-"+phone_num[:3]+ "-"+phone_num[3:]
            phone_nums.append(phone_num)
        else:
            phone_nums.append(phone_num.replace("(","").replace(")","-").replace(".","-"))

with open("phone_numbers.txt","w") as file:
    for email in phone_nums:
        file.writelines(f"{email}\n")

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_regex , content)

emails.sort()
emails_list = []
for email in emails:
    if email not in emails_list:
        emails_list.append(email)

with open("emails.txt","w") as file:
    for email in emails_list:
        file.writelines(f"{email}\n")