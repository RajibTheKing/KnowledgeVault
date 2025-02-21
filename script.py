import os

# Configuration
root_dir = '.'  # Root directory to start searching
readme_file = 'README.md'
ignore_files = {readme_file}  # Files to ignore

def collect_md_files(dir_path):
    """ Recursively collect all .md files from subdirectories. """
    md_files = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.md') and file not in ignore_files:
                md_files.append(os.path.join(root, file))
    return sorted(md_files)

def generate_readme(md_files):
    """ Generate the README.md by concatenating all .md files. """
    with open(readme_file, 'w') as readme:
        readme.write("# Study Notes Collection\n\n")
        readme.write("Automatically compiled from subdirectories.\n\n")

        for md_file in md_files:
            # Create a section title from the file path
            relative_path = os.path.relpath(md_file, root_dir)
            section_title = relative_path.replace('.md', '').replace('/', ' > ')
            readme.write(f"## {section_title}\n\n")

            # Include the content of the markdown file
            with open(md_file, 'r') as file_content:
                readme.write(file_content.read() + "\n\n")

            # Add a horizontal rule for separation
            readme.write("---\n\n")

def main():
    md_files = collect_md_files(root_dir)
    generate_readme(md_files)
    print(f"{readme_file} has been updated with the latest notes.")

if __name__ == '__main__':
    main()