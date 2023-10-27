#!/usr/bin/env python3 

import reports
import emails
import os
import re
# email subject will include today's date
import datetime

def process_data():
  supplier_descr = 'supplier-data/descriptions'
  summary_list = []

  for x in os.listdir(supplier_descr):
    # again I really don't want to deal with rogue files
    file_name = re.search(r'(\d+\.txt)', x)
    if file_name is not None:

      file_path = supplier_descr + '/' + x
      with open (file_path, 'r') as f:
        contents = f.read()
        lines = contents.split('\n')
        item_summary = '<br/>name: {}<br/>weight: {}'.format(lines[0], lines[1])
        summary_list.append(item_summary)
  return summary_list

def main():
  summary = process_data()
  reports.generate_report('/tmp/processed.pdf',
                          'Processed Update on ' + datetime.datetime.now().strftime('%B %d, %Y'),
                          '<br/>'.join(summary)) 

  email_message = emails.generate_email('automation@example.com',
                                        '{}@example.com'.format(os.environ["USER"]),
                                        'Upload Completed - Online Fruit Store',
                                        'All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
                                        '/tmp/processed.pdf')
  emails.send_email(email_message)


if __name__ == "__main__":
  main()
