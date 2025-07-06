import os 


def main():
    nombre = os.getenv("USERNAME")
    print(f"HOLA, {nombre}, DESDE GITHUB ACTIONS")

if __name__ == "__main__":
    main()
    
