import requests

# urls = ["https://shantanuuchak.tech","https://quastech.com","https://infogain.com/about/contact-us/"]



# res = requests.get('https://shantanuuchak.tech')

# func to split on
def split_quote(text):
  return text.split('"')

#function to remove mailto
def remove_mailto(data):
  return data.replace("mailto:" , "")


#function to find email in list
def find_email(data_list):
  email_list=[]
  for el in data_list:
    if "@" in el and "." in el and not "/" in el:
      email_list.append(remove_mailto(el))
     
  return email_list    

# function to request a url
def fetch(url):
  res = requests.get(url)

  if res.status_code==200:
   return res.text

  print(f"failed with error code: {res.status_code}")
  return ""

#taking inout
urls=[]
while True:
  User_Input=input("Enter a URL: or N to Exit")

  if User_Input =="N":
    print("Url List Ready!")
    break

  if "://" not in User_Input:
    print("Enter a valid URL!")
  else:
    urls.append(User_Input)

emails=[]
# Iterating over URLs
for url in urls:
  data = fetch(url)
  data_list = split_quote(data)
  email_list = find_email(data_list)
  emails.extend(email_list)
print(set(emails))  

f = open('email.txt','w')
f.write(str(emails))
f.close()


