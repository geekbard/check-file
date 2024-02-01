# --==( 'Import Libraries' )==--
from os import listdir
from hashlib import md5

# --==( ' Get inputs from user ' )==--
source_path = input("Source Path: ")

# --==( ' Get list of source directory files ' )==--
try:
    source_files = listdir(source_path)
except Exception as e:
    if type(e) == FileNotFoundError:
        print("[ERR]: We did not find your source directory !")
        exit()
    else:
        print(e)


dest_path = input("Destination Path: ")

# --==( ' Get list of destination directory files ' )==--
try:
    source_files = listdir(source_path)
except Exception as e:
    if type(e) == FileNotFoundError:
        print("[ERR]: We did not find your destination directory !")
        exit()
    else:
        print(e)

try:
    dest_files = listdir(dest_path)
except Exception as e:
    if type(e) == FileNotFoundError:
        print("[ERR]: We did not find your directory !")
        exit()
    else:
        print(e)

# --==( ' Make MD5 Hash from files and save those ' )==--
def calculate_hashs(path, files):
    hashs = {}

    for file in files:
        file_path = path + '/' + file
        target_file = open(file_path,'rb').read()
        file_hash = md5(target_file).hexdigest()
        hashs[file] = file_hash
    
    return hashs

print("Calculating source files...", end='\r')
# --==( ' Calculate Source Files ' )==--
source_hashs = calculate_hashs(source_path, source_files)

print("Calculating destination files...")
# --==( ' Calculate Source Files ' )==--
dest_hashs = calculate_hashs(dest_path, dest_files)

print('Calculate Done.')

if ( dest_hashs == source_hashs ):
    print("All files are OK.")
else:
    print("We found bad files. We're going to find those.")
    bad_files = {}
    for source_file in source_files:
            if ( source_file in dest_files ):
                if ( source_hashs[source_file] == dest_hashs[source_file] ):
                    pass
                else:
                    bad_files[source_file] = 'Not equal with destination file.'
            else:
                bad_files[source_file] = 'Not found in destination'

print('We found these problems:')
for bad_file,reason in bad_files.items():
    print(bad_file + ' -- ' + reason)