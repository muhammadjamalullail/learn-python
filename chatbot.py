import string
#nama variabel bot yang kita buat
chatbot_name = "chat" + "Bot"

# disini melakukan perulangan
while(True):
    # disini kita melakukan inputan ke pada kita sebagai user
    user_message = input("You: ").lower().strip(string.punctuation+string.whitespace)
    print(chatbot_name + ":", end=' ')

    # kondisi jiki kita ingin keluar dari perulangan
    if user_message == "quit" or user_message == "selesai":
        print("Sampai ketemu lagi 👋")
        break
      
    # disini kondisi-kondisi tertentu jika kita menjawabnya 
    if user_message == "halo":
      # kondisi jika kita mengisi inputan halo
        print("Halo juga 😊", end='')
    elif user_message == "apa kabar":
      # kondisi jika kita mengisi inputan apa kabar
        print("Baik nih 👌 kamu gimana?", end='')
    elif "cuaca cerah" in user_message:
      # kondisi jika kita mengisi inputan cuaca cerah
        print("Iyaa, secerah hatiku ketika memandang wajahmu 😳", end='')
    elif "mendung" in user_message:
      # kondisi jika kita memilih mendung
        print("Hati atau cuaca?", end='')
    elif user_message == "hati":  
      # kondisi jika kita memilih hati
        print("*sending virtual hugs 🤗*", end='')
    elif user_message == "cuaca":  
      # kondisi jika kita memilih cuaca
        print("Cuma cuaca kan, bukan hati 😝", end='')
    elif user_message == "makasih" or user_message == "thanks":
      # kondisi jika kita memilih makasih / thanks
        print("Masama 👍", end='')
    else:
      # kondisi jika kita tidak memilih inputan yang ada diatas
        print("Eh2, gimana? 😵", end='')
    print()

