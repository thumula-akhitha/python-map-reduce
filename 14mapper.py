# Case 1 - Mapper using Files
# Easy to test
# Not quite Hadoop-ready

# open returns a file object
with open("departmentreduced.txt", "r") as input:
  with open("bonusmapoutput.txt", "w") as output:

    # iterate through each line in the file object
    for line in input:
      datalist = line.strip().split("	")
      if (len(datalist) == 2) : 
          department, amount = datalist
          output.write(amount + "\t" + department + "\n")
          print(amount + "\t" + department + "\n")

