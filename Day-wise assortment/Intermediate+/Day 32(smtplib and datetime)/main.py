import smtplib

# Initialising my email
my_email = "test.user.python0520@gmail.com"
my_password = "ezyjbzaszosbhner"

# Creating an obj that establishes connection with the mail server
connection = smtplib.SMTP("smtp.gmail.com", port=587)
# Starting TLS - Transport Layer Security, it's a way of securing connection with the mail server
# Reason: So that no one can intercept our message, since tls encrypts our message
connection.starttls()

# Logging in
connection.login(user=my_email, password=my_password)
# Sending the message
connection.sendmail(
    from_addr=my_email,
    to_addrs="crueser123@gmail.com",
    msg="Subject:Hello\n\nHi, this is my first msg using the SMTP module.")
# Closing the connection
connection.close()