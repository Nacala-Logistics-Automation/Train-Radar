import json as js
import time

railway_line = [
    {"id": "", "local": "", "lat": -14.5348503565994, "lon":40.6126569614062}, # PORTO
   
    {"id": "34", "local": "WPOP", "lat": -14.598072, "lon": 40.596644},#OFICINA NACALA-A-VELHA
    {"id": "113", "local": "WPOWVT", "lat": -14.584300, "lon": 40.597099}, #OFICINA  NACALA-A-VELHA
   
   
    {"id": "1385", "local": "WBOWPOC", "lat": -14.602534, "lon":40.596527}, # BRANCH OFF
    {"id": "1380", "local": "WBOWPOB", "lat": -14.628983, "lon":40.592565}, # BRANCH OFF
    {"id": "1375", "local": "WBOWPOA", "lat": -14.651975, "lon":40.580821}, # BRANCH OFF
    {"id": "50815", "local": "WBOW2T", "lat": -14.689959, "lon":40.579710}, # BRANCH OFF
    {"id": "1370", "local": "WBO1", "lat":-14.705333, "lon": 40.581142}, 
    {"id": "1365", "local": "WBOP", "lat":-14.719254, "lon": 40.587033}, # BRANCH OFF
    {"id": "50810", "local": "WBOW1T", "lat":-14.728555, "lon": 40.594921}, # BRANCH OFF

    {"id": "42", "local": "WTFWSMB", "lat":-14.737009, "lon": 40.600293}, 
    {"id": "111", "local": "WTFWSMA", "lat":-14.759589, "lon": 40.608622}, 
    {"id": "32", "local": "WTFWBOB", "lat":-14.783273, "lon":  40.567133}, # TAKE OFF
    {"id": "1355", "local": "WTFWBOA", "lat":-14.796407, "lon": 40.526703}, # TAKE OFF
    {"id": "50805", "local": "WTFW1T", "lat":-14.823338, "lon":  40.486595}, # TAKE OFF
    
        
    {"id": "1350", "local": "WLLWTFB", "lat":-14.823300, "lon": 40.465406}, # NAMARRAL NEW
    {"id": "1345", "local": "WLLWTFA", "lat":-14.815968, "lon": 40.423610}, # NAMARRAL NEW
    {"id": "50800", "local": "WLLW2T", "lat":-14.829025, "lon": 40.389735}, # NAMARRAL NEW
    {"id": "1335", "local": "WLLP", "lat": -14.861915, "lon": 40.376073}, # NAMARRAL NEW
    {"id": "1340", "local": "WLL1", "lat": -14.876278, "lon": 40.353737}, 
    {"id": "50795", "local": "WLLW1T", "lat":-14.902668, "lon": 40.328333}, # NAMARRAL NEW
    

    {"id": "1330", "local": "WMOWLLB", "lat":-14.911549, "lon": 40.320536}, # MONAPO
    {"id": "1325", "local": "WMOWLLA", "lat":-14.902101, "lon": 40.302867}, # MONAPO
    {"id": "50790", "local": "WMOW2T", "lat": -14.904372, "lon": 40.282122}, # MONAPO
    {"id": "1305", "local": "WMO1", "lat":-14.919348, "lon": 40.268614},
    {"id": "1310", "local": "WMOP", "lat":-14.925137, "lon": 40.251891}, # MONAPO
    {"id": "50780", "local": "WMOW1T", "lat":-14.927871, "lon": 40.221920}, # MONAPO
    

    {"id": "1300", "local": "WEVWMOB", "lat":-14.919887, "lon": 40.211826}, # EVATE
    {"id": "1295", "local": "WEVWMOA", "lat":-14.907557, "lon": 40.195149}, # EVATE
    {"id": "50775", "local": "WEVW2T", "lat":-14.902410, "lon": 40.166526}, # EVATE
    {"id": "1290", "local": "WEV1", "lat":-14.904228, "lon": 40.142932}, 
    {"id": "1285", "local": "WEVP", "lat":-14.900333, "lon": 40.1292845}, # EVATE
    {"id": "50770", "local": "WEVW1T", "lat":-14.897976, "lon":40.113888}, # EVATE
    

    {"id": "1280", "local": "WHWWEVB", "lat":-14.894702, "lon": 40.104425}, # METOCHERIA
    {"id": "1275", "local": "WHWWEVA", "lat":-14.893598, "lon": 40.096415}, # METOCHERIA
    {"id": "50765", "local": "WHWW2T", "lat":-14.893538, "lon": 40.085811}, # METOCHERIA
    {"id": "1270", "local": "WHW1", "lat":-14.895680, "lon": 40.075678},
    {"id": "1265", "local": "WHWP", "lat":-14.897978, "lon": 40.063808}, # METOCHERIA
    {"id": "50760", "local": "WHWW1T", "lat":-14.899312, "lon": 40.054209}, # METOCHERIA

    {"id": "1260", "local": "WCSWHWB", "lat":-14.905501, "lon": 40.032693}, # CRUSHER
    {"id": "1255", "local": "WCSWHWA", "lat": -14.905833, "lon": 40.030385}, # CRUSHER
    {"id": "50755", "local": "WCSW1T", "lat":-14.912099, "lon": 40.014925}, # CRUSHER
    {"id": "1250", "local": "WCS11", "lat":-14.918930, "lon": 39.997314},

    {"id": "1245", "local": "WNLWCS", "lat":-14.921428, "lon": 39.990428}, # NAMIALO
    {"id": "50750", "local": "WNLW2T", "lat":-14.933202, "lon": 39.959031}, # NAMIALO
    {"id": "1235", "local": "WNL21", "lat":-14.942414, "lon": 39.937494},
    {"id": "1240", "local": "WNL2P", "lat":-14.950936, "lon": 39.920876}, # NAMIALO
    {"id": "1225", "local": "WNL12", "lat":-14.956925, "lon": 39.905872},
    {"id": "50740", "local": "WNLW3T", "lat":-14.962923, "lon": 39.890053}, # NAMIALO
    {"id": "1220", "local": "WNL1P", "lat":-14.961559, "lon": 39.867569}, # NAMIALO
    {"id": "1230", "local": "WNL11", "lat":-14.957335, "lon": 39.848559},
    {"id": "50730", "local": "WNLW1T", "lat":-14.958088, "lon": 39.825026}, # NAMIALO

    {"id": "1215", "local": "WTAWNLB", "lat":-14.959097, "lon":39.814645}, # MECONTA NEW
    {"id": "1210", "local": "WTAWNLA", "lat":-14.955368, "lon": 39.800790}, # MECONTA NEW
    {"id": "50725", "local": "WTAW2T", "lat":-14.964405, "lon": 39.788821}, # MECONTA NEW
    {"id": "1200", "local": "WTAP", "lat":-14.977868, "lon": 39.756319},
    {"id": "1205", "local": "WTA1", "lat":-14.989147, "lon": 39.734369}, # MECONTA NEW
    {"id": "50720", "local": "WTAW1T", "lat":-15.006352, "lon": 39.700375}, # MECONTA NEW
   
#    #MITANDE NAO APARECE NO MAPEAMENTO DE POSICOES 
#     {"id": "166", "local": "WTDWMSB", "lat": -0, "lon": 0}, # MITANDE 
#     {"id": "164", "local": "WTDWMSA", "lat": -0, "lon": 0}, # MITANDE
#     {"id": "163", "local": "WTDW2T", "lat":-0, "lon": 0}, # MITANDE
#     {"id": "162", "local": "WTDW4T", "lat": 0, "lon":0},
#     {"id": "66", "local": "WTDW6T", "lat": 0, "lon":0},
#     {"id": "61", "local": "WTD23", "lat": 0, "lon":0},
#     {"id": "68", "local": "WTD2", "lat": 0, "lon":0},
#     {"id": "161", "local": "WTDP", "lat": 0, "lon":0},
#     {"id": "64", "local": "WTD13", "lat": 0, "lon":0},
#     {"id": "67", "local": "WTD1", "lat": 0, "lon":0},
#     {"id": "159", "local": "WTDW3T", "lat": 0, "lon":0},
#     {"id": "158", "local": "WTDW1T", "lat": 0, "lon":0},

    {"id": "1195", "local": "WCVWTAB", "lat":-15.009575, "lon": 39.676741}, # NACAVALA
    {"id": "1190", "local": "WCVWTAA", "lat":-15.021683, "lon": 39.651955}, # NACAVALA
    {"id": "50715", "local": "WCVW2T", "lat":-15.040424, "lon": 39.633922}, # NACAVALA
    {"id": "1180", "local": "WCVP", "lat":-15.053788, "lon": 39.611515},
    {"id": "1185", "local": "WCV1", "lat":-15.066771, "lon": 39.588121}, # NACAVALA
    {"id": "50710", "local": "WCVW1T", "lat":-15.076335, "lon": 39.553658}, # NACAVALA
    

    {"id": "1175", "local": "WZAWCVB", "lat":-15.086103, "lon": 39.540282}, # MUIZIA
    {"id": "1170", "local": "WZAWCVA", "lat": -15.087284, "lon": 39.519191}, # MUIZIA
    {"id": "50705", "local": "WZAW2T", "lat": -15.086029, "lon": 39.499603}, # MUIZIA
    {"id": "1160", "local": "WZAP", "lat":-15.091148, "lon": 39.478117}, # MUIZIA
    {"id": "1165", "local": "WZA1", "lat":-15.098190, "lon": 39.455424},
    {"id": "50700", "local": "WZAW1T", "lat": -15.105781, "lon": 39.437574}, # MUIZIA
   

    {"id": "1155", "local": "WANWZAB", "lat": -15.112127, "lon": 39.427386}, # ANCHILO
    {"id": "1150", "local": "WANWZAA", "lat": -15.122366, "lon": 39.409433}, # ANCHILO
    {"id": "50695", "local": "WANW2T", "lat":-15.132475, "lon": 39.399341}, # ANCHILO
    {"id": "108", "local": "WAN12", "lat":-15.135484, "lon": 39.390143},
    {"id": "1140", "local": "WANP", "lat":-15.131765, "lon": 39.376164}, # ANCHILO
    {"id": "1145", "local": "WAN11", "lat":-15.125826, "lon": 39.367342},
    {"id": "50690", "local": "WANW1T", "lat":-15.121839, "lon": 39.357439}, # ANCHILO
    

    {"id": "1135", "local": "WNWWANB", "lat": -15.119852, "lon": 39.348950}, # NAMPULA NEW
    {"id": "1130", "local": "WNWWANA", "lat":-15.116709, "lon": 39.326466}, # NAMPULA NEW
    {"id": "50685", "local": "WNWW2T", "lat": -15.113900, "lon": 39.279757}, # NAMPULA NEW
    {"id": "1120", "local": "WNWWP", "lat": -15.112298, "lon": 39.255456}, # NAMPULA NEW
    {"id": "1125", "local": "WNWW1", "lat":-15.108271, "lon": 39.230579},
    {"id": "50680", "local": "WNWW1T", "lat": -15.092662, "lon": 39.209458}, # NAMPULA NEW
    
#FAZER TODOS 
    {"id": "1115", "local": "WPLWNWB", "lat":-15.087699, "lon": 39.204334}, # NAMPULA
    {"id": "1110", "local": "WPLWNWA", "lat":-15.083239, "lon": 39.199004}, # NAMPULA
    {"id": "50675", "local": "WPLW2T", "lat": -15.077398, "lon": 39.199268}, # NAMPULA
    {"id": "1085", "local": "WPL21", "lat":-15.074010, "lon": 39.199789},
    {"id": "1095", "local": "WPL3P", "lat":-15.070281, "lon": 39.199461}, # NAMPULA
    {"id": "29", "local": "WPLW4T", "lat":-15.063249, "lon": 39.194128}, # NAMPULA
    {"id": "107", "local": "WPLW6T", "lat":-15.058298, "lon":  39.189376},
    {"id": "106", "local": "WPL3", "lat":-15.053647, "lon": 39.185976},
    {"id": "31", "local": "WPL22", "lat":-15.050096, "lon":  39.181019},
    {"id": "1090", "local": "WPL2P", "lat":-15.046442, "lon": 39.176790},
    {"id": "1105", "local": "WPL12", "lat":-15.043575, "lon": 39.171573}, # NAMPULA
    {"id": "50660", "local": "WPLW3T", "lat":-15.041898, "lon": 39.166977}, # NAMPULA
    {"id": "1075", "local": "WPL1P", "lat":-15.035093, "lon": 39.160315}, # NAMPULA
    {"id": "1080", "local": "WPL11", "lat":-15.028865, "lon":  39.156860}, # NAMPULA
    {"id": "50655", "local": "WPLW1T", "lat":-15.025083, "lon": 39.148756},
    
    {"id": "1065", "local": "WRPWPLB", "lat":-15.021567, "lon": 39.140268}, # RAPALE
    {"id": "1060", "local": "WRPWPLA", "lat":-15.011171, "lon": 39.109210}, # RAPALE
    {"id": "50650", "local": "WRPW2T", "lat":-15.009504, "lon": 39.065693}, # RAPALE
    {"id": "1035", "local": "WRPP", "lat":-15.008377, "lon": 39.018674}, # RAPALE
    {"id": "1040", "local": "WRP1", "lat":-15.021676, "lon": 38.996864}, 
    {"id": "50635", "local": "WRPW1T", "lat": -15.007657, "lon":  38.975248}, # RAPALE
    

    {"id": "1030", "local": "WMUWRPB", "lat":-15.003750, "lon": 38.964972}, # MUTIVAZE
    {"id": "1025", "local": "WMUWRPA", "lat":-15.000498, "lon": 38.949823}, # MUTIVAZE
    {"id": "50630", "local": "WMUW2T", "lat":-14.999426, "lon": 38.936191}, # MUTIVAZE
    {"id": "1015", "local": "WMUP", "lat":-14.990402, "lon": 38.925480}, # MUTIVAZE
    {"id": "1020", "local": "WMU1", "lat": -14.983030, "lon": 38.897531},
    {"id": "50625", "local": "WMUW1T", "lat": -14.982718, "lon": 38.866841}, # MUTIVAZE
  

    {"id": "1010", "local": "WJAWMUB", "lat":-14.984595, "lon": 38.839560}, # CARAMAJA
    {"id": "1005", "local": "WJAWMUA", "lat":-14.973714, "lon": 38.812537}, # CARAMAJA
    {"id": "50620", "local": "WJAW2T", "lat":-14.954688, "lon": 38.793977}, # CARAMAJA
    {"id": "995", "local": "WJAP", "lat":-14.936739, "lon": 38.787540}, # CARAMAJA
     {"id": "1000", "local": "WJA1", "lat":-14.916525, "lon": 38.759340},
    {"id": "50615", "local": "WJAW1T", "lat":-14.926910, "lon": 38.711207}, # CARAMAJA

    {"id": "990", "local": "WNIWJAB", "lat": -14.945777, "lon":38.688893}, # NAMINA
    {"id": "985", "local": "WNIWJAA", "lat": -14.947959, "lon": 38.667157}, # NAMINA
    {"id": "50610", "local": "WNIW2T", "lat": -14.952305, "lon": 38.653748}, # NAMINA
    {"id": "975", "local": "WNI3P", "lat":-14.959243, "lon": 38.644663}, # NAMINA
    {"id": "50605", "local": "WNIW4T", "lat": -14.963201, "lon": 38.632503}, # NAMINA
    {"id": "965", "local": "WNI1", "lat":-14.963195, "lon": 38.625027},
    {"id": "980", "local": "WNI2P", "lat":-14.961506, "lon" :38.6213910}, # NAMINA
    {"id": "50600", "local": "WNIW3T", "lat": -14.962024, "lon":38.607296}, # NAMINA
    {"id": "970", "local": "WNI2", "lat":-14.954845, "lon": 38.584570},
    {"id": "960", "local": "WNI1P", "lat": -14.956463, "lon": 38.572177}, # NAMINA
    {"id": "50595", "local": "WNIW1T", "lat":-14.961450, "lon":38.561302}, # NAMINA
   

    {"id": "955", "local": "WMRWNIB", "lat": -14.964724, "lon":38.556687}, # MURRULA
    {"id": "950", "local": "WMRWNIA", "lat":-14.973216, "lon": 38.544843},
    {"id": "50590", "local": "WMRW2T", "lat":-14.983708, "lon": 38.518605}, # MURRULA
    {"id": "104", "local": "WMR12", "lat":-15.004252, "lon": 38.507833}, # MURRULA
    {"id": "940", "local": "WMRWP", "lat":-15.015690, "lon": 38.497786},
    {"id": "945", "local": "WMR11", "lat":-15.025359, "lon": 38.474894}, # MURRULA
    {"id": "50585", "local": "WMRW1T", "lat":-15.031291, "lon":38.449170}, # MURRULA
 

    {"id": "935", "local": "WAAWMRB", "lat":-15.032074, "lon": 38.439128}, # CAIAIA NEW
    {"id": "930", "local": "WAAWMRA", "lat":-15.051135, "lon": 38.421443}, # CAIAIA NEW
    {"id": "50580", "local": "WAAW2T", "lat":-15.053354, "lon": 38.389574}, # CAIAIA NEW
    {"id": "50540", "local": "WAAW1T", "lat":-15.047114, "lon": 38.344920},
    

    {"id": "885", "local": "WRBWAAB", "lat":-15.046743, "lon":38.332907}, # RIBAUE
    {"id": "880", "local": "WRBWAAA", "lat":-15.065068, "lon":38.302880}, # RIBAUE
    {"id": "50535", "local": "WRBW2T", "lat": -15.085166, "lon": 38.282798}, # RIBAUE
    {"id": "875", "local": "WRBP", "lat":-15.106621,"lon": 38.263739}, # RIBAUE
    {"id": "870", "local": "WRB1", "lat":-15.107467, "lon": 38.236569},
    {"id": "50530", "local": "WRBW1T", "lat":-15.092623, "lon": 38.210069}, # RIBAUE

    {"id": "865", "local": "WOTWRBB", "lat":-15.089926, "lon":38.203325}, # OUTEIRO NEW
    {"id": "860", "local": "WOTWRBA", "lat":-15.067617, "lon": 38.168459}, # OUTEIRO NEW
    {"id": "50525", "local": "WOTW2T", "lat":-15.045977, "lon": 38.142536}, # OUTEIRO NEW
    {"id": "850", "local": "WOTP", "lat":-15.042387, "lon":38.107916}, # OUTEIRO NEW
    {"id": "855", "local": "WOT1", "lat":-15.032071, "lon": 38.082711},
    {"id": "50520", "local": "WOTW1T", "lat":-15.025816, "lon": 38.049586}, # OUTEIRO NEW
   

    {"id": "845", "local": "WIWWOTB", "lat":-15.026540, "lon": 38.042350}, # IAPALA
    {"id": "840", "local": "WIWWOTA", "lat":-15.026637, "lon": 38.034055}, # IAPALA
    {"id": "50515", "local": "WIWW2T", "lat":-15.021227, "lon": 38.025440}, # IAPALA
    {"id": "820", "local": "WIW3P", "lat":-15.015633, "lon": 38.018048}, # IAPALA
    {"id": "50500", "local": "WIWW4T", "lat": -15.013226, "lon": 38.008023}, # IAPALA
    {"id": "27", "local": "WIW22", "lat":-15.011073, "lon": 37.999110},
    {"id": "815", "local": "WIW1", "lat":-15.010543, "lon": 37.988943},
    {"id": "825", "local": "WIW2P", "lat": -15.010243, "lon": 37.978078}, # IAPALA
    {"id": "50495", "local": "WIWW3T", "lat":-15.005364, "lon": 37.956469}, # IAPALA
    {"id": "810", "local": "WIW1P", "lat":-15.007066, "lon":  37.933723}, # IAPALA
    {"id": "26", "local": "WIW12", "lat":-15.001337, "lon": 37.906800},
    {"id": "50490", "local": "WIWW1T", "lat":-15.009506, "lon": 37.875228}, # IAPALA

    {"id": "805", "local": "WSAWIWA", "lat":-15.011558, "lon": 37.862254}, # MUSSA
    {"id": "800", "local": "WSAWIWB", "lat":-15.029517, "lon": 37.839894}, # MUSSA
    {"id": "50485", "local": "WSAW2T", "lat":-15.030667, "lon": 37.811895}, # MUSSA
    {"id": "790", "local": "WSAP", "lat":-15.013947, "lon": 37.786015},
    {"id": "795", "local": "WSA1", "lat":-15.001536, "lon": 37.757240}, # MUSSA
    {"id": "50480", "local": "WSAW1T", "lat":-14.986941, "lon": 37.725447}, # MUSSA


    # {"id": "46", "local": "WSMWCHB", "lat": -15.0297352538032, "lon":37.8106699723352}, # SERRA DA MESA
    # {"id": "45", "local": "WSMWCHA", "lat":-0, "lon": 0},
    # {"id": "54", "local": "WSMW2T", "lat":-0, "lon": 0},
    # {"id": "43", "local": "WSMP", "lat":-0, "lon": 0},
    # {"id": "44", "local": "WSM1", "lat":-0, "lon": 0},
    # {"id": "53", "local": "WSMW1T", "lat":-0, "lon": 0},
    

    {"id": "785", "local": "WCRWSAB", "lat":-14.985593, "lon": 37.719417}, # CAIS DE RIANE
    {"id": "780", "local": "WCRWSAA", "lat":-14.983163 , "lon": 37.707915}, # CAIS DE RIANE
    {"id": "50475", "local": "WCRW2T", "lat":-14.981452, "lon": 37.693090}, # CAIS DE RIANE
    {"id": "775", "local": "WCR1", "lat":-14.970097, "lon": 37.679870},
    {"id": "770", "local": "WCRP", "lat":-14.959101, "lon": 37.670151}, # CAIS DE RIANE
    {"id": "50470", "local": "WCRW1T", "lat":-14.945707, "lon":37.655661}, # CAIS DE RIANE
  

    {"id": "765", "local": "WNCWCR", "lat":-14.942826, "lon":37.652992}, # NAMECUNA
    {"id": "50465", "local": "WNCW2T", "lat": -14.938008, "lon":37.649347}, # NAMECUNA
    {"id": "21", "local": "WNCW2P", "lat":-14.933604, "lon":37.646160}, # NAMECUNA
    {"id": "22", "local": "WNCW4T", "lat":-14.922981, "lon":37.636984}, # NAMECUNA
    {"id": "23", "local": "WNC22", "lat":-14.914551, "lon": 37.629333},
    {"id": "760", "local": "WNC12", "lat":-14.910137, "lon": 37.618373},
    {"id": "102", "local": "WNC3", "lat":-14.912891, "lon": 37.607099},
    {"id": "755", "local": "WNC1P", "lat":-14.913811, "lon": 37.595449}, # NAMECUNA
    {"id": "103", "local": "WNCWST", "lat":-14.917304, "lon": 37.584669},
    {"id": "24", "local": "WNC1", "lat":-14.919687, "lon": 37.573279},
    {"id": "19", "local": "WNCW3T", "lat":-14.922340, "lon": 37.558498}, # NAMECUNA
    {"id": "50460", "local": "WNCW1T", "lat":-14.926220, "lon": 37.545024}, # NAMECUNA

    

    {"id": "750", "local": "WEAWNCB", "lat":-14.927900, "lon": 37.542133}, # NATALEIA
    {"id": "745", "local": "WEAWNCA", "lat":-14.939862, "lon": 37.521878}, # NATALEIA
    {"id": "50455", "local": "WEAW2T", "lat":-14.929506, "lon":37.503063}, # NATALEIA
    {"id": "735", "local": "WEAP", "lat":-14.922211, "lon":37.481130}, # NATALEIA
    {"id": "740", "local": "WEA1", "lat":-14.929211, "lon":37.463783},
    {"id": "50450", "local": "WEAW1T", "lat":-14.931657, "lon": 37.442887}, # NATALEIA
   

    {"id": "730", "local": "WMWWEAB", "lat":-14.935066, "lon":37.437163}, # MALEMA NEW
    {"id": "725", "local": "WMWWEAA", "lat":-14.938596, "lon":37.432349}, # MALEMA NEW
    {"id": "50445", "local": "WMWW2T", "lat":-14.944189, "lon": 37.428492}, # MALEMA NEW
    {"id": "715", "local": "WMWP", "lat":-14.948911, "lon": 37.424342},
    {"id": "720", "local": "WMW1", "lat":-14.952629, "lon": 37.420361}, 
    {"id": "50440", "local": "WMWW1T", "lat":-14.948280, "lon": 37.415093}, # MALEMA NEW
    

    {"id": "710", "local": "WMMWMW", "lat":-14.941885, "lon": 37.407819}, # MALEMA
    {"id": "50420", "local": "WMMW2T", "lat":-14.949975, "lon": 37.374007}, # MALEMA
    {"id": "680", "local": "WMMP", "lat":-14.952504, "lon": 37.349045}, # MALEMA
    {"id": "41", "local": "WMM1", "lat":-14.961813, "lon": 37.309198},
    {"id": "50415", "local": "WMMW1T", "lat":-14.938021, "lon": 37.260475}, # MALEMA
 

    {"id": "675", "local": "WTUWMMB", "lat":-14.930952, "lon": 37.247263}, # TUI
    {"id": "670", "local": "WTUWMMA", "lat":-14.930622, "lon": 37.227073}, # TUI
    {"id": "50410", "local": "WTUW2T", "lat":-14.935821, "lon": 37.212420}, # TUI
    {"id": "660", "local": "WTUP", "lat":-14.937271, "lon": 37.194403}, # TUI
    {"id": "50405", "local": "WTUW1T", "lat":-14.934048, "lon": 37.170015}, # TUI
    

    {"id": "655", "local": "WTWWTU", "lat":-14.932072, "lon": 37.162880}, # NACATA NEW
    {"id": "50400", "local": "WTWW2T", "lat":-14.923627, "lon": 37.133210}, # NACATA NEW
    {"id": "650", "local": "WTW1", "lat":-14.899666, "lon": 37.085039},
    {"id": "645", "local": "WTWP", "lat":-14.871459, "lon": 37.054620}, # NACATA NEW
    {"id": "50395", "local": "WTWW1T", "lat":-14.840412, "lon": 37.012080}, # NACATA NEW


    {"id": "640", "local": "WMTWTWC", "lat":-14.826273, "lon":36.997750}, # MUTUALI
    {"id": "635", "local": "WMTWTWB", "lat": -14.817661, "lon": 36.986387}, # MUTUALI
    {"id": "630", "local": "WMTWTWA", "lat":-14.810459, "lon": 36.972286}, # MUTUALI
    {"id": "50390", "local": "WMTW2T", "lat":-14.810279, "lon": 36.954385}, # MUTUALI
    {"id": "17", "local": "WMT3P", "lat":-14.811531, "lon": 36.933116}, # MUTUALI
    {"id": "14", "local": "WMTW4T", "lat":-14.810152, "lon": 36.913370}, # MUTUALI
    {"id": "18", "local": "WMT3", "lat":-14.808193, "lon": 36.898252},
    {"id": "16", "local": "WMT2P", "lat":-14.802486, "lon": 36.885446}, # MUTUALI
    {"id": "13", "local": "WMTW3T", "lat":-14.795687, "lon": 36.873265}, # MUTUALI
    {"id": "625", "local": "WMT1", "lat":-14.798180, "lon": 36.861608},
    {"id": "620", "local": "WMT1P", "lat":-14.792773, "lon": 36.850446}, # MUTUALI
    {"id": "50385", "local": "WMTW1T", "lat":-14.799465, "lon": 36.838377}, # MUTUALI
   
    {"id": "615", "local": "WLUWMTB", "lat":-14.800185, "lon": 36.830066}, # LURIO NEW
    {"id": "610", "local": "WLUWMTA", "lat":-14.799950, "lon": 36.809115}, # LURIO NEW
    {"id": "50380", "local": "WLUW2T", "lat":-14.800026, "lon": 36.780350}, # LURIO NEW
    {"id": "600", "local": "WLUP", "lat":-14.799377, "lon": 36.745275}, # LURIO NEW
    {"id": "605", "local": "WLU1", "lat":-14.799190, "lon": 36.714879},
    {"id": "50375", "local": "WLUW1T", "lat":-14.786551, "lon": 36.697623}, # LURIO NEW
    
 
    {"id": "595", "local": "WSSWLUB", "lat":-14.786177, "lon":36.689925}, # MURISSA
    {"id": "590", "local": "WSSWLUA", "lat":-14.791448, "lon": 36.659802}, # MURISSA
    {"id": "39", "local": "WSSW2T", "lat":-14.794651, "lon":36.634491}, # MURISSA
    {"id": "580", "local": "WSSP", "lat":-14.802291, "lon":36.596725}, # MURISSA
    {"id": "585", "local": "WSS1", "lat":-14.804829, "lon": 36.569428},
    {"id": "37", "local": "WSSW1T", "lat":-14.802421, "lon": 36.551404}, # MURISSA

    {"id": "575", "local": "WCBWSSB", "lat":-14.803801, "lon":36.533933}, # CUAMBA
    {"id": "570", "local": "WCBWSSA", "lat":-14.808347, "lon": 36.521927}, # CUAMBA
    {"id": "36", "local": "WCBW2T", "lat":-14.810814, "lon": 36.517989}, # CUAMBA
    {"id": "555", "local": "WCB23", "lat":-14.814281, "lon": 36.513273},
    {"id": "98", "local": "WCBW6T", "lat":-14.817920, "lon": 36.508966},
    {"id": "99", "local": "WCBW8T", "lat":-14.821471, "lon": 36.504588},
    {"id": "50355", "local": "WCBW4T", "lat":-14.821045, "lon":36.504749}, # CUAMBA
    {"id": "101", "local": "WCBW10T", "lat":-14.825062, "lon": 36.499771},
    {"id": "97", "local": "WCB22", "lat":-14.830025, "lon": 36.493678},
    {"id": "530", "local": "WCB4", "lat":-14.831860, "lon": 36.491036},
    {"id": "550", "local": "WCB13", "lat":-14.834859, "lon": 36.487288 },
    {"id": "535", "local": "WCBP", "lat":-14.838339, "lon": 36.483794}, # CUAMBA
    {"id": "565", "local": "WCB1", "lat":-14.840897, "lon": 36.481867},
    {"id": "50345", "local": "WCBW3BT", "lat":-14.843768, "lon": 36.479846},
    {"id": "50340", "local": "WCBW3AT", "lat":-14.846722, "lon": 36.477691}, # CUAMBA
    {"id": "540", "local": "WCB12", "lat":-14.850180, "lon": 36.475124},
    {"id": "50330", "local": "WCBW1T", "lat":-14.852265, "lon": 36.470868}, # CUAMBA


    {"id": "520", "local": "WCWWCBB", "lat":-14.853747, "lon": 36.466326}, # CUAMBA NEW
    {"id": "515", "local": "WCWWCBA", "lat":-14.857035 , "lon": 36.458584}, # CUAMBA NEW
    {"id": "50325", "local": "WCWW2T", "lat":-14.862929, "lon": 36.445718}, # CUAMBA NEW
    {"id": "93", "local": "WCWW4T", "lat":-14.869437, "lon": 36.436504},
    {"id": "96", "local": "WCW22", "lat":-14.878753, "lon": 36.429771},
    {"id": "510", "local": "WCW21", "lat":-14.886623, "lon": 36.422212},
    {"id": "94", "local": "WCW12", "lat":-14.893393, "lon": 36.415829},
    {"id": "92", "local": "WCWW3T", "lat":-14.916117, "lon": 36.384296},
    {"id": "505", "local": "WCWP", "lat":-14.922514, "lon": 36.347088}, # CUAMBA NEW
    {"id": "109", "local": "WCW11", "lat":-14.936615, "lon":  36.313370},
    {"id": "50320", "local": "WCWW1T", "lat":-14.961269, "lon": 36.255330}, # CUAMBA NEW
   
    {"id": "500", "local": "WCAWCWD", "lat":-14.968065, "lon":36.243838}, # CARONGA
    {"id": "490", "local": "WCAWCWC", "lat":-14.975947, "lon":36.222767}, # CARONGA
    {"id": "485", "local": "WCAWCWB", "lat":-14.980364, "lon": 36.204010}, # CARONGA
    {"id": "480", "local": "WCAWCWA", "lat":-14.987513, "lon": 36.175424}, # CARONGA
    {"id": "50300", "local": "WCAW2T", "lat": -14.996331, "lon":36.149301}, # CARONGA
    {"id": "470", "local": "WCAP", "lat":-15.005721, "lon": 36.136821}, # CARONGA
    {"id": "475", "local": "WCA1", "lat":-15.016566, "lon": 36.115646},
    {"id": "50295", "local": "WCAW1T", "lat": -15.022102, "lon": 36.086223}, # CARONGA
    

    {"id": "465", "local": "WTOWCAB", "lat":-15.022669, "lon": 36.077694}, # TO-BUE
    {"id": "460", "local": "WTOWCAA", "lat":-15.017050, "lon": 36.032637}, # TO-BUE
    {"id": "50290", "local": "WTOW2T", "lat":-15.011641, "lon": 35.993705}, # TO-BUE
    {"id": "450", "local": "WTOP", "lat":-15.009825, "lon":35.956589}, # TO-BUE
    {"id": "455", "local": "WTO1", "lat":-15.005416, "lon": 35.927652},
    {"id": "50285", "local": "WTOW1T", "lat":-14.998917 , "lon": 35.904782}, # TO-BUE


    {"id": "445", "local": "WELWTOB", "lat":-14.991375, "lon": 35.893987}, # ENTRE LAGOS
    {"id": "440", "local": "WELWTOA", "lat":-14.990074, "lon": 35.891325}, # ENTRE LAGOS
    {"id": "84", "local": "WEL24", "lat":-14.988045, "lon":35.887689},
    {"id": "50280", "local": "WELW2T", "lat":-14.986242, "lon": 35.884722}, # ENTRE LAGOS
    {"id": "50260", "local": "WELW4T", "lat":-14.984733, "lon": 35.882654}, # ENTRE LAGOS
    {"id": "88", "local": "WELW6T", "lat":-14.983249, "lon":35.879945},
    {"id": "425", "local": "WEL21", "lat":-14.981982, "lon": 35.877728},
    {"id": "89", "local": "WELW8T", "lat":-14.980751, "lon": 35.875008},
    {"id": "83", "local": "WEL23", "lat":-14.980751, "lon": 35.875008},
    {"id": "11", "local": "WEL22", "lat":-14.979124, "lon": 35.872584},
    {"id": "82", "local": "WEL13", "lat":-14.977391, "lon": 35.869258},
    {"id": "12", "local": "WEL12", "lat":-14.975766, "lon": 35.864911},
    {"id": "415", "local": "WELP", "lat":-14.974053, "lon": 35.861150},
    {"id": "91", "local": "WEL14", "lat":-14.972849, "lon": 35.857932},
    {"id": "87", "local": "WELW7T", "lat":-14.970966, "lon": 35.852795},
    {"id": "420", "local": "WEL11", "lat":-14.969507, "lon": 35.848447},
    {"id": "50255", "local": "WELW3T", "lat":-14.968602, "lon": 35.845358}, # ENTRE LAGOS
    {"id": "86", "local": "WELW5T", "lat":-14.966961, "lon": 35.838561}, # ENTRE LAGOS
    {"id": "50250", "local": "WELW1T", "lat":-14.964591, "lon": 35.831334}, # ENTRE LAGOS


    {"id": "410", "local": "XNYWELA", "lat":-14.962937, "lon":35.823129}, # NAYUCI
    {"id": "50245", "local": "XNYW2T", "lat":-14.960115, "lon": 35.772578}, # NAYUCI
    {"id": "50240", "local": "XNYW4T", "lat": -14.959503, "lon":35.753614}, # NAYUCI
    {"id": "405", "local": "XNY22", "lat": -14.962060, "lon": 35.719326}, # NAYUCI
    {"id": "395", "local": "XNY21", "lat":-0, "lon": 0},
    {"id": "400", "local": "XNY12", "lat":-0, "lon": 0},
    {"id": "50235", "local": "XNYW3T", "lat":-0, "lon": 0},
    {"id": "385", "local": "XNYP", "lat":-0, "lon": 0},
    {"id": "390", "local": "XNY11", "lat":-0, "lon": 0},
    {"id": "50230", "local": "XNYW1T", "lat":-14.964199, "lon": 35.694756}, # NAYUCI
    {"id": "9", "local": "XNYWELB", "lat":-0, "lon": 0},


    {"id": "380", "local": "XNJXNYB", "lat":-14.965768, "lon": 35.689131 }, # NAMANJA
    {"id": "375", "local": "XNJXNYA", "lat":-14.972352, "lon": 35.657914}, # NAMANJA
    {"id": "50225", "local": "XNJW2T", "lat":-14.973237 , "lon": 35.606777}, # NAMANJA
    {"id": "365", "local": "XNJP", "lat":-14.982665, "lon": 35.567728}, # NAMANJA
    {"id": "370", "local": "XNJ1", "lat":-0, "lon": 0},
    {"id": "50220", "local": "XNJW1T", "lat": -14.997544, "lon": 35.522145}, # NAMANJA

    {"id": "360", "local": "XLAXNJB", "lat":-14.999883, "lon": 35.516856}, # LAMBULILA
    {"id": "355", "local": "XLAXNJA", "lat": -15.004484, "lon": 35.473592}, # LAMBULILA
    {"id": "50215", "local": "XLAW2T", "lat": -15.020005, "lon": 35.429154}, # LAMBULILA
    {"id": "8", "local": "XLA21", "lat":-0, "lon": 0},
    {"id": "50210", "local": "XLAW4T", "lat":-0, "lon": 0},
    {"id": "350", "local": "XLA2", "lat":-0, "lon": 0},
    {"id": "345", "local": "XLA11", "lat":-0, "lon": 0},
    {"id": "340", "local": "XLAP", "lat":-15.050549, "lon": 35.392930}, # LAMBULILA
    {"id": "50205", "local": "XLAW3T", "lat":-0, "lon": 0},
    {"id": "50200", "local": "XLAW1T", "lat": -15.052288, "lon": 35.328034}, # LAMBULILA


    {"id": "335", "local": "XMWXLAC", "lat":-15.055132, "lon": 35.321064}, # MOLIPA
    {"id": "330", "local": "XMWXLAB", "lat": -15.054548, "lon": 35.307338}, # MOLIPA
    {"id": "325", "local": "XMWXLAA", "lat": -15.056640, "lon": 35.291373}, # MOLIPA
    {"id": "50195", "local": "XMWW2T", "lat": -15.060028, "lon": 35.270615}, # MOLIPA
    {"id": "315", "local": "XMWP", "lat":-15.063915 , "lon": 35.251920}, # MOLIPA
    {"id": "320", "local": "XMW1", "lat":-0, "lon": 0},
    {"id": "50190", "local": "XMWW1T", "lat": -15.064601, "lon": 35.237027}, # MOLIPA


    {"id": "310", "local": "XLWXMWB", "lat": -15.063864, "lon": 35.233658}, # LIWONDE
    {"id": "305", "local": "XLWXMWA", "lat":-15.071046, "lon": 35.193953}, # LIWONDE
    {"id": "290", "local": "XLW31", "lat":-0, "lon": 0},
    {"id": "50180", "local": "XLWW2T", "lat": -15.080988, "lon": 35.166647}, # LIWONDE
    {"id": "50175", "local": "XLWW4AT", "lat":-15.086635, "lon": 35.147101}, # LIWONDE
    {"id": "50155", "local": "XLWW4BT", "lat":-0, "lon": 0},
    {"id": "74", "local": "XLWW8T", "lat":-0, "lon": 0},
    {"id": "81", "local": "XLW25", "lat":-0, "lon": 0},
    {"id": "76", "local": "XLWW10T", "lat":-0, "lon": 0},
    {"id": "50170", "local": "XLWW6T", "lat":-0, "lon": 0},
    {"id": "300", "local": "XLW23", "lat":-0, "lon": 0},
    {"id": "77", "local": "XLWW12T", "lat":-0, "lon": 0},
    {"id": "78", "local": "XLW24", "lat":-0, "lon": 0},
    {"id": "79", "local": "XLW15", "lat":-0, "lon": 0},
    {"id": "285", "local": "XLW21", "lat":-0, "lon": 0},
    {"id": "295", "local": "XLW2", "lat":-0, "lon": 0},
    {"id": "275", "local": "XLW14", "lat":-0, "lon": 0},
    {"id": "270", "local": "XLW13", "lat":-0, "lon": 0},
    {"id": "265", "local": "XLWP", "lat":-15.093813, "lon": 35.125468}, # LIWONDE
    {"id": "50145", "local": "XLWW7T", "lat":-0, "lon": 0},
    {"id": "50150", "local": "XLWW3AT", "lat":-15.100646, "lon": 35.106244}, # LIWONDE
    {"id": "50160", "local": "XLWW3BT", "lat":-0, "lon": 0},
    {"id": "280", "local": "XLW11", "lat":-0, "lon": 0},
    {"id": "50140", "local": "XLWW1T", "lat":-15.111770, "lon": 35.080206}, # LIWONDE

    {"id": "260", "local": "XNWXLWC", "lat": -15.109689, "lon": 35.077250}, # NKAYA NEW
    {"id": "255", "local": "XNWXLWB", "lat":-15.107041, "lon": 35.073128}, # NKAYA NEW
    {"id": "250", "local": "XNWXLWA", "lat":-15.106188, "lon": 35.065343}, # NKAYA NEW
    {"id": "50135", "local": "XNWW2T", "lat": -15.113591, "lon": 35.052057}, # NKAYA NEW
    {"id": "240", "local": "XNWP", "lat":-0, "lon": 0},
    {"id": "245", "local": "XNW1", "lat":-0, "lon": 0}, 
    {"id": "50130", "local": "XNWW1T", "lat": -15.119886, "lon": 35.037286}, # NKAYA NEW
    
   
    {"id": "235", "local": "XNTXNW", "lat": -15.120123, "lon": 35.036548}, # NKAYA JUNCTION
    {"id": "50125", "local": "XNTW1T", "lat":-15.204188, "lon": 34.954296}, # NKAYA JUNCTION
  
  
    {"id": "230", "local": "XL6XNTC", "lat":-15.262248, "lon": 34.928802}, # LOOP 6 CL
    {"id": "225", "local": "XL6XNTB", "lat":-15.289011, "lon": 34.917683}, # LOOP 6 CL
    {"id": "220", "local": "XL6XNTA", "lat":-15.308907, "lon": 34.898314}, # LOOP 6 CL
    {"id": "50120", "local": "XL6W2T", "lat": -15.310663, "lon": 34.891729}, # LOOP 6 CL
    {"id": "210", "local": "XL6P", "lat":-15.358982, "lon": 34.864628}, # LOOP 6 CL
    {"id": "215", "local": "XL61", "lat":-0, "lon": 0},
    {"id": "50115", "local": "XL6W1T", "lat": -15.385787, "lon": 34.848715}, # LOOP 6 CL


    {"id": "205", "local": "XZAXL6B", "lat": -15.411509910165, "lon":34.8243404319391}, # FACILITIES ZALEWA
    {"id": "4", "local": "XZAXL6A", "lat": -15.412535, "lon": 34.822071}, # FACILITIES ZALEWA
    {"id": "7", "local": "XZAW2T", "lat": -15.415670, "lon": 34.816683}, # FACILITIES ZALEWA
    {"id": "6", "local": "XZAW1T", "lat":-15.420398, "lon": 34.810637}, # FACILITIES ZALEWA
    {"id": "73", "local": "XZA2", "lat":-0, "lon": 0},
    {"id": "72", "local": "XZA1", "lat":-0, "lon": 0},
    
    
    {"id": "200", "local": "XL5XZAB", "lat": -15.4227564469314, "lon":34.8089932888488}, # LOOP 5 CL
    {"id": "195", "local": "XL5XZAA", "lat":-15.444041, "lon": 34.792220}, # LOOP 5 CL
    {"id": "50110", "local": "XL5W2T", "lat":-15.475741, "lon": 34.758440}, # LOOP 5 CL
    {"id": "185", "local": "XL5P", "lat":-15.512134, "lon": 34.721874}, # LOOP 5 CL
    {"id": "190", "local": "XL51", "lat":-0, "lon": 0},
    {"id": "50105", "local": "XL5W1T", "lat":-15.543006, "lon": 34.680472}, # LOOP 5 CL

    {"id": "180", "local": "XL4XL5C", "lat": -15.5629497804683, "lon":34.6678802631617}, # LOOP 4 CL
    {"id": "175", "local": "XL4XL5B", "lat": -15.589116, "lon": 34.640521}, # LOOP 4 CL
    {"id": "170", "local": "XL4XL5A", "lat":-15.621767, "lon": 34.611555}, # LOOP 4 CL
    {"id": "50100", "local": "XL4W2T", "lat":-15.650991, "lon": 34.550998}, # LOOP 4 CL
    {"id": "160", "local": "XL4P", "lat":-15.710740, "lon": 34.522648}, # LOOP 4 CL
    {"id": "165", "local": "XL41", "lat":-0, "lon": 0},
    {"id": "50095", "local": "XL4W1T", "lat":-15.764191, "lon": 34.493239}, # LOOP 4 CL

    {"id": "155", "local": "XL3XL4D", "lat":-15.770906, "lon": 34.490816}, # LOOP 3 CL
    {"id": "150", "local": "XL3XL4C", "lat":-15.790163, "lon": 34.481218}, # LOOP 3 CL 
    {"id": "145", "local": "XL3XL4B", "lat": -15.805397, "lon": 34.456430}, # LOOP 3 CL
    {"id": "140", "local": "XL3XL4A", "lat":-15.811192, "lon": 34.429843}, # LOOP 3 CL
    {"id": "50090", "local": "XL3W2T", "lat":-15.823531, "lon": 34.398662}, # LOOP 3 CL
    {"id": "115", "local": "XL321", "lat":-0, "lon": 0},
    {"id": "50065", "local": "XL3W4T", "lat":-0, "lon": 0},
    {"id": "110", "local": "XL311", "lat":-0, "lon": 0},
    {"id": "125", "local": "XL32", "lat":-0, "lon": 0},
    {"id": "105", "local": "XL3P", "lat":-15.819891, "lon": 34.354121}, # LOOP 3 CL
    {"id": "3", "local": "XL3W3T", "lat":-0, "lon": 0},
    {"id": "50055", "local":"XL3W1T", "lat":-15.817426, "lon": 34.304692}, # LOOP 3 CL
 
 
    {"id": "100", "local": "XL2XL3D", "lat": -15.8197868392766, "lon":34.2810857141549}, # LOOP 2 CL
    {"id": "95", "local": "XL2XL3D", "lat":-15.849381, "lon": 34.243381}, # LOOP 2 CL
    {"id": "90", "local": "XL2XL3B", "lat": -15.869945, "lon": 34.189507}, # LOOP 2 CL
    {"id": "85", "local": "XL2XL3A", "lat":-15.887151, "lon": 34.134961}, # LOOP 2 CL
    {"id": "50050", "local": "XL2W2T", "lat":-15.915874, "lon": 34.089737}, # LOOP 2 CL
    {"id": "75", "local": "XL2P", "lat":-15.946431, "lon": 34.050878}, # LOOP 2 CL
    {"id": "80", "local": "XL21", "lat":-0, "lon": 0},
    {"id": "50045", "local": "XL2W1T", "lat":-15.971837, "lon": 34.003305}, # LOOP 2 CL


    {"id": "65", "local": "WL1XL2D", "lat": -15.978821, "lon": 33.997530}, # LOOP 1 CL 
    {"id": "60", "local": "WL1XL2C", "lat":-15.996321, "lon": 33.974954}, # LOOP 1 CL
    {"id": "70", "local": "WL1WL2B", "lat":-16.015424, "lon": 33.954668}, # LOOP 1 CL
    {"id": "55", "local": "WL1XL2A", "lat":-16.039052, "lon": 33.937208}, # LOOP 1 CL   
    {"id": "50040", "local": "WL1W2T", "lat": -16.058548, "lon": 33.918891}, # LOOP 1 CL
    {"id": "2", "local": "WL131", "lat":-16.080588, "lon": 33.9024223}, # LOOP 1 CL
    {"id": "50015", "local": "WL1W4T", "lat":-16.108250, "lon": 33.870087}, # LOOP 1 CL
    {"id": "40", "local": "WL122", "lat":-16.115015, "lon": 33.842186}, # LOOP 1 CL        
    {"id": "35", "local": "WL121", "lat":-16.119586, "lon": 33.812839}, # LOOP 1 CL
    {"id": "38", "local": "WL112", "lat":-16.136014, "lon": 33.792017}, # LOOP 1 CL
    {"id": "1", "local": "WL1W3T", "lat": -16.161205, "lon": 33.793738}, # LOOP 1
    {"id": "25", "local": "WL1P", "lat":-0, "lon": 0},
    {"id": "30", "local": "WL111", "lat":-0, "lon": 0},
    {"id": "50010", "local": "WL1W1T", "lat":-0, "lon": 0},

    {"id": "20", "local": "RMVWL1D", "lat": -16.1633212771317, "lon":33.795387671617}, # MOATIZE TERMINAL
    {"id": "15", "local": "RMVWL1C", "lat": -16.163321, "lon":33.795388}, # MOATIZE TERMINAL
    {"id": "10", "local": "RMVWL1B", "lat": -16.1633212771317, "lon":33.795387671617}, # MOATIZE TERMINAL
    {"id": "5", "local": "RMVWL1A", "lat": -16.1633212771317, "lon":33.795387671617}, # MOATIZE TERMINAL
    {"id": "112", "local": "RMVWVT", "lat": -16.1633212771317, "lon":33.795387671617}, # MOATIZE TERMINAL
    {"id": "33", "local": "RMVP", "lat": -16.1633212771317, "lon":33.795387671617} # MOATIZE TERMINAL
   
    # {"id": "9", "local": "", "lat": -16.1633783146919, "lon":33.7954033704417} # COORESPONDE A NAYUCI
]