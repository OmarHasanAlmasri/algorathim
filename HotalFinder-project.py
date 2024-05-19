class WordInfo:
    def __init__(self, word, content, rating):
        self.word = word
        self.content = content
        self.rating = rating

# Function to perform bubble sort in descending order based on rating
def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j].rating < arr[j + 1].rating:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Function to perform bubble sort based on alphabetical order of words
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j].word > arr[j + 1].word:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Function to perform linear search for a word in an array
def linear_search(arr, key):
    for i, word_info in enumerate(arr):
        if key == word_info.word:
            return i
    return -1

# Function to perform binary search for a word in a sorted array
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key == arr[mid].word:
            return mid
        elif key < arr[mid].word:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Function to perform linear search for hotels with a specific rating
def search_by_rating(arr, rating):
    results = []
    for word_info in arr:
        if word_info.rating == rating:
            results.append(word_info)
    return results

def main():
    MAX_SIZE = int(input("Enter THE NUMBER OF THE HOTELS: "))

    # Input data into the array
    data = []
    print(f"Enter {MAX_SIZE} HOTELS, their content, and rating:")
    for i in range(MAX_SIZE):
        word = input(f"HOTEL {i + 1}: ")
        content = input(f"Content for {word}: ")
        
        # Rating input validation
        while True:
            try:
                rating = int(input(f"Rating for {word} (1-5): "))
                if 1 <= rating <= 5:
                    break
                else:
                    print("Rating must be between 1 and 5. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
        
        data.append(WordInfo(word, content, rating))

    while True:
        print("\nMenu:")
        print("1. Sort hotels by rating (descending)")
        print("2. Sort hotels by name (alphabetical)")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            bubble_sort_descending(data)
            print("\nHotels sorted by rating (descending order):")
            for word_info in data:
                print("\nHOTEL:", word_info.word)
                print("Content:", word_info.content)
                print("Rating:", word_info.rating)
        
        elif choice == '2':
            bubble_sort(data)
            print("\nHotels sorted by name (alphabetical order):")
            for word_info in data:
                print("\nHOTEL:", word_info.word)
                print("Content:", word_info.content)
                print("Rating:", word_info.rating)
        
        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        while True:
            print("\nSearch Menu:")
            print("1. Search hotel by name")
            print("2. Search hotels by rating")
            print("3. Display all hotels")
            print("4. Exit to main menu")
            
            search_choice = input("Enter your choice: ").strip()

            if search_choice == '1':
                key = input("Enter the hotel name to search: ").strip()
                result = linear_search(data, key)
                if result != -1:
                    print(f"\nHOTEL '{key}' found at index {result}:")
                    print("Content:", data[result].content)
                    print("Rating:", data[result].rating)
                else:
                    print(f"\nHOTEL '{key}' not found")
            
            elif search_choice == '2':
                while True:
                    try:
                        rating = int(input("Enter the rating to search for hotels (1-5): ").strip())
                        if 1 <= rating <= 5:
                            break
                        else:
                            print("Rating must be between 1 and 5. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 5.")
                
                results = search_by_rating(data, rating)
                if results:
                    print(f"\nHotels with rating {rating}:")
                    for word_info in results:
                        print("\nHOTEL:", word_info.word)
                        print("Content:", word_info.content)
                        print("Rating:", word_info.rating)
                else:
                    print(f"\nNo hotels found with rating {rating}")
            
            elif search_choice == '3':
                print("\nAll hotels:")
                for word_info in data:
                    print("\nHOTEL:", word_info.word)
                    print("Content:", word_info.content)
                    print("Rating:", word_info.rating)

            elif search_choice == '4':
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
