import re


def extract_sentences(text):
    # Regular expression pattern to match sentences
    pattern = r'[A-Z0-9].*?[.!?](?=\s[A-Z0-9]|$)'
    sentences = re.findall(pattern, text, flags=re.DOTALL)
    return sentences


def main():
    text = input("Enter your text: ")

    # Extracts sentences
    sentences = extract_sentences(text)

    # Display sentences and count
    print("\nExtracted Sentences:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")


if __name__ == "__main__":
    main()
