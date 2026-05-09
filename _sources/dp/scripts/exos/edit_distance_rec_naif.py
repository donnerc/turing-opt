
# Récursion naïve

def edit_distance(s1: str, s2: str) -> int:
    if s1 == '':
        return len(s2)
    if s2 == '':
        return len(s1)
        
    if s1[0] == s2[0]:
        return edit_distance(s1[1:], s2[1:])
    else:
        remove_dist = 1 + edit_distance(s1[1:], s2)
        update_dist = 1 + edit_distance(s1[1:], s2[1:])
        insert_dist = 1 + edit_distance(s1, s2[1:])

        value = min(remove_dist, update_dist, insert_dist)
        # print(s1, s2, remove_dist, update_dist, insert_dist)
        return value

d = edit_distance("kitten", "sitting")
print(d)
