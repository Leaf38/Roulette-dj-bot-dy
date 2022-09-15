import locale
from time import strftime

import discord
import validators
from discord.ext import commands
import requests
import random
from datetime import datetime, date, timedelta

intents = discord.Intents.default()  # or .all() if you ticked all, that is easier
intents.members = True  # If you ticked the SERVER MEMBERS INTENT
client = commands.Bot(command_prefix=".", intents=intents)  # "Import" the intents

TOKEN = "MTAxOTMwMDUwNzgxNjMwODc5Nw.GA3OoI.02RedRui49LYFRmeea5OBTB67IjPhzCzzv418g"
locale.setlocale(category=locale.LC_ALL, locale='fr_FR.utf8')

# liste des donjons
listDonjons = [
    ["4051", "1", "Kardorim"],
    ["799", "1", "Tournesol Affamé"],
    ["928", "1", "Mob l'Éponge"],
    ["147", "1", "Bouftou Royal"],
    ["3945", "1", "Kankreblath"],
    ["2975", "1", "Boostache"],
    ["797", "1", "Scarabosse Doré"],
    ["800", "1", "Batofu"],
    ["3238", "1", "Chafer Rönin"],
    ["https://doflex.fr/s/npcs/png/ba710cdcde62e2cbab2e54e06a3a7456.png", "1", "Grunob"],
    ["792", "1", "Bworkette"],
    ["252", "1", "Coffre des Forgerons"],
    ["457", "1", "Shin Larve"],
    ["1027", "1", "Corailleur Magistral"],
    ["2995", "1", "Kwakwa"],
    ["180", "2", "Wa wabbit"],
    ["2960", "2", "Kanniboul Ebil"],
    ["3100", "2", "Nelween"],
    ["1051", "2", "Gourlo le Terrible"],
    ["669", "2", "Craqueleur Légendaire"],
    ["5823", "2", "Draegnerys"],
    ["3460", "2", "Wa wobot"],
    ["4621", "2", "Mantiscore"],
    ["3996", "2", "Reine Nyée"],
    ["173", "2", "Abraknyde Ancestral"],
    ["230", "2", "le Chouque"],
    ["4860", "2", "Choudini"],
    ["113", "3", "Dragon Cochon"],
    ["670", "3", "Koulosse"],
    ["232", "3", "Meulou"],
    ["226", "3", "Moon"],
    ["3476", "3", "Maitre des Pantins"],
    ["3652", "3", "Malléfisk"],
    ["5819", "3", "Kharnozor"],
    ["1071", "3", "Silf le Rasboul Majeur"],
    ["289", "3", "Maitre Corbac"],
    ["940", "3", "Rat Blanc"],
    ["939", "3", "Rat Noir"],
    ["4278", "3", "Pounicheur"],
    [
        "https://static.wikia.nocookie.net/dofus-rp/images/a/a1/Damadrya.webp/revision/latest?cb=20210407203650&path-prefix=fr",
        "3", "Damadrya"],
    ["1188", "3", "Blop Multicolore Royal"],
    ["121", "3", "Minotoror"],
    ["2854", "3", "Royalmouth"],
    ["382", "3", "Tofu Royal"],
    ["854", "3", "Crocabulia"],
    ["780", "3", "Skeunk"],
    ["3852", "3", "Fraktale"],
    ["3618", "3", "Haute Truche"],
    ["4609", "3", "El Piko"],
    ["3753", "3", "Capitaine Ekarlatte"],
    [
        "https://static.wikia.nocookie.net/krosmoz/images/c/cd/Nagate_la_Dame_des_eaux.png/revision/latest/top-crop/width/360/height/360?cb=20210422205010&path-prefix=fr",
        "3", "Nagate"],
    [
        "https://static.wikia.nocookie.net/krosmoz/images/1/16/Tanukou%C3%AF_San.png/revision/latest?cb=20210422214342&path-prefix=fr",
        "3", "Tanukoui San"],
    ["257", "3", "Chêne Mou"],
    ["1086", "3", "Tynril"],
    ["2848", "3", "Mansot Royal"],
    ["https://pbs.twimg.com/media/EqkmPb_W4AEjN-F?format=jpg&name=large", "3", "Hanshi et Shihan"],
    ["https://www.dofus.com/fr/mmorpg/encyclopedie/monstres/6249-founoroshi", "3", "Founoroshi"],
    ["2877", "3", "Ben le Ripate"],
    ["943", "3", "Sphincter Cell"],
    ["3651", "3", "Phossile"],
    ["107", "3", "Hell mina"],
    ["1045", "4", "Kimbo"],
    ["827", "4", "Minotot"],
    ["2924", "4", "Obsidiantre"],
    ["3556", "4", "Kanigroula"],
    ["4264", "4", "Ush Galesh"],
    [
        "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-shogun-tofugawa.png",
        "4", "Shogun"],
    ["2967", "4", "Tengu Givrefoux"],
    ["4726", "4", "Père Ver"],
    ["3849", "4", "XLII"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Koumiho/boss_2.png", "4", "Koumiho"],
    ["2968", "4", "Korriandre"],
    ["478", "4", "Bworker"],
    ["1159", "4", "Ougah"],
    ["3752", "5", "Toxoliath"],
    ["2986", "5", "Kolosso"],
    ["2970", "5", "Fuji Givrefoux"],
    ["2942", "5", "Grolloum"],
    ["2864", "5", "Glourséleste"],
    ["3564", "5", "Ombre"],
    ["4803", "5", "Comte Razof"],
    ["3391", "5", "Missiz Frizz"],
    ["3409", "5", "Sylargh"],
    ["3384", "5", "Klime"],
    ["3397", "5", "Nileza"],
    ["3416", "5", "Comte Harebourg"],
    ["3534", "5", "Merkator"],
    ["3648", "5", "Roi Nidas"],
    ["3726", "5", "Reine des Voleurs"],
    ["3828", "5", "Protozorreur"],
    ["3835", "5", "Vortex"],
    ["4263", "5", "Chaloeil"],
    ["4460", "5", "Capitaine Meno"],
    ["4453", "5", "larve de Koutoulou"],
    ["4444", "5", "Dantinéa"],
    ["4744", "5", "Tal kasha"],
    ["4882", "5", "Anerice la Shushess"],
    ["4967", "5", "Ilyzaelle"],
    ["5100", "5", "Solar"],
    ["5110", "5", "Bethel Akarna"],
    ["5319", "5", "Dazak Martegel"],
    ["5806", "5", "Torkélonia"],
    [
        "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-corruption.png",
        "5", "Corruption"],
    ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgwukbMo2HBtgWYORFotBd30p-jYdzUE96Fw&usqp=CAU", "5",
     "Guerre"],
    ["https://jolstatic.fr/www/captures/93/4/141454.png", "5", "Servitude"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Misere/misere.png", "5", "Misère"],
    [
        "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-orukam.png",
        "5", "Roi imagami"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj19-amirukam-sommaire_orig.jpg", "5",
     "Reine Amirukam"],
    ["http://image.noelshack.com/fichiers/2022/36/7/1662902767-kabahal.png", "5", "Kabahal"],
    # "xxx": "5", #4 Cavaliers
    # "xxx": "5", #Eternel Conflit
]
donjonsDict = {
    "4051": "1",  # Kardorim
    "799": "1",  # Tournesol Affamé
    "928": "1",  # Mob l'Éponge
    "147": "1",  # Bouftou Royal
    "3945": "1",  # Kankreblath
    "2975": "1",  # Boostache
    "797": "1",  # Scarabosse Doré
    "800": "1",  # Batofu
    "3238": "1",  # Chafer Rönin
    "https://doflex.fr/s/npcs/png/ba710cdcde62e2cbab2e54e06a3a7456.png": "1",  # Grunob
    "792": "1",  # Bworkette
    "252": "1",  # Coffre des Forgerons
    "457": "1",  # Shin Larve
    "1027": "1",  # Corailleur Magistral
    "2995": "1",  # Kwakwa
    "180": "2",  # Wa wabbit
    "2960": "2",  # Kanniboul Ebil
    "3100": "2",  # Nelween
    "1051": "2",  # Gourlo le Terrible
    "669": "2",  # Craqueleur Légendaire
    "5823": "2",  # Draegnerys
    "3460": "2",  # Wa wobot
    "4621": "2",  # Mantiscore
    "3996": "2",  # Reine Nyée
    "173": "2",  # Abraknyde Ancestral
    "230": "2",  # le Chouque
    "4860": "2",  # Choudini
    "113": "3",  # Dragon Cochon
    "670": "3",  # Koulosse
    "232": "3",  # Meulou
    "226": "3",  # Moon
    "3476": "3",  # Maitre des Pantins
    "3652": "3",  # Malléfisk
    "5819": "3",  # Kharnozor
    "1071": "3",  # Silf le Rasboul Majeur
    "289": "3",  # Maitre Corbac
    "940": "3",  # Rat Blanc
    "939": "3",  # Rat Noir
    "4278": "3",  # Pounicheur
    "https://static.wikia.nocookie.net/dofus-rp/images/a/a1/Damadrya.webp/revision/latest?cb=20210407203650&path-prefix=fr": "3",
    # Damadrya
    "1188": "3",  # Blop Multicolore Royal
    "121": "3",  # Minotoror
    "2854": "3",  # Royalmouth
    "382": "3",  # Tofu Royal
    "854": "3",  # Crocabulia
    "780": "3",  # Skeunk
    "3852": "3",  # Fraktale
    "3618": "3",  # Haute Truche
    "4609": "3",  # El Piko
    "3753": "3",  # Capitaine Ekarlatte
    "https://static.wikia.nocookie.net/krosmoz/images/c/cd/Nagate_la_Dame_des_eaux.png/revision/latest/top-crop/width/360/height/360?cb=20210422205010&path-prefix=fr": "3",
    # Nagate
    "https://static.wikia.nocookie.net/krosmoz/images/1/16/Tanukou%C3%AF_San.png/revision/latest?cb=20210422214342&path-prefix=fr": "3",
    # Tanukoui San
    "257": "3",  # Chêne Mou
    "1086": "3",  # Tynril
    "2848": "3",  # Mansot Royal
    "https://pbs.twimg.com/media/EqkmPb_W4AEjN-F?format=jpg&name=large": "3",  # Hanshi et Shihan
    "https://www.dofus.com/fr/mmorpg/encyclopedie/monstres/6249-founoroshi": "3",  # Founoroshi
    "2877": "3",  # Ben le Ripate
    "943": "3",  # Sphincter Cell
    "3651": "3",  # Phossile
    "107": "3",  # hell mina
    "1045": "4",  # Kimbo
    "827": "4",  # Minotot
    "2924": "4",  # Obsidiantre
    "3556": "4",  # Kanigroula
    "4264": "4",  # Ush Galesh
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-shogun-tofugawa.png": "4",
    # Shogun
    "2967": "4",  # Tengu Givrefoux
    "4726": "4",  # Père Ver
    "3849": "4",  # XLII
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Koumiho/boss_2.png": "4",  # Koumiho
    "2968": "4",  # Korriandre
    "478": "4",  # Bworker
    "1159": "4",  # Ougah
    "3752": "5",  # Toxoliath
    "2986": "5",  # Kolosso
    "2970": "5",  # Fuji Givrefoux
    "2942": "5",  # Grolloum
    "2864": "5",  # Glourséleste
    "3564": "5",  # Ombre
    "4803": "5",  # Comte Razof
    "3391": "5",  # Missiz Frizz
    "3409": "5",  # Sylargh
    "3384": "5",  # Klime
    "3397": "5",  # Nileza
    "3416": "5",  # Comte Harebourg
    "3534": "5",  # Merkator
    "3648": "5",  # Roi Nidas
    "3726": "5",  # Reine des Voleurs
    "3828": "5",  # Protozorreur
    "3835": "5",  # Vortex
    "4263": "5",  # Chaloeil
    "4460": "5",  # Capitaine Meno
    "4453": "5",  # larve de Koutoulou
    "4444": "5",  # Dantinéa
    "4744": "5",  # Tal kasha
    "4882": "5",  # Anerice la Shushess
    "4967": "5",  # Ilyzaelle
    "5100": "5",  # Solar
    "5110": "5",  # Bethel Akarna
    "5319": "5",  # Dazak Martegel
    "5806": "5",  # Torkélonia
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-corruption.png": "5",
    # Corruption
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgwukbMo2HBtgWYORFotBd30p-jYdzUE96Fw&usqp=CAU": "5",
    # Guerre
    "https://jolstatic.fr/www/captures/93/4/141454.png": "5",  # Servitude
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Misere/misere.png": "5",  # Misère
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-orukam.png": "5",
    # Roi imagami
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj19-amirukam-sommaire_orig.jpg": "5",  # Reine Amirukam
    "http://image.noelshack.com/fichiers/2022/36/7/1662902767-kabahal.png": "5",  # Kabahal
    # "xxx": "5", #4 Cavaliers
    # "xxx": "5", #Eternel Conflit
}

global messageBot


def checkGoodFormatGrp(listArg):
    nbUserInGrp = int(listArg[1])

    if (listArg[1].isdigit()):
        return nbUserInGrp
    else:
        return False

def checkGoodFormatRandom(listArg):
    boolFormat = False
    if (listArg[1].isdigit()):
        level = int(listArg[1])
    else:
        return False
    if (listArg[2].isdigit()):
        nbDay = int(listArg[2])
    else:
        return False
    if (listArg[3].isdigit()):
        nbHours = int(listArg[3])
    else:
        return False
    if (level > 0 and level <= 5):
        boolFormat = True
    else:
        return False
    if (nbHours > 0 and nbHours <= 24):
        boolFormat = True
    else:
        return False
    return boolFormat

def checkGoodFormat(listArg):
    argument = 1
    boolFormat = False
    if len(listArg) <= 1:
        return False
    if len(listArg) == 5:
        name = listArg[1] + " " + listArg[2]
        argument += 2
    else:
        name = listArg[1]
        argument += 1
    nbDj = len(listDonjons)
    boolname = False
    idName = ""
    for i in range(0, nbDj):
        if (name in listDonjons[i][2].lower() and len(name) >= 4):
            idName = listDonjons[i][0]
            boolname = True
        i += 1
    if (boolname == False):
        return False
    if (listArg[argument].isdigit()):
        nbDay = int(listArg[argument])
        argument += 1
    else:
        return False
    if (listArg[argument].isdigit()):
        nbHours = int(listArg[argument])
    else:
        return False
    if (boolname):
        boolFormat = True
    else:
        return False
    if (nbHours > 0 and nbHours <= 24):
        boolFormat = True
    else:
        return False
    return idName


async def sendRandomDj(listArg):
    level = listArg[1]
    nbDay = int(listArg[2])
    nbHours = listArg[3]

    keys = [k for k, v in donjonsDict.items() if v == level]
    idChoixDonjon = random.choice(keys)

    valid = validators.url(idChoixDonjon)
    if valid == True:
        choixDonjon = ""
        imgUrl = idChoixDonjon
    else:
        response = requests.get("https://fr.dofus.dofapi.fr/monsters/" + idChoixDonjon)
        if response.status_code != 200:
            return
        data = response.json()
        choixDonjon = data["name"]
        imgUrl = data["imgUrl"]

    dateNbDay = date.today() + timedelta(nbDay)
    nameDay = dateNbDay.strftime("%A")
    dateNbDay = dateNbDay.strftime("%d/%m/%Y")

    await channelBot.send(
        '@everyone Reagi par :thumbsup: si tu souhaites y participer pour le ' + str(nameDay) + " " + str(
            dateNbDay) + ' à ' + nbHours + 'h\nLe donjon choisi **aléatoirement** est : ' + choixDonjon + ' :arrow_down:')
    messageBot = await channelBot.send(imgUrl)
    emoji = '\N{THUMBS UP SIGN}'
    await messageBot.add_reaction(emoji)


async def randomDj(lastMsgSend):
    lastMsgSendContent = lastMsgSend.content
    if ("%randomdj" in lastMsgSendContent and lastMsgSendContent.startswith('%')):
        channelSend = lastMsgSend.channel
        user = lastMsgSend.author
        if (str(user) != "Solticia#6985" and str(user) != "Milimilix#7983"):
            print("commande random lancer par " + str(user) + " qui n'est pas dans la whitelist")
            await channelSend.send("Vous n'êtes pas autorisé à lancer cette commande")
            return
        listArg = lastMsgSendContent.split()
        if (checkGoodFormatRandom(listArg)):
            await sendRandomDj(listArg)
        else:
            await channelSend.send("Essaies en tapant : %randomdj <level(1-5)> <dans combien de jour> <à quelle heure>")
    else:
        return


async def sendDonjon(lastMsgSend, idName):
    listArg = lastMsgSend.content.split()
    argument = 1
    if len(listArg) == 5:
        name = listArg[1] + " " + listArg[2]
        argument += 2
    else:
        name = listArg[1]
        argument += 1
    user = lastMsgSend.author.name
    channel = lastMsgSend.channel
    nbDay = int(listArg[argument])
    argument+=1
    nbHours = listArg[argument]

    valid = validators.url(idName)
    if valid == True:
        choixDonjon = name
        imgUrl = idName
    else:
        response = requests.get("https://fr.dofus.dofapi.fr/monsters/" + idName)
        if response.status_code != 200:
            return
        data = response.json()
        choixDonjon = data["name"]
        imgUrl = data["imgUrl"]

    dateNbDay = date.today() + timedelta(nbDay)
    nameDay = dateNbDay.strftime("%A")
    dateNbDay = dateNbDay.strftime("%d/%m/%Y")
    await channel.send('Reagi par :thumbsup: si tu souhaites y participer pour le ' + str(nameDay) + " " + str(
        dateNbDay) + ' à ' + nbHours + 'h\nLe donjon choisi par ' + str(
        user) + ' est : ' + choixDonjon + ' :arrow_down:')
    messageBot = await channel.send(imgUrl)
    emoji = '\N{THUMBS UP SIGN}'
    await messageBot.add_reaction(emoji)


async def donjon(lastMsgSend):
    lastMsgSendContent = lastMsgSend.content
    if ("%donjon" in lastMsgSendContent and lastMsgSendContent.startswith('%')):
        channelSend = lastMsgSend.channel
        listArg = lastMsgSendContent.split()
        if (checkGoodFormat(listArg) != False):
            await sendDonjon(lastMsgSend, checkGoodFormat(listArg))
        else:
            await channelSend.send("Essaies en tapant : %donjon <nom du boss> <dans combien de jour> <à quelle heure>")
    else:
        return


async def createRandomGrp(messageBot, nbUser):
    users = set()
    for reaction in messageBot.reactions:
        async for user in reaction.users():
            users.add(user)
    if len(users) <= 1:
        return
    usersReact = set()
    for x in users:
        usersReact.add(x.name)
    usersReact.remove('Roulette des donjons')
    await channelBot.send(((f"Les Participants: " + str(usersReact)).replace("{", "")).replace("}", ""))

    nbOfGrp = 1
    # keys name, value group
    groupes = {
    }
    if (len(usersReact) <= nbUser):
        for x in usersReact:
            groupes[x] = nbOfGrp
    else:
        while len(usersReact) >= nbUser:
            thisgrp = random.sample(usersReact, k=nbUser)
            for x in thisgrp:
                groupes[x] = nbOfGrp
                usersReact.remove(x)
            nbOfGrp += 1
    if (len(usersReact) <= nbUser):
        for x in usersReact:
            groupes[x] = nbOfGrp

    nbOfGrp = groupes[list(groupes.keys())[-1]]
    i = 1
    while i <= nbOfGrp:
        thisGrp = [k for k, v in groupes.items() if v == i]
        jolimsgGrp = ((f"Groupe: " + str(i) + " " + str(thisGrp)).replace("[", "")).replace("]", "")
        await channelBot.send(jolimsgGrp)
        i += 1


async def groupe(lastMsgSend):
    lastMsgSendContent = lastMsgSend.content
    if ("%groupe" in lastMsgSendContent and lastMsgSendContent.startswith('%')):
        channelSend = lastMsgSend.channel
        user = lastMsgSend.author
        if (str(user) != "Solticia#6985" and str(user) != "Milimilix#7983"):
            print("commande random lancer par " + str(user) + " qui n'est pas dans la whitelist")
            await channelSend.send("Vous n'êtes pas autorisé à lancer cette commande")
            return
        listArg = lastMsgSendContent.split()
        if (checkGoodFormatGrp(listArg) != False):
            nbUserInGrp = checkGoodFormatGrp(listArg)
        else:
            await channelSend.send(
                "Essaies en tapant : %groupe <nombre joueur par groupe>")
    else:
        return

    messageBot = await channelBot.fetch_message(channelBot.last_message_id)
    if 'https://' in messageBot.content:
        await createRandomGrp(messageBot, nbUserInGrp)
    else:
        messages = set()
        async for message in channelBot.history(limit=100):
            # do something with all messages
            messages.add(message)
        latestMsgContentImg = set()
        for msg in messages:
            if "https://" in str(msg.content):
                latestMsgContentImg = msg
        await createRandomGrp(latestMsgContentImg, nbUserInGrp)


async def usage_help(lastMsgSend):
    lastMsgSendContent = lastMsgSend.content
    if ("%help" in lastMsgSendContent and lastMsgSendContent.startswith('%')):
        channelSend = lastMsgSend.channel
        await channelSend.send(
            "```%randomdj <level(1-5)(1facile-5difficile)> <dans combien de jour> <à quelle heure>```:arrow_right: Envoi un donjon de manière aléatoire (autorisation requise)\n```%donjon <nom du boss> <dans combien de jour> <à quelle heure>```:arrow_right: Envoi un donjon\n```%groupe <nombre de joueurs par groupe>```:arrow_right: Créer des groupes aléatoires depuis la liste des participants (réactions à un donjon par :thumbsup:)")


@client.event
async def on_message(message):  # this event is called when a message is sent by anyone
    global channelBot
    channelBot = client.get_channel(1018522610218319923)
    user = message.author
    if user == client.user:
        return
    lastMsgSend = await message.channel.fetch_message(message.channel.last_message_id)

    # Set command random donjon with level and date (ex : %randomdj 4 14/09/2022
    await randomDj(lastMsgSend)
    await donjon(lastMsgSend)
    # await groupe(lastMsgSend)
    await usage_help(lastMsgSend)


# Lance le bot
client.run(TOKEN)
