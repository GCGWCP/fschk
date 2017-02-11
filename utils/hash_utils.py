#!/usr/bin/env python

# With many thanks to Omnifarious
# https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
# Not in the SO answer: Remember to set the file to 'rb'
# to read it into the function as a binary to avoid having to deal
# with varied encodings.


def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if ashexstr else hasher.digest())


def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


if __name__ == '__main__':
    pass
