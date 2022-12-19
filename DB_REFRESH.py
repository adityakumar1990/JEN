import sys

print(f"Name of python script is {sys.argv[0]}")

if sys.argv[1]=="dev":
    print("Deploying the code in dev")
elif sys.argv[1]=="sit":
    print("Deploying the code in dev")
elif sys.argv[1]=="uat":
    print("Deploying the code in dev")
elif sys.argv[1]=="prod":
    print("Deploying the code in dev")
else :
    print("Deploying the other code in not respected env")
print("This is to test the git polling in jenkins")
if sys.argv[2]:
    print("In case of true!!")
else:
    print("in case of failure!!!")
