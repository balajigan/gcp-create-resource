
import pandas as pd
import os
import shutil
# Import the Secret Manager client library.
from google.cloud import secretmanager

print ("main.py started ...")
#print(os.environ)

# read by default sheet of an excel file
#dataframe1 = pd.read_excel('sample.xlsx')
#print(dataframe1.to_dict('records'))

#f = open("terraform/terraform_commands.txt", "w")
#f.write("This file is newly created ...")
#f.close()

# Create the Secret Manager client....
client = secretmanager.SecretManagerServiceClient()

# Access the secret version.
response = client.access_secret_version(request={"name": "projects/352967962442/secrets/credentials/versions/1"})
payload = response.payload.data.decode("UTF-8")
print(payload)

credentialFile = open("terraform/credentials.json", "w")
credentialFile.write(payload)
credentialFile.close()

values_auto_file_name = 'terraform/values.auto.tfvars'
tf_module_file_path = 'terraform/modules/'
xls = pd.ExcelFile('Infra_variable_sheet.xlsx')
print(xls.sheet_names[0])
dataframe1 = pd.read_excel('Infra_variable_sheet.xlsx')
print("Raw dataframe = ")
print(dataframe1)

src1 = tf_module_file_path + xls.sheet_names[0] + '/main.tf'
src2 = tf_module_file_path + xls.sheet_names[0] + '/variables.tf'
dst1 = 'terraform/main.tf'
dst2 = 'terraform/variables.tf'

shutil.copyfile(src1, dst1)
shutil.copyfile(src2, dst2)

f = open(values_auto_file_name, "w")
for index, row in dataframe1.iterrows():
    if(row['isMandatory'] == 'yes'):
        param = row['Parameter Name'] + '  =   '
        if(row['Data Type'] == 'string'):
            param = param + '"' + row['Values'] + '"'
        else:
            param = param + row['Values']
        print(param)
        f.writelines(param + "\n")
f.close()
