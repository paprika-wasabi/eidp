# mi84, pw221, ms2149
if __name__ == "__main__":
    path = input("You are a wandering Adventurer chasing fame, you hear the rumors of a Monster in the Area. Which path you will take, will you fight against the Monster by yourself, become the champion of the people or fight for the Kingdom? [Cave / Castle / Village]: ")
    if path == "Cave":
        Cavepath = input("You decide to enter a nearby Cave. As you start to explore it you hear the sounds, sounds that cannot come from animals. You think that you have entered the Monster’s Den. Will you fight right now, or run to fight another day? [Fight / Run]: ")
        if Cavepath == "Fight":
            print("You didn’t even had a chance and became the monsters’ meal", "\n YOU DIED \n")
        elif Cavepath == "Run":
            Runpath = input("Where will you run,to the secure and stoned Castle of the King, or to the Village, that could be on its last days due to this Monster? [Run to Castle / Run to Village]: ")
            if Runpath == "Run to Castle":
                Castlepath = input("After running away from such Monster, maybe you want to relax a little? Or maybe you should remember the fact that lives of many others depend on you to go into the Castle and inform the King? [ Look Around/ Go inside]: ")
                if Castlepath == "Look Around":
                    Lookaroundpath = input("Will you think that your life is more important and run away like a coward on a stolen Horse? Or will you finally steeled yourself to go in and inform the King?  [Steal the Horse/ Go inside]: ")
                    if Lookaroundpath == "Steal the Horse":
                        steal_the_horse = input("Will you go West and run away from the King, or maybe you will go to East and disappear in front of their eyes? [go West / go East]: ")
                        if steal_the_horse == "go West":
                            print("You were able to escape the King's Mens and find your way Home safely")
                        elif steal_the_horse == "go East":
                            print("You got Captured by the King's Mens")
                            help_the_King = input("He asks will you to help to defeat a Monster which has been vandalizing everything all around the place? [Yes / No]:")
                            if help_the_King == "Yes":
                                print("Together you were able to destroy the horrifying monster and tThe King rewarded you by letting you marry his daughter")
                            elif help_the_King == "No":
                                print("You were terminated by King's Mens", "\n YOU DIED \n")
                    if Castlepath == "Go inside":
                        help_the_King = input("You enter into a great hall. Many people turn around and look at you. A man, supposedly a king, implies that he wants to talk to you. He asks will you to help to defeat the Monster which has been vandalizing everything all around the place? [Yes / No]:")
                        if help_the_King == "Yes":
                            print("The King aplauds you for your bravery, and orders his elite force to accompany to rid the world of this evil monster.")
                            marchpath = input("You lead a March to the Cave, but the visage of this terrifying monster have been burned into your eyes, will you run away of overcome your fear and save the Kingdom[Run away/March towards the Cave]")
                            if marchpath == "Run away":
                                print("The King's Elite Force had no patience for a coward like you, and took care of you Swiftly", "\n YOU DIED \n")
                            elif marchpath == "March towards the Cave":
                                print("With the overwhelming majority given by the sheer number of the Elites, the Monster is no more")
                                FuturePath = input("As you return to the castle, the King greets yu warmly and aplauds you for your courage. As a result of your bravery he gives you a chance to choose from two gifts, his daughter, the Princess, or Gold[Princess/Gold]")
                                if FuturePath == "Princess":
                                    print("You marry the Princess and live a long life as the King")
                                elif FuturePath == "Gold":
                                    print("The King gives you a huge sum of gold; however, after you get out of the Castle this huge sum of Gold attracts all the wrong kind of attention and you die in an ambush by a horde of Bandits", "\n YOU DIED \n")
                        elif help_the_King == "No":
                            print("You were terminated by King's Mens")
            elif Runpath == "Run to Village":
                Villagepath = input("As you arrive at the village people start applauding and praising. An old man comes up to you and asks you to help the village and slay the monster in the cave. He offers you his greatest weapon. pick the path [Help / Not help]: ")
                if Villagepath == "Help":
                    print("You get the Weapon and go back to kill the monster.")
                    MemoryPath = input("As you are rushing towards the Cave, you think to your self, whether this villagers are worth your life. You can still escape, but will you?[Yes / No] ")
                    if MemoryPath == "Yes":
                        print("As you are running away in fear, you don't notice the cliff, you fall down. As you wake up you have no idea how you are here, and what are you doing. You decide to move to a nearby city and lead a normal life")
                        print("Neutral Ending")
                    elif MemoryPath == "No":
                        print("You go inside the den of the Monster, but your hands are shaking uncontrolably. You try to fight this Monster but all you can do is to wound it before you fall to the ground. As you are breathing your last breath you hope that some will be able to finish the Monster")
                elif Villagepath == "Not Help":
                    print("You leave the Village and continue on your Journey. As you are leaving the Monster attacks the village, you freeze from fear. You, like the rest of the Village, have been slaughtered by the Monster", "\n YOU DIED\n")
    if path == "Castle":
        Castlepath = input("You have decided to go towards the castle, the warmth of people around the castle grounds warms your soul, maybe you will look around more? Or will you go inside and find out the truth about disturbing Monster rumors you heard? [ Look Around/ Go inside]: ")
        if Castlepath == "Look Around":
            Lookaroundpath = input("You heard the rumors of a Monster, are you brave enough to face this Monster at the Cost of your life? Maybe you will run away on these horses that you can easily steal, or have you steeled your resolve to go inside the castle to find out the truth? [Steal the Horse/ Go inside]: ")
            if Lookaroundpath == "Steal the Horse":
                steal_the_horse = input("You saddle up but recognize a few men lurking around the corner, ready to chase you. Will you go West and run away from the King, or maybe you will go to East and disappear in front of their eyes? [go West / go East]: ")
                if steal_the_horse == "go West":
                    print("You were able to escape the King's Men and go Home safely")
                elif steal_the_horse == "go East":
                    print("You got Captured by the King's Men")
                    help_the_King = input("He ask will you help to defeat the Monster? [Yes / No]:")
                    if help_the_King == "Yes":
                        print("The King rewarded you by letting you live")
                    elif help_the_King == "No":
                        print("You were terminated by King's Men", "\n YOU DIED \n")
            if Lookaroundpath == "Go inside":
                help_the_King = input("You enter into a great hall. Many people turn around and look at you. A man, supposedly a king, implies that he wants to talk to you. He asks will you to help to defeat the Monster which has been vandalizing everything all around the place? [Yes / No]:")
                if help_the_King == "Yes":
                    print("The King aplauds you for your bravery, and orders his elite force to accompany to rid the world of this evil monster.")
                    marchpath = input("You lead a March to the Cave, but the visage of this terrifying monster have been burned into your eyes, will you run away of overcome your fear and save the Kingdom[Run away/March towards the Cave]")
                    if marchpath == "Run away":
                        print("The King's Elite Force had no patience for a coward like you, and took care of you Swiftly", "\n YOU DIED \n")
                    elif marchpath == "March towards the Cave":
                        print("With the overwhelming majority given by the sheer number of the Elites, the Monster is no more")
                        FuturePath = input("As you return to the castle, the King greets yu warmly and aplauds you for your courage. As a result of your bravery he gives you a chance to choose from two gifts, his daughter, the Princess, or Gold[Princess/Gold]")
                        if FuturePath == "Princess":
                            print("You marry the Princess and live a long life as the King")
                        elif FuturePath == "Gold":
                            print("The King gives you a huge sum of gold; however, after you get out of the Castle this huge sum of Gold attracts all the wrong kind of attention and you die in an ambush by a horde of Bandits", "\n YOU DIED \n")
                elif help_the_King == "No":
                    print("You were terminated by King's Men")
        if Castlepath == "Go inside":
            help_the_King = input("You enter into a great hall. Many people turn around and look at you. A man, supposedly a king, implies that he wants to talk to you. He asks will you help to defeat the Monster which has been vandalizing everything all around the place? [Yes / No]:")
            if help_the_King == "Yes":
                print("The King aplauds you for your bravery, and orders his elite force to accompany to rid the world of this evil monster.")
                marchpath = input("You lead a March to the Cave, but are you really ready to sacrifice your life for random Strangers, will you run away of overcome your fear and save the Kingdom[Run away/March towards the Cave]")
                if marchpath == "Run away":
                    print("The King's Elite Force had no patience for a coward like you, and took care of you Swiftly", "\n YOU DIED \n")
                elif marchpath == "March towards the Cave":
                    print("With the overwhelming majority given by the sheer number of the Elites, the Monster is no more")
                    FuturePath = input("As you return to the castle, the King greets yu warmly and aplauds you for your courage. As a result of your bravery he gives you a chance to choose from two gifts, his daughter, the Princess, or Gold[Princess/Gold]")
                    if FuturePath == "Princess":
                        print("You marry the Princess and live a long life as the King")
                        print("Happy Ending")
                    elif FuturePath == "Gold":
                        print("The King gives you a huge sum of gold; however, after you get out of the Castle this huge sum of Gold attracts all the wrong kind of attention and you die in an ambush by a horde of Bandits", "\n YOU DIED \n")
            elif help_the_King == "No":
                print("You were terminated by King's Men")
    if path == "Village":
        Villagepath = input("You have come to the village, Will you help these poor people and protect them from their upcoming doom,or will you run away with the blood of the death of everyone in the village in your hands?  [Help / Not help]: ")
        if Villagepath == "Help":
            print("You get the Weapon and go back to kill the monster")
            HeroofPeopPath = input("You go into the cave and you see the monster slumbering, will you kill it [Yes/No]")
            if HeroofPeopPath == "Yes":
                print("You return to the village, the shame of killing a sleeping enemy sinks sometimes bothers you, but you think to yourself that it does not matter as long as everyone is alive")
            elif HeroofPeopPath == "No":
                print("The slumbering Monster has woken up due to your loud steps, you fight with all you have and finally deal a deadly blow to the monster, but so does it. Villagers found your dead body, and the Kingdom declares you a Hero.")
        elif Villagepath == "Not help":
            print("You leave the Village and continue on your Journey ")
            JourneyPath = input("During your Journey you come to a new city and you learn what happened to the Village you abandoned. After you selfishly left the town, the entire town was slaughtered by the Monster. You feel this burdening feeling in your chest. You think of drowning your sorrows in booze.[Drink/Not Drink]")
            if JourneyPath == "Drink":
                print("After you became drunk and start to cause a scene, the bartender -kindly- threw you out.")
                DrunkPath = input("During your drunken state you see a river in the city, and you want to go inside, but you are tired and want to lay down also [River/Lay Down]")
                if DrunkPath == "River":
                    print("In your drunk state you drown yourself in the river, in your last moments you think that maybe this is a deserving end for a coward")
                elif DrunkPath == "Lay Down":
                    print("As you are dozing off, random people carry you to an unknown location, where a certain magician experiments on you till you finally die, as you are dying you think maybe this is the end deserving of a coward")
            elif JourneyPath == "Not Drink":
                print("Your guilt swallows you and you decide to go back to the Village and face this monster, even if at the cost of your life.")
                RedempPath = input("You go back to the village, and find everything turned into rubble; however, in the rubble you notice a faint reflection, and want to dig it.[Dig/Not Dig]")
                if RedempPath == "Dig":
                    print("As you dig you find a sword with immpecable worksmanship, you think of avenging the Village, but as you are lost in your thoughts the monster attacks you")
                    FightPath = input("Will you fight the Monster? [Yes/No]")
                    if FightPath == "Yes":
                        print("You have finally decide to attack, but unfortunately the sword slips from your hands. As you embrace your impending death and close your eyes, you see that the sword has stuck the monster. You leave the sword and the corpse of the monster there and leave. You leave the now destroyed village and live in a faraway place alone to repent for the blood on your hands.")
                    elif FightPath == "No":
                        print("You leave the Village with the sword.")
                        HonnorPath = input("After you run away from the village you see a blacksmith shop. If you sell this sword you might have a fortune, you think to yourself[Sell/Not Sell]")
                        if HonnorPath == "Sell":
                            print("After you put the sword on the counter the blacksmith recognizes the handiwork of the sword, and orders guards around to arrest you")
                            ResArrPath = input("Will you resist arrest? [Yes / No]")
                            if ResArrPath == "Yes":
                                print("After you resited arrest, one guard strucks you down, and mumbles 'Must have been the Wind'")
                            elif ResArrPath == "No":
                                print("Even though you did not resist arrest, due to the Value of the sword, you are stripped of everything you have and thrown into mines for a life of manual labor. You die at unknown age, maybe from a cave in or maybe from something else, as you are dying you think that this is a deserving end for a coward")
                        elif HonnorPath == "Not Sell":
                            print("You decide go into the blacksmiths shop, and ask for a swordsmaster to train you. Blacksmith suggest a client of his and you start this new journey to avenge the village")
                            AvengerPath = input("You go to the swordmaster and train, now you are ready to attack the monster. Will you go and end this monster once and for all?[Yes / No]")
                            if AvengerPath == "Yes":
                                print("You go and face the Monster. You kill it, easily, maybe too easily... You think of the people living in the village, and after all those years you finally have hope.")
                                print("Happy Ending")
                            elif AvengerPath == "No":
                                print("Your cowardice is a shame for me and my disciples says the swordsmaster, and kills you. You think maybe this is a deserving end for a coward.", "\n YOU DIED \n")
                elif RedempPath == "Not Dig":
                    print("As you attempt to go back you hear a sound, sound of the Monster. You die in the hands of the beast, as you look you see your legs in the other claw of this monster, you final thoughts waver around how could a coward like you can kill such a monster and your end is well deserved.", "\n YOU DIED \n")