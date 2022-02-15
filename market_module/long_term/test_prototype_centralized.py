"""
script that makes input datastructures, then applies market functions
"""
import sys
import os

# import own modules
from ...market_module.long_term.market_functions.run_longterm_market import run_longterm_market


# TEST CENTRALIZED #######################################################################################
# DATA
gmin = {'gmin': [[0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.]]}
gmax = {'gmax': [[6.81279421, 5.48159026, 2.38203374, 7.54674342],
                 [7.73197636, 6.75262824, 6.13657797, 5.47254192],
                 [5.86579999, 5.95020091, 3.76366327, 4.05507067],
                 [1.18167335, 4.17573217, 1.41616823, 2.34215857],
                 [2.19163749, 7.77541161, 2.81032255, 7.4761665],
                 [4.5741167, 6.75919357, 6.21927571, 5.74836098],
                 [6.22212381, 1.91511001, 4.06307573, 5.83767865],
                 [6.36843014, 7.66673468, 6.51067986, 2.76202555],
                 [7.99213298, 3.28463054, 2.14008723, 4.81859988],
                 [4.84881943, 6.07239153, 3.50539812, 4.0056891],
                 [5.67365983, 5.79733113, 3.10921705, 3.54790162],
                 [6.95717435, 4.55091406, 2.48218211, 7.41664744],
                 [5.69268107, 4.42518286, 2.97715422, 2.50145058],
                 [2.15710765, 1.59310888, 5.65967187, 5.27469419],
                 [5.24498763, 4.9540565, 2.39749202, 5.74072435],
                 [7.53863603, 4.16504471, 3.86014678, 2.96934612],
                 [6.96382683, 6.67372459, 5.94530707, 6.63892558],
                 [7.317812, 1.83657156, 6.70789776, 2.75662762],
                 [7.07499528, 2.42587038, 6.1706021, 5.4981892],
                 [6.97148801, 7.05997225, 3.52273118, 6.62876902],
                 [2.16922855, 4.31348899, 4.30557403, 3.23994962],
                 [3.82504438, 2.67386771, 1.68003485, 5.64750217],
                 [5.40047808, 1.91646981, 3.59418954, 1.09672258],
                 [6.29814598, 4.02241878, 5.27326252, 6.09480521],
                 [2.69606513, 7.63757569, 3.17130793, 3.44815115],
                 [5.59784589, 4.9306368, 3.45113264, 3.29767968],
                 [3.24094873, 3.12578813, 1.45320935, 6.67104377],
                 [5.78586703, 3.95596192, 6.84303397, 2.10661967],
                 [3.7887989, 6.5486513, 3.07785403, 3.60380964],
                 [3.20091969, 7.7503339, 6.24451058, 1.90373486],
                 [5.17401756, 2.78129657, 1.17589666, 6.26912408],
                 [7.03513909, 6.55285841, 3.73273392, 4.33640134],
                 [3.61249769, 3.80342665, 7.44747618, 4.50402269],
                 [5.94778895, 5.3608797, 2.8769483, 3.86887712],
                 [3.13246545, 6.36724406, 3.71652152, 7.60167176],
                 [4.67742743, 1.65695433, 3.20028434, 7.91329453],
                 [3.99776739, 6.31033852, 5.43325466, 2.47580213],
                 [4.13948408, 3.48386338, 7.71900285, 5.77064969],
                 [4.52568196, 4.91659718, 6.93977097, 3.94895211],
                 [6.6256862, 5.77341133, 6.80371263, 1.34361074],
                 [3.26141437, 4.49993962, 1.68485819, 5.3147235],
                 [1.08189101, 5.56395583, 1.48395816, 2.65083842],
                 [7.14808208, 1.48139293, 4.29576693, 2.9776666],
                 [2.98128993, 2.15954819, 3.19827962, 2.41323174],
                 [5.22537012, 6.57342013, 6.26486327, 5.97748896],
                 [1.82566887, 6.58877424, 1.77688948, 2.79539801],
                 [4.64454952, 4.27345544, 6.23743588, 7.3482227],
                 [1.93072291, 5.74884582, 1.87968023, 6.82473192],
                 [7.87296843, 3.87794836, 1.92155594, 1.31497615],
                 [4.3399886, 4.98653865, 1.72007305, 5.66227152],
                 [5.01889551, 5.24342204, 2.20231781, 2.96186041],
                 [4.85599427, 6.59807892, 1.21777911, 6.29858846],
                 [2.34022628, 3.87682505, 3.19957817, 3.59727344],
                 [7.04416616, 3.99839662, 3.64180563, 1.91136555],
                 [6.5114406, 6.94374886, 1.65493277, 6.55568024],
                 [7.82710967, 5.33423141, 6.52431907, 1.58232403],
                 [7.37920491, 4.65306114, 6.55197453, 6.52944581],
                 [6.303906, 7.44278536, 7.83629157, 5.11304249],
                 [3.79373684, 7.05380275, 4.40950976, 1.57972342],
                 [4.90674599, 5.66711117, 6.34650697, 5.29065072]]}
lmin = {'lmin': [[0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.],
                 [0., 0., 0., 0.]]}
lmax = {'lmax': [[2.4935019, 1.4944589, 1.88135898, 2.20944796],
                 [2.57555433, 2.244752, 1.0236515, 2.3565902],
                 [2.49724635, 1.77962053, 2.96266008, 1.44590098],
                 [2.96087544, 2.94812206, 2.03026534, 2.20723121],
                 [1.76085143, 1.49096826, 1.39765642, 1.16251181],
                 [2.82963129, 1.35383106, 1.77552776, 1.24439869],
                 [1.09884414, 2.03422805, 2.2492305, 1.53084692],
                 [2.82303632, 1.88166389, 1.84319061, 1.29588381],
                 [1.97806952, 1.84790951, 1.77785018, 1.45716377],
                 [1.23056462, 1.49422586, 1.01213978, 2.94573036],
                 [1.99811508, 1.38137611, 2.62592292, 2.75320558],
                 [1.38209606, 2.61208489, 1.79715204, 1.16634321],
                 [2.56640007, 2.04005714, 2.56329186, 2.06122731],
                 [1.63609659, 1.18973614, 2.15577346, 1.13841571],
                 [1.92198305, 2.34159628, 2.11848064, 2.40263685],
                 [1.79313463, 1.48875074, 1.92011639, 1.18142711],
                 [2.66485242, 1.27042479, 2.3156718, 2.99216516],
                 [1.05993061, 1.42309544, 1.56496767, 2.51686048],
                 [1.52054763, 2.62398401, 2.76103876, 2.68444336],
                 [1.30902394, 1.36132194, 2.50739732, 2.70343723],
                 [2.39040133, 1.61934963, 2.69293434, 1.12532187],
                 [1.98002813, 1.64122774, 1.82268801, 1.54038439],
                 [1.20661946, 2.49567954, 2.90945932, 1.62256764],
                 [2.15691238, 2.14950358, 1.28346773, 1.98481753],
                 [1.56862569, 1.7359953, 2.29843024, 1.80274407],
                 [1.95665164, 2.57853732, 2.42264417, 2.25819575],
                 [1.08850743, 1.45360313, 2.52877107, 1.91851321],
                 [1.78056869, 1.93506441, 2.23491166, 1.53937752],
                 [1.55719781, 2.46277026, 1.2636222, 2.69029428],
                 [1.46645514, 2.23946344, 1.66608207, 2.0424281],
                 [1.20617811, 2.8818393, 1.78737019, 2.3914452],
                 [1.76695319, 2.28113323, 2.49568342, 1.46153172],
                 [1.47578807, 2.02302443, 2.54255977, 2.8626375],
                 [1.13284789, 2.62550046, 1.48539477, 2.83160457],
                 [1.72889701, 2.07646979, 2.01933188, 1.46547644],
                 [1.334455, 2.89477224, 1.40746265, 1.47023371],
                 [1.08130617, 1.56738575, 2.74284728, 1.60017618],
                 [1.4384908, 1.46170184, 2.1574706, 2.50845476],
                 [1.33350436, 1.20465615, 1.34265871, 2.45348578],
                 [1.13813951, 1.64374756, 1.21568818, 1.03283433],
                 [1.06447298, 2.30962331, 1.23994848, 2.7216214],
                 [2.72566025, 1.39713186, 2.69439742, 2.93845097],
                 [1.4631755, 1.21239011, 2.81030637, 1.66805094],
                 [2.1028488, 1.80412383, 1.8233221, 1.85534788],
                 [1.16362285, 2.70364246, 2.60804663, 1.76389731],
                 [1.40127861, 1.12556846, 1.20314183, 2.78318962],
                 [1.32911354, 1.36548744, 2.50357719, 1.11056724],
                 [2.2357762, 2.89399015, 1.71227513, 2.52345596],
                 [1.20617329, 2.42498289, 2.648498, 2.87838768],
                 [2.8638441, 1.04696864, 1.47256063, 1.16434577],
                 [1.26025927, 1.96283935, 2.01107619, 2.41667371],
                 [1.59126259, 2.42711149, 2.185096, 1.5976365],
                 [1.26927857, 2.61841082, 1.07142623, 1.82118253],
                 [2.8931519, 2.7661906, 1.53433326, 2.39714476],
                 [1.16862607, 2.99549205, 2.09047661, 2.03468269],
                 [2.95925997, 2.14628351, 1.7505885, 2.62118416],
                 [1.3012746, 1.94387832, 2.39310903, 2.90257741],
                 [1.64599568, 2.42560511, 1.53962999, 1.49195857],
                 [2.45845157, 1.28750951, 2.03827484, 2.27514878],
                 [1.61609424, 1.30107699, 1.90794572, 2.64288107]]}

cost = {'cost': [[21.80873631, 23.09678187, 21.66155811, 25.47176384],
                 [25.40583445, 24.66546694, 21.90671238, 24.00665486],
                 [25.63521273, 24.4490884, 23.98987611, 21.78921037],
                 [29.50086366, 23.22223733, 28.04136762, 25.6085926],
                 [28.86386344, 24.36450108, 23.67618325, 29.10029865],
                 [26.69558133, 24.90409124, 23.56789987, 21.42756175],
                 [27.31683903, 22.15605449, 23.1971176, 24.74376389],
                 [21.23063982, 24.93707861, 20.11349067, 23.33752529],
                 [21.24674889, 25.51711735, 24.72701286, 24.09202817],
                 [22.41067029, 29.67066748, 21.19903342, 29.61922618],
                 [27.52866196, 28.15570884, 21.23165345, 25.20343137],
                 [23.36326095, 28.52667868, 25.34550647, 26.25882948],
                 [26.73644066, 21.42854177, 27.39793339, 27.90425732],
                 [23.4111869, 23.07018679, 22.24217551, 29.7479236],
                 [23.62837125, 21.38029711, 20.24533887, 24.32712061],
                 [24.79863172, 23.4068124, 25.03851515, 28.66056091],
                 [23.78454039, 28.42611904, 22.46595785, 26.19014451],
                 [25.91849428, 27.11254529, 22.95777376, 25.81211438],
                 [25.76214094, 28.68025906, 24.01973866, 28.24173715],
                 [23.38318814, 25.56239977, 24.83593821, 28.8330513],
                 [21.81549567, 21.18034947, 29.28905788, 21.37126274],
                 [24.26557041, 24.21874424, 29.83028051, 25.65606616],
                 [22.69900784, 22.05452214, 28.61630757, 20.11837011],
                 [29.65778843, 21.30803923, 27.7385456, 28.4168048],
                 [21.73337376, 28.55795263, 25.46091057, 26.50589296],
                 [26.50513307, 25.1114987, 25.9188959, 20.83505577],
                 [26.41545879, 27.94135483, 28.44091449, 27.87959411],
                 [28.33852571, 24.60332914, 29.72500543, 20.83638382],
                 [21.66795331, 29.11119595, 21.51552817, 27.50260225],
                 [26.37809922, 23.67887767, 27.76840804, 23.01430666],
                 [25.26584332, 21.65140038, 27.68250758, 25.61653581],
                 [26.15270779, 20.56096422, 28.03161785, 27.29942985],
                 [25.94703844, 25.58606693, 21.97670176, 20.04584428],
                 [26.33287142, 21.39517818, 20.87793238, 24.37638337],
                 [26.35200799, 24.60712694, 27.04397573, 23.55124525],
                 [21.56014458, 25.54370363, 26.55965106, 27.77430977],
                 [28.66932683, 24.61754706, 20.06545025, 24.03030455],
                 [28.91301685, 24.90874961, 28.71250805, 20.27005343],
                 [23.00757971, 22.45939907, 25.78947781, 25.39207499],
                 [21.32413448, 28.14728586, 29.16644377, 29.23179315],
                 [24.52474183, 22.32627782, 20.07086919, 20.52344699],
                 [27.29270461, 21.28319899, 23.13939102, 29.03520942],
                 [25.91848443, 27.53630218, 23.24421481, 29.89378712],
                 [28.35542414, 21.39635273, 23.58103921, 24.87226309],
                 [20.43322317, 21.19090182, 26.19441882, 28.33418843],
                 [21.68632441, 25.5691469, 29.30856517, 26.45975304],
                 [23.11244003, 22.58492989, 20.17331494, 28.13842288],
                 [25.63122974, 25.83435523, 27.53620792, 24.47009033],
                 [23.81824877, 23.16217723, 20.02789584, 26.70338728],
                 [29.32167008, 23.58840112, 21.57056914, 22.52747428],
                 [24.27404407, 29.2845921, 28.72923264, 28.46523761],
                 [23.10327646, 21.45857096, 24.19180103, 28.19638084],
                 [27.94619177, 26.89542847, 22.16202829, 25.52636158],
                 [26.55852671, 22.57570825, 21.72162756, 27.38708461],
                 [24.4644283, 27.5941599, 25.25689451, 21.70639379],
                 [21.04322262, 23.8871697, 29.23535424, 20.50328705],
                 [23.68748248, 23.45123254, 26.20962184, 20.22210683],
                 [20.93499212, 22.76174482, 23.63959004, 26.64799975],
                 [20.2919086, 22.55427727, 21.30184169, 23.12631751],
                 [22.09914997, 23.47055928, 29.85231492, 28.86468223]]}
util = {'util': [[27.05626488, 34.49762427, 33.04094703, 29.97261182],
                 [34.99270544, 31.55004364, 30.55612451, 31.73060776],
                 [30.75104538, 34.75574184, 31.02038489, 26.02361977],
                 [33.68979719, 29.26471572, 33.23204199, 25.13797041],
                 [33.25932516, 33.13178807, 31.72467464, 34.48595564],
                 [34.79031735, 32.89018917, 33.81403441, 31.71725415],
                 [26.23722563, 32.05145525, 33.01560267, 34.96817422],
                 [28.4105292, 27.13102925, 34.45029732, 31.57717824],
                 [28.95611451, 25.362917, 27.31160139, 34.57328907],
                 [25.4560014, 29.57440656, 29.87307265, 27.43873272],
                 [29.14030416, 34.44553629, 34.41579755, 27.94925312],
                 [30.81373397, 30.20638012, 28.28189321, 25.66835987],
                 [25.14619208, 28.46447814, 29.12727567, 28.28921119],
                 [28.27571707, 25.78650299, 25.89260334, 32.40652994],
                 [25.03696398, 33.766149, 27.32480868, 27.21111175],
                 [29.82949448, 32.07744031, 33.26522, 27.67025837],
                 [25.29945402, 26.20127628, 25.82120413, 30.82208129],
                 [31.2525135, 30.838882, 30.6365454, 34.68191239],
                 [26.78585234, 27.07244312, 33.69942042, 34.12204776],
                 [32.91884988, 30.45859402, 32.86287423, 30.25147713],
                 [34.11831321, 25.33335683, 27.01393382, 33.23352335],
                 [28.48132998, 26.946859, 25.52688435, 33.52475394],
                 [28.06592243, 29.80096904, 26.10060827, 32.1404258],
                 [31.83050805, 28.1921663, 31.43734545, 32.3431643],
                 [25.80699614, 27.44199184, 31.32955428, 32.39757685],
                 [26.27164686, 25.80296751, 32.96794849, 27.89424658],
                 [25.29249778, 31.85963535, 32.41278141, 29.69012593],
                 [34.21475316, 27.2308766, 34.64251954, 27.87867662],
                 [30.25354105, 28.20852638, 34.42135513, 31.51516853],
                 [30.50760749, 29.34494583, 33.0490914, 34.39863784],
                 [31.91384047, 34.48063101, 32.64398345, 32.9195515],
                 [27.33552038, 30.12973098, 28.04399056, 33.73024968],
                 [31.37092095, 28.92282533, 25.21683637, 30.81454242],
                 [28.68965582, 30.19422247, 26.40743883, 33.96838077],
                 [26.60807552, 32.07041469, 25.40000733, 25.83598566],
                 [29.00349555, 32.31643869, 26.25837994, 32.96103429],
                 [26.57202031, 26.17150995, 26.7360711, 28.86187465],
                 [32.22271015, 33.65448238, 30.14659161, 33.79357578],
                 [25.52538095, 28.71960544, 33.4432494, 27.7189132],
                 [32.91094567, 29.45056866, 33.83672454, 25.45102797],
                 [32.89846045, 28.96067856, 31.62425698, 28.60903315],
                 [31.61148734, 25.28203618, 26.8670788, 30.61259955],
                 [30.21218092, 32.06397277, 29.78698347, 26.89952406],
                 [28.2169871, 27.08800828, 30.3658812, 28.74579616],
                 [29.305566, 32.15140651, 32.38503481, 30.26721441],
                 [34.63419388, 33.8562909, 31.64768021, 30.65570031],
                 [26.66511578, 32.58434349, 29.1597394, 33.03630024],
                 [33.47823162, 34.86043982, 31.79610563, 29.02390748],
                 [27.20940589, 33.45244035, 25.85428722, 28.19613959],
                 [30.21685817, 33.27594072, 33.78610745, 27.81917545],
                 [26.21505466, 34.41507756, 34.59457448, 29.83410669],
                 [30.00379498, 31.95012823, 29.04695118, 30.34088987],
                 [32.85748352, 31.57981687, 30.24490217, 28.46880735],
                 [31.31201078, 30.54116754, 26.26098686, 28.76560955],
                 [30.38661958, 31.26609108, 30.64073671, 29.33541506],
                 [26.18820514, 25.0317703, 28.92629726, 31.71186597],
                 [28.95729177, 29.15832557, 28.43488318, 34.04208405],
                 [32.35630316, 28.96845555, 25.3567505, 26.57077046],
                 [28.16806745, 31.99506071, 31.98591712, 34.1815143],
                 [34.25644764, 28.8701482, 25.72129159, 34.92952105]]}

# setup inputs --------------------------------------------
user_input = {'md': 'centralized',
              'horizon_basis': 'months',
              'data_profile': 'daily',
              'recurrence': 2,
              'yearly_demand_rate': 0.05,
              'prod_diff_option': "co2Emissions",
              'agent_ids': ["prosumer_1", "prosumer_2", "consumer_1", "producer_1"],
              'agent_types': ["prosumer", "prosumer", "consumer", "producer"],
              'name': 'test_centralized_noPref',
              'co2_emissions': [1, 1.1, 0, 1.8],
              'gmin': gmin['gmin'],
              'gmax': gmax['gmax'],
              'lmin': lmin['lmin'],
              'lmax': lmax['lmax'],
              'cost': cost['cost'],
              'util': util['util'],
              'gis_data': {'From/to': [(0, 1), (1, 2), (1, 3)],
                           'Losses total [W]': [22969.228855, 24122.603833, 18138.588662],
                           'Length': [1855.232413, 1989.471069, 1446.688900],
                           'Total_costs': [1.848387e+06, 1.934302e+06, 1.488082e+06]}
              }

settings, agent_data, network, result, result_dict = run_longterm_market(user_input)


# MAIN RESULTS
# ADG
print(result.ADG)

print(result.SPM)

# Shadow price per hour
print(result.shadow_price)
print(result_dict['shadow_price'])
# Energy dispatch
# print(result.Pn)
print(result_dict['Pn'])
print(result.Ln)
print(result.Gn)

# Settlement
# print(result.settlement)

# Social welfare
# print(result.social_welfare_h)


# Find the best price
print(result.find_best_price(15, 'prosumer_1', agent_data, settings))  # user must select hour and agent_id

print(result_dict['shadow_price'])
