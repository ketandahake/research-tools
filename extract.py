import os
import json
PAPER_DIR = "papers"

def extract_info(paper_id: str) -> str:
    """
    Search for information about a specific paper across all topic directories.

    Args:
        paper_id: The ID of the paper to look for

    Returns:
        JSON string with paper information if found, error message if not found
    """

    for item in os.listdir(PAPER_DIR):
        item_path = os.path.join(PAPER_DIR, item)
        print(item_path)
        if os.path.isdir(item_path):
            file_path = os.path.join(item_path, "papers_info.json")
            print(file_path)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "r") as json_file:
                        papers_info = json.load(json_file)
                        if paper_id in papers_info:
                            return json.dumps(papers_info[paper_id], indent=2)
                except (FileNotFoundError, json.JSONDecodeError) as e:
                    print(f"Error reading {file_path}: {str(e)}")
                    continue

    return f"There's no saved information related to paper {paper_id}."

if __name__ == "__main__":
    info = extract_info("2603.28944v1")
    print(info)