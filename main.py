import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

logo = '''


░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

'''

print(logo)

keep_going = True


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def caesar():
    global keep_going
    while keep_going:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("\nType your message:\n").lower()
        try:
            shift = int(input("\nType the shift number:\n"))
            shift = int(shift)
            shift = shift % 26
        except:
            clear_console()
            print(logo)
            print("Please try again , correctly this time! \n")

            continue

        if direction == "encode":
            final_string = ""
            for char in text:
                if char in alphabet:
                    position = alphabet.index(char)
                    new_position = position + shift

                    if char == alphabet[position]:
                        final_string += alphabet[new_position]
                else:
                    final_string += char
            print("\nYour encrypted message is : ")
            print(f"{final_string}\n")
            print("----\n")
            again = input("if you want to try again enter 'Y' , if you want to quit enter 'Q' : \n").lower()
            if again == 'y':
                clear_console()
                print(logo)
                continue

            elif again == 'q':
                print("Have a good day  \n")
                keep_going = False
            else:
                print("Error acquired \n")
                break
        elif direction == "decode":
            final_string = ""

            for char in text:
                if char in alphabet:
                    position = alphabet.index(char)
                    new_position = position - shift
                    if char == alphabet[position]:
                        final_string += alphabet[new_position]
                else:
                    final_string += char
            print("\nYour encrypted message is : ")
            print(f"{final_string}\n")
            print("----\n")
            again = input("if you want to try again enter 'Y' , if you want to quit enter 'Q' : \n").lower()
            if again == 'y':
                clear_console()
                print(logo)

                continue
            elif again == 'q':
                print("Have a good day  \n")
                keep_going = False
            else:
                print("Error acquired \n")
                break

        else:
            clear_console()
            print(logo)
            print("Please choose one of these options \n")


caesar()
