fp = open("text.txt", "a")
print(fp)
line = input("Give me some text, don't be shy: ")
fp.write(line)
fp.write("\n")
fp.close()