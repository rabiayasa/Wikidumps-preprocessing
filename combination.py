import os
#Finding all files to combine
def find_the_way():
    path = './text/'
    xml_files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                xml_files.append(os.path.join(r, file))
    return xml_files
filenames=find_the_way()

# combination of all txt files and writing in one all_text file
with open('all_text.txt', 'w') as outfile:
    for fname in filenames:
        print(fname)
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


