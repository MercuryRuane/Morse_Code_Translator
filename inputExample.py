from pathlib import Path
import morsecode

def main():
    phrase = "Hi\nHow are you?"
    morse = morsecode.encrypt(phrase.upper())
    Path("encrypted.txt").write_text(morse, encoding="utf-8")
    print("Encrypted text saved to encrypted.txt")

    message = Path("message.txt").read_text(encoding="utf-8")
    morse2 = morsecode.encrypt(message.upper())
    print(morse2)

if __name__ == '__main__':
    main()
