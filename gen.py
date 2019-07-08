#!python3

SEPARATORS="-_. +"
SUFFIXES_FILE="suffixes.txt"

def main():
    names = []
    prefix = input("prefix (company/app name) : ")
    with open(SUFFIXES_FILE) as f:
        suffixes = f.readlines()
        for suffix in suffixes:
            for separator in SEPARATORS:
                name = '%s%s%s' %(prefix, separator, suffix)
                print(name, end='')
    

if __name__ == "__main__":
    exit(main())
