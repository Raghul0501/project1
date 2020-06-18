import csv

def upload(detail):
    
    with open("studinfo.csv",mode='a+',newline='') as file:
        a=csv.writer(file)
        if file.tell()==0:
            a.writerow(["Name","Age","Mobile_No","Email_ID"])
        a.writerow(detail)

if __name__ == "__main__":
    count=1
    while True:
        print(f"Enter student {count}'s info seperated by comma in following format")
        studinfo=input("Name,Age,Mobile_No,Email_ID:\n").split(",")
        print(f"Name      :  {studinfo[0]} \nAge       :  {studinfo[1]} \nMobile_No :  {studinfo[2]} \nEmail_ID  :  {studinfo[3]}")
        choice=input("Is entered info correct{yes/no}?")
        if choice=='yes':
            upload(studinfo)
            next_choice=input("Do you want to continue{yes/no}?")
            if next_choice=='no':
                break
            else:
                count+=1

        
