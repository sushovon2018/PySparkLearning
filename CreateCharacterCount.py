

InputStr="I am Idiet and I am foolish I am the best"

ls_str=list(InputStr.replace(" ",""))

ls_distict=set(ls_str)

Result_dict={}


for i in ls_distict:
    Result_dict[i]=InputStr.count(i)

print(Result_dict)

print(__name__)

