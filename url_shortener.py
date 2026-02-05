import json
import uuid
import os

FILE_NAME = "urls.json"


# Load saved URLs
def load_urls():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}


# Save URLs
def save_urls(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


# Shorten URL
def shorten_url(long_url):
    data = load_urls()

    # Check duplicate URL
    for code, url in data.items():
        if url == long_url:
            print("URL already shortened.")
            return code

    short_code = str(uuid.uuid4())[:6]
    data[short_code] = long_url
    save_urls(data)

    return short_code


# Retrieve original URL
def get_url(code):
    data = load_urls()
    return data.get(code, None)


# CLI Menu
def main():
    while True:
        print("\n===== URL SHORTENER =====")
        print("1. Shorten URL")
        print("2. Retrieve URL")
        print("3. Show All URLs")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            long_url = input("Enter long URL: ").strip()
            if long_url:
                code = shorten_url(long_url)
                print("Short code:", code)
            else:
                print("Invalid URL.")

        elif choice == "2":
            code = input("Enter short code: ").strip()
            url = get_url(code)

            if url:
                print("Original URL:", url)
            else:
                print("URL not found.")

        elif choice == "3":
            data = load_urls()
            if data:
                print("\nStored URLs:")
                for k, v in data.items():
                    print(f"{k} -> {v}")
            else:
                print("No URLs stored yet.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
