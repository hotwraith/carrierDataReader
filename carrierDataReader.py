import json
import os
import glob

def addCarrier(initialCarrierDict):
    out_file = open("testCallsigns.json", "w")
    testVariable = input("Carrier iD : ")
    testVariable = testVariable.upper()
    shortname = input("Carrier shortname : ")
    if(initialCarrierDict == None):
        initialCarrierDict = {
        "ID": [f"{testVariable}"],
        "shortname": [f"{shortname}"],
        "logID": []
        }
    else:
        initialCarrierDict["ID"].append(f"{testVariable}")
        initialCarrierDict["shortname"].append(f"{shortname}")
    json.dump(initialCarrierDict, indent= 4, fp=out_file)

def delCarrier(initialCarrierDict):
    out_file = open("testCallsigns.json", "w")
    shortname = input("Carrier shortname : ")
    if(initialCarrierDict == None):
        print("There are no carriers to delete")
    else:
        print(f"Carrier deleted, shortname: {shortname}, ID: {initialCarrierDict['ID'][initialCarrierDict['shortname'].index(f'{shortname}')]}")
        initialCarrierDict["ID"].pop(initialCarrierDict["shortname"].index(f"{shortname}"))
        try:
            initialCarrierDict["logID"].pop(initialCarrierDict["shortname"].index(f"{shortname}"))
        except IndexError:
            print(f"{shortname} had no associated logID !")
        #initialCarrierDict["ID"].remove(f"{testVariable}")
        initialCarrierDict["shortname"].remove(f"{shortname}")
    json.dump(initialCarrierDict, indent= 4, fp=out_file)

    
def Menu() :
    open("testCallsigns.json", "a")
    global test_list
    test_list = [("Captain", 0), ('Commodities', 0), ('CarrierFuel', 0), ('BlackMarket', 2000000), ('Refuel', 1500000), ('Repair', 1500000), ('Rearm', 1500000), ('VoucherRedemption', 1850000), ('Exploration', 1850000), ('Shipyard', 6500000), ('Outfitting', 5000000), ('VistaGenomics', 1500000), ('PioneerSupplies', 5000000), ('Bartender', 1750000)]
    default = True
    while default:
        selection = input("Do you want to 1: consult all carrier data, or 2: add a carrier to the DB, or 3: remove a carrier from the DB, or 4: see carrier DB ? (type 'EXIT' to end program) : ")
        if(selection == "1"):
            #default = False
            sync()
            try:
                carrierDB = json.load(open('testCallsigns.json', 'r'))
                j = len(carrierDB['ID'])
                for i in range(j):
                    ReadJournal('CarrierStats', i)
                    ReadJournal('CarrierLocation', i)
            except json.decoder.JSONDecodeError as e:
                pass
        elif(selection == "2"):
            #default = False
            CarrierAdd()
        elif(selection == "3"):
            #default = False
            CarrierRemove()
        elif(selection == "4"):
            carrierDBsee()
        elif(selection == "EXIT"):
            default = False
        else:
            print("Wrong answer")

def CarrierAdd():
    try:
        addCarrier(json.load(open("testCallsigns.json", "r")))
    except json.JSONDecodeError as e:
        addCarrier(None)
    value = True
    while value:
        truthValue = input("Do you want to add another carrier ? y/n ")
        if(truthValue == 'y'):
            fuckingfile = open("testCallsigns.json", "r")
            addCarrier(json.load(fuckingfile))
        elif(truthValue == 'n'):
            value = False
        else: 
            print("No such possibility")

def CarrierRemove():
    try:
        delCarrier(json.load(open("testCallsigns.json", "r")))
    except json.JSONDecodeError as e:
        print("There is no carrier to delete")
    value = True
    while value:
        truthValue = input("Do you want to remove another carrier ? y/n ")
        if(truthValue == 'y'):
            fuckingfile = open("testCallsigns.json", "r")
            try:
                delCarrier(json.load(fuckingfile))
            except ValueError:
                print("No more carriers (?)")
        elif(truthValue == 'n'):
            value = False
        else: 
            print("No such possibility")

def ReadJournal(keypass, z):
    try:
        global data
        carrierDB = json.load(open('testCallsigns.json', 'r'))
        j = len(carrierDB['ID'])
        local = os.environ['USERPROFILE']
        infolder = glob.glob(f'{local}\Saved Games\Frontier Developments\Elite Dangerous\*.log') #this shit doesn't work for general file path smh
        why = len(infolder)-1
        #for z in range(j):
        exit = True
        why = len(infolder)-1
        while exit:
            important = []
            keep_phrase = [f"{keypass}"]
            try:
                with open(infolder[why], 'r') as file:
                    try:
                        data = file.readlines()
                    except UnicodeDecodeError as e:
                        # print(f"Reader threw an {type(e)}, error in carrier DB")
                        pass
                for line in data:
                    for phrase in keep_phrase:
                        if phrase in line:
                            important.append(line)
                            break
            except IndexError as e:
                print(f"No data was found for this carrier ({carrierDB['shortname'][z]}). Skipping to next one (returned {type(e)})")
                exit = False
            #print(data)
                
            for i in range(len(important)-1, -1, -1):
                jsonFile = json.dumps(important[i])
                data = json.loads(jsonFile)
                data = json.loads(data)
                if(data['CarrierID'] == carrierDB['logID'][z] and keypass == 'CarrierStats'):
                    somme = 5000000
                    statPrint(serviceCost(somme))
                    print("This data was collected at: "+data["timestamp"]+"\n")
                    exit = False
                    break
                if(data['CarrierID'] == carrierDB['logID'][z] and keypass == 'CarrierLocation'):
                    print(f"{carrierDB['ID'][z]} is in : {data['StarSystem']}")
                    print("This data was collected at: "+data["timestamp"]+"\n")
                    exit = False
                    break
            why -= 1
    except (json.decoder.JSONDecodeError, IndexError)as e:
        print(f'Carrier DB is most likely empty. Returned {type(e)}')

def serviceCost(somme):
    for i in range(len(data['Crew'])):
        if(data['Crew'][i]['Activated']):
            for j in range(len(test_list)):
                if(data['Crew'][i]['CrewRole'] == test_list[j][0]):
                    somme += test_list[j][1]
    return somme

def statPrint(somme): 
#with open("testdata.json", "w") as file:
    #json.dump(test, file, indent=4)

    print(data['Name']+" ("+data['Callsign']+")")
    print("Carrier balance: " + str(data['Finance']['AvailableBalance'])+ " credits")
    print("Or: "+str("{:.1e}".format(data['Finance']['AvailableBalance']))+ " credits")
    print("That makes for: "+str(round(data['Finance']['AvailableBalance']/(52.1429*somme), 1))+" years of maintenance")
    print(json.dumps(data['SpaceUsage'], indent=4))

def carrierDBsee():
    try:
        carrierDB = json.load(open("testCallsigns.json", "r"))
        print('The DB currently contains the following carriers:')
        for i in range(len(carrierDB['ID'])):
            print(f"shortname : {carrierDB['shortname'][i]}, ID : {carrierDB['ID'][i]}")
    except Exception as e :
        print(f'DB has no elements. Returned {type(e)}')

def sync():
    try:
        global data
        carrierDB = json.load(open('testCallsigns.json', 'r'))
        j = len(carrierDB['ID'])
        if(j > len(carrierDB['logID'])):
            local = os.environ['USERPROFILE']
            infolder = glob.glob(f'{local}\Saved Games\Frontier Developments\Elite Dangerous\*.log') #this shit doesn't work for general file path smh
            why = len(infolder)-1
            for z in range(len(carrierDB['logID']), j):
                exit = True
                why = len(infolder)-1
                while exit:
                    important = []
                    keep_phrase = ["CarrierStats"]
                    try:
                        with open(infolder[why], 'r') as file:
                            try:
                                data = file.readlines()
                            except UnicodeDecodeError as e:
                                #print(f"Reader threw an {type(e)}, error in carrier DB")
                                pass
                        for line in data:
                            for phrase in keep_phrase:
                                if phrase in line:
                                    important.append(line)
                                    break
                    except IndexError as e:
                        print(f"ERROR: couldn't sync {carrierDB['shortname'][z]} with logID (check for typos)")
                        exit = False
                    #print(data)
                        
                    for i in range(len(important)-1, 0, -1):
                        jsonFile = json.dumps(important[i])
                        data = json.loads(jsonFile)
                        data = json.loads(data)
                        if(data['Callsign'] == carrierDB['ID'][z]):
                            carrierID = data['CarrierID']
                            out_file = open("testCallsigns.json", "w")
                            carrierDB["logID"].append(carrierID)
                            json.dump(carrierDB, indent= 4, fp=out_file)
                            exit = False
                            break
                    why -= 1
        print("Carrier DB sync complete ! \n")
    except (json.decoder.JSONDecodeError, IndexError)as e:
        print(f'Carrier DB is most likely empty. Returned {type(e)}')

if __name__ == '__main__':
    Menu()