#uhfisfis
import sys

def main():
  # your code goes here
  print("This is/are the system arguments:" , sys.argv)
  print(sys.argv[1], "r")
  #open file now
  ##print("Argument List:" , str(sys.argv))

# boilerplate
if __name__ == "__main__":
  main()
else:
  print("Script can only run as a stand-alone.")