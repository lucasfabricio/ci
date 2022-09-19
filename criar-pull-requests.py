import sys

if len(sys.argv) == 1:
    print("O nome da branch não foi informado")
    sys.exit()

branch = sys.argv[1]

print(f"Nome da branch informada: '{branch}'")