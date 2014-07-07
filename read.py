import codecs
inputfile = codecs.open("text.csv","rb","utf-16")
inputtext = inputfile.read()
outputtext = inputtext.replace('\r\n"','"')
outputfile = codecs.open("text_out.csv","wb","utf-16")
outputfile.write(outputtext)
inputfile.close()
outputfile.close()

