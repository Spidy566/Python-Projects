import emoji

# Print all emojis in text

text = ("Once upon a time in a faraway land 🌍, there lived a grumpy 🧙‍♂️ wizard who had a peculiar fondness for 🍕 "
         "pizza. He spent his days casting spells 🔮 to summon the perfect slice. One day, he accidentally turned his "
         "wand into a 🍆 eggplant emoji! Frantically, he tried to reverse the spell, but all he got were floating 🎈 "
         "balloons. 😱 Eventually, he gave up and decided to open a pizza parlor 🍕 where all the toppings were emojis!"
         " Customers came from near and far to taste his magical creations, and the grumpy wizard finally found "
         "happiness in the doughy embrace of a pepperoni pizza 🍕 with extra 😂 laughter and 💥😂 fireworks!")
emojis = [c for c in text if c in emoji.EMOJI_DATA]
emoji_list = set(emojis)
print(emoji_list)

#Demoji translates emojis to their description

tweet = "I love Python programming! 🐍👨‍💻 "
print(emoji.demojize(tweet))