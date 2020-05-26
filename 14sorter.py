# Case 1 - Sorter using Files
# Easy to test
# Not needed for Hadoop (Hadoop performs this automatically)

# An inplace sort is good for small data only 
# This step is done automatically in Hadoop

with open("bonusmapoutput.txt", "r") as unsorted:
  with open("bonussorted.txt", "w") as sorted:

    dataList = unsorted.readlines()
    dataList.sort(reverse=True)

    # output sorted intermediate key-value pairs
    for line in dataList:
      sorted.write(line)  # output
      print (line)        # display to console

