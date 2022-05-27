# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here return contents
    with open(filename, 'r') as f:
        contents = f.read()
    return contents


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here

    # Create an empty dictionary
    dic = dict()

    # Loop through each Line of the file contents
    for contentLine in text:
        # Remove the empty spaces and newLine character
        contentLine = contentLine.strip()

        # Convert the characters in each Line to lowercase to avoid case mismatch
        contentLine = contentLine.lower()

        # Split the contentLine into words
        words = contentLine.split(" ")

        # Iterate over each word in Line
        for word in words:
            # Check if the word is already in dictionary
            if word in dic:
                # Increment count of word by 1 if it's there already
                dic[word] = dic[word] + 1
            else:
                # Add the word to dictionary with count 1 if it's not there already
                dic[word] = 1

    # Return the contents of the dictionary in a key and value pair
    for key in list(dic.keys()):

        return {key, ":", dic[key]}
