import hashlib

file_name = 'filename.exe'

original_sha3 = ('3706a96a8fa96b3fc5ff30c'
                'bca36ce666042e2d07762022'
                'a78a2ec82439848fc3695e83'
                '336ab71f47dddbc24b96454df2a43'
                '7e343801a4e13faab89e8d0fda61')

with open(file_name) as file_to_check:
    data = file_to_check.read().encode()
    sha3_returned = hashlib.sha3_512(data).hexdigest()

if original_sha3 == sha3_returned:
    print('SHA-3 verified.')
else:
    print('SHA-3 verification failed!.')