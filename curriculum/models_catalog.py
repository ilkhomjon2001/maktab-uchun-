# -*- coding: utf-8 -*-
"""
Robot master(PM) instruction — to'liq katalog (Google Drive skrinshotlaridan yig'ilgan, 2026-08).
9 bo'lim tasdiqlangan (to'liq), 10-bo'lim CSV orqali tasdiqlangan.
"""

CATALOG = {
    "1.Basic": [
        "Little Lantern 1", "Little Lantern 2", "Little Lantern 3", "Little Lantern 4",
        "Swing", "Cellphone Mount", "Hand Fan", "Crane", "Teeterboard", "Barbecue Grill",
        "Jack", "Sewing Machine", "Triangle", "Quadrilateral", "Parallelogram", "Pilers",
        "Jackknife", "Wheelbarrow", "Expansion Clamp", "Spinning Top 3", "Spinning Top 4",
        "Big Hand Fan", "Weirdo Clock", "Elastic Band Gun", "Hand Drill", "Balance",
        "Wheel Car", "Pulley Crane", "Counter Scale", "Grinding Machine",
        "Vigorous Extrusion Machine", "Lantern", "Rake", "Wheel Barrow", "Hayfork",
        "Siege Vehicle", "Trailer (Basic)", "Skateboard", "Scooter", "Rabble",
        "Sewing Machine 2", "Balance 2", "Stirrer", "Extrusion Machine", "Rail Gate",
        "Flail", "Grinding Donkey", "Mini Locomotive", "Twister Machine", "Balance Car",
    ],
    "2.Inertia": [
        "Elasti-Pumper", "Inertia Pull-Back Car", "Inertia Car 1", "Inertia Car 2",
        "Inertia Car 3", "Top Launcher (with wheels)", "Elasti-Car",
        "Top Launcher (with stand)", "Flytrap",
    ],
    "3.YL Corps": [
        "Tumbler", "Manual Gatling Gun", "Manual Buhr Mill", "Manual Drill Car",
        "Car with YL Man 1", "Car with YL Man 2", "Car with YL Man 3", "Car with YL Man 4",
        "Manual Joint Motion 1", "Manual Joint Motion 2", "Manual Joint Motion 3",
        "Manual Joint Motion 4", "Manual Jumping YL Man 1", "Manual Jumping YL Man 2",
        "Manual Jumping YL Man 3", "Manual Jumping YL Man 4", "Manual Jumping YL Man 5",
        "Manual Jumping YL Man 6", "Manual Jumping YL Man 7", "Manual Jumping YL Man 8",
        "Manual Jumping YL Man 9", "Manual Rotating YL Man 1", "Manual Rotating YL Man 2",
        "Manual Rotating YL Man 3", "Manual Rotating YL Man 4", "Manual Rotating YL Man 5",
        "Manual Rotating YL Man 6", "Manual Rotating YL Man 7", "Manual Rocking YL Man 1",
        "Manual Rocking YL Man 2", "Manual Rocking YL Man 3", "Manual Rocking YL Man 4",
        "Manual Rocking YL Man 5", "Manual Rocking YL Man 6", "Manual Rocking YL Man 7",
        "Manual Rocking YL Man 8", "Manual Rocking YL Man 9", "Manual Rocking YL Man 10",
        "Wings Car", "Copter With YL Man",
    ],
    "4.Electric Engineering": [
        "Santa's Sleigh", "Santa Claus Car", "Armoured Vehicle", "Christmas Tree",
        "Santa Claus Car 2", "Crawler Excavator", "Gear Shifting Fan", "Pivoting Fan",
        "Inchworm", "Skiing Man", "Car Puller", "Hoeing Man", "Weighting Man",
        "Dancing Man", "Forklift", "Hammer Machine", "Sweeper", "Scarecrow", "Pterosaur",
        "Electric Sewing Machine", "RWD Car", "Lifting Platform", "Oil Extractor",
        "Step Man", "Electric Fan", "Rotating Plane", "Electric Helicopter",
        "Dotting Machine", "Circling Machine", "Drawing Machine", "Line Car",
        "Excavator (Gear-driven)", "Excavator (Belt-driven)",
    ],
    "5.Electric YL Crops": [
        "Electric Buhr Mill", "Joint Motion 1", "Joint Motion 2", "Joint Motion 3",
        "Joint Motion 4", "Electric Gatling Gun", "Jumping YL Man 1", "Jumping YL Man 2",
        "Jumping YL Man 3", "Jumping YL Man 4", "Jumping YL Man 5", "Jumping YL Man 6",
        "Jumping YL Man 7", "Jumping YL Man 8", "Jumping YL Man 9", "Roating YL Man 1",
        "Roating YL Man 2", "Roating YL Man 3", "Roating YL Man 4", "Roating YL Man 5",
        "Roating YL Man 6", "Roating YL Man 7", "Rocking YL Man 1", "Rocking YL Man 2",
        "Rocking YL Man 3", "Rocking YL Man 4", "Rocking YL Man 5", "Rocking YL Man 6",
        "Rocking YL Man 7", "Rocking YL Man 8", "Rocking YL Man 9", "Rocking YL Man 10",
    ],
    "6.Electric Animals": [
        "Buffalo (electric)", "Electric Tyrannosaurus", "Electric Stegosaurus",
        "Electric Crocodile", "Electric Mouse", "Electric Cat and Mouse", "Crab (electric)",
        "Electric Tortoise", "Triceratops (electric)", "Dolphin (electric)",
        "Hadrosaur (electric)", "Brachiosaurus (electric)", "Euoplocephalus (electric)",
    ],
    "7.Jr Programming": [
        "Bull", "Tyrannosaurus (AI)", "Rabbit (AI)", "Crocodile (AI)", "Stegosaurus (AI)",
        "Crab (AI)", "Cat And Mouse (AI)", "Mouse (AI)", "Score Indicator",
        "Score Maker (AI)", "Color Sorting", "Programmable Car (AI)", "Automatic Gate",
        "Little Deer", "Mine Clearance", "Bus", "Sorting Box", "Conveyor", "Little Bear",
    ],
    "8.Advanced Building": [
        "Infantry Fighting Vehicle", "Formula Car", "Transformers", "Speeding Car",
        "Trailer", "Kowtow Machine", "Hooded Motorcycle", "Ploughing Tractor", "Cheetch",
        "Dragon Boat", "Propeller-driven Vehicle", "Shark", "Infinite Loop",
        "Osprey Aircraft", "Transport Helicopter", "Steam Train", "Upside Down", "Koi",
        "Telecar",
    ],
    "9.Advanced Programming": [
        "Crab Premium", "Patrol Car", "Tyannosaurus Rex (Adv)", "Stegosaurus (Adv)",
        "Woodpecker", "Tower Crane", "Ladder", "Fork Lift Truck", "Bridge Crane",
        "Eggbeater", "Dual Motor Lunar Rover", "Inspection Robot",
    ],
    "10.Space Series": [
        "Moon Rover", "Star War Aircraft", "Armoured Vehicle (Space)", "Twin Propeller Aircraft",
        "Transport Walker", "Reconnaissance Walker", "Moon Exploration Vehicle",
        "Space Shuttle", "Star Fighting", "Batmobile", "Intersteller Radar Forklift",
        "X Fighter", "Alien Reconnaissance Aircraft", "Interstellar Cannon",
        "Interplanetary Jet", "Satellite Car", "Intersteller Pathfinder Robot",
        "Exploration Robot", "Combat Robot", "Lunar Transporter", "Space Transport Aircraft",
        "Plantary System", "Collection Robot", "Moon Collection Rover", "War Robot",
        "Satellite Rover", "Off-road Rover", "Probe Robot", "Interplanetary Repair Station",
    ],
    "11.Newly-Updated Programming": [
        "Intelligent Gate", "Harley", "Obstacle Avoiding Car", "Line Patrol Tank", "Scooter (Prog)",
        "Elevator", "Ferris Wheel", "Storage Robot", "Rocking Trojan", "Flytrap (Prog)",
        "Turnable F1", "Battle Robot", "Line Patrol Dog", "Line Patrol Dragon",
        "Interstellar Train", "Insert With Clips", "Combat Forklift", "Obstacle Avoiding (2)",
        "Obstacle Avoiding (3)", "Intelligent Forklift", "Pastry Chef", "Big Truck",
        "Automatic Gate (Prog)", "Electric Crocodile 2.0", "Animal Trap",
    ],
}

total = sum(len(v) for v in CATALOG.values())
if __name__ == "__main__":
    for k, v in CATALOG.items():
        print(k, len(v))
    print("TOTAL:", total)
