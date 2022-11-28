import urllib.request

def main():
    url = input("Enter a URL for a file: ").strip()
    infile = urllib.request.urlopen(url)
    s = infile.read().decode() #Read the content as string

    counts = countLetters(s.lower())

    #Display Results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i]) + (" time" if counts[i] == 1 else " times"))

    infile.close()

#Count each letter in the string
def countLetters(s):
    counts = 26 * [0] #Create and initilize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts

main()
