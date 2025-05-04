import requests

def get_drug_label_data(drug_name):
    # URL to fetch drug label information
    url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}&limit=1"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if there is any drug label data
            if 'results' in data and len(data['results']) > 0:
                drug_label_info = data['results'][0]
                
                # Extract useful information like active ingredients, dosage, and warnings
                brand_name = drug_label_info.get('openfda', {}).get('brand_name', 'N/A')
                ingredients = drug_label_info.get('openfda', {}).get('ingredient', 'N/A')
                dosage = drug_label_info.get('dosage_and_administration', 'N/A')
                
                # Return formatted data
                label_data = f"Brand Name: {brand_name}\nActive Ingredients: {ingredients}\nDosage: {dosage}"
                return label_data
            else:
                return "No label information available for this drug."
        else:
            return f"Error fetching label data. Status Code: {response.status_code}"
    except Exception as e:
        return f"Error fetching data: {str(e)}"


def get_drug_event_data(drug_name):
    # URL to fetch drug event (side effects) data
    url = f"https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:{drug_name}&limit=1"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()

            # Check if there are results
            if 'results' in data and len(data['results']) > 0:
                drug_event_info = data['results'][0]
                
                # Extract side effects (if available)
                side_effects = []
                if 'patient' in drug_event_info and 'reaction' in drug_event_info['patient']:
                    reactions = drug_event_info['patient']['reaction']
                    for reaction in reactions:
                        if 'reactionmeddrapt' in reaction:
                            side_effects.append(reaction['reactionmeddrapt'])
                
                # Remove duplicate side effects
                side_effects = list(set(side_effects))
                
                # Return side effects or message if none available
                if side_effects:
                    return ", ".join(side_effects)
                else:
                    return "No side effects data available."
            else:
                return "No event data available for this drug."
        else:
            return f"Error fetching event data. Status Code: {response.status_code}"
    except Exception as e:
        return f"Error fetching data: {str(e)}"
