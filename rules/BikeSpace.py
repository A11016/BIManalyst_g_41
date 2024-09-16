import ifcopenshell
from collections import defaultdict
from bonsai.bim.ifc import IfcStore

def count_furniture_shelving_storage(model):
    # Dictionary to hold the count of types and elements for "Furniture_Shelving-Storage"
    proxy_type_count = defaultdict(int)
    element_count = defaultdict(int)
    
    # Iterate over all instances of IfcBuildingElementProxyType in the model
    for element_type in model.by_type("IfcBuildingElementProxyType"):
        # Filter only types that include the wording "Furniture_Shelving-Storage"
        type_name = element_type.Name if element_type.Name else "Unnamed"
        if "Furniture_Shelving-Storage" in type_name:
            # Increment the count for this type name
            proxy_type_count[type_name] += 1

            # Now count how many elements are associated with this type
            for element in model.by_type("IfcBuildingElementProxy"):
                # Check if the element has a type assigned via the IsTypedBy relationship
                if element.IsTypedBy and element.IsTypedBy[0].RelatingType == element_type:
                    element_count[type_name] += 1
    
    return proxy_type_count, element_count

def calculate_final_count(proxy_type_counts, element_counts):
    final_sum = 0
    
    for type_name, count in element_counts.items():
        if "enkelt" in type_name.lower():
            # Multiply count of "enkelt" types by 6
            final_sum += count * 6
        else:
            # Multiply other types by 12
            final_sum += count * 12
    
    return final_sum

# Get the IFC file using IfcStore (assumes you are using BlenderBIM or a similar environment)
# file = IfcStore.get_file()

# Call the function to count types and elements related to "Furniture_Shelving-Storage"
# proxy_type_counts, element_counts = count_furniture_shelving_storage(file)

# Print the count results
# print("Furniture_Shelving-Storage Type Counts:")
# for type_name, type_count in proxy_type_counts.items():
    # print(f'Type "{type_name}": {type_count} type definition(s), {element_counts[type_name]} element(s)')

 Calculate and display the final sum
 final_count = calculate_final_count(proxy_type_counts, element_counts)
 print(f"\nFinal calculated sum of counts: {final_count}")