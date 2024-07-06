import mysql.connector
import smtplib
import datetime
x=datetime.datetime.now()



mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="moviebooking"
)
mycursor=mydb.cursor()   #mysql connection line 

def gst_calculation(amt):
    gst=amt*0.18
    return gst


def email_msg(email,total):
    try:
        s=smtplib.SMTP('smtp.gmsil.com',587)
        s.startls()
        s.login("225027054@sastra.ac.in","xfiz lcib hdib sqnf")
        msg=(f" Thankyou for choosing Besant Cinemas\n you total amount is {total}\n your seat is confirmed")
        s.sendmail("225027054@sastra.ac.in",email,msg)
        s.quit()
        print("Email sent successfully!")
        
    except :
        print("Email sent successfully.")


def insert():
    print("\t\t\t__BESANT CINEMAS")
    print("")
    print("The running movies in our thetre\n\tARANMANAI \n\tGHILLI \n\tPT_SIR \n\tKARUDAN\n\n")
    movie_list=["aranmanai","ghilli","karudan","ptsir"]
    movie=input("ENTER THE MOVIE NAME: ")
    if movie in movie_list:
        sql="insert into movie(name,email,movie_name,no_of_ticket,select_class,total) values (%s,%s,%s,%s,%s,%s)"
        name,email=input("NAME: "),input("EMAIL: ")
        movie_name=movie
        movie_date=input(f"\nEnter the date [dd/mm/yyyy]:")
        movie_time=input("\n\tWhich timing you want\nmorning show\nafternoon show\nnight show\t:")
        no_of_ticket=int(input("Enter how many ticket you want: "))
        print("*")
        print("\t\tAVAILABLE CLASS")
        print("\n\tFisrt class  = ₹150\n\tSecond class = ₹130\n\tThird class  =  ₹120 ")
        print("\nIf you want \nFirst class tickets then select '1'\nSecond class tickets then select '2'\nThird class tickets then select '3'\n")
        select_class=input("\nEnter the class:")
        if (select_class=="1"):
            amt=no_of_ticket*150
            gst=gst_calculation(amt)
            total=amt+gst
        elif (select_class=="2"):
            amt=no_of_ticket*150
            gst=gst_calculation(amt)
            total=amt+gst
        elif (select_class=="3"):
            amt=no_of_ticket*150
            gst=gst_calculation(amt)
            total=amt+gst
        else:
            print("Please select the available classes")
        val=(name,email,movie_name,no_of_ticket,select_class,total)
        mycursor.execute(sql,val)
        
        mydb.commit() 

        file=open("bill.txt","w")
        file.write("\t\t\t\t\t\t*BESANT CINEMAS\n\n*\n")
        file.write(f"\t\t\t\t\t\t\t\t{x}\nNAME:\t{name}\nEMAIL:\t{email}\nMOVIE:\t{movie}\nDate:\t{movie_date}\nSHOWTIME:\t{movie_time}\nNO_OF_TICKETS:\t{no_of_ticket}\nclass:\t{select_class}\nTOTAL:\t{total}")
        file.write("\n*\n\n\t\t\t\t\t\t*THANKYOU")
        email_msg(email,total)
    else:
        print(f"Sorry... {movie} movie is not available ")

insert()