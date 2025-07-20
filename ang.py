def stringAnagram(dictionary, query):
    sorted_query = ''.join(sorted(query))
    
    for word in dictionary:
        if ''.join(sorted(word)) == sorted_query:
            return len(query)
  
    return 0            
    
dictionary = ["jeo", "oej", "ejo"]
query = "joe"

print(stringAnagram(dictionary, query))