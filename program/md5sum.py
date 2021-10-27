import hashlib

file_name = 'filename.exe'

original_md5 = '6941402abc4b2a76b9719d911420c592'  

with open(file_name) as file_to_check:
    data = file_to_check.read().encode()
    md5_returned = hashlib.md5(data).hexdigest()

if original_md5 == md5_returned:
    print('MD5 verified.')
else:
    print('MD5 verification failed!.')