
import pandas as pd
import os
# Import the Secret Manager client library.
from google.cloud import secretmanager


print ("main.py started ...")
print(os.environ)

# read by default sheet of an excel file
dataframe1 = pd.read_excel('sample.xlsx')
print(dataframe1.to_dict('records'))

f = open("terraform/terraform_commands.txt", "w")
f.write("This file is newly created ...")
f.close()
print("Raw dataframe = ")
print(dataframe1)

# Create the Secret Manager client....
client = secretmanager.SecretManagerServiceClient()

# Access the secret version.
response = client.access_secret_version(request={"name": "projects/352967962442/secrets/credentials/versions/1"})
payload = response.payload.data.decode("UTF-8")
print(payload)

credentialFile = open("terraform/credentials.json", "w")
credentialFile.write(payload)
credentialFile.close()



