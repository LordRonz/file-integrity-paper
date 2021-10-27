import hashlib

file_name = 'filename.exe'

original_sha1 = ('d1e67b8819b009ec6942033'
                'b6fc1928dd64b5df31bcde63'
                '81b9d3f90488d25324049046'
                '0c0a5a1a873da8236c12ef969')

with open(file_name) as file_to_check:
    data = file_to_check.read().encode()
    sha1_returned = hashlib.sha1(data).hexdigest()

if original_sha1 == sha1_returned:
    print('SHA-1 verified.')
else:
    print('SHA-1 verification failed!.')