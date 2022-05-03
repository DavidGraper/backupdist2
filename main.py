import csv
import subprocess

backupdevicesizes = {"8GB": 7,
                     "16GB": 14,
                     "500GB": 465,
                     "1TB": 931,
                     "2TB": 1862,
                     "3TB": 2793,
                     "4TB": 3725,
                     "6TB": 5587,
                     "8TB": 7450,
                     "10TB": 9313
                     }

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def generate_backup_directorylist(rawlistingfilename, backupclientlist, outputfile):

    accum = 0
    clientindex = 0

    backupclientname = backupclientlist[clientindex][0]
    backupclientsize = backupdevicesizes[backupclientlist[clientindex][1]] * 10E8

    print("Writing directories to backup for client '{0}', size '{1}'".format(backupclientname, str(backupclientlist[clientindex][1])))

    fileout = open(outputfile, "w+")

    directoryname = ""

    with open(rawlistingfilename, 'r') as f:
        reader = csv.reader(f, dialect='excel', delimiter='\t')
        for row in reader:

            directoryname = row[1]
            directorysize = row[0]

            accum += int(directorysize)

            if accum > backupclientsize:
                clientindex += 1
                backupclientname = backupclientlist[clientindex][0]
                backupclientsize = backupdevicesizes[backupclientlist[clientindex][1]] * 10E8
                accum = 0

                print("Writing directories to backup for client '{0}', size '{1}'".format(backupclientname, str(backupclientlist[clientindex][1])))

            textout = "{0}\t{1}\t{2}\t{3}\n"

            fileout.write(textout.format(backupclientname, directoryname, directorysize, str(accum)))

    fileout.close()
    print("Done")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    backup_clients = [("Mint01Backup01", "6TB"), ("Mint01Backup02", "6TB"),("Mint02Backup01", "8TB"), ("Mint02Backup02", "8TB")]
    # backup_clients = [("BackupDevice1","8GB"),("BackupDevice2","16GB"),("Mint01Backup01", "6TB"), ("Mint01Backup02", "6TB"),("Mint02Backup01", "8TB"), ("Mint02Backup02", "8TB")]
    # generate_backup_directorylist("~/Documents/videooutput_sorted.txt", backup_clients, "~/Documents/backupjobdivisions.txt")
    generate_backup_directorylist(r"/home/dgraper/backupserver_share0/output_sorted.txt", backup_clients, r"/home/dgraper/backupserver_share0/backupjobdivisions.txt")


