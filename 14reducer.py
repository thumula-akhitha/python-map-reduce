with open("bonussorted.txt","r") as sorted:
  with open("bonusreduced.txt", "w") as output:

    thisKey = ""
    thisValue = 0.0

    for line in sorted:
      datalist = line.strip().split('\t')
      if (len(datalist) == 2) : 
        amount,department = datalist

        if department != thisKey:
          if thisKey:
            # output the previous key-summaryvalue result
            output.write(str(thisValue)+ '\t' + thisKey +'\n')
            print(str(thisValue)+ '\t' + thisKey +'\n')

          # start over for each new key
          thisKey = department 
          thisValue = 0.0
  
        # apply the aggregation function
        thisValue += float(amount)

    # output the final key-summaryvalue result outside the loop
    output.write(str(thisValue)+ '\t' + thisKey +'\n')
    print(str(thisValue)+ '\t' + thisKey + '\n')
