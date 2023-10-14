import sys
file_path = sys.argv[1]
print('example:   ./xxx  <url_file>')

def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    return unique_list

with open(file_path, 'r') as f:
    lines = f.readlines()
    copy_lines = []
    for i in lines:
        i = i.strip()
        if i.count(':') != 2:
            if 'http:' in i:
                i = i + ':80'
            elif 'https:' in i:
                i = i + ':443'
        copy_lines.append(i)
    lines = unique(copy_lines)
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