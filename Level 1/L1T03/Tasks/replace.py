# ===== This is the PSEUDOCODE =====
# Store sentence in a variable
# Replace exclamation marks from the sentence with blank spaces
# Print the new sentence
# Capitalise characters in the new sentence
# Re-print the sentence
# Reverse the sentence
# Re-print the sentence

# ==== Program starts here ====
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog"
print("Original sentence:")
print(sentence)
no_excl_sentence = sentence.replace("!"," ")
print("Sentence with blank spaces instead of '!' marks:")
print(no_excl_sentence)
print("Sentence with all capital leters:")
cap_sentence = no_excl_sentence.upper()
print(cap_sentence)
print("Printing sentence in reverse order:")
print(cap_sentence[::-1])   # Prints all characters of the string starting from the last character and in reverse order.
