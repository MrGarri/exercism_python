song = ((0, "first", "a Partridge in a Pear Tree."),
        (1, "first", "and a Partridge in a Pear Tree."),
        (2, "second", "two Turtle Doves, "),
        (3, "third", "three French Hens, "),
        (4, "fourth", "four Calling Birds, "),
        (5, "fifth", "five Gold Rings, "),
        (6, "sixth", "six Geese-a-Laying, "),
        (7, "seventh", "seven Swans-a-Swimming, "),
        (8, "eighth", "eight Maids-a-Milking, "),
        (9, "ninth", "nine Ladies Dancing, "),
        (10, "tenth", "ten Lords-a-Leaping, "),
        (11, "eleventh", "eleven Pipers Piping, "),
        (12, "twelfth", "twelve Drummers Drumming, "))


def recite(start_verse, end_verse):
    result = []
    for day in range(start_verse, end_verse + 1):
        verse = f"On the {song[day][1]} day of Christmas my true love gave to me: "
        if day == 1:
            verse += song[0][2]
        else:
            for i in range(day, 0, -1):
                verse += song[i][2]

        result.append(verse)

    return result
