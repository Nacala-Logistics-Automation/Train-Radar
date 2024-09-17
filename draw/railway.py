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
    {"id": "1255", "local": "WCSWHWA", "lat": -0, "lon":0}, # CRUSHER
    {"id": "50755", "local": "WCSW1T", "lat": -14.913004, "lon":40.012391}, # CRUSHER
    #{"id": "1250", "local": "WCS11", "lat": -14.9003683192548, "lon":40.0448164306434}, # CRUSHER

    {"id": "1220", "local": "WNL1P", "lat": -14.9290125444662, "lon":39.9692138858065}, # NAMIALO
    {"id": "1240", "local": "WNL2P", "lat": -0, "lon":0}, # NAMIALO
    {"id": "1245", "local": "WNLWCS", "lat": -0, "lon":0}, # NAMIALO
    {"id": "50730", "local": "WNLW1T", "lat": -0, "lon":0}, # NAMIALO
    {"id": "50740", "local": "WNLW3T", "lat": -0, "lon":0}, # NAMIALO
    {"id": "50750", "local": "WNLW2T", "lat": -0, "lon":0}, # NAMIALO

    {"id": "1200", "local": "WTAP", "lat": -14.957781439806, "lon":39.8230385691887}, # MECONTA NEW
    {"id": "1205", "local": "WTA1", "lat": -0, "lon":0}, # MECONTA NEW
    {"id": "1210", "local": "WTAWNLA", "lat": -0, "lon":0}, # MECONTA NEW
    {"id": "1215", "local": "WTAWNLB", "lat": -0, "lon":0}, # MECONTA NEW
    {"id": "50720", "local": "WTAW1T", "lat": -0, "lon":0}, # MECONTA NEW
    {"id": "50725", "local": "WTAW2T", "lat": -0, "lon":0}, # MECONTA NEW

    {"id": "161", "local": "WTDP", "lat": -14.9771798399609, "lon":39.7566404566802}, # MITANDE
    {"id": "164", "local": "WTDWMSA", "lat": -0, "lon":0}, # MITANDE
    {"id": "166", "local": "WTDWMSB", "lat": -0, "lon":0}, # MITANDE

    {"id": "1180", "local": "WCVP", "lat": -15.0096175260524, "lon":39.6697624058575}, # NACAVALA
    {"id": "1185", "local": "WCV1", "lat": -0, "lon":0}, # NACAVALA
    {"id": "1190", "local": "WCVWTAA", "lat": -0, "lon":0}, # NACAVALA
    {"id": "1195", "local": "WCVWTAB", "lat": -0, "lon":0}, # NACAVALA
    {"id": "50710", "local": "WCVW1T", "lat": -0, "lon":0}, # NACAVALA
    {"id": "50715", "local": "WCVW2T", "lat": -0, "lon":0}, # NACAVALA

    {"id": "1160", "local": "WZAP", "lat": -15.0850858648838, "lon":39.5147159974871}, # MUIZIA
    {"id": "1165", "local": "WZA1", "lat": -0, "lon":0}, # MUIZIA
    {"id": "1170", "local": "WZAWCVA", "lat": -0, "lon":0}, # MUIZIA
    {"id": "1175", "local": "WZAWCVB", "lat": -0, "lon":0}, # MUIZIA
    {"id": "50700", "local": "WZAW1T", "lat": -0, "lon":0}, # MUIZIA
    {"id": "50705", "local": "WZAW2T", "lat": -0, "lon":0}, # MUIZIA

    {"id": "1140", "local": "WANP", "lat": -15.1298273548822, "lon":39.4023754526333}, # ANCHILO
    {"id": "1145", "local": "WAN11", "lat": -0, "lon":0}, # ANCHILO
    {"id": "1150", "local": "WANWZAA", "lat": -0, "lon":0}, # ANCHILO
    {"id": "1155", "local": "WANWZAB", "lat": -0, "lon":0}, # ANCHILO
    {"id": "50690", "local": "WANW1T", "lat": -0, "lon":0}, # ANCHILO
    {"id": "50695", "local": "WANW2T", "lat": -0, "lon":0}, # ANCHILO

    {"id": "1120", "local": "WNWP", "lat": -15.1231019108111, "lon":39.3628636976737}, # NAMPULA NEW
    {"id": "1125", "local": "WNW1", "lat": -0, "lon":0}, # NAMPULA NEW
    {"id": "1130", "local": "WNWWANA", "lat": -0, "lon":0}, # NAMPULA NEW
    {"id": "1135", "local": "WNWWANB", "lat": -0, "lon":0}, # NAMPULA NEW
    {"id": "50680", "local": "WNWW1T", "lat": -0, "lon":0}, # NAMPULA NEW
    {"id": "50685", "local": "WNWW2T", "lat": -0, "lon":0}, # NAMPULA NEW

    {"id": "29", "local": "WPLW4T", "lat": -15.0876989514352, "lon":39.2043342601724}, # NAMPULA
    {"id": "31", "local": "WPL22", "lat": -0, "lon":0}, # NAMPULA
    {"id": "106", "local": "WPL3", "lat": -0, "lon":0}, # NAMPULA
    {"id": "107", "local": "WPLW6T", "lat": -0, "lon":0}, # NAMPULA
    {"id": "1075", "local": "WPL1P", "lat": -0, "lon":0}, # NAMPULA
    {"id": "1080", "local": "WPL11", "lat": -0, "lon":0}, # NAMPULA
    {"id": "1085", "local": "WPL21", "lat": -0, "lon":0}, # NAMPULA
    {"id": "1090", "local": "WPL2P", "lat": -0, "lon":0}, # NAMPULA
    {"id": "1095", "local": "WPL3P", "lat": -0, "lon":0}, # NAMPULA
    {"id": "1105", "local": "WPL12", "lat": -0, "lon":0}, # NAMPULA
    {"id": "1110", "local": "WPLWNWA", "lat": -0, "lon":0}, # NAMPULA
    {"id": "1115", "local": "WPLWNWB", "lat": -0, "lon":0}, # NAMPULA
    {"id": "50655", "local": "WPLW1T", "lat": -0, "lon":0}, # NAMPULA
    {"id": "50660", "local": "WPLW3T", "lat": -0, "lon":0}, # NAMPULA
    {"id": "50675", "local": "WPLW2T", "lat": -0, "lon":0}, # NAMPULA

    {"id": "1035", "local": "WRPP", "lat": -15.0105928697529, "lon":39.1138433741827}, # RAPALE
    {"id": "1040", "local": "WRP1", "lat": -0, "lon":0}, # RAPALE
    {"id": "1060", "local": "WRPWPLA", "lat": -0, "lon":0}, # RAPALE
    {"id": "1065", "local": "WRPWPLB", "lat": -0, "lon":0}, # RAPALE
    {"id": "50635", "local": "WRPW1T", "lat": -0, "lon":0}, # RAPALE
    {"id": "50650", "local": "WRPW2T", "lat": -0, "lon":0}, # RAPALE

    {"id": "1015", "local": "WMUP", "lat": -14.9977552427057, "lon":38.9466585291397}, # MUTIVAZE
    {"id": "1020", "local": "WMU1", "lat": -0, "lon":0}, # MUTIVAZE
    {"id": "1025", "local": "WMUWRPA", "lat": -0, "lon":0}, # MUTIVAZE
    {"id": "1030", "local": "WMUWRPB", "lat": -0, "lon":0}, # MUTIVAZE
    {"id": "50625", "local": "WMUW1T", "lat": -0, "lon":0}, # MUTIVAZE
    {"id": "50630", "local": "WMUW2T", "lat": -0, "lon":0}, # MUTIVAZE

    {"id": "995", "local": "WJAP", "lat": -14.9755831302345, "lon":38.8220174259305}, # CARAMAJA
    {"id": "1000", "local": "WJA1", "lat": -0, "lon":0}, # CARAMAJA
    {"id": "1005", "local": "WJAWMUA", "lat": -0, "lon":0}, # CARAMAJA
    {"id": "1010", "local": "WJAWMUB", "lat": -0, "lon":0}, # CARAMAJA
    {"id": "50615", "local": "WJAW1T", "lat": -0, "lon":0}, # CARAMAJA
    {"id": "50620", "local": "WJAW2T", "lat": -0, "lon":0}, # CARAMAJA

    {"id": "960", "local": "WNI1P", "lat": -14.9467833870871, "lon":38.6658835603247}, # NAMINA
    {"id": "965", "local": "WNI1", "lat": -0, "lon":0}, # NAMINA
    {"id": "970", "local": "WNI2", "lat": -0, "lon":0}, # NAMINA
    {"id": "975", "local": "WNI3P", "lat": -0, "lon":0}, # NAMINA
    {"id": "980", "local": "WNI2P", "lat": -0, "lon":0}, # NAMINA
    {"id": "985", "local": "WNIWJAA", "lat": -0, "lon":0}, # NAMINA
    {"id": "990", "local": "WNIWJAB", "lat": -0, "lon":0}, # NAMINA
    {"id": "50595", "local": "WNIW1T", "lat": -0, "lon":0}, # NAMINA
    {"id": "50600", "local": "WNIW3T", "lat": -0, "lon":0}, # NAMINA
    {"id": "50605", "local": "WNIW4T", "lat": -0, "lon":0}, # NAMINA
    {"id": "50610", "local": "WNIW2T", "lat": -0, "lon":0}, # NAMINA



    {"id": "104", "local": "WMR12", "lat": -15.0024377678818, "lon":38.5104178535439}, # MURRULA
    {"id": "940", "local": "WMRP", "lat": -0, "lon":0}, # MURRULA
    {"id": "945", "local": "WMR11", "lat": -0, "lon":0}, # MURRULA
    {"id": "950", "local": "WMRWNIA", "lat": -0, "lon":0}, # MURRULA
    {"id": "955", "local": "WMRWNIB", "lat": -0, "lon":0}, # MURRULA
    {"id": "50585", "local": "WMRW1T", "lat": -0, "lon":0}, # MURRULA
    {"id": "50590", "local": "WMRW2T", "lat": -0, "lon":0}, # MURRULA

    {"id": "28", "local": "WAA1", "lat": -15.0559849531874, "lon":38.3977227024661}, # CAIAIA NEW
    {"id": "890", "local": "WAAP", "lat": -0, "lon":0}, # CAIAIA NEW
    {"id": "930", "local": "WAAWMRA", "lat": -0, "lon":0}, # CAIAIA NEW
    {"id": "935", "local": "WAAWMRB", "lat": -0, "lon":0}, # CAIAIA NEW
    {"id": "50540", "local": "WAAW1T", "lat": -0, "lon":0}, # CAIAIA NEW
    {"id": "50580", "local": "WAAW2T", "lat": -0, "lon":0}, # CAIAIA NEW

    {"id": "870", "local": "WRBP", "lat": -15.0597302650479, "lon":38.3090102201312}, # RIBAUE
    {"id": "880", "local": "WRBWAAA", "lat": -0, "lon":0}, # RIBAUE
    {"id": "885", "local": "WRBWAAB", "lat": -0, "lon":0}, # RIBAUE
    {"id": "50530", "local": "WRBW1T", "lat": -0, "lon":0}, # RIBAUE
    {"id": "50535", "local": "WRBW2T", "lat": -0, "lon":0}, # RIBAUE

    {"id": "850", "local": "WOTP", "lat": -15.1073462781304, "lon":38.2604825038061}, # OUTEIRO NEW
    {"id": "855", "local": "WOT1", "lat": -0, "lon":0}, # OUTEIRO NEW
    {"id": "860", "local": "WOTWRBA", "lat": -0, "lon":0}, # OUTEIRO NEW
    {"id": "865", "local": "WOTWRBB", "lat": -0, "lon":0}, # OUTEIRO NEW
    {"id": "50520", "local": "WOTW1T", "lat": -0, "lon":0}, # OUTEIRO NEW
    {"id": "50525", "local": "WOTW2T", "lat": -0, "lon":0}, # OUTEIRO NEW

    {"id": "26", "local": "WIW12", "lat": -15.009825348236, "lon":37.9938442650251}, # IAPALA
    {"id": "27", "local": "WIW22", "lat": -0, "lon":0}, # IAPALA
    {"id": "810", "local": "WIW1P", "lat": -0, "lon":0}, # IAPALA
    {"id": "815", "local": "WIW1", "lat": -0, "lon":0}, # IAPALA
    {"id": "820", "local": "WIW3P", "lat": -0, "lon":0}, # IAPALA
    {"id": "825", "local": "WIW2P", "lat": -0, "lon":0}, # IAPALA
    {"id": "840", "local": "WIWWOTA", "lat": -0, "lon":0}, # IAPALA
    {"id": "845", "local": "WIWWOTB", "lat": -0, "lon":0}, # IAPALA
    {"id": "50490", "local": "WIWW1T", "lat": -0, "lon":0}, # IAPALA
    {"id": "50495", "local": "WIWW3T", "lat": -0, "lon":0}, # IAPALA
    {"id": "50500", "local": "WIWW4T", "lat": -0, "lon":0}, # IAPALA
    {"id": "50515", "local": "WIWW2T", "lat": -0, "lon":0}, # IAPALA

    {"id": "790", "local": "WSAP", "lat": -15.0005409449611, "lon":37.9033751224228}, # MUSSA
    {"id": "795", "local": "WSA1", "lat": -0, "lon":0}, # MUSSA
    {"id": "800", "local": "WSAWIWA", "lat": -0, "lon":0}, # MUSSA
    {"id": "805", "local": "WSAWIWB", "lat": -0, "lon":0}, # MUSSA
    {"id": "50480", "local": "WSAW1T", "lat": -0, "lon":0}, # MUSSA
    {"id": "50485", "local": "WSAW2T", "lat": -0, "lon":0}, # MUSSA

    {"id": "43", "local": "WSMP", "lat": -15.0297352538032, "lon":37.8106699723352}, # SERRA DA MESA
    {"id": "44", "local": "WSM1", "lat": -0, "lon":0}, # SERRA DA MESA
    {"id": "45", "local": "WSMWCHA", "lat": -0, "lon":0}, # SERRA DA MESA
    {"id": "46", "local": "WSMWCHB", "lat": -0, "lon":0}, # SERRA DA MESA

    {"id": "770", "local": "WCRP", "lat": -15.0035221947313, "lon":37.7608888815851}, # CAIS DE RIANE
    {"id": "775", "local": "WCR1", "lat": -0, "lon":0}, # CAIS DE RIANE
    {"id": "780", "local": "WCRWSAA", "lat": -0, "lon":0}, # CAIS DE RIANE
    {"id": "785", "local": "WCRWSAB", "lat": -0, "lon":0}, # CAIS DE RIANE
    {"id": "50470", "local": "WCRW1T", "lat": -0, "lon":0}, # CAIS DE RIANE
    {"id": "50475", "local": "WCRW2T", "lat": -0, "lon":0}, # CAIS DE RIANE

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