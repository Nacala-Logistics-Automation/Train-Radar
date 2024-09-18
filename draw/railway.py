import json as js
import time

railway_line = [
    {"id": "", "local": "", "lat": -14.5348503565994, "lon":40.6126569614062}, # PORTO
    {"id": "34", "local": "OFICINAS DE NACALA VELHA", "lat": -14.598072, "lon": 40.596644},
    {"id": "113", "local": "OFICINAS DE NACALA VELHA", "lat": -14.584300, "lon": 40.597099}, # NACALA-A-VELHA
    {"id": "1385", "local": "WBOWPOC", "lat": -14.602534, "lon":40.596527}, # BRANCH OFF
    {"id": "1380", "local": "WBOWPOB", "lat": -14.628983, "lon":40.592565}, # BRANCH OFF
    {"id": "1375", "local": "WBOWPOA", "lat": -14.651975, "lon":40.580821}, # BRANCH OFF
    {"id": "50815", "local": "WBOW2T", "lat": -14.689959, "lon":40.579710}, # BRANCH OFF
    {"id": "1365", "local": "WBOP", "lat": -14.7283733959927, "lon":40.5953025545407}, # BRANCH OFF
    {"id": "50810", "local": "WBOW1T", "lat": -14.735640, "lon":40.600168}, # BRANCH OFF

    #{"id": "1370", "local": "WBO1", "lat": -0, "lon":0}, # BRANCH OFF
    {"id": "32", "local": "WTFWBOB", "lat": -14.743241, "lon":40.605755}, # TAKE OFF
    {"id": "1355", "local": "WTFWBOA", "lat": -14.752210, "lon":40.615176}, # TAKE OFF
    {"id": "50805", "local": "WTFW1T", "lat": -14.761105, "lon":40.606928}, # TAKE OFF
    #{"id": "42", "local": "WTFWSMB", "lat": -0, "lon":0}, # TAKE OFF
    #{"id": "111", "local": "WTFWSMA", "lat": -0, "lon":0}, # TAKE OFF
    
    {"id": "1350", "local": "WLLWTFB", "lat": -14.779676, "lon":40.575618}, # NAMARRAL NEW
    {"id": "1345", "local": "WLLWTFA", "lat": -14.786757, "lon":40.542254}, # NAMARRAL NEW
    {"id": "50800", "local": "WLLW2T", "lat": -14.807125, "lon":40.519002}, # NAMARRAL NEW
    {"id": "1335", "local": "WLLP", "lat": -14.820062, "lon":40.496692}, # NAMARRAL NEW
    {"id": "50795", "local": "WLLW1T", "lat": -14.821249, "lon":40.467362}, # NAMARRAL NEW
    #{"id": "1340", "local": "WLL1", "lat": -0, "lon":0}, # NAMARRAL NEW

    {"id": "1330", "local": "WMOWLLB", "lat": -14.881804, "lon":40.348140}, # MONAPO
    {"id": "1325", "local": "WMOWLLA", "lat": -14.910241, "lon":40.320337}, # MONAPO
    {"id": "50790", "local": "WMOW2T", "lat": -14.912329, "lon":40.276630}, # MONAPO
    {"id": "1310", "local": "WMOP", "lat": -14.91938, "lon":40.259445}, # MONAPO
    {"id": "50780", "local": "WMOW1T", "lat": -14.926709, "lon":40.238899}, # MONAPO
    #{"id": "1305", "local": "WMO1", "lat": -14.9123410109001, "lon":40.2767334573375}, # MONAPO

    {"id": "1300", "local": "WEVWMOB", "lat": -14.926893, "lon":40.227859}, # EVATE
    {"id": "1295", "local": "WEVWMOA", "lat": -14.922464, "lon":40.218113}, # EVATE
    {"id": "50775", "local": "WEVW2T", "lat": -14.918122, "lon":40.212131}, # EVATE
    {"id": "1285", "local": "WEVP", "lat": -14.908721, "lon":40.198255}, # EVATE
    {"id": "50770", "local": "WEVW1T", "lat": -14.899599, "lon":40.184851}, # EVATE
    #{"id": "1290", "local": "WEV1", "lat": -0, "lon":0}, # EVATE

    {"id": "1280", "local": "WHWWEVB", "lat": -14.901851, "lon":40.163922}, # METOCHERIA
    {"id": "1275", "local": "WHWWEVA", "lat": -14.903831, "lon":40.150584}, # METOCHERIA
    {"id": "50765", "local": "WHWW2T", "lat": -14.900340, "lon":40.133956}, # METOCHERIA
    {"id": "1265", "local": "WHWP", "lat": -14.894172, "lon": 40.105124}, # METOCHERIA
    {"id": "50760", "local": "WHWW1T", "lat": -14.897578, "lon": 40.060990}, # METOCHERIA
    #{"id": "1270", "local": "WHW1", "lat": -0, "lon":0}, # METOCHERIA


    {"id": "1260", "local": "WCSWHWB", "lat": -14.899686, "lon":40.048899}, # CRUSHER
    {"id": "1255", "local": "WCSWHWA", "lat": -14.905833, "lon": 40.030385}, # CRUSHER
    {"id": "50755", "local": "WCSW1T", "lat": -14.913004, "lon":40.012391}, # CRUSHER
    #{"id": "1250", "local": "WCS11", "lat": -14.9003683192548, "lon":40.0448164306434}, # CRUSHER

    {"id": "1220", "local": "WNL1P", "lat":-14.9290125444662, "lon":39.9692138858065}, # NAMIALO
    {"id": "1240", "local": "WNL2P", "lat":-14.940658, "lon":39.940430}, # NAMIALO
    {"id": "1245", "local": "WNLWCS", "lat":-14.952681, "lon":39.917835}, # NAMIALO
    {"id": "50730", "local": "WNLW1T", "lat":-14.963050, "lon":39.890642}, # NAMIALO
    {"id": "50740", "local": "WNLW3T", "lat":-14.961607, "lon":39.866187}, # NAMIALO
    {"id": "50750", "local": "WNLW2T", "lat":-14.957839, "lon":39.837558}, # NAMIALO

    {"id": "1200", "local": "WTAP", "lat":-14.959024, "lon":39.814451}, # MECONTA NEW
    {"id": "1205", "local": "WTA1", "lat":-14.955048, "lon":39.801658}, # MECONTA NEW
    {"id": "1210", "local": "WTAWNLA", "lat":-14.968118, "lon":39.785149}, # MECONTA NEW
    {"id": "1215", "local": "WTAWNLB", "lat":-14.975086, "lon":39.764939}, # MECONTA NEW
    # {"id": "50720", "local": "WTAW1T", "lat":-14.982568, "lon":39.745371}, # MECONTA NEW
    # {"id": "50725", "local": "WTAW2T", "lat":-14.983519, "lon": 39.743082}, # MECONTA NEW

    {"id": "161", "local": "WTDP", "lat": -14.9771798399609, "lon":39.7566404566802}, # MITANDE
    {"id": "164", "local": "WTDWMSA", "lat": -14.982568, "lon":39.745371}, # MITANDE
    {"id": "166", "local": "WTDWMSB", "lat":-14.996950, "lon": 39.723037}, # MITANDE

    {"id": "1180", "local": "WCVP", "lat": -15.0096175260524, "lon":39.6697624058575}, # NACAVALA
    {"id": "1185", "local": "WCV1", "lat":-15.017461, "lon": 39.676117}, # NACAVALA
    {"id": "1190", "local": "WCVWTAA", "lat":-15.032277, "lon":39.641838}, # NACAVALA
    {"id": "1195", "local": "WCVWTAB", "lat":-15.051672, "lon":39.619916}, # NACAVALA
    {"id": "50710", "local": "WCVW1T", "lat":-15.067869, "lon":39.592427}, # NACAVALA
    {"id": "50715", "local": "WCVW2T", "lat":-15.081304, "lon":39.551260}, # NACAVALA

    {"id": "1160", "local": "WZAP", "lat": -15.084612, "lon":39.541797}, # MUIZIA
    {"id": "1165", "local": "WZA1", "lat": -15.085974, "lon": 39.529859}, # MUIZIA
    {"id": "1170", "local": "WZAWCVA", "lat": -15.085202, "lon": 39.508670}, # MUIZIA
    {"id": "1175", "local": "WZAWCVB", "lat":-15.089623, "lon": 39.483590}, # MUIZIA
    {"id": "50700", "local": "WZAW1T", "lat": -15.096151, "lon": 39.458665}, # MUIZIA
    {"id": "50705", "local": "WZAW2T", "lat": -15.107326, "lon": 39.433845}, # MUIZIA

    {"id": "1140", "local": "WANP", "lat": -15.110711, "lon": 39.427934}, # ANCHILO
    {"id": "1145", "local": "WAN11", "lat": -15.122366, "lon": 39.409433}, # ANCHILO
    {"id": "1150", "local": "WANWZAA", "lat":-15.135122, "lon": 39.386439}, # ANCHILO
    {"id": "1155", "local": "WANWZAB", "lat":-15.131530, "lon": 39.376912}, # ANCHILO
    {"id": "50690", "local": "WANW1T", "lat":-15.125826, "lon": 39.367342}, # ANCHILO
    {"id": "50695", "local": "WANW2T", "lat": -15.120899, "lon": 39.354009}, # ANCHILO

    {"id": "1120", "local": "WNWP", "lat": -15.119852, "lon": 39.348950}, # NAMPULA NEW
    {"id": "1125", "local": "WNW1", "lat":-15.116709, "lon": 39.326466}, # NAMPULA NEW
    {"id": "1130", "local": "WNWWANA", "lat": -15.113900, "lon": 39.279757}, # NAMPULA NEW
    {"id": "1135", "local": "WNWWANB", "lat": -15.108751, "lon": 39.234463}, # NAMPULA NEW
    {"id": "50680", "local": "WNWW1T", "lat": -15.102791, "lon": 39.218499}, # NAMPULA NEW
    {"id": "50685", "local": "WNWW2T", "lat":-15.090480, "lon": 39.207048}, # NAMPULA NEW

    {"id": "29", "local": "WPLW4T", "lat": -15.0876989514352, "lon":39.2043342601724}, # NAMPULA
    {"id": "31", "local": "WPL22", "lat": -15.07842, "lon": 39.198993}, # NAMPULA
    {"id": "106", "local": "WPL3", "lat": -15.069426, "lon": 39.198754}, # NAMPULA
    {"id": "107", "local": "WPLW6T", "lat":-15.060950, "lon": 39.191958}, # NAMPULA
    {"id": "1075", "local": "WPL1P", "lat": -15.053460, "lon": 39.185046}, # NAMPULA
    {"id": "1080", "local": "WPL11", "lat": -15.047827, "lon":39.178226}, # NAMPULA
    {"id": "1085", "local": "WPL21", "lat": -15.042784, "lon": 39.169718}, # NAMPULA
    {"id": "1090", "local": "WPL2P", "lat": -15.038703, "lon": 39.161941}, # NAMPULA
    {"id": "1095", "local": "WPL3P", "lat":-15.034440, "lon": 39.160029}, # NAMPULA
    {"id": "1105", "local": "WPL12", "lat": -15.030373, "lon": 39.159328}, # NAMPULA
    {"id": "1110", "local": "WPLWNWA", "lat": -15.028687, "lon": 39.155463}, # NAMPULA
    {"id": "1115", "local": "WPLWNWB", "lat": -15.026658, "lon": 39.150658}, # NAMPULA
    {"id": "50655", "local": "WPLW1T", "lat":-15.024751, "lon": 39.146514}, # NAMPULA
    {"id": "50660", "local": "WPLW3T", "lat":-15.022900, "lon": 39.144173}, # NAMPULA
    {"id": "50675", "local": "WPLW2T", "lat":-15.021644, "lon": 39.141267}, # NAMPULA

    {"id": "1035", "local": "WRPP", "lat": -15.021204, "lon": 39.140527}, # RAPALE
    {"id": "1040", "local": "WRP1", "lat": -15.017043, "lon": 39.129877}, # RAPALE
    {"id": "1060", "local": "WRPWPLA", "lat":-15.011123, "lon": 39.112545}, # RAPALE
    {"id": "1065", "local": "WRPWPLB", "lat":-15.009130, "lon": 39.065778}, # RAPALE
    {"id": "50635", "local": "WRPW1T", "lat": -15.008793, "lon": 39.012643}, # RAPALE
    {"id": "50650", "local": "WRPW2T", "lat":-15.0097210, "lon": 38.977686}, # RAPALE

    {"id": "1015", "local": "WMUP", "lat": -15.003294, "lon": 38.965874}, # MUTIVAZE
    {"id": "1020", "local": "WMU1", "lat": -14.999391, "lon": 38.948152}, # MUTIVAZE
    {"id": "1025", "local": "WMUWRPA", "lat": -14.990394, "lon": 38.923422}, # MUTIVAZE
    {"id": "1030", "local": "WMUWRPB", "lat": -14.983679, "lon": 38.896635}, # MUTIVAZE
    {"id": "50625", "local": "WMUW1T", "lat": -14.983948, "lon": 38.873338}, # MUTIVAZE
    {"id": "50630", "local": "WMUW2T", "lat": -14.986143, "lon": 38.845446}, # MUTIVAZE

    {"id": "995", "local": "WJAP", "lat": -14.983846, "lon": 38.839658}, # CARAMAJA
    {"id": "1000", "local": "WJA1", "lat":-14.973665, "lon":38.812536}, # CARAMAJA
    {"id": "1005", "local": "WJAWMUA", "lat":-14.949649, "lon":38.792692}, # CARAMAJA
    {"id": "1010", "local": "WJAWMUB", "lat": -14.919333, "lon":38.764301}, # CARAMAJA
    {"id": "50615", "local": "WJAW1T", "lat":-14.912222, "lon": 38.732897}, # CARAMAJA
    {"id": "50620", "local": "WJAW2T", "lat": -14.938334, "lon":38.698035}, # CARAMAJA

    {"id": "960", "local": "WNI1P", "lat": -14.945777, "lon":38.688893}, # NAMINA
    {"id": "965", "local": "WNI1", "lat": -14.947959, "lon": 38.667157}, # NAMINA
    {"id": "970", "local": "WNI2", "lat": -14.952305, "lon": 38.653748}, # NAMINA
    {"id": "975", "local": "WNI3P", "lat":-14.959243, "lon": 38.644663}, # NAMINA
    {"id": "980", "local": "WNI2P", "lat": -14.963201, "lon": 38.632503}, # NAMINA
    {"id": "985", "local": "WNIWJAA", "lat":-14.961506, "lon" :38.6213910}, # NAMINA
    {"id": "990", "local": "WNIWJAB", "lat": -14.962024, "lon": 38.607296}, # NAMINA
    {"id": "50595", "local": "WNIW1T", "lat": -14.961174, "lon": 38.596417}, # NAMINA
    {"id": "50600", "local": "WNIW3T", "lat":-14.953990, "lon": 38.586503}, # NAMINA
    {"id": "50605", "local": "WNIW4T", "lat":-14.955798, "lon": 38.574671}, # NAMINA
    {"id": "50610", "local": "WNIW2T", "lat":-14.962257, "lon": 38.560987}, # NAMINA



    {"id": "104", "local": "WMR12", "lat": -14.964724, "lon":38.556687}, # MURRULA
    {"id": "940", "local": "WMRP", "lat":-14.975244, "lon":38.539786}, # MURRULA
    {"id": "945", "local": "WMR11", "lat": -14.982838, "lon": 38.519791}, # MURRULA
    {"id": "950", "local": "WMRWNIA", "lat":-14.999491, "lon": 38.511523}, # MURRULA
    {"id": "955", "local": "WMRWNIB", "lat": -15.012176, "lon": 38.500650}, # MURRULA
    {"id": "50585", "local": "WMRW1T", "lat":-15.023724, "lon": 38.482686}, # MURRULA
    {"id": "50590", "local": "WMRW2T", "lat": -15.028872, "lon":38.454107}, # MURRULA

    {"id": "28", "local": "WAA1", "lat":-15.031857, "lon":38.438837}, # CAIAIA NEW
    {"id": "890", "local": "WAAP", "lat": -15.042442, "lon": 38.426794}, # CAIAIA NEW
    {"id": "930", "local": "WAAWMRA", "lat": -15.051980, "lon": 38.420652}, # CAIAIA NEW
    {"id": "935", "local": "WAAWMRB", "lat": -15.059346, "lon": 38.401481}, # CAIAIA NEW
    {"id": "50540", "local": "WAAW1T", "lat":-15.048690, "lon": 38.381675}, # CAIAIA NEW
    {"id": "50580", "local": "WAAW2T", "lat": -15.050296, "lon": 38.353000}, # CAIAIA NEW

    {"id": "870", "local": "WRBP", "lat": -15.046738, "lon":38.333490}, # RIBAUE
    {"id": "880", "local": "WRBWAAA", "lat":-15.065068, "lon":38.302880}, # RIBAUE
    {"id": "885", "local": "WRBWAAB", "lat": -15.085166, "lon": 38.282798}, # RIBAUE
    {"id": "50530", "local": "WRBW1T", "lat":-15.108330, "lon": 38.260037}, # RIBAUE
    {"id": "50535", "local": "WRBW2T", "lat":-15.094550, "lon": 38.215674}, # RIBAUE

    {"id": "850", "local": "WOTP", "lat":-15.088919, "lon": 38.204200}, # OUTEIRO NEW
    {"id": "855", "local": "WOT1", "lat":-15.067617, "lon": 38.168459}, # OUTEIRO NEW
    {"id": "860", "local": "WOTWRBA", "lat":-15.074642, "lon": 38.179349}, # OUTEIRO NEW
    {"id": "865", "local": "WOTWRBB", "lat":-15.041731, "lon": 38.134134}, # OUTEIRO NEW
    {"id": "50520", "local": "WOTW1T", "lat":-15.038682, "lon": 38.092628}, # OUTEIRO NEW
    {"id": "50525", "local": "WOTW2T", "lat":-15.026220, "lon": 38.052899}, # OUTEIRO NEW

    {"id": "26", "local": "WIW12", "lat":-15.026647, "lon": 38.042310}, # IAPALA
    {"id": "27", "local": "WIW22", "lat":-15.026637, "lon": 38.034055}, # IAPALA
    {"id": "810", "local": "WIW1P", "lat":-15.024254, "lon": 38.028725}, # IAPALA
    {"id": "815", "local": "WIW1", "lat":-15.015633, "lon": 38.018048}, # IAPALA
    {"id": "820", "local": "WIW3P", "lat": -15.013226, "lon": 38.008023}, # IAPALA
    {"id": "825", "local": "WIW2P", "lat": -15.010243, "lon": 37.978078}, # IAPALA
    {"id": "840", "local": "WIWWOTA", "lat":-15.005364, "lon": 37.956469}, # IAPALA
    {"id": "845", "local": "WIWWOTB", "lat":-15.007066, "lon":  37.933723}, # IAPALA
    {"id": "50490", "local": "WIWW1T", "lat":-15.004226, "lon":37.913619}, # IAPALA
    {"id": "50495", "local": "WIWW3T", "lat":-15.002528, "lon": 37.896516}, # IAPALA
    {"id": "50500", "local": "WIWW4T", "lat": -15.005836, "lon": 37.882399}, # IAPALA
    {"id": "50515", "local": "WIWW2T", "lat":-15.012113, "lon": 37.866305}, # IAPALA

    {"id": "790", "local": "WSAP", "lat":-15.011025, "lon": 37.862662}, # MUSSA
    {"id": "795", "local": "WSA1", "lat":-15.016738, "lon": 37.853384}, # MUSSA
    {"id": "800", "local": "WSAWIWA", "lat":-15.021720, "lon": 37.848542}, # MUSSA
    {"id": "805", "local": "WSAWIWB", "lat":-15.027824, "lon": 37.842491}, # MUSSA
    {"id": "50480", "local": "WSAW1T", "lat":-15.028871, "lon": 37.827755}, # MUSSA
    {"id": "50485", "local": "WSAW2T", "lat":-15.030834, "lon": 37.814389}, # MUSSA

    {"id": "43", "local": "WSMP", "lat": -15.0297352538032, "lon":37.8106699723352}, # SERRA DA MESA
    {"id": "44", "local": "WSM1", "lat":-15.015420, "lon":37.790182}, # SERRA DA MESA
    {"id": "45", "local": "WSMWCHA", "lat":-15.002154, "lon": 37.758267}, # SERRA DA MESA
    {"id": "46", "local": "WSMWCHB", "lat":-14.987306, "lon": 37.723623}, # SERRA DA MESA

    {"id": "770", "local": "WCRP", "lat":-14.985593, "lon":  37.719417}, # CAIS DE RIANE
    {"id": "775", "local": "WCR1", "lat":-14.983163 , "lon": 37.707915}, # CAIS DE RIANE
    {"id": "780", "local": "WCRWSAA", "lat":-14.981199, "lon": 37.693791}, # CAIS DE RIANE
    {"id": "785", "local": "WCRWSAB", "lat":-14.968789, "lon": 37.679422}, # CAIS DE RIANE
    {"id": "50470", "local": "WCRW1T", "lat":-14.961639, "lon": 37.673120}, # CAIS DE RIANE
    {"id": "50475", "local": "WCRW2T", "lat":-14.945302, "lon": 37.655560}, # CAIS DE RIANE

    {"id": "19", "local": "WNCW3T", "lat": -14.9188676485196, "lon":37.6344490494706}, # NAMECUNA
    {"id": "21", "local": "WNC2P", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "22", "local": "WNCW4T", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "23", "local": "WNC22", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "24", "local": "WNC1", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "102", "local": "WNC3", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "103", "local": "WNCW5T", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "755", "local": "WNC1P", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "760", "local": "WNC12", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "765", "local": "WNCWCR", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "50460", "local": "WNCW1T", "lat": -0, "lon":0}, # NAMECUNA
    {"id": "50465", "local": "WNCW2T", "lat": -0, "lon":0}, # NAMECUNA
    
    {"id": "735", "local": "WEAP", "lat": -14.931261043373, "lon":37.5362635794731}, # NATALEIA
    {"id": "740", "local": "WEA1", "lat": -0, "lon":0}, # NATALEIA
    {"id": "745", "local": "WEAWNCA", "lat": -0, "lon":0}, # NATALEIA
    {"id": "750", "local": "WEAWNCB", "lat": -0, "lon":0}, # NATALEIA
    {"id": "50450", "local": "WEAW1T", "lat": -0, "lon":0}, # NATALEIA
    {"id": "50455", "local": "WEAW2T", "lat": -0, "lon":0}, # NATALEIA

    {"id": "715", "local": "WMWP", "lat": -14.9289178432668, "lon":37.4544751646126}, # MALEMA NEW
    {"id": "720", "local": "WMW1", "lat": -0, "lon":0}, # MALEMA NEW
    {"id": "725", "local": "WMWWEAA", "lat": -0, "lon":0}, # MALEMA NEW
    {"id": "730", "local": "WMWWEAB", "lat": -0, "lon":0}, # MALEMA NEW
    {"id": "50440", "local": "WMWW1T", "lat": -0, "lon":0}, # MALEMA NEW
    {"id": "50445", "local": "WMWW2T", "lat": -0, "lon":0}, # MALEMA NEW

    {"id": "41", "local": "WMM1", "lat": -14.946474319992, "lon":37.415591062648}, # MALEMA
    {"id": "680", "local": "WMMP", "lat": -0, "lon":0}, # MALEMA
    {"id": "710", "local": "WMMWMW", "lat": -0, "lon":0}, # MALEMA
    {"id": "50415", "local": "WMMW1T", "lat": -0, "lon":0}, # MALEMA
    {"id": "50420", "local": "WMMW2T", "lat": -0, "lon":0}, # MALEMA

    {"id": "660", "local": "WTUP", "lat": -14.9298662431994, "lon":37.2499006363285}, # TUI


    {"id": "13", "local": "WMTW3T", "lat": -14.8346879656397, "lon":37.0075678611033}, # MUTUALI
    {"id": "50380", "local": "WLUP", "lat": -14.7952666818142, "lon":36.8545000405412}, # LURIO NEW
    {"id": "37", "local": "MURISSA", "lat": -14.7860372282036, "lon":36.6979903657642}, # MURISSA
    {"id": "97", "local": "WCB22", "lat": -14.8043375120626, "lon":36.5296808606601}, # CUAMBA
    {"id": "36", "local": "WCBW2T", "lat": -14.8066639273132, "lon":36.5245002199562}, # CUAMBA
    {"id": "92", "local": "WCWW3T", "lat": -14.958864746194, "lon":36.2595929617856}, # CUAMBA NEW
    {"id": "470", "local": "WCAP", "lat": -14.9968642008328, "lon":36.1488691784477}, # CARONGA
    {"id": "450", "local": "TO-BUE", "lat": -15.0222812429901, "lon":36.0775125243594}, # TO-BUE
    {"id": "11", "local": "WEL22", "lat": -14.9819778844452, "lon":35.8786666806612}, # ENTRE LAGOS
    {"id": "9", "local": "XNYWELB", "lat": -14.9727343627882, "lon":35.8589443221309}, # NAYUCI
    {"id": "365", "local": "XNJP", "lat": -14.9696775724661, "lon":35.6650559669449}, # NAMANJA
    {"id": "8", "local": "LAMBULILA", "lat": -15.0006109953298, "lon":35.5100726166156}, # LAMBULILA
    {"id": "315", "local": "XMWP", "lat": -15.049790361392, "lon":35.3940609209406}, # MOLIPA
    {"id": "78", "local": "XLW24", "lat": -15.0708537718331, "lon":35.1930967255084}, # LIWONDE
    {"id": "240", "local": "XNWP", "lat": -15.1050965420217, "lon":35.0687993216519}, # NKAYA NEW
    {"id": "235", "local": "XNTXNW", "lat": -15.1288377298938, "lon":35.0268297277536}, # NKAYA JUNCTION
    {"id": "50120", "local": "LOOP 6 CL", "lat": -15.2619974181341, "lon":34.9290582805273}, # LOOP 6 CL
    {"id": "4", "local": "FACILITIES ZALEWA", "lat": -15.411509910165, "lon":34.8243404319391}, # FACILITIES ZALEWA
    {"id": "50110", "local": "LOOP 5 CL", "lat": -15.4227564469314, "lon":34.8089932888488}, # LOOP 5 CL
    {"id": "160", "local": "LOOP 4 CL", "lat": -15.5629497804683, "lon":34.6678802631617}, # LOOP 4 CL
    {"id": "3", "local": "LOOP 3 CL", "lat": -15.7698454818077, "lon":34.4916313220434}, # LOOP 3 CL
    {"id": "75", "local": "LOOP 2 CL", "lat": -15.8197868392766, "lon":34.2810857141549}, # LOOP 2 CL
    {"id": "1", "local": "LOOP 1 CL", "lat": -15.9783404816619, "lon":33.9974187369633}, # LOOP 1 CL
    {"id": "5", "local": "RMVWL1A", "lat": -16.1633212771317, "lon":33.795387671617}, # MOATIZE TERMINAL
    {"id": "9", "local": "", "lat": -16.1633783146919, "lon":33.7954033704417} # MINA
]