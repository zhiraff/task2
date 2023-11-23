from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
#gauth.LocalWebserverAuth()
gauth.CommandLineAuth()

def create_and_upload_file(file_name='test.txt', file_content='Hey Dude!'):
    
    folderID = ''
    try:
        drive = GoogleDrive(gauth)
        
        fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file in fileList:
            #print('Title: %s, ID: %s' % (file['title'], file['id']))
            if(file['title'] == "pythontask"):
                folderID = file['id']
        my_file = drive.CreateFile({'title': f'{file_name}', 'parents':[{'id': folderID}]})
        my_file.SetContentString(file_content) # if text file
        #my_file.SetContentFile(file_content)
        my_file.Upload()
        
        return f'File {file_name} was uploaded!Have a good day!'
    except Exception as _ex:
        return 'Got some trouble, check your code please!'
    
def main():
    print(create_and_upload_file(file_name='hello.txt', file_content='Hello Friend'))
    
    
if __name__ =='__main__':
    main()
