import sys
from azure.storage.blob.blockblobservice import BlockBlobService
from azure.storage.blob import ContentSettings


block_blob_service = BlockBlobService(account_name='YourAccountName', account_key='Your Key');

#------------------------- Credentials ---------------------------#
#                                                                 #
# You can try using this filename and type to upload sample Image #
# fileName : 'storage.png'                                        #
# type : 'image/png'                                              #
#-----------------------------------------------------------------#


def CreateBlob(name,container,type,file):
    block_blob_service.create_blob_from_path(
    container,
    name,
    file,
    content_settings= ContentSettings(content_type=type)
            );


def ListBlobs(container):
    generator = block_blob_service.list_blobs(container)
    for blob1 in generator:
        print(blob1.name)

def DownloadBlob(container,blobname,filepath):
    block_blob_service.get_blob_to_path(container,blobname,filepath)

def WriteBlobinText(container,blobname,encodingtype):
    block_blob_service.get_blob_to_text(container, blobname, encodingtype)
    
    
def DeleteBlob(container,blobname):
    block_blob_service.delete_blob(container, blobname)
  
def DeleteContainer(container):
    block_blob_service.delete_container(container)

def CreateBlobFromBytes(container,blobname,bytesContent):
    block_blob_service.create_blob_from_bytes(container,blobname,bytesContent);

     
def main():
    print("YourTestHer")
    input()   

if __name__ == "__main__":
    sys.exit(int(main() or 0))
