
import pandas as pd
import os
from google.cloud import secretmanager

def isNotBlank (myString):
    return bool(myString and myString.strip())
def isNaN(num):
    return num != num

print ("main.py started ...")

# Create the Secret Manager client....
client = secretmanager.SecretManagerServiceClient()

# Access the secret version.
response = client.access_secret_version(request={"name": "projects/352967962442/secrets/credentials/versions/1"})
payload = response.payload.data.decode("UTF-8")
#print(payload)

requested_modules_file_name = 'requested_modules.txt'
tf_module_file_path = 'terraform/modules/'

xls = pd.ExcelFile('Infra_variable_sheet.xlsx')
print(xls.sheet_names)

requested_modules = open(requested_modules_file_name, "w")

for resource_type in xls.sheet_names:
    print(resource_type)
    dataframe1 = pd.read_excel('Infra_variable_sheet.xlsx', sheet_name=resource_type, converters={'Parameter Name':str,'Values':str})

    requested_modules.writelines('/workspace/terraform/modules/' + resource_type + "\n")
    
    credentialFileName = 'terraform/modules/'+ resource_type + '/credentials.json'
    credentialFile = open(credentialFileName, "w")
    credentialFile.write(payload)
    credentialFile.close()

    values_auto_file_name = 'terraform/modules/' + resource_type + '/values.auto.tfvars'
    f = open(values_auto_file_name, "w")
    for index, row in dataframe1.iterrows():
        # process only the records with filled in 'Values'
        if not isNaN(row['Values']) and isNotBlank(row['Values']):
            param = row['Parameter Name'] + '  =   '
            if(row['Data Type'] == 'string'):
                param = param + '"' + row['Values'] + '"'
                print(param)
                f.writelines(param + "\n")
            elif(row['Data Type'] == 'map(string)'):
                mapStringList = row['Values'].strip()[1:-1].split('\n')
                for item in mapStringList:
                    if '=' in item:
                        param = row['Parameter Name'] + '_' + item.strip()
                        print(param)
                        f.writelines(param + "\n")                
            elif(row['Data Type'] == 'map(string)111111111111111111111'):
                param = param + '"' + row['Values'] + '"'
                print(param)
                f.writelines(param + "\n")
            else:
                param = param + row['Values']
                print(param)
                f.writelines(param + "\n")
    f.close()
requested_modules.close()
print ("main.py completed...")
