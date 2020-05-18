import os

#print(f'File Size in Bytes is {file_stats.st_size}')
#print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

def size(file):
    file_stats = os.stat(file)
    GB =  file_stats.st_size
    MB = file_stats.st_size / (1024 * 1024)
    CO2 = GB * 20
    text = "File Size in Bytes: " + str(GB) + "\nFile Size in MegaBytes: " + str(MB)+ "\nYou have used " + str(CO2) + "g of CO2 for sending this email."
    
    return text

def difference(file1, file2):
    file_stats1 = os.stat(file1)
    file_stats2 = os.stat(file2)
    GB1 =  file_stats1.st_size
    GB2 =  file_stats2.st_size
    CO2A = GB1 * 20
    CO2B = GB2 * 20
    return abs(CO2A-CO2B)
    
    