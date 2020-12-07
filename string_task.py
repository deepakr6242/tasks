statement  =  ' I love Python and  I read python everyday and I do programe everyday'
statement = statement.replace(' ','')
for char in statement:
    first_occr = statement.find(char)
    second_occr = statement.find(char,first_occr+1)
    third_occr = statement.find(char,second_occr+1)
    if second_occr != -1:
        if third_occr == -1:
            print(f"the first occurence of '{char}' is '{first_occr}' and next occurence is '{second_occr} after there is no occurence of '{char}' and hence returning {third_occr}'\n")
        else:
            print(f"the first occurence of '{char}' is '{first_occr}' and next occurence is '{second_occr}' next occurence is '{third_occr}'\n")
    else:
         print(f"there is no occurence of '{char}' and hence returning '{second_occr}'\n")

            
#             Hint:
# for  each_char in statement:
#        statement.find(each_char,[statment.index(each_char)+1,len(statement)])
