import eva
import threading
import sys

def main():
    my_eva = eva.eva()
    start_article = input("Start Article: ")

    def SearchWithUpdate():
        my_eva.search(start_article)

    search_thread = threading.Thread(target=SearchWithUpdate)
    search_thread.start()

    # Live counter of checked links
    while search_thread.is_alive():
        sys.stdout.write(f"\rChecked Links: {my_eva.checked} ● ")
        sys.stdout.flush()

    # Clear counter before results
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

    # Outputs
    if my_eva.depth == -1:
        print(f"Limit reached or article [{my_eva.start}] doesn't exist.")
    elif my_eva.EndIsExact:
        print(f"{my_eva.start} → Neon_Genesis_Evangelion ({my_eva.depth} clicks)")
    else:
        print(f"{my_eva.start} → {my_eva.end} ({my_eva.depth} clicks)")
        print(f"{my_eva.end} references Evangelion")

    if input("Print path? (y/n): ") == "y": 
        print(f"{' → '.join(my_eva.path)}")

if __name__ == "__main__":
    main()
