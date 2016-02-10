import os
import sys


def sultan():
  if len(sys.argv) != 2:
        print("Invalid usage. Provide a SultanScript file name to compile and run")
        print("Example: Sultan trump_file.tr")
        return

    if not os.path.isfile(sys.argv[1]):
        print("Invalid file specified")
        return

    
    
   

    # Compile and go
    Compiler().compile(sys.argv[1])

if __name__ == "__sultan__":
    sultan()
