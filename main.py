
import pandas as pd
import os
import shutil
# Import the Secret Manager client library.
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
print(payload)

credentialFile = open("terraform/credentials.json", "w")
credentialFile.write(payload)
credentialFile.close()

values_auto_file_name = 'terraform/values.auto.tfvars'
tf_module_file_path = 'terraform/modules/'
xls = pd.ExcelFile('Infra_variable_sheet.xlsx')

print(xls.sheet_names)

for resource_type in xls.sheet_names:
    print("")
    print(resource_type)
    dataframe1 = pd.read_excel('Infra_variable_sheet.xlsx', sheet_name=resource_type, converters={'Parameter Name':str,'Values':str})

    src1 = tf_module_file_path + resource_type + '/main.tf'
    src2 = tf_module_file_path + resource_type + '/variables.tf'
    dst1 = 'terraform/main.tf'
    dst2 = 'terraform/variables.tf'

    shutil.copyfile(src1, dst1)
    shutil.copyfile(src2, dst2)

    f = open(values_auto_file_name, "w")
    for index, row in dataframe1.iterrows():
        # process only the records with filled in 'Values'
        if not isNaN(row['Values']) and isNotBlank(row['Values']):
            param = row['Parameter Name'] + '  =   '
            if(row['Data Type'] == 'string'):
                param = param + '"' + row['Values'] + '"'
                print(param)
                f.writelines(param + "\n")
            elif(row['Data Type'] == 'map(string)ttttt'):
                mapStringList = row['Values'].strip()[1:-1].split('\n')
                for item in mapStringList:
                    if '=' in item:
                        param = row['Parameter Name'] + '_' + item.strip()
                        print(param)
                        f.writelines(param + "\n")
            elif(row['Data Type'] == 'map(string)'):
                param = param + '"' + row['Values'] + '"'
                print(param)
                f.writelines(param + "\n")
            else:
                param = param + row['Values']
                print(param)
                f.writelines(param + "\n")
    f.close()
    # execute the terraform commands here.
    os.system('cd terraform')
    os.system('ls')
    os.system('terraform init')

print ("main.py completed...")
