import sys
import copy
file_path = sys.argv[1]
print('example:   ./xxx  <url_file>')
with open(file_path, 'r') as f:
    lines = f.readlines()
    copy_lines = []
    for i in lines:
        copy_lines.append(i.strip())
    lines = copy.copy(copy_lines)
    with open('output.txt', 'w') as w:
        for line in lines:
            try:
                protocol, sub = line.strip().split('://')
                
                if protocol == 'http':
                    if 'https://'+ sub in lines:
                        copy_lines.remove('http://'+ sub)
                
                if protocol == 'https':
                    if 'http://'+ sub in lines:
                        copy_lines.remove('http://'+ sub)
            except:
                pass
        for i in copy_lines:
            w.write(i + '\n')
    print('\nDone! output in local file: ./output.txt')