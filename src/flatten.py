import sys
import json


# Flattens a dict with a separator
# Takes a child value that is to be flattened, parent key and the separator.
# Returns a flattened dictionary
def flatten(child, parent, separator):
    un_nested = {}

    for key, value in child.items():
        # Updates key value with separator and child key
        parent_key = parent + separator + key if len(parent) > 0 else key

        # Only flattening nested dict types
        if isinstance(value, dict):
            un_nested.update(flatten(value, parent_key, separator))
        else:
            un_nested.update({parent_key:value})
    return un_nested

if __name__ == "__main__":
    try:
        j = sys.stdin
        data = json.load(j)
        out = flatten(data,'', '.')
        
        outfile = ""
        if len(sys.argv) > 1: 
            outfile = open(sys.argv[1], "w")
        else:
            outfile = open("result.json", "w")
        json.dump(out, outfile, indent=4) 
    except:
        print("Something went wrong...")

