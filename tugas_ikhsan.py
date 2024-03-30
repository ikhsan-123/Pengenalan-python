import random

def main():
  while True:
    kata = input("Masukkan kata yang ingin diacak: ")

    acak_kata = ''.join(random.sample(kata, len(kata)))
    print(f"Kata setelah diacak: {acak_kata}")

    main_lagi = input("acak kata lagi? (y/n): ").lower()
    if main_lagi != 'y':
      break

if __name__ == "__main__":
  main()
