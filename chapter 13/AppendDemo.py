def main():
    #Open file for appending data
    outfile = open("test.txt", "a")
    outfile.write("1\nDonald Trump")
    outfile.close() #Close the file

main()
