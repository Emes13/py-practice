'''
a123453789a
m--m--m---m
1. From a given index, find all value matches in the string
-----no, actually just find the first one
-----when the loop reaches the end of the string without a match, return the length until the end of the string.
-----  abcda - length without matches is 4, index math gives str[4]-str[0] so good.
-----  abcde - lw/om is 5, so len(str) has to be added to lengths.
-----  abbde - lw/om is 3, have to do len(str)-str[2]...
==========so basically, create a special index value of len(str) that is put as the second # in the tuple and then everything is uniform
2. Get the max distance for every consecutive distance in the match list
3. Save a record of index1 and index2 (segment), and the distance.
   (It seems that this should be a dict where the distance is the key (for easy finding
     of max) and the segment should be the value (stored as a tuple?))
4. Do the same for each next index in the string and add to the list of records.
5. Now starting with the max distance recorded in the records, find if
   any of the other segments in the records are inside it (index1sub2>index1sub1 && index2sub2<index2sub1)
6. If so, break and proceed to the next largest distance.
7. When a distance is found with no other segments inside it, it is the max distance without 
   repeated chars. 
   
s = abcdbfgh
if index1 = 1 then it will find the match at index2 = 2, which is 4 of the orig string, so index2 + index1 + 1 is good.
'''
from random import random
from math import floor

def lengthOfLongestSubstring(s: str) -> int:
	
	slen = len(s)
	if slen < 1: return 0
	if slen == 1: return 1
	segments = {} # dict[int or float, tuple[int, int]] | dict[distance, tuple[index1, index2]
	# for each char in the str, match against all later chars and if matched, find distance and position.
	# we will need to know the position because if a repeated char is nested between two that are spaced
	# further apart, it will not be a valid length of only nonrepeating characters.
	
	# abcb = b -> 
	
	for index1, char1 in enumerate(s):
		for index2, char2 in enumerate(s[index1+1:]):
			if char2 == char1:
				seg_distance = (index2 + index1 + 1) - index1
				segments[float(seg_distance) + random()] = (index1, index2 + index1 + 1) 
				# False assumption: it shouldn't matter if we overwrite a key with a key of equal value bc we only need to know the max value, 
				## not how many instances of it there are.
				# Truth: You end up deleting substrings without any interpolating strings and keeping one that does have and ends up getting deleted.
				### Solution: add a random float to the key, then remove it with floor() later to compare.
				# test
				print(f"{segments} (f1-1)")
				break
			elif (index2 + index1 + 1) + 1 == slen: # are we at the end of the string slice without a match?
				segments[slen - index1] = (index1, slen) # slen is a "phantom" index representing the end of the str for our purposes
				#test
				print(f"{segments} (f1-2)")
			else:
				continue
	# We should now have segments filled with every segment that begins and ends with the same char
	assert segments != {}
	return max_non_nested_value(segments, s) # should give us the length of longest substring with no repetitions inside it...
			
def max_non_nested_value(segments_to_consume: dict, original_string: str)  -> int: # let's try this recursively
	slen = len(original_string)
	max_to_try = max(segments_to_consume)
	max_index1 = segments_to_consume[max_to_try][0]
	max_index2 = segments_to_consume[max_to_try][1]
	for val, positions in segments_to_consume.items(): # positions: tuple[int, int]
		if val == max_to_try: continue
		
		if (
			positions[0] >= max_index1 
			and positions[1] <= max_index2 
			and positions[1] < slen
			and original_string[positions[0]] == original_string[positions[1]]
		): # a substring interpolates this one
			
			# thought - should I do random()/100 to make sure it's very small in case two are added together?
			if positions[0] > max_index1:
				segments_to_consume[(positions[1] - max_index1) + random()] = (max_index1, positions[1] - 1)
				
			if positions[1] < max_index2 and max_index2 != slen:
				segments_to_consume[(max_index2 - positions[0]) + random()] = (positions[0] + 1, max_index2)
			
			# Cut out the record of the interpolated larger substring.
			del segments_to_consume[max_to_try]
			
			#test
			print(f"{segments_to_consume} (f2)")
			max_non_nested_value(segments_to_consume, original_string)
			break # needed to prevent the for loop from needlessly continuing in each recursion
		else:
			continue
			'''
			Is it a problem that two segs of equal length will be assigned
			different float signatures, one greater than the other?
			'''			
	return floor(max(segments_to_consume))
	
while True:
	print(lengthOfLongestSubstring(input("string: ")))
	