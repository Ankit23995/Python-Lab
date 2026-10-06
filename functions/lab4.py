from mailerpy import Mailer
my_mailer = Mailer("smtp.gmail.com",587,"kayastha.aayush@gmail.com","wafy ypqk lztj ukbc")
content ="""Hello ALL,
Our course will be completed next week.

Thanks,
Yours sincerely,
Ankit Man Kayastha

"""
my_mailer.send_mail(
    "rabindrasapkota2@gmail.com","Test Mail",content
)