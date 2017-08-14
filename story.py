def begin_story():
    print('You are outside in a forest with your friends in the middle of the night playing around. You start hearing noises from one of the bushes.',
    'What do you do?')
    print ('Enter the number that corresponds to your decision')
    user_response = int(input('1. You go ahead and check it out by yourself. \n2. You tell your friends. \n3. You ignore the sound and continue on with your friends'))
    middle_story(user_response, user_name)

def middle_story(user_response, user_name):
    #1. You go ahead and check it out by yourself.
    if (user_response == 1):
        print("As you go and check it out, you notice there is someone behind the bush.", 'What do you do?')
        user_response = int(input("1.You try and talk to the person. \n2.You go and run towards your friends to warn them."))
        middle_storypt2(user_response, user_name)
        
    #2. You tell your friends.
    elif (user_response == 2):
        print("'Guys, there's something behind the bushes.'", "'Calm down", user_name,". 'Its probably nothing.'", "What do you do?")
        user_response = int(input("1.You calm down and continue with your friends"))
        middle_storypt2(user_response, user_name)
        
    #3. You ignore the sound and continue on with your friends.    
    elif (user_response == 3):   
        print("'Guys, did you hear that? It sounds like its coming from those bushes over there.'","'Yeah... Lets go check it out.'", 'What do you do?')
        user_response = int(input("1.Go and check it out."))
        middle_storypt2(user_response, user_name)
        
def middle_storypt2(user_response, user_name):
    #1. You try and talk to the person. 
    if (user_response == 1):
        print("'Hey! What are doing there!.' You see that the person is getting closer, so you react and you try to punch him, but the person grabs your hand and knocks you out.                                                                                                                                     You wake up not remembering where you are. You can barely see because of the fog that was around. You start coming to your senses and notice that you are bleeding. You walk around trying to find your friends but have no luck trying to locate them.'Guys!!!' No answer. As you walk around you notice something on the floor. As you walk closer to it you notice that its one of your friend's phone.", "What do you do?")
        user_response = int(input("1.You pick up the phone. \n2.You ignore the phone and keep on looking."))
        middle_storypt2(user_response, user_name)
        
user_name = input("Enter your name")
begin_story()
