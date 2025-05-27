import os
import sys
import glob

def main():
    if len(sys.argv) != 2:
        print("Usage: cleanup_vhp_id.py <vhp_id>")
        sys.exit(1)
    
    vhp_id = sys.argv[1]
    cache_file = '.vhp-cache/vhp-ids.txt'
    
    if not vhp_id or vhp_id == 'null':
        print("No VHP ID provided")
        sys.exit(0)
    
    # Check if ID appears in any template tables
    id_in_templates = False
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
                    # Check if VHP ID is in the ID column
                    for line in lines[1:]:  # Skip header
                        columns = line.strip().split('\t')
                        if len(columns) > id_column_index:
                            cell_value = columns[id_column_index].strip()
                            if cell_value == vhp_id:
                                id_in_templates = True
                                print(f"ID {vhp_id} found in {template_file}")
                                break
                
                if id_in_templates:
                    break
        except Exception as e:
            print(f"Error reading {template_file}: {e}")
    
    # If ID not in templates, remove from cache
    if not id_in_templates and os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            cached_ids = set(line.strip() for line in f if line.strip())
        
        if vhp_id in cached_ids:
            cached_ids.remove(vhp_id)
            with open(cache_file, 'w') as f:
                for id_str in sorted(cached_ids):
                    f.write(f"{id_str}\n")
            print(f"Removed {vhp_id} from cache")
        else:
            print(f"ID {vhp_id} not found in cache")
    else:
        print(f"ID {vhp_id} is in use in templates, keeping in cache")

if __name__ == "__main__":
    main()
