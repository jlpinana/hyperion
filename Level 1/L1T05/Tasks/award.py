# === Triathlon award example program ====

print("Welcome to the triathlon provincial awards")
print("Enter your times below to check your award:\n")

# Input times from user
# Casting the input to float so the user can add half minutes.
t_running = float(input("Please add your running completion time (in min):\n"))
t_cycling = float(input("Please add your cycling completion time (in min):\n"))
t_swimming = float(input("Please add your swiming completion time (in min):\n"))

# Calculate total event time
total_t = t_running + t_cycling + t_swimming 

# Check what award the user will get
if total_t <= 100:
    print(f"Your total triathlon time was: {total_t} min.")
    print("Congratulations! You have won the Privincial Colours Award")
elif total_t <=105:
    print(f"Your total triathlon time was: {total_t} min.")
    print("Congratulations! You have won the Provincial Half Colours Award")
elif total_t <=110:
    print(f"Your total triathlon time was: {total_t} min.")
    print("Congratulations! You have won the Provincial Scroll Award")
else:
    print(f"Your total triathlon time was: {total_t} min.")
    print("Sorry, you did well but on this ocassion you didn't win any award")

