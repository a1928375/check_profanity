import urllib

def file_read():
    quotes=open("C:\Users\Arthur Shih\Desktop\movies quotes.txt")
    contents=quotes.read()
    print contents
    quotes.close()
    words_check(contents)

def words_check(text):
    check=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=check.read()
    #print output
    check.close()
    if "true" in output:
        print "There are some curse words!"
    elif "false" in output:
        print "The file is good!"
    else:
        print "The file or format us not correct"

file_read()
    
