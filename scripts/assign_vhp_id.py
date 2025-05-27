import os
import re
import glob

def main():
    # Load existing cached IDs or create new cache
    cache_file = '.vhp-cache/vhp-ids.txt'
    os.makedirs('.vhp-cache', exist_ok=True)
    
    cached_ids = set()
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            cached_ids = set(line.strip() for line in f if line.strip())
    
    # Extract IDs from template tables
    template_ids = set()
    for template_file in glob.glob('templates/**/*.tsv', recursive=True):
        try:
            with open(template_file, 'r') as f:
                lines = f.readlines()
                if not lines:
                    continue
                
                # Parse TSV header to find ID column
                header = lines[0].strip().split('\t')
                id_column_index = None
                for i, col in enumerate(header):
                    if col == 'ID':
                        id_column_index = i
                        break
                
                if id_column_index is not None:
                    # Extract VHP IDs from the ID column
                    for line in lines[1:]:  # Skip header
                        columns = line.strip().split('\t')
                        if len(columns) > id_column_index:
                            cell_value = columns[id_column_index].strip()
                            if re.match(r'VHP\d{7}', cell_value):
                                template_ids.add(cell_value)
        except Exception as e:
            print(f"Error reading {template_file}: {e}")
    
    # Combine cached and template IDs
    all_ids = cached_ids.union(template_ids)
    
    # Generate next ID
    if all_ids:
        # Extract numeric parts and find max
        numeric_ids = [int(id_str.replace('VHP', '')) for id_str in all_ids if id_str.startswith('VHP')]
        next_num = max(numeric_ids) + 1 if numeric_ids else 1
    else:
        next_num = 1
        
    new_id = f"VHP{next_num:07d}"
    
    # Add new ID to cache
    all_ids.add(new_id)
    with open(cache_file, 'w') as f:
        for id_str in sorted(all_ids):
            f.write(f"{id_str}\n")
    
    # Set output for GitHub Actions
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f"vhp_id={new_id}\n")

if __name__ == "__main__":
    main()
