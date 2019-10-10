import pysftp

host = 'upload-5097.tvsquared.com'
username = 'swoon'
password = 'AdABlPjesDVizvhLNNT6'

def upload(file):
    with pysftp.Connection(host, username=username, password=password) as sftp:
        with sftp.cd('/default/spots'):  # temporarily chdir to public
            print("uploading via SFTP.....")
            sftp.put(file)  # upload file to public/ on remote
            print("successfully dropped to "+ username)