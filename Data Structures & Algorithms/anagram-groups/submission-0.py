from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sample list of strings
        words = strs

        # Dictionary to hold groups
        groups = defaultdict(list)

        for word in words:
            # Create a signature: sorted ASCII codes tuple
            signature = tuple(sorted(ord(ch) for ch in word))
            groups[signature].append(word)

        # Convert to list of sublists
        output = list(groups.values())

        return(output)


        # temp = []
        # for i in strs:
        #     temp.append("".join(sorted(i)))
        # output = []
        # for i in range(len(temp)-1):
        #     out = [temp[i]]
        #     if temp[i] == temp[i+1]:
        #         out.append(temp[i+1])
        #     else:
        #         output.append(out)
        # return output
        



# Example output: [['bat', 'tab'], ['cat', 'act', 'tac'], ['dog']]


# data = [1, 1, 2, 2, 3, 3]
# sublists = []
# current = [data[0]]

# for item in data[1:]:
#     if item == current[-1]:  # Same as last element → same group
#         current.append(item)
#     else:
#         sublists.append(current)
#         current = [item]
# sublists.append(current)  # Add last group

# print(sublists)
# # Output: [[1, 1], [2, 2], [3, 3]]


        