import re
import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Data structures for travel recommendations and jokes
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket","Elafonissi Beach", "Tianya Haijiao", "Cannon Beach"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Mount Mitchell", "Mount Everest", "Aconcagua"],
    "cities": ["Tokyo", "Paris", "New York", "Tokyo", "Shanghai" , "Bengaluru", "Los Angeles" , "Singapore"]
    "Wonders of the World": ["Great Wall of China", "Petra", "Christ the Redeemer", "Machu Picchu", "Chichen Itza", "Colosseum", "Taj Mahal", "The Pyramids of Giza"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!",
    "Why do airlines never lose luggage? They just “reunite” it with you… eventually.",
    "I asked the hotel front desk for a room with a view. Got one—of the parking lot. Bonus: free car exhaust!",
    "Rental car GPS: “Turn right in 500 feet.” Me: turns GPS: “Recalculating… forever.”",
    "Tried to order “local cuisine” at a tourist trap. Got a burger. Turns out “local” means “sold here.”",
    "My travel buddy said, “Let’s wing it!” Now we’re lost in a village where no one speaks English. Wings: 0, Panic: 10.",
    "Hotel Wi-Fi: “Free and fast!” Translation: “Free to connect, fast at disconnecting.”",
    "Why did the suitcase go to therapy? It had too much baggage… and was always getting thrown around.",
    "I packed light for the trip. Now I’m wearing the same shirt for 3 days. Win? Maybe.",
    "Airport security: “Any liquids?” Me: holds up coffee Them: “That’s fine.” Also them: “Empty your water bottle.” Logic: vacation mode.",
    "Tried to take a “serene mountain photo.” Guy in a neon fanny pack photobombed it. Now it’s my favorite souvenir."
]

# Function to greet the user
def greet_user():
    print(Fore.CYAN + "Hello! I'm Travel Bot, your virtual travel assistant ")
    name = input(Fore.YELLOW + "May I know your name? ")
    print(Fore. GREEN+ f"Nice to meet you, {name}! How can I assist you today?")
    return name

# Function to show help options
def show_help():
    print(Fore.MAGENTA + "\nI can assist you with the following:")
    print(Fore.GREEN + "- Provide travel recommendations")
    print(Fore.GREEN + "- Offer packing")
    print(Fore.GREEN + "- Tell Travel jokes")
    print(Fore.CYAN + "Just ask me a question or type 'exit' to leave.\n")

# Function to process user input
def process_input(user_input):
    # Convert input to lowercase, remove leading/trailing spaces, and replace multiple spaces with one
    user_input = user_input.strip().lower()
    user_input = re.sub(r'\s+',' ',user_input)  # Replace multiple spaces with a single space
    return user_input

# Function to provide travel recommendations
def provide_recommendations():
    print(Fore.CYAN + "TravelBot: Sure! Are you interested in beaches, mountains, 7 Wonders of the World or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = process_input(preference)  # Normalize the input

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about visiting {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like this suggestion? (yes/no)")
        response = input(Fore.YELLOW + "You: ").strip().lower()

        if response == "yes":
            print(f"{Fore.GREEN} TravelBot: Great! Have an amazing time in {suggestion}!")
        elif response == "no":
            print(f"{Fore.RED}TravelBot: No worries! Let's find another place.")
            provide_recommendations()  # Recur to suggest another destination
        else:
            print(f"{Fore.RED}TravelBot: I didn't catch that. Let's start over.")
            provide_recommendations()  # Recur to handle unexpected input
    else:
        print(f"{Fore.RED}TravelBot: Sorry, I don't have recommendations for that preference.")

    # Show the help options again
    show_help()

# Function to offer packing tips
def offer_packing_tips():
    print(f"{Fore.CYAN} TravelBot: Where are you traveling to?")
    user_dest = input(f"{Fore.YELLOW}You: ")
    user_dest = (user_dest)  # Normalize the input

    print(f"{Fore.CYAN}TravelBot: How many days will you be staying?")
    days = input(f"{Fore.YELLOW}You: ")

    print(f"{Fore.GREEN}- TravelBot: Packing tips for {days} days in {user_dest}:")
    print(f"{Fore.GREEN}- Invest in Carry-on Sized Bags.")
    print(f"{Fore.GREEN}- Don't Pack Last Minute.")
    print(f"{Fore.GREEN}- Pack Versatile, Layer-able Matching Clothes.")
    print(f"{Fore.GREEN}- Pack Lightweight, Quick-Drying, Easy-Wash Clothes.")
    print(f"{Fore.GREEN}- Bring a Maximum of Four Pairs of Shoes.")
    print(f"{Fore.GREEN}- Use Packing Cubes and Stuff Sacks.")
    print(f"{Fore.GREEN}- Ditch 'Nice to Have' and 'Just in Case' Items.")
    print(f"{Fore.GREEN}- Prioritise Packing Hard-to-Find Items.")

# Function to tell a joke
def tell_joke():
    joke = random.choice (jokes)
    print(f"{Fore.YELLOW}TravelBot:{joke}")
 
# Main chat function
def chat():
    name = greet_user()
    show_help()
    while True:
        user_input = input(f"{Fore.YELLOW}{name}: ")
        processed_input = process_input(user_input)
        
        if "recommendation" in processed_input or "suggest" in processed_input:
            provide_recommendations()
        elif "pack" in processed_input or "packing" in processed_input:
            offer_packing_tips()
        elif "joke" in processed_input or "funny" in processed_input:
            tell_joke()
        elif "help" in processed_input:
            show_help()
        elif "exit" in processed_input or "bye" in processed_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: I'm sorry, I didn't quite catch that. Could you please rephrase?")

# Start the chatbot
if __name__ == "__main__":
 chat()
