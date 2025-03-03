import random
import time
import os

class TimeWeaver:
    def __init__(self):
        self.chrono_energy = 100
        self.focus_points = 0
        self.current_era = "Chronos Sanctum"
        self.disruptions = []
        self.protected_events = []
        self.abilities = ["Observe", "Subtle Influence"]
        self.game_over = False
        self.turns = 1
        self.max_turns = 20
        
        # Initialize some timeline disruptions
        self.generate_disruptions(3)
    
    def generate_disruptions(self, count):
        eras = ["Ancient Rome", "Medieval Japan", "Renaissance Italy", 
                "Industrial Revolution", "World War II", "Digital Age", "Mars Colony"]
        events = ["assassination", "invention sabotage", "book burning", 
                 "technology theft", "battle outcome change", "cultural revolution"]
        severities = ["minor", "moderate", "major", "critical"]
        
        for _ in range(count):
            era = random.choice(eras)
            event = random.choice(events)
            severity = random.choice(severities)
            energy_cost = 10 if severity == "minor" else 20 if severity == "moderate" else 30 if severity == "major" else 40
            
            self.disruptions.append({
                "era": era,
                "event": event,
                "severity": severity,
                "energy_cost": energy_cost,
                "turns_remaining": random.randint(2, 5)
            })
    
    def display_loom(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*60)
        print(f"TIME WEAVER - Turn {self.turns}/{self.max_turns}")
        print("="*60)
        print(f"Location: {self.current_era}")
        print(f"Chrono-Energy: {self.chrono_energy}")
        print(f"Focus Points: {self.focus_points}")
        print(f"Abilities: {', '.join(self.abilities)}")
        print("="*60)
        
        if self.current_era == "Chronos Sanctum":
            # Display timeline disruptions
            print("\nTIMELINE DISRUPTIONS:")
            if not self.disruptions:
                print("No active disruptions detected.")
            else:
                for i, disruption in enumerate(self.disruptions):
                    print(f"{i+1}. [{disruption['severity'].upper()}] {disruption['era']}: {disruption['event']} " +
                          f"(Cost: {disruption['energy_cost']} energy, {disruption['turns_remaining']} turns remaining)")
            
            # Display protected events
            print("\nPROTECTED EVENTS:")
            if not self.protected_events:
                print("No protected events.")
            else:
                for i, event in enumerate(self.protected_events):
                    print(f"{i+1}. {event['era']}: {event['description']} (Strength: {event['strength']})")
        else:
            # Display era-specific information
            current_disruptions = [d for d in self.disruptions if d['era'] == self.current_era]
            print(f"\nYou are currently in {self.current_era}.")
            
            if current_disruptions:
                print("\nActive disruptions in this era:")
                for i, disruption in enumerate(current_disruptions):
                    print(f"{i+1}. [{disruption['severity'].upper()}] {disruption['event']} " +
                          f"(Cost: {disruption['energy_cost']} energy, {disruption['turns_remaining']} turns remaining)")
            else:
                print("\nThis era is currently stable.")
    
    def display_menu(self):
        print("\n" + "-"*60)
        if self.current_era == "Chronos Sanctum":
            print("ACTIONS:")
            print("1. Travel to an era")
            print("2. Repair a timeline disruption")
            print("3. Strengthen a key event")
            print("4. Research new abilities (costs 2 focus points)")
            print("5. End turn")
            print("6. Quit game")
        else:
            print("ACTIONS:")
            print("1. Observe (cost: 5 energy)")
            print("2. Subtle Influence (cost: 15 energy)")
            if "Direct Intervention" in self.abilities:
                print("3. Direct Intervention (cost: 25 energy)")
            if "Emergency Extraction" in self.abilities:
                print("4. Emergency Extraction (cost: 40 energy)")
            print("5. Return to Chronos Sanctum")
            print("6. Quit game")
        print("-"*60)
    
    def take_action(self, choice):
        if self.current_era == "Chronos Sanctum":
            if choice == "1":
                self.travel_to_era()
            elif choice == "2":
                self.repair_disruption()
            elif choice == "3":
                self.strengthen_event()
            elif choice == "4":
                self.research_ability()
            elif choice == "5":
                self.end_turn()
            elif choice == "6":
                self.quit_game()
            else:
                print("Invalid choice. Please try again.")
        else:
            if choice == "1":
                self.observe()
            elif choice == "2":
                self.subtle_influence()
            elif choice == "3" and "Direct Intervention" in self.abilities:
                self.direct_intervention()
            elif choice == "4" and "Emergency Extraction" in self.abilities:
                self.emergency_extraction()
            elif choice == "5":
                self.return_to_sanctum()
            elif choice == "6":
                self.quit_game()
            else:
                print("Invalid choice. Please try again.")
    
    def travel_to_era(self):
        print("\nAvailable eras:")
        eras = ["Ancient Rome", "Medieval Japan", "Renaissance Italy", 
                "Industrial Revolution", "World War II", "Digital Age", "Mars Colony"]
        
        for i, era in enumerate(eras):
            disruption_count = len([d for d in self.disruptions if d['era'] == era])
            print(f"{i+1}. {era} ({disruption_count} disruptions)")
        
        while True:
            choice = input("\nEnter number of era to travel to (or 0 to cancel): ")
            if choice == "0":
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(eras):
                    self.current_era = eras[index]
                    self.chrono_energy -= 10
                    print(f"\nTraveling to {self.current_era}. (-10 chrono-energy)")
                    input("Press Enter to continue...")
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
    
    def repair_disruption(self):
        if not self.disruptions:
            print("\nNo disruptions to repair.")
            input("Press Enter to continue...")
            return
        
        print("\nSelect disruption to repair:")
        for i, disruption in enumerate(self.disruptions):
            print(f"{i+1}. [{disruption['severity'].upper()}] {disruption['era']}: {disruption['event']} " +
                  f"(Cost: {disruption['energy_cost']} energy)")
        
        while True:
            choice = input("\nEnter number of disruption to repair (or 0 to cancel): ")
            if choice == "0":
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.disruptions):
                    disruption = self.disruptions[index]
                    if self.chrono_energy >= disruption['energy_cost']:
                        self.chrono_energy -= disruption['energy_cost']
                        self.focus_points += 1
                        print(f"\nRepairing {disruption['era']} {disruption['event']}. " +
                              f"(-{disruption['energy_cost']} chrono-energy, +1 focus point)")
                        self.disruptions.pop(index)
                        input("Press Enter to continue...")
                        return
                    else:
                        print("Not enough chrono-energy.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
    
    def strengthen_event(self):
        eras = ["Ancient Rome", "Medieval Japan", "Renaissance Italy", 
                "Industrial Revolution", "World War II", "Digital Age", "Mars Colony"]
        events = [
            "Founding of the Republic", "Samurai code established", "Renaissance art movement",
            "Steam engine invention", "D-Day landing", "Internet development", "First Mars landing"
        ]
        
        print("\nSelect an event to strengthen:")
        for i in range(len(eras)):
            print(f"{i+1}. {eras[i]}: {events[i]} (Cost: 15 energy)")
        
        while True:
            choice = input("\nEnter number of event to strengthen (or 0 to cancel): ")
            if choice == "0":
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(eras):
                    if self.chrono_energy >= 15:
                        self.chrono_energy -= 15
                        
                        # Check if already protected
                        existing = next((e for e in self.protected_events if e['era'] == eras[index] and e['description'] == events[index]), None)
                        
                        if existing:
                            existing['strength'] += 1
                            print(f"\nStrengthening {eras[index]}: {events[index]}. (-15 chrono-energy)")
                            print(f"Protection strength increased to {existing['strength']}.")
                        else:
                            self.protected_events.append({
                                'era': eras[index],
                                'description': events[index],
                                'strength': 1
                            })
                            print(f"\nProtecting {eras[index]}: {events[index]}. (-15 chrono-energy)")
                        
                        input("Press Enter to continue...")
                        return
                    else:
                        print("Not enough chrono-energy.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
    
    def research_ability(self):
        if self.focus_points < 2:
            print("\nNot enough focus points. You need 2 focus points to research a new ability.")
            input("Press Enter to continue...")
            return
        
        available_abilities = []
        if "Direct Intervention" not in self.abilities:
            available_abilities.append("Direct Intervention")
        if "Emergency Extraction" not in self.abilities:
            available_abilities.append("Emergency Extraction")
        if "Time Loop" not in self.abilities:
            available_abilities.append("Time Loop")
        
        if not available_abilities:
            print("\nNo more abilities to research.")
            input("Press Enter to continue...")
            return
        
        print("\nSelect an ability to research:")
        for i, ability in enumerate(available_abilities):
            print(f"{i+1}. {ability}")
        
        while True:
            choice = input("\nEnter number of ability to research (or 0 to cancel): ")
            if choice == "0":
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(available_abilities):
                    self.focus_points -= 2
                    self.abilities.append(available_abilities[index])
                    print(f"\nResearched new ability: {available_abilities[index]}. (-2 focus points)")
                    input("Press Enter to continue...")
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
    
    def observe(self):
        if self.chrono_energy < 5:
            print("\nNot enough chrono-energy.")
            input("Press Enter to continue...")
            return
        
        self.chrono_energy -= 5
        print(f"\nObserving events in {self.current_era}. (-5 chrono-energy)")
        
        # Get disruptions in this era
        current_disruptions = [d for d in self.disruptions if d['era'] == self.current_era]
        
        if current_disruptions:
            print("\nYour observations reveal:")
            for disruption in current_disruptions:
                print(f"- {disruption['event'].capitalize()} disruption details:")
                
                if disruption['severity'] == "minor":
                    print("  This is a small anomaly with limited impact.")
                elif disruption['severity'] == "moderate":
                    print("  This disruption could cause noticeable timeline changes.")
                elif disruption['severity'] == "major":
                    print("  This event threatens major historical developments.")
                else:  # critical
                    print("  This could cause a catastrophic timeline collapse!")
                
                print(f"  Estimated resolution cost: {disruption['energy_cost']} energy")
                print(f"  Time remaining before permanent damage: {disruption['turns_remaining']} turns")
        else:
            print("\nThis era appears stable. No immediate threats detected.")
        
        input("\nPress Enter to continue...")
    
    def subtle_influence(self):
        if self.chrono_energy < 15:
            print("\nNot enough chrono-energy.")
            input("Press Enter to continue...")
            return
        
        current_disruptions = [d for d in self.disruptions if d['era'] == self.current_era]
        if not current_disruptions:
            print("\nNo disruptions to influence in this era.")
            input("Press Enter to continue...")
            return
        
        print("\nSelect disruption to influence:")
        for i, disruption in enumerate(current_disruptions):
            print(f"{i+1}. [{disruption['severity'].upper()}] {disruption['event']} (Cost: 15 energy)")
        
        while True:
            choice = input("\nEnter number of disruption to influence (or 0 to cancel): ")
            if choice == "0":
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(current_disruptions):
                    disruption = current_disruptions[index]
                    self.chrono_energy -= 15
                    
                    success_chance = 40  # 40% chance of success
                    if random.randint(1, 100) <= success_chance:
                        # Find this disruption in the main list
                        main_index = self.disruptions.index(disruption)
                        self.disruptions.pop(main_index)
                        self.focus_points += 1
                        
                        print(f"\nYou successfully influenced the {disruption['event']} disruption! (-15 chrono-energy, +1 focus point)")
                        print("The timeline thread has been repaired.")
                    else:
                        print(f"\nYour subtle influence wasn't enough to fix the {disruption['event']} disruption. (-15 chrono-energy)")
                        print("You might need a more direct approach.")
                    
                    input("\nPress Enter to continue...")
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
    
    def direct_intervention(self):
        if self.chrono_energy < 25:
            print("\nNot enough chrono-energy.")
            input("Press Enter to continue...")
            return
        
        current_disruptions = [d for d in self.disruptions if d['era'] == self.current_era]
        if not current_disruptions:
            print("\nNo disruptions to intervene with in this era.")
            input("Press Enter to continue...")
            return
        
        print("\nSelect disruption for direct intervention:")
        for i, disruption in enumerate(current_disruptions):
            print(f"{i+1}. [{disruption['severity'].upper()}] {disruption['event']} (Cost: 25 energy)")
        
        while True:
            choice = input("\nEnter number of disruption to intervene with (or 0 to cancel): ")
            if choice == "0":
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(current_disruptions):
                    disruption = current_disruptions[index]
                    self.chrono_energy -= 25
                    
                    success_chance = 75  # 75% chance of success
                    if random.randint(1, 100) <= success_chance:
                        # Find this disruption in the main list
                        main_index = self.disruptions.index(disruption)
                        self.disruptions.pop(main_index)
                        self.focus_points += 2
                        
                        print(f"\nYour direct intervention successfully resolved the {disruption['event']} disruption! (-25 chrono-energy, +2 focus points)")
                        print("The timeline has been restored.")
                    else:
                        print(f"\nYour intervention created additional complications! (-25 chrono-energy)")
                        print("The disruption remains, and your presence has been noticed by temporal forces.")
                        
                        # 50% chance of creating a new disruption
                        if random.randint(1, 100) <= 50:
                            self.generate_disruptions(1)
                            print("Your actions have caused a new timeline disruption elsewhere!")
                    
                    input("\nPress Enter to continue...")
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
    
    def emergency_extraction(self):
        if self.chrono_energy < 40:
            print("\nNot enough chrono-energy.")
            input("Press Enter to continue...")
            return
        
        current_disruptions = [d for d in self.disruptions if d['era'] == self.current_era]
        if not current_disruptions:
            print("\nNo disruptions requiring extraction in this era.")
            input("Press Enter to continue...")
            return
        
        print("\nSelect disruption for emergency extraction:")
        for i, disruption in enumerate(current_disruptions):
            print(f"{i+1}. [{disruption['severity'].upper()}] {disruption['event']} (Cost: 40 energy)")
        
        while True:
            choice = input("\nEnter number of disruption for extraction (or 0 to cancel): ")
            if choice == "0":
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(current_disruptions):
                    disruption = current_disruptions[index]
                    self.chrono_energy -= 40
                    
                    # Emergency extraction always succeeds
                    main_index = self.disruptions.index(disruption)
                    self.disruptions.pop(main_index)
                    self.focus_points += 3
                    
                    print(f"\nEmergency extraction successful! (-40 chrono-energy, +3 focus points)")
                    print(f"You've temporarily removed key figures from the {disruption['event']} disruption.")
                    print("The timeline has been stabilized, but there may be consequences later...")
                    
                    # 25% chance of creating a new disruption due to the drastic action
                    if random.randint(1, 100) <= 25:
                        self.generate_disruptions(1)
                        print("Your extraction has caused a new timeline disruption elsewhere!")
                    
                    input("\nPress Enter to continue...")
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
    
    def return_to_sanctum(self):
        self.current_era = "Chronos Sanctum"
        print("\nReturning to Chronos Sanctum.")
        input("Press Enter to continue...")
    
    def end_turn(self):
        # Process end of turn
        self.turns += 1
        self.chrono_energy += 20  # Regenerate some energy
        if self.chrono_energy > 100:
            self.chrono_energy = 100  # Cap at maximum
        
        # Process disruptions
        for disruption in self.disruptions[:]:  # Create a copy to safely modify during iteration
            disruption['turns_remaining'] -= 1
            if disruption['turns_remaining'] <= 0:
                # Check if this event is protected
                protected = next((e for e in self.protected_events 
                                 if e['era'] == disruption['era']), None)
                
                if protected and random.randint(1, 10) <= protected['strength']:
                    print(f"\nA protected event in {disruption['era']} has resisted disruption!")
                    self.disruptions.remove(disruption)
                else:
                    # The disruption causes permanent damage
                    print(f"\nTimeline disruption in {disruption['era']} has caused permanent damage!")
                    print(f"The {disruption['event']} has been irreversibly altered.")
                    self.disruptions.remove(disruption)
                    
                    # Critical disruptions cause game over
                    if disruption['severity'] == "critical":
                        print("\nA critical timeline event has been altered, causing a timeline collapse!")
                        self.game_over = True
                        return
        
        # Random new disruption (30% chance)
        if random.randint(1, 100) <= 30:
            self.generate_disruptions(1)
            print("\nA new timeline disruption has been detected!")
        
        print(f"\nTurn {self.turns} completed. Chrono-energy regenerated (+20).")
        
        # Check for game over conditions
        if self.turns >= self.max_turns:
            print("\nYou've reached the maximum number of turns.")
            if not self.disruptions:
                print("Congratulations! You've successfully maintained the timeline!")
            else:
                print(f"The timeline has {len(self.disruptions)} unresolved disruptions.")
            self.game_over = True
        
        input("Press Enter to continue...")
    
    def quit_game(self):
        confirm = input("\nAre you sure you want to quit? (y/n): ")
        if confirm.lower() == 'y':
            self.game_over = True
            print("\nThank you for playing Time Weaver!")
        else:
            return

def main():
    # Display title screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "="*60)
    print("""
    ████████╗██╗███╗   ███╗███████╗    ██╗    ██╗███████╗ █████╗ ██╗   ██╗███████╗██████╗ 
    ╚══██╔══╝██║████╗ ████║██╔════╝    ██║    ██║██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
       ██║   ██║██╔████╔██║█████╗      ██║ █╗ ██║█████╗  ███████║██║   ██║█████╗  ██████╔╝
       ██║   ██║██║╚██╔╝██║██╔══╝      ██║███╗██║██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
       ██║   ██║██║ ╚═╝ ██║███████╗    ╚███╔███╔╝███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
       ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝     ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                                         
    """)
    print("Guardian of the Timeline")
    print("="*60)
    print("\nWelcome to the Chronos Sanctum, Time Weaver.")
    print("Your mission is to protect the timeline from disruptions and maintain the fabric of history.")
    print("\nYou have 20 turns to stabilize the timeline. Good luck!")
    input("\nPress Enter to begin your temporal journey...")
    
    game = TimeWeaver()
    
    while not game.game_over:
        game.display_loom()
        game.display_menu()
        choice = input("Enter your choice: ")
        game.take_action(choice)
    
    print("\nGame Over")
    
    # Display final results
    if game.turns >= game.max_turns and not game.disruptions:
        print("\nCONGRATULATIONS!")
        print("You've successfully maintained the timeline and completed your duty as a Time Weaver.")
    else:
        print("\nThe timeline has been altered.")
        if game.disruptions:
            print(f"There were {len(game.disruptions)} unresolved disruptions.")
        print("Perhaps another Time Weaver will have better luck next time.")
    
    print(f"\nFinal Score:")
    print(f"Turns Survived: {game.turns}/{game.max_turns}")
    print(f"Focus Points Earned: {game.focus_points}")
    print(f"Protected Events: {len(game.protected_events)}")
    
    print("\nThank you for playing Time Weaver!")

if __name__ == "__main__":
    main()
