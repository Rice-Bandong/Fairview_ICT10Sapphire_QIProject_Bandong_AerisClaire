menu = {
    "Japanese strawberry shortcake": 120,
    "Daifuku": 150,
    "Matcha Roll Cake": 160,
    "Strawberry Flavored Macarons": 180,
    "Castella": 150
}

selected_items = [
    "Japanese strawberry shortcake",
    "Daifuku",
    "Matcha Roll Cake"
]

subtotal = 0
for item in selected_items:
    subtotal += menu[item]

vat = subtotal * 0.12
total = subtotal + vat

print("==== OBMC Entrep Fair Group 4 ====")
print("  𐙚 A Mini Japanese Dessert Shop 𐙚")
print("==================================")
print("==== Receipt ====")
print(f"Subtotal: P{subtotal:.2f}")
print(f"Tax: P{vat:.2f}")
print(f"Total Amount: P{total:.2f}")