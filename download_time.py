# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(seconds):
    hours = int(seconds/3600)
    minutes = int(((seconds - (hours * 3600)) / 60))
    seconds = seconds - (hours * 3600) - (minutes * 60)
    #create proper labels for singular/plural
    if hours == 1:
        hours_label = " hour, "
    else:
        hours_label = " hours, "
    if minutes == 1:
        minutes_label = " minute, "
    else:
        minutes_label = " minutes, "
    if seconds == 1:
        seconds_label = " second, "
    else:
        seconds_label = " seconds, "
    #
    return str(hours) + hours_label + str(minutes) + minutes_label + str(seconds) + seconds_label

def download_time(file_size, file_units, bandwidth, band_units):
    #unit definitions
    kb = 2 ** 10
    kB = kb * 8
    Mb = 2 ** 20
    MB = Mb * 8
    Gb = 2 ** 30
    GB = Gb * 8
    Tb = 2 ** 40
    TB = Tb * 8
    #convert file_units string to integer
    if file_units == "kb":
        file_units_converted = kb
    elif file_units == "kB":
        file_units_converted = kB
    elif file_units == "Mb":
        file_units_converted = Mb
    elif file_units == "MB":
        file_units_converted = MB
    elif file_units == "Gb":
        file_units_converted = Gb
    elif file_units == "GB":
        file_units_converted = GB
    elif file_units == "Tb":
        file_units_converted = Tb
    elif file_units == "TB":
        file_units_converted = TB
    else:
        return
    #convert bandwidth_units string to integer
    if band_units == "kb":
        band_units_converted = kb
    elif band_units == "kB":
        band_units_converted = kB
    elif band_units == "Mb":
        band_units_converted = Mb
    elif band_units == "MB":
        band_units_converted = MB
    elif band_units == "Gb":
        band_units_converted = Gb
    elif band_units == "GB":
        band_units_converted = GB
    elif band_units == "Tb":
        band_units_converted = Tb
    elif band_units == "TB":
        band_units_converted = TB
    else:
        return
        
    total_seconds = (file_size * file_units_converted) / (bandwidth * band_units_converted)
    return "It will take you this long to download your file: " + str(convert_seconds(total_seconds))

file_size = int(input("What is the numerical size of the file that you want to download? "))
file_units = raw_input("In which size unit (KB, MB, GB, etc.) is the file you want to download? ")
bandwidth = int(input("What is the numerical size of your bandwidth? "))
band_units = raw_input("In which size unit (KB, MB, GB, etc.) is your bandwidth measured? ")

print download_time(file_size, file_units, bandwidth, band_units)


# print download_time(1024,'kB', 1, 'MB')
# #>>> 0 hours, 0 minutes, 1 second

# print download_time(1024,'kB', 1, 'Mb')
# #>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

# print download_time(13,'GB', 5.6, 'MB')
# #>>> 0 hours, 39 minutes, 37.1428571429 seconds

# print download_time(13,'GB', 5.6, 'Mb')
# #>>> 5 hours, 16 minutes, 57.1428571429 seconds

# print download_time(10,'MB', 2, 'kB')
# #>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

# print download_time(10,'MB', 2, 'kb')
# #>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


