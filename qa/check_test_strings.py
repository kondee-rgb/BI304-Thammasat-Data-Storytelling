import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('qa/*.js'):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if '42,850' in c:
        print(f'{f} checks for 42,850')
    if '7,094' in c:
        print(f'{f} checks for 7,094')
    if '62.4%' in c:
        print(f'{f} checks for 62.4%')
