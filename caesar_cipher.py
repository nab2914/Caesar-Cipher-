from logo import logo

Alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start,shift,cipher_dir):
    end=""
    if cipher_dir=="decode":
        shift *= -1
    for character in start:
        if character in Alphabets:
             
            position = Alphabets.index(character)
            new_pos = position + shift
            end += Alphabets[new_pos]
        else:
            end += character
    print(f"Here's the {cipher_dir}d result : {end}")
        
        
print(logo) 
user_choice=True
while user_choice:
    
    dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    shift=shift % 26
    caesar(start=text, shift=shift, cipher_dir=dir)
    choice=input("Do you want to continue?yes/no?\n").lower()
    if choice == "no" :
        user_choice=False
        print("End")