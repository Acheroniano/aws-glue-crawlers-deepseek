import random
# import pandas as pd
from collections import defaultdict

# Name data by nationality
names_data = {
    'Brazilian': {
        'first_names': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Julia', 'Carlos', 'Beatriz', 'Gabriel', 'Larissa'],
        'last_names': ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Almeida', 'Pereira', 'Lima', 'Costa']
    },
    'Argentinian': {
        'first_names': ['Santiago', 'Valentina', 'Mateo', 'Sofia', 'Benjamin', 'Isabella', 'Lucas', 'Emma', 'Joaquin', 'Mia'],
        'last_names': ['González', 'Rodríguez', 'Fernández', 'López', 'Martínez', 'García', 'Pérez', 'Sánchez', 'Romero', 'Díaz']
    },
    'Croatian': {
        'first_names': ['Luka', 'Ana', 'Ivan', 'Marija', 'Petar', 'Nina', 'Tomislav', 'Elena', 'Matej', 'Sara'],
        'last_names': ['Horvat', 'Kovačić', 'Babić', 'Marić', 'Jurić', 'Novak', 'Kovačević', 'Knežević', 'Vuković', 'Pavić']
    },
    'Ukrainian': {
        'first_names': ['Oleksandr', 'Yulia', 'Dmitro', 'Natalia', 'Ivan', 'Kateryna', 'Andriy', 'Maria', 'Sergiy', 'Olena'],
        'last_names': ['Shevchenko', 'Kovalenko', 'Bondarenko', 'Tkachenko', 'Kravchenko', 'Oleksenko', 'Melnyk', 'Pavlenko', 'Rudenko', 'Lysenko']
    },
    'British': {
        'first_names': ['Oliver', 'Emma', 'Harry', 'Sophie', 'Jack', 'Emily', 'George', 'Charlotte', 'William', 'Lucy'],
        'last_names': ['Smith', 'Jones', 'Williams', 'Brown', 'Taylor', 'Davies', 'Wilson', 'Evans', 'Thomas', 'Johnson']
    },
    'German': {
        'first_names': ['Maximilian', 'Sophie', 'Alexander', 'Emma', 'Paul', 'Hannah', 'Leon', 'Marie', 'Felix', 'Anna'],
        'last_names': ['Müller', 'Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Wagner', 'Becker', 'Schulz', 'Hoffmann']
    },
    'Chinese': {
        'first_names': ['Wei', 'Yan', 'Ming', 'Hui', 'Li', 'Xiao', 'Jun', 'Ying', 'Feng', 'Hong'],
        'last_names': ['Wang', 'Li', 'Zhang', 'Liu', 'Chen', 'Yang', 'Huang', 'Zhao', 'Wu', 'Zhou']
    },
    'Indian': {
        'first_names': ['Aarav', 'Diya', 'Arjun', 'Zara', 'Vihaan', 'Aanya', 'Reyansh', 'Anaya', 'Vivaan', 'Anika'],
        'last_names': ['Patel', 'Sharma', 'Kumar', 'Singh', 'Shah', 'Verma', 'Rao', 'Malhotra', 'Mehta', 'Chopra']
    },
    'Mexican': {
        'first_names': ['José', 'María', 'Juan', 'Guadalupe', 'Miguel', 'Ana', 'Carlos', 'Isabel', 'Francisco', 'Rosa'],
        'last_names': ['García', 'Hernández', 'López', 'Martínez', 'González', 'Rodríguez', 'Pérez', 'Sánchez', 'Ramírez', 'Torres']
    },
    'Vietnamese': {
        'first_names': ['Minh', 'Linh', 'Hung', 'Mai', 'Tuan', 'Hoa', 'Duc', 'Lan', 'Nam', 'Thu'],
        'last_names': ['Nguyen', 'Tran', 'Le', 'Pham', 'Hoang', 'Phan', 'Vu', 'Dang', 'Bui', 'Do']
    },
    'Japanese': {
        'first_names': ['Hiroto', 'Yui', 'Haruto', 'Aoi', 'Yuto', 'Hina', 'Sota', 'Yuna', 'Kento', 'Sakura'],
        'last_names': ['Sato', 'Suzuki', 'Takahashi', 'Tanaka', 'Watanabe', 'Ito', 'Yamamoto', 'Nakamura', 'Kobayashi', 'Kato']
    }
}

# Distribution percentages
distribution = {
    'Brazilian': 10,
    'Argentinian': 15,
    'Croatian': 5,
    'Ukrainian': 10,
    'British': 5,
    'German': 10,
    'Chinese': 5,
    'Indian': 15,
    'Mexican': 10,
    'Vietnamese': 10,
    'Japanese': 5
}

def generate_unique_names(total=100):
    names = []
    used_combinations = set()
    
    # Calculate number of names needed for each nationality
    name_counts = {nat: round((perc/100) * total) for nat, perc in distribution.items()}
    
    # Adjust counts to ensure total is exactly 100
    total_count = sum(name_counts.values())
    if total_count < total:
        name_counts['Indian'] += total - total_count
    
    # Generate names for each nationality
    for nationality, count in name_counts.items():
        first_names = names_data[nationality]['first_names']
        last_names = names_data[nationality]['last_names']
        
        for _ in range(count):
            while True:
                first = random.choice(first_names)
                last = random.choice(last_names)
                full_name = f"{first} {last}"
                
                if full_name not in used_combinations:
                    names.append({'name': full_name, 'nationality': nationality})
                    used_combinations.add(full_name)
                    break
    
    # Shuffle the names
    random.shuffle(names)
    return names

# Generate and print the names
generated_names = generate_unique_names()
for i, name_data in enumerate(generated_names, 1):
    print(f"{i}. {name_data['name']} ({name_data['nationality']})")

