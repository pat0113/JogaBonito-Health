import json
import os

# List of top 20 Brazilian footballers
players = [
    "Pele", "Garrincha", "Ronaldo", "Socrates", "Zico", 
    "Ronaldinho", "Falcao", "Romario", "Neymar", "Jairzinho", 
    "Cafu", "Didi", "Tostao", "Rivelino", "Carlos Alberto Torres", 
    "Roberto Carlos", "Rivaldo", "Marcelo", "Claudio Taffarel", "Gerson"
]

def create_fhir_patient(name):
    """Creates a simple FHIR R4 Patient resource."""
    return {
        "resourceType": "Patient",
        "name": [
            {
                "text": name
            }
        ],
        "gender": "male"  # Simplified for this exercise
    }

def main():
    output_dir = "fhir_patients"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"Generating FHIR Patient resources in {output_dir}...")
    
    for player in players:
        patient_resource = create_fhir_patient(player)
        filename = f"{player.replace(' ', '_').lower()}.json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(patient_resource, f, indent=2)
        
        print(f"Created: {filename}")

    print("\nSuccess! All patient resources created.")

if __name__ == "__main__":
    main()
