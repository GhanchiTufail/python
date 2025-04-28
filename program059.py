# program 58 :

# Assuming that we have some email addresses
# in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.


def user_name(email):
    name = ""
    for i in email:
        if i == "@":
            break
        name = name + i
    return name

def company_name(email: str):
    company = ""
    for i in email[len(user_name(email))+1:]:
        if i == ".":
            break
        company = company + i
    return company


email = input("Enter the mail : ")

username = user_name(email)
company = company_name(email)

print(username)
print(company)