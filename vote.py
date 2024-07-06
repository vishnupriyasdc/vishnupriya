
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Establish the MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="election"
)

cursor = db.cursor()

def display():
    cursor.execute("SELECT name FROM candidates")
    candidates = cursor.fetchall()
    print("\nList of candidates:")
    for candidate in candidates:
        print(candidate[0])

def email_msg(email):
    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login("your_email@gmail.com", "your_email_password")
        msg = MIMEMultipart()
        msg['From'] = "your_email@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Thank you for your vote"
        body = "Thank you for voting in the election."
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        s.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def add_vote(candidate_name):
    cursor.execute("SELECT vote_count FROM candidates WHERE name=%s", (candidate_name,))
    result = cursor.fetchone()
    if result:
        current_count = result[0]
        cursor.execute("UPDATE candidates SET vote_count = %s WHERE name = %s", (current_count + 1, candidate_name))
    else:
        cursor.execute("INSERT INTO candidates (name, vote_count) VALUES (%s, %s)", (candidate_name, 1))
    db.commit()

def add_user(name, email, candidate):
    cursor.execute("INSERT INTO users (name, email, candidate) VALUES (%s, %s, %s)", (name, email, candidate))
    db.commit()

def main():
    print("    Welcome to the Election Voting System...! ")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    display()
    candidate = input("Enter your favorite candidate: ")
    
    cursor.execute("SELECT name FROM candidates WHERE name = %s", (candidate,))
    if cursor.fetchone() is None:
        print("Invalid candidate selected. Please try again.")
        return
    
    add_user(name, email, candidate)
    add_vote(candidate)
    email_msg(email)

main()

# Close the cursor and connection
cursor.close()
db.close()