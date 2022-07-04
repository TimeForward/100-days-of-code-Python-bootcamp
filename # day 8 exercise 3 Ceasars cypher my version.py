# day 8 exercise 2 Ceasars cypher my version


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

  encrypted_text=[]
  alphabet_index=0
  shifted_index=0
  
  for i in text:    
    #getting letter index 
    alphabet_index=alphabet.index(i)
    #and adding the shift to it
    shifted_index=alphabet_index+shift
    #adjusting for when shifted_index is beyond indexable range
    if shifted_index>=len(alphabet):
        shifted_index=shifted_index-len(alphabet)
    # getting letters with shifted index 
    encrypted_text+=alphabet[shifted_index]
    #list to string conversion
    encrypted_text_to_string = ''.join(encrypted_text)
  print(encrypted_text_to_string)
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if "encode" was chosen: call "encrypt" function
if direction=="encode":
    encrypt(text, shift)    

