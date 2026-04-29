import json
import os

# Expanded data for top 20 Brazilian footballers
# Data sourced from general knowledge and search results
players_data = [
    {"name": "Pele", "birthDate": "1940-10-23", "city": "Três Corações", "achievement": "3 World Cups"},
    {"name": "Garrincha", "birthDate": "1933-10-28", "city": "Itapoá", "achievement": "1962 World Cup Hero"},
    {"name": "Ronaldo", "birthDate": "1976-09-22", "city": "Rio de Janeiro", "achievement": "2 World Cups"},
    {"name": "Socrates", "birthDate": "1954-01-12", "city": "São Paulo", "achievement": "1982 World Cup Captain"},
    {"name": "Zico", "birthDate": "1953-03-03", "city": "Rio de Janeiro", "achievement": "Flamengo Legend"},
    {"name": "Ronaldinho", "birthDate": "1980-03-21", "city": "Porto Alegre", "achievement": "Ballon d'Or 2005"},
    {"name": "Falcao", "birthDate": "1953-10-16", "city": "São Paulo", "achievement": "Midfield Maestro"},
    {"name": "Romario", "birthDate": "1966-01-29", "city": "Jacarepaguá", "achievement": "1994 World Cup Star"},
    {"name": "Neymar", "birthDate": "1992-02-05", "city": "Mogi das Cruzes", "achievement": "All-time Top Scorer"},
    {"name": "Jairzinho", "birthDate": "1944-12-04", "city": "Olinda", "achievement": "1970 World Cup Scorer"},
    {"name": "Cafu", "birthDate": "1970-06-07", "city": "São Paulo", "achievement": "Most Capped Player"},
    {"name": "Didi", "birthDate": "1928-01-07", "city": "Sertãozinho", "achievement": "1958 & 1962 Champion"},
    {"name": "Tostao", "birthDate": "1944-01-25", "city": "Juiz de Fora", "achievement": "1970 World Cup Winner"},
    {"name": "Rivelino", "birthDate": "1944-07-07", "city": "São Paulo", "achievement": "The Flip-Flap Pioneer"},
    {"name": "Carlos Alberto Torres", "birthDate": "1944-09-14", "city": "Rio de Janeiro", "achievement": "1970 Captain"},
    {"name": "Roberto Carlos", "birthDate": "1973-04-10", "city": "Garça", "achievement": "Free-kick Specialist"},
    {"name": "Rivaldo", "birthDate": "1973-04-19", "city": "Recife", "achievement": "2002 World Cup Winner"},
    {"name": "Marcelo", "birthDate": "1988-05-12", "city": "Rio de Janeiro", "achievement": "Real Madrid Legend"},
    {"name": "Claudio Taffarel", "birthDate": "1966-08-15", "city": "São Paulo", "achievement": "1994 Hero Goalkeeper"},
    {"name": "Gerson", "birthDate": "1941-01-11", "city": "Rio de Janeiro", "achievement": "1970 Midfield Engine"},
]

def create_fhir_patient(player):
    """Creates an enriched FHIR R4 Patient resource."""
    return {
        "resourceType": "Patient",
        "name": [
            {
                "text": player["name"]
            }
        ],
        "gender": "male",
        "birthDate": player["birthDate"],
        "address": [
            {
                "city": player["city"],
                "country": "Brazil"
            }
        ],
        "extension": [
            {
                "url": "http://hl7.org/fhir/StructureDefinition/football-achievement",
                "valueString": player["achievement"]
            }
        ]
    }

def main():
    output_dir = "fhir_patients"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"Generating enriched FHIR Patient resources in {output_dir}...")
    
    for player in players_data:
        patient_resource = create_fhir_patient(player)
        filename = f"{player['name'].replace(' ', '_').lower()}.json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(patient_resource, f, indent=2)
        
        print(f"Created enriched: {filename}")

    print("\nSuccess! All enriched patient resources created.")

if __name__ == "__main__":
    main()
