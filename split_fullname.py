import os
import Utils
##direction_trans={
##      'n': 'n',  's': 's', 'w': 'w', 'e':'e',
##        'north': 'n',  'south': 's', 'west': 'w', 'east':'e'
##    }

direction_trans={
      'n': 'north',  's': 'south', 'w': 'west', 'e':'east',
        'north': 'north',  'south': 'south', 'west': 'west', 'east':'east'
    }

abbrevation_trans={
'aly':'aly','alley':'aly','ally':'aly','allee':'aly',
    'anx':'anx','annex':'anx','anex':'anx','annx':'anx',
    'arc':'arc','arcade':'arc',
    'avenue': 'ave', 'ave': 'ave', 'av':'ave','aven':'ave','avenu':'ave','avn':'ave','avnue':'ave',
        
        'bayoo':'byu','bayou':'byu','byu':'byu',
        'beach':'bch','bch':'bch',
        'bnd':'bnd','bend':'bnd',
        'bluff':'blf','blf':'blf','bluf':'blf',
          'bluffs':'blfs','blfs':'blfs',
          'bot':'btm','bottm':'btm','bottom':'btm','btm':'btm',
          'blvd':'blvd','boulevard':'blvd','boul':'blvd','boulv':'blvd',
          'br':'br','brnch':'br','branch':'br',
          'brg':'brg','bridge':'brg','brdge':'brg',
          'brook':'brk','brk':'brk',
          'brooks':'brks','brks':'brks',
          'bg':'bg','burg':'bg',
          'bgs':'bgs','burgs':'bgs',
          'bypass':'byp','byp':'byp','bypa':'byp','bypas':'byp','byps':'byp',
        'bldg':'bldg','building':'bldg',
          

          'camp':'cp','cp':'cp','cmp':'cp',
          'cyn':'cyn','canyn':'cyn','canyon':'cyn','cnyn':'cyn',
          'cape':'cpe','cpe':'cpe',
         'cswy':'cswy','causeway':'cswy','causwa':'cswy',
         'center': 'ctr','ctr': 'ctr','cen': 'ctr','cent': 'ctr','centr': 'ctr','centre': 'ctr','cnter': 'ctr','cntr': 'ctr',
          'centers': 'ctrs','ctrs': 'ctrs',
          'crcle':'cir','crcl':'cir','circl':'cir','circ':'cir','cir':'cir','circle':'cir',
          'circles':'cirs','cirs':'cirs',
          'clf':'clf','cliff':'clf',
          'clfs':'clfs','cliffs':'clfs',
          'club':'clb','clb':'clb',
          'common':'cmn','cmn':'cmn',
          'commons':'cmns','cmns':'cmns',
          'cor':'cor','corner':'cor',
          'cors':'cors','corners':'cors',
          'course':'crse','crse':'crse',
          'ct':'ct','court':'ct',
          'courts':'cts','cts':'cts',
          'cove':'cv','cv':'cv',
          'coves':'cvs','cvs':'cvs',
          'crk':'crk','creek':'crk',
          'crsent':'cres','crsnt':'cres','cres':'cres','crescent':'cres',
          'crst':'crst','crest':'crst',
          'xing':'xing','crossing':'xing','crssng':'xing',
          'crossroad':'xrd','xrd':'xrd',
          'crossroads':'xrds','xrds':'xrds',
          'curve':'curv','curv':'curv',
          
      'dale':'dl','dl':'dl',
      'dam':'dm','dm':'dm',
          'dvd':'dv','div':'dv','divide':'dv','dv':'dv',
          'driv':'dr','drv':'dr','dr':'dr','drive':'dr',
          'drs':'drs','drives':'drs',

          'est':'est','estate':'est',
          'ests':'ests','estates':'ests',
      'extension':'ext','ext':'ext','extn':'ext','extnsn':'ext',
      'expy':'expy','exp':'expy','expr':'expy','express':'expy','expressway':'expy','expw':'expy',
    
        'falls':'fls','fls':'fls',
        'fry':'fry','freey':'fry','frry':'fry',
        'flds':'flds','fields':'flds',
        'fld':'fld','field':'fld',
        'flat':'flt','flt':'flt',
        'flats':'flts','flts':'flts',
        'ford':'frd','frd':'frd',
        'fords':'frds','frds':'frds',
        'frst':'frst','forest':'frst','forests':'frst',
        'frg':'frg','forg':'frg','forge':'frg',
        'frgs':'frgs','forges':'frgs',
        'frk':'frk','fork':'frk',
        'frks':'frks','forks':'frks',
        'fwy':'fwy','freeway':'fwy','freewy':'fwy','frway':'fwy','frwy':'fwy',
        'fort':'ft','fort':'ft','frt':'ft',
    
    'gdn':'gdn','garden':'gdn','gardn':'gdn','grdn':'gdn',
    'gdns':'gdns','gardens':'gdns','grdns':'gdns',
    'gtwy':'gtwy','gateway':'gtwy','gatewy':'gtwy','gatway':'gtwy','gtway':'gtwy',
    'glen':'gln','gln':'gln',
    'glens':'glns','glns':'glns',
    
    'grn':'grn','green':'grn',
    'grns':'grns','greens':'grns',
    'grv':'grv','grov':'grv','grove':'grv',
    'grvs':'grvs','groves':'grvs',
    
    'hbr':'hbr','barb':'hbr','harbor':'hbr','harbr':'hbr','brbor':'hbr',
    'hbrs':'hbrs','harbors':'hbrs',
    'hvn':'hvn','haven':'hvn',
    'ht':'hts','hts':'hts',
    'hway':'hwy','hiwy':'hwy','hiway':'hwy','highwy':'hwy','highway':'hwy','hwy':'hwy',
    'hill':'hl','hl':'hl',
    'hills':'hls','hls':'hls',
    'hllw':'holw','holw':'holw','hollow':'holw','hollows':'holw','holws':'holw',
    
    'inlt':'inlt',
    'is':'is','island':'is','islnd':'is',
    'iss':'iss','islands':'iss','islnds':'iss',
    'isle':'isle','isles':'isle',
    
    'jct':'jct','jction':'jct','junction':'jct','junctn':'jct','juncton':'jct','jctn':'jct',
    'jcts':'jcts','jctions':'jcts','junctions':'jcts',
    
    'ky':'ky','key':'ky',
    'kys':'kys','keys':'kys',
    'knl':'knl','knol':'knl','knoll':'knl',
    'knls':'knls','knolls':'knls',
    
    'lk':'lk','lake':'lk',
    'lks':'lks','lakes':'lks',
    'land':'land',
    'landing':'lndg','lndg':'lndg','lndng':'lndg',
    'ln':'ln','lane':'ln',
    'lgt':'lgt','light':'lgt',
    'lgts':'lgts','lights':'lgts',
    'lf':'lf','load':'lf',
    'lck':'lck','lock':'lck',
    'lcks':'lcks','locks':'lcks',
    'ldg':'ldg','ldge':'ldg','lodg':'ldg','lodge':'ldg',
    'loop':'loop','loops':'loop',
    
    'mall':'mall',
    'mnr':'mnr','manor':'mnr',
    'mnrs':'mnrs','manors':'mnrs',
    'meadow':'mdw','mdw':'mdw',
    'meadows':'mdws','mdws':'mdws','medows':'mdws',
    'mill':'ml','ml':'ml',
    'mills':'mls','mls':'mls',
    'msn':'msn','missn':'msn','mssn':'msn',
    'mountain':'mtn','mtn':'mtn','mntain':'mtn','mntn':'mtn','mountin':'mtn','mtin':'mtn',
    'mt':'mt','mount':'mt','mnt':'mt',
    'mtwy':'mtwy','motorway':'mtwy',
    
    'neck':'nck','nck':'nck',
    
    'orch':'orch','orchard':'orch','orchrd':'orch',
    'oval':'oval','ovl':'oval',
    'opas':'opas','overpass':'opas',
    
    'park':'park','prk':'park','pk':'park',
    'parkways':'pkwy','pkwys':'pkwy','parkway':'pkwy','pkwy':'pkwy','parkwy':'pkwy','pky':'pkwy','pkway':'pkwy',
    'pass':'pass',
    'passage':'psge','psge':'psge',
    'path':'path','paths':'paths',
    'pike':'pike','pikes':'pike',
    'pine':'pne','pne':'pne',
    'pines':'pnes','pnes':'pnes',
    'pl':'pl','plaza':'pl',
    'place':'plc',
    'pln':'pln','plain':'pln',
    'plains':'plns','plns':'plns',
    'plaza':'plz','plz':'plz','plza':'plz',
        'point':'pt','pt':'pt',
        'points':'pts','pts':'pts',
        'prt':'prt','port':'prt',
        'prts':'prts','ports':'prts',
        'pr':'pr','prairie':'pr','prr':'pr',
        
        'radl':'radl','rad':'radl','radial':'radl','radiel':'radl',
        'ramp':'ramp',
        'ranch':'rnch','ranches':'rnch','rnch':'rnch','rnchs':'rnch',
        'rpd':'rpd','rapid':'rpd',
        'rpds':'rpds','rapids':'rpds',
        'rst':'rst','rest':'rst',
        'rdg':'rdg','rdge':'rdg','ridge':'rdg',
        'rdgs':'rdgs','ridges':'rdgs',
        'riv':'riv','river':'riv','rvr':'riv','rivr':'riv',
      'road':'rd','rd':'rd',
      'roads':'rds','rds':'rds',
      'rte':'rte','route':'rte',
      'row':'row',
      'rue':'rue',
      'run':'run',
      
      'shl':'shl','shoal':'shl',
      'shls':'shls','shoals':'shls',
      'shr':'shr','shoar':'shr','shore':'shr',
      'shrs':'shrs','shoars':'shrs','shores':'shrs',
      'skwy':'skwy','skyway':'skwy',
      'spg':'spg','spng':'spg','spring':'spg','sprng':'spg',
      'spgs':'spgs','spngs':'spgs','springs':'spgs','sprngs':'spgs',
      'spur':'spur','spurs':'spur',
      'sq':'sq','sqr':'sq','square':'sq','squ':'sq','sqre':'sq',
      'sqs':'sqs','sqrs':'sqs','squares':'sqs',
      'sta':'sta','station':'sta','statn':'sta','stn':'sta',
      'stra':'stra','strav':'stra','straven':'stra','stravenue':'stra','stravn':'stra','strvn':'stra','strvnue':'stra',
      'strm':'strm','stream':'strm','streme':'strm',
      'street': 'st','st': 'st','str':'st','strt':'st',
        'streets':'sts','sts':'sts',
        'smt':'smt','sumit':'smt','sumitt':'smt','summit':'smt',

      'ter':'ter','terrace':'ter','terr':'ter',
      'trwy':'trwy','throughway':'trwy',
      'trce':'trce','trace':'trce','traces':'trce',
      'trak':'trak','track':'trak','tracks':'trak','trk':'trak','trk':'trak','trks':'trak',
      'trfy':'trfy','trafficway':'trfy',
      'trl':'trl','trail':'trl','trails':'trl','trls':'trl',
      'trlr':'trlr','trailer':'trlr','trlrs':'trlr',
      'tunel':'tunl','tunl':'tunl','tunls':'tunl','tunnel':'tunl','tunnels':'tunl','tunnl':'tunl',
      'tpke':"tpke","turnpike":"tpke",'trunpk':'tpke',
      'underpass':'upas','upas':'upas',
      'un':'un','union':'un',
      'uns':'uns','unions':'uns',
      
        
        'vally':'vly','vly':'vly','valley':'vly','vlly':'vly',
        'vallys':'vlys','vlys':'vlys',
        'via':'via','vdct':'via','viadct':'via','viaduct':'via',
        'view':'vw','vw':'vw',
        'views':'vws','vws':'vws',
        'vlg':'vlg','vill':'vlg','village':'vlg','villag':'vlg','villg':'vlg','villiage':'vlg',
        'vlgs':'vlgs','villages':'vlgs',
        'vl':'vl','ville':'vl',
        'vis':'vis','vist':'vis','vista':'vis','vst':'vis','vsta':'vis',
        
        'walk':'walk',
         'walks':'walks',
          'wall':'wall',
          'way':'way','wy':'way',
          'ways':'ways',
          'well':'wl','wl':'wl',
          'wells':'wls','wls':'wls',
          
    }

import csv

# filename = "/home/amogh/Desktop/OpenAddresses_Data/ny/Clean_version/broome.csv"
# newfile="/home/amogh/Desktop/OpenAddresses_Data/ny/Cleaner_version/broome.csv"

def split_fullname(path, file):
    filename = path + file
    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/split_full_name"):
        os.makedirs(Utils.PATH + "/tmp" + "/split_full_name")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/split_full_name/"

    newfile = Utils.PATH + "tmp" + "/split_full_name" + "/" + file

    longtermtrans={}
    from collections import defaultdict
    longtermset=defaultdict(set)

    for abbr in abbrevation_trans:
        value=abbrevation_trans[abbr]
        longtermset[value].add(abbr)

    for longterm in longtermset:
        longest=max(longtermset[longterm],key=lambda x:len(x))
        for longt in longtermset[longterm]:
            longtermtrans[longt]=longest

    out=open(newfile,'wb')
    # fields = ['LON', 'LAT', 'NUMBER', 'PREFIX', 'STREET', 'POSTDIRECTIONAL', 'POSTFIX', 'UNIT', 'CITY', 'DISTRICT', 'REGION', 'POSTCODE',
    #           'ID', 'HASH']
    fields = Utils.keep_cols
    fields.append("PREFIX")
    fields.append("POSTFIX")
    fields.append("POSTDIRECTIONAL")
    outf=csv.DictWriter(out,fieldnames=fields)
    outf.writeheader()
    with open(filename,"Ur") as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:

            fname=row[Utils.street_column].lower()

            fs=fname.split(' ')

            start,end=0,len(fs)

            if direction_trans.has_key(fs[0]):
                fs[0]=direction_trans[fs[0]]
                row['PREFIX']=fs[0]
                start+=1
            if abbrevation_trans.has_key(fs[-1]):
                fs[-1]=longtermtrans[fs[-1]]
                row['POSTFIX']=fs[-1]
                end-=1

            # # if fs[-1] is direction, check fs[-2] is abbr
            # if direction_trans.has_key(fs[-1]):
            #     fs[0]=direction_trans[fs[-1]]
            #     row['POSTDIRECTIONAL']=fs[-1]
            #     end-=1
            #     if(len(fs) > 1):
            #         if abbrevation_trans.has_key(fs[-2]):
            #             fs[-1] = longtermtrans[fs[-2]]
            #             row['POSTFIX'] = fs[-2]
            #             end -= 1


            if start>=end and start>0:
                start-=1
                del row['PREFIX']

            if start>=end and end<len(fs):
                end+=1
                del row['POSTFIX']
                # if(row['POSTFIX']):
                #     del row['POSTFIX']
                # if(row['POSTDIRECTIONAL']):
                #     del row['POSTDIRECTIONAL']


            fs = fs[start:end]

            row_street_long = []
            for token in fs:
                if abbrevation_trans.has_key(token):
                    token = longtermtrans[token]
                row_street_long.append(token)

            row_street = ' '.join(row_street_long)
            row_street = row_street.strip()

            row[Utils.street_column] = row_street

            outf.writerow(row)

    out.close()

    return return_manipulatedcsv

def postDirectionalProcessing(path, file):

    filename = path + file
    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/post_directional_process"):
        os.makedirs(Utils.PATH + "/tmp" + "/post_directional_process")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/post_directional_process/"

    newfile = Utils.PATH + "tmp" + "/post_directional_process" + "/" + file

    longtermtrans = {}
    from collections import defaultdict
    longtermset = defaultdict(set)

    for abbr in abbrevation_trans:
        value = abbrevation_trans[abbr]
        longtermset[value].add(abbr)

    for longterm in longtermset:
        longest = max(longtermset[longterm], key=lambda x: len(x))
        for longt in longtermset[longterm]:
            longtermtrans[longt] = longest

    out = open(newfile, 'wb')
    # fields = ['LON', 'LAT', 'NUMBER', 'PREFIX', 'STREET', 'POSTDIRECTIONAL', 'POSTFIX', 'UNIT', 'CITY', 'DISTRICT', 'REGION', 'POSTCODE',
    #           'ID', 'HASH']
    fields = Utils.keep_cols
    # fields.append("PREFIX")
    # fields.append("POSTFIX")
    # fields.append("POSTDIRECTIONAL")
    outf = csv.DictWriter(out, fieldnames=fields)
    outf.writeheader()
    with open(filename, "Ur") as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            fname = row[Utils.street_column].lower()

            fs = fname.split(' ')

            start, end = 0, len(fs)

            if len(fs) > 1:
                if direction_trans.has_key(fs[-1]):
                    fs[-1] = direction_trans[fs[-1]]
                    row['POSTDIRECTIONAL'] = fs[-1]
                    end -= 1
                    # if(len(fs) > 2):
                    #     if abbrevation_trans.has_key(fs[-2]):
                    #         fs[-1] = longtermtrans[fs[-2]]
                    #         row['POSTFIX'] = fs[-2]
                    #         end -= 1


            fs = fs[start:end]
            if(len(fs) == 0):
                fs = row['PREFIX']
                del row['PREFIX']

            row_street_long = []
            for token in fs:
                if abbrevation_trans.has_key(token):
                    token = longtermtrans[token]
                row_street_long.append(token)

            row_street = ' '.join(row_street_long)
            row_street = row_street.strip()

            row[Utils.street_column] = row_street

            outf.writerow(row)

    out.close()
    csvfile.close()

    return return_manipulatedcsv

def remedyPostDirectional(path, file):
    filename = path + file
    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/remedy_post_dir"):
        os.makedirs(Utils.PATH + "/tmp" + "/remedy_post_dir")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/remedy_post_dir/"

    newfile = Utils.PATH + "tmp" + "/remedy_post_dir" + "/" + file

    longtermtrans = {}
    from collections import defaultdict
    longtermset = defaultdict(set)

    for abbr in abbrevation_trans:
        value = abbrevation_trans[abbr]
        longtermset[value].add(abbr)

    for longterm in longtermset:
        longest = max(longtermset[longterm], key=lambda x: len(x))
        for longt in longtermset[longterm]:
            longtermtrans[longt] = longest

    out = open(newfile, 'wb')
    # fields = ['LON', 'LAT', 'NUMBER', 'PREFIX', 'STREET', 'POSTDIRECTIONAL', 'POSTFIX', 'UNIT', 'CITY', 'DISTRICT', 'REGION', 'POSTCODE',
    #           'ID', 'HASH']
    fields = Utils.keep_cols
    # fields.append("PREFIX")
    # fields.append("POSTFIX")
    # fields.append("POSTDIRECTIONAL")
    outf = csv.DictWriter(out, fieldnames=fields)
    outf.writeheader()
    with open(filename, "Ur") as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            fname = row[Utils.street_column].lower()

            fs = fname.split(' ')

            start, end = 0, len(fs)

            if abbrevation_trans.has_key(fs[-1]):
                fs[-1] = longtermtrans[fs[-1]]
                if(len(fs) > 1 or row['PREFIX']):
                    row['POSTFIX'] = fs[-1]
                    end -= 1

            fs = fs[start:end]
            if (len(fs) == 0):
                fs = row['PREFIX']
                fs = fs.split()
                # print fs
                del row['PREFIX']

            row_street_long = []
            for token in fs:
                if abbrevation_trans.has_key(token):
                    token = longtermtrans[token]
                row_street_long.append(token)

            row_street = ' '.join(row_street_long)
            row_street = row_street.strip()

            row[Utils.street_column] = row_street

            outf.writerow(row)

    out.close()

    return return_manipulatedcsv


