import random
import math
def RSV():
    f = open('base_stats.txt','r')
    statfile = f.readlines()
    for i in range(len(statfile)):
        rand = str(random.randint(1,10))
        statfile[i] = statfile[i].split(':')
        statfile[i] = statfile[i][0]+':'+rand+'\n'
    f.close()
    f = open('Starting_Stats.txt','w')
    f.writelines(statfile)
    f.close()
    Set_V()

def Set_V():
#Load starting stats into dictionary
    global stats
    global activities
    global AL
    global Acquaintance
    global Family
    global Friend
    global BF
    global BFFL
    global Partner
    global Spouse
    global pets
    stats = {}
    activities = {'Gym':0, 'School':0, 'Sleep':0, 'Work':0}
    AL = ['Gym', 'School', 'Sleep', 'Work']
    Acquaintance = {}
    Family = {}
    BF = {}
    BFFL = {}
    Friend = {}
    Spouse = {}
    pets = {}
    Partner = {}
    f = open('Starting_Stats.txt','r+')
    for line in f:
        line = line.rstrip('\n')
        line = line.split(':')
        stats[line[0]] = int(line[1])
    Smarts = stats['Education'] * stats['IQ']
    Beauty = stats['Dental_Health'] + stats['Skin_Health'] + stats['Added_Beauty']
    BMI  = stats['Weight'] / ((stats['Height'])^2)
    Physical_Appeal = stats['Strength'] - math.fabs(BMI - 21) + Beauty - math.fabs(stats['Age'] - 24)
    Popularity = sum(Acquaintance.values()) + 2*sum(Friend.values()) + 4*sum(BF.values()) + 8 * sum(Partner.values()) + sum(BFFL.values()) + 16 *sum(Spouse.values()) + stats['Added_Popularity']
    Self_Confidence = stats['Care_About_Image'] * (Physical_Appeal) + stats['Care_About_Friends'] * Popularity + stats['Care_About_Smarts'] * Smarts + stats['Care_About_Englightenment'] * stats['Enlightenment'] + stats['Care_About_Culture'] * stats['Culture'] + stats['Added_Self_Confidence']
    Happiness = Self_Confidence + stats['Added_Happiness']
    
    Sense_of_Humour = stats['Culture'] + Smarts + stats['Creativity'] + stats['Added_Sense_of_Humour']
    Social_Skills = Self_Confidence + Popularity + stats['Added_Social_Skills']
    Appeal = Social_Skills + Physical_Appeal + Happiness + stats['Creativity'] + stats['Education'] + Sense_of_Humour + stats['Enlightenment'] + stats['Money'] + stats['Energy'] + Self_Confidence - math.fabs(stats['Age'] - 25) + stats['Added_Appeal']
    turn()
    
def turn():
    print("hey wassup, here's some activities, so choose some times for tommorow but remember the time allocations will be a percentage of the total time you added in")
    totaltime = 0
    for i in range(len(activities)):
        alloc = input("How much time for "+AL[i]+"?: ")
        alloc = int(alloc)
        activities[(AL[i])] = alloc
        totaltime += alloc
    for i in range(len(activities)):
        num = activities[(AL[i])]
        num = math.floor(((num/totaltime) *100)+.5)
        activities[(AL[i])] = num
    print(activities)
        
def End_Turn():
    try:
        #statement trying to get time allocation.
        stats = stats
    except KeyError:
        #If it can't find it (thus an index error is raised) run this statement.
        stats = stats
    #Now do what you want with the time allocation.
    Beauty = stats['Dental_Health'] + stats['Skin_Health'] + stats['Added_Beauty']
    BMI  = stats['Weight'] / ((stats['Height'])^2)
    Physical_Appeal = stats['Strength'] - math.fabs(BMI - 21) + Beauty - math.fabs(stats['Age'] - 24)
    Popularity = sum(Acquaintance) + 2*sum(Friend) + 4*sum(BF) + 8 * sum(Partner + BFFL) + 16 *sum(Spouse) + Added_Popularity
    Self_Confidence = stats['Care_About_Image'] * (Physical_Appeal) + stats['Care_About_Friends'] * Popularity + stats['Care_About_Smarts'] * Smarts + stats['Care_About_Enlightenment'] * stats['Enlightenment'] + stats['Care_About_Culture'] * Culture + stats['Added_Self_Confidence']
    Happiness = Self_Confidence + stats['Added_Happiness']
    Smarts = stats['Education'] * stats['IQ']
    Sense_of_Humour = stats['Culture'] + Smarts + stats['Creativity'] + stats['Added_Sense_of_Humour']
    Social_Skills = Self_confidence + Popularity + stats['Added_Social_Skills']
    Appeal = Social_Skills + Physical_Appeal + Happiness + stats['Creativity'] + stats['Education'] + Sense_of_Humour + stats['Enlightenment'] + stats['Money'] + stats['Energy'] + Self_Confidence - math.fabs(stats['Age'] - 25) + stats['Added_Appeal']
def Random_Events_Calculator():
    #Work out the random events here
    stats = stats


RSV()
