import os

paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk('YOUR_FOLDER_PATH')
        for filename in filenames)

# The keys of the dictionary are the values to replace, each corresponding
# item is the string to replace it with
replacements = {'REPLACE_THIS': 'WITH_THIS'}

for path in paths:
    # Copy the path name to apply changes (if any) to
    newname = path 
    # Loop over the dictionary elements, applying the replacements
    for k, v in replacements.items():
        newname = newname.replace(k, v)
    if newname != path:
        os.rename(path, newname)