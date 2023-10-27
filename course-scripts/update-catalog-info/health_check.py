#!/usr/bin/env python3

import emails
import os
# shutil for disk usage
import shutil
# psutil for CPU and RAM usage
import psutil
# socket for name resolution
import socket

def email_error(subject):
  email_message = emails.generate_error_report('automation@example.com', 
                                               '{}@example.com'.format(os.environ["USER"]), 
                                               subject, 
                                               'Please check your system and resolve the issue as soon as possible.')
  emails.send_email(email_message)

def system_usage():
  # based on whether check_sys values < threshold values; name resolution handled separately
  thresholds = {'cpu':20, 'du':20, 'RAM':500}
  check_sys = {}

  error_line = {'cpu':'Error - CPU usage is over 80%', 
                'du':'Error - Available disk space is less than 20%', 
                'RAM':'Error - Available memory is less than 500MB'}

  # check cpu usage in 1 second increments
  cpu_usage = psutil.cpu_percent(1)
  # provide free amount of cpu
  cpu_free = 100 - cpu_usage
  check_sys['cpu'] = cpu_free

  # check disk usage from root directory
  disk_usage = shutil.disk_usage('/')
  # provide free amount of disk space
  disk_free = disk_usage.free/disk_usage.total*100
  check_sys['du'] = disk_free
 
  # check memory usage; provides bytes
  ram_usage = psutil.virtual_memory()
  # provide free amount of RAM; convert byte to MB
  check_sys['RAM'] = ram_usage.available / (1024**2)

  #iterate over check_sys dictionary for cpu, disk usage, and RAM issues 
  for key, value in check_sys.items():
    if check_sys[key] < thresholds[key]:
      subject = error_line[key]
      email_error(subject)

  # name resolution check
  ip_addy = socket.gethostbyname('localhost')
  if ip_addy != '127.0.0.1':
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    email_error(subject)

def main():
  system_usage()

if __name__ == '__main__':
  main()
