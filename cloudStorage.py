import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BDS8VbxPQazXEawx8qZWoQZSraIlV2y-UMNHuRt0zatBVSIQu8t4e46dsws45UPO8QJkzYfYQ5jptlzYwcv8yV8cDQBiniEZ56h_tJ00Jmmxb282x2g7pxvLIwRcpSaxETSGlzxyB1Ce'
    transferData = TransferData(access_token)

    file_from = '/Users/jaicobremon/Documents/Phyton/file.txt'
    file_to = '/random.txt'
    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
