import re

def extract_source_from_map(map_file_path):
    with open(map_file_path, "r") as map_file:
        map_content = map_file.read()

        # Extract the source code using regular expressions
        source_code = re.search(r'sourcesContent":\s*\[(.*?)\]', map_content, re.DOTALL)

        if source_code:
            return source_code.group(1)
        else:
            return None


def save_source_to_file(source_code, output_file_path):
    with open(output_file_path, "w") as output_file:
        output_file.write(source_code)


# Provide the path to your JavaScript map file
map_file_path = "path/to/your/javascript.map"

# Extract the source code from the map file
source_code = extract_source_from_map(map_file_path)

if source_code:
    # Provide the path to the output file where you want to save the source code
    output_file_path = "path/to/output/file.js"

    # Save the source code to the output file
    save_source_to_file(source_code, output_file_path)

    print("Source code extracted and saved successfully.")
else:
    print("Failed to extract the source code from the map file.")
