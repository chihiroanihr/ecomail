import os

print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

def size(file):
    file_stats = os.stat(file)
    GB =  file_stats.st_size
    MB = file_stats.st_size / (1024 * 1024)
    CO2 = GB * 20
    text = "File Size in Bytes: " + GB + "\nFile Size in MegaBytes: " + MB 
    + "\nYou have used " + CO2 + "g of CO2 for sending this email."
    
    return text
