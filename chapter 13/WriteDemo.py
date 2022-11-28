def main():
    #Open file for output
    outfile = open("Presidents.txt", "w")

    #Write data to the file
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama\n")

    outfile.close() #Close the output file

main()

