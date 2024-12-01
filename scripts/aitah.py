import pandas as pd
import re
import sys

def count_YTA_NTA(comments_list):
    # Extract 'body' content from each comment
    bodies = [comment['body'] for comment in comments_list if 'body' in comment]

    # Initialize counters for YTA and NTA
    YTA = 0
    NTA = 0
    
    # Loop through each comment body and count occurrences of YTA and NTA (including YTAH and NTAH)
    for body in bodies:
        YTA += len(re.findall(r'\bYTA\b', body)) + len(re.findall(r'\bYTAH\b', body))
        NTA += len(re.findall(r'\bNTA\b', body)) + len(re.findall(r'\bNTAH\b', body))
    
    return YTA, NTA

def main(file_path):
    # Read the JSON file
    df = pd.read_json(file_path)

    # Get the list of comments
    comments_list = df.T.loc['data', 'comments']

    # Get the counts for YTA and NTA
    YTA, NTA = count_YTA_NTA(comments_list)

    print(f'YTA: {YTA}\nNTA: {NTA}')

if __name__ == "__main__":
    # Ensure a file path is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_json_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)
