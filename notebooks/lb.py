import random
from IPython.display import display, Image

# Define dice sides and their respective image URLs
dice_sides = ['Itta', 'Paan', 'Hukum', 'Chidi', 'Jhandi', 'Burja']
image_paths = {
    'Itta': 'modules\langur-burja\itta.png',   
    'Paan': 'modules\langur-burja\paan.png',   
    'Hukum': 'modules\langur-burja\hukum.png', 
    'Chidi': 'modules\langur-burja\chidi.png', 
    'Jhandi': 'modules\langur-burja\jhandi.png', 
    'Burja': 'modules\langur-burja\burja.png'  
}

# Function to simulate throwing six dice
def throw_six_dice():
    return [random.choice(dice_sides) for _ in range(6)]

# Function to count occurrences of each side
def count_occurrences(dice_results):
    counts = {side: dice_results.count(side) for side in dice_sides}
    return counts

# Function to determine outcome based on counts
def determine_outcome(counts):
    max_count = max(counts.values())
    min_count = min(counts.values())
    if max_count == 6:
        return "Chhaparal"
    elif max_count == 5:
        return "Pacharal"
    elif max_count == 4:
        return "Chaural"
    elif max_count == 3:
        return "Triple"
    elif max_count == 2:
        return "Double"
    elif min_count == 1 and len(set(counts.values())) == 1:
        return "Chhakkadau"
    else:
        return "No special outcome"

# Function to display images for each side
def display_side_images():
    for side, url in image_paths.items():
        display(Image(url=url))

# Simulate throwing six dice
results = throw_six_dice()

# Count occurrences of each side
occurrences = count_occurrences(results)

# Determine outcome based on counts
outcome = determine_outcome(occurrences)

# Display images for each side
display_side_images()

# Display results
print("Outcome of the throw:", results)
